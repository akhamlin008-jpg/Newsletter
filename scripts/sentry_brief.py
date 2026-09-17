"""
sentry_brief.py — reads the same three files the Sentry page reads and saves a
small summary to data/sentry_brief.json for the Morning Letter.

  snapshot.json  (Sentry)      -> market pulse (dir, volZ), composite, grade
  arb.json       (Sentry)      -> pair dislocations, correlation breaks
  signal.json    (es-meanrev-) -> ES mean-reversion verdict

Numbers are copied, not recomputed, so they match the page. The risk block
repeats the page's own Risk Console math with its default settings: top 8 by
composite, shrinkage 0.35, risk parity, $1M, 95% 1-day VaR, -35% equity and
-150bp rate stress.

Standard library only. Always writes a file; failures are recorded, never
filled in.
"""
import datetime as dt
import json
import math
import os
import statistics
import sys
import urllib.request

SOURCES = {
    "snapshot": "https://raw.githubusercontent.com/akhamlin008-jpg/Sentry/main/snapshot.json",
    "arb": "https://raw.githubusercontent.com/akhamlin008-jpg/Sentry/main/arb.json",
    "signal": "https://raw.githubusercontent.com/akhamlin008-jpg/es-meanrev-/main/signal.json",
}
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "sentry_brief.json")
LOCAL_DIR = os.environ.get("SENTRY_LOCAL_DIR")  # for offline testing only

N_TOP = 20          # risk console candidate pool
N_BOOK = 8          # risk console default book
N_PULSE = 10
N_TURNOVER = 5
N_ARB = 5
SHRINK = 0.35       # the page's fixed shrinkage
CAPITAL = 1_000_000
CONF = 0.95
SHOCK_EQ = -0.35
SHOCK_RATE_BP = -150


def load(name):
    if LOCAL_DIR:
        with open(os.path.join(LOCAL_DIR, name + ".json")) as fh:
            return json.load(fh)
    req = urllib.request.Request(SOURCES[name], headers={"User-Agent": "MorningLetter/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def num(x, nd=2):
    try:
        x = float(x)
    except (TypeError, ValueError):
        return None
    return round(x, nd) + 0.0 if math.isfinite(x) else None


def hours_old(stamp):
    """Age in hours. Stamps without a timezone are treated as UTC (GitHub runners)."""
    try:
        t = dt.datetime.fromisoformat(str(stamp).replace("Z", "+00:00"))
    except ValueError:
        return None
    if t.tzinfo is None:
        t = t.replace(tzinfo=dt.timezone.utc)
    return num((dt.datetime.now(dt.timezone.utc) - t).total_seconds() / 3600, 1)


# ------------------------------------------------------------------ pulse + composite

def stock_row(o, sectors):
    f = o.get("f") or {}
    return {
        "ticker": o["tk"],
        "sector": sectors[o["sec"]] if isinstance(o.get("sec"), int) and o["sec"] < len(sectors) else o.get("sec"),
        "composite": num(o.get("comp")),
        "percentile": num(o.get("pct"), 0),
        "grade": o.get("grade"),
        "dir_5d": num(o.get("dir")),
        "pulse": None if o.get("dir") is None else ("bullish" if o["dir"] > 0 else "bearish"),
        "pulse_strength": None if o.get("dir") is None else round(abs(o["dir"]) * 100),
        "turnover_sigma": num(o.get("volZ")),
        "dcf_mos_pct": num(o.get("mos"), 1),
        "price": num(o.get("px")),
        "price_stale": bool(o.get("px_stale")),
        "factors": {k: num(v) for k, v in f.items()},
    }


# ------------------------------------------------------------------ risk console (port of the page's JS)

def page_risk(book, snap):
    ret = snap.get("returns") or {}
    idx = {c: i for i, c in enumerate(ret.get("cols") or [])}
    names = [o for o in book if o["tk"] in idx]
    if len(names) < 2:
        return {"status": "skipped", "reason": "returns missing for the book"}
    series = [ret["m"][idx[o["tk"]]] for o in names]
    days = [d for d in range(min(len(s) for s in series))
            if all(s[d] is not None for s in series)]
    mat = [[s[d] for d in days] for s in series]
    n, D = len(mat), len(days)
    if D < 60:
        return {"status": "skipped", "reason": f"only {D} shared days"}

    mu = [sum(r) / D for r in mat]
    S = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i, n):
            v = sum((mat[i][k] - mu[i]) * (mat[j][k] - mu[j]) for k in range(D)) / (D - 1)
            S[i][j] = S[j][i] = v
    sd = [math.sqrt(S[i][i]) for i in range(n)]
    rb = statistics.fmean(S[i][j] / (sd[i] * sd[j]) for i in range(n) for j in range(i + 1, n))
    S = [[S[i][j] if i == j else SHRINK * rb * sd[i] * sd[j] + (1 - SHRINK) * S[i][j]
          for j in range(n)] for i in range(n)]

    w = [1 / n] * n                                   # risk parity, as on the page
    for _ in range(300):
        Sw = [sum(S[i][j] * w[j] for j in range(n)) for i in range(n)]
        pv = math.sqrt(sum(w[i] * Sw[i] for i in range(n)))
        rc = [w[i] * Sw[i] / pv for i in range(n)]
        w = [w[i] * (pv / n / max(rc[i], 1e-9)) ** 0.35 for i in range(n)]
        s = sum(w)
        w = [v / s for v in w]

    pvol = math.sqrt(sum(w[i] * w[j] * S[i][j] * 252 for i in range(n) for j in range(n)))
    port = [sum(w[i] * mat[i][d] for i in range(n)) for d in range(D)]
    pm = sum(port) / D
    psd = statistics.stdev(port)
    z = statistics.NormalDist().inv_cdf(1 - CONF)
    srt = sorted(port)
    k = int((1 - CONF) * D)
    tail = srt[:max(k, 1)]
    sectors = snap.get("sectors") or []
    sec_name = lambda o: sectors[o["sec"]] if isinstance(o.get("sec"), int) else str(o.get("sec"))
    stress = sum(w[i] * ((names[i].get("beta") or 1) * SHOCK_EQ
                         + (-0.9 if sec_name(names[i]) in ("Real Estate", "Utilities") else 0.15)
                         * (SHOCK_RATE_BP / 10000) * -1) for i in range(n)) * CAPITAL
    sec_w = {}
    for i, o in enumerate(names):
        sec_w[sec_name(o)] = sec_w.get(sec_name(o), 0) + w[i]
    sd2 = [math.sqrt(S[i][i]) for i in range(n)]
    pairs = sorted(((names[i]["tk"], names[j]["tk"], S[i][j] / (sd2[i] * sd2[j]))
                    for i in range(n) for j in range(i + 1, n)), key=lambda p: -abs(p[2]))
    return {
        "status": "ok",
        "book": [{"ticker": o["tk"], "weight_pct": num(w[i] * 100, 1)} for i, o in enumerate(names)],
        "days": D,
        "portfolio_vol_ann_pct": num(pvol * 100, 1),
        "sector_hhi": num(sum(v * v for v in sec_w.values())),
        "var95_1d_parametric_usd": round(-(pm + z * psd) * CAPITAL),
        "var95_1d_historical_usd": round(-srt[k] * CAPITAL),
        "cvar95_1d_usd": round(-(sum(tail) / len(tail)) * CAPITAL),
        "stress_usd": round(stress),
        "tightest_correlations": [{"pair": [a, b], "corr": num(c)} for a, b, c in pairs[:4]],
        "settings": "top 8 by composite, $1M, risk parity, shrinkage 0.35, 95% 1-day, equity -35% / rates -150bp",
    }


# ------------------------------------------------------------------ build

def build_sentry(snap):
    sectors = snap.get("sectors") or []
    stocks = [o for o in snap["stocks"] if o.get("px") is not None and o.get("cap") is not None]
    by_comp = sorted([o for o in stocks if o.get("comp") is not None], key=lambda o: -o["comp"])
    by_dir = sorted([o for o in stocks if o.get("dir") is not None], key=lambda o: -o["dir"])
    by_vol = sorted([o for o in stocks if o.get("volZ") is not None], key=lambda o: -abs(o["volZ"]))
    try:
        risk = page_risk(by_comp[:N_BOOK], snap)
    except Exception as e:  # noqa: BLE001
        risk = {"status": "failed", "reason": f"{type(e).__name__}: {e}"}
    row = lambda o: stock_row(o, sectors)
    return {
        "as_of": snap.get("as_of"),
        "hours_old": hours_old(snap.get("as_of")),
        "names": len(stocks),
        "stale_prices": sum(1 for o in stocks if o.get("px_stale")),
        "top20_composite": [{"rank": i + 1, **row(o)} for i, o in enumerate(by_comp[:N_TOP])],
        "pulse_top_bulls": [row(o) for o in by_dir[:N_PULSE]],
        "pulse_top_bears": [row(o) for o in by_dir[::-1][:N_PULSE]],
        "highest_turnover": [row(o) for o in by_vol[:N_TURNOVER]],
        "risk_console": risk,
    }


def build_arb(arb):
    rv = sorted(arb.get("rv") or [], key=lambda p: -abs(p.get("z") or 0))
    breaks = [c for c in arb.get("corr") or [] if c.get("read") != "normal"]
    return {
        "as_of": arb.get("as_of"),
        "hours_old": hours_old(arb.get("as_of")),
        "top_pair_dislocations": [
            {k: p.get(k) for k in ("a", "b", "sector", "rich", "cheap", "z", "hl", "corr", "beta")}
            | {"over_2_5_sigma": abs(p.get("z") or 0) > 2.5}
            for p in rv[:N_ARB]],
        "correlation_breaks": [
            {k: c.get(k) for k in ("a", "b", "cl", "cs", "gap", "read", "leader", "laggard")}
            for c in sorted(breaks, key=lambda c: -abs(c.get("gap") or 0))[:N_ARB]],
        "warnings": {k: (arb.get("warnings") or {}).get(k) for k in ("rv", "corr")},
    }


def build_signal(sig):
    return {k: sig.get(k) for k in ("as_of", "verdict", "rsi2", "rsi2_threshold", "down3", "close", "generated_utc")}


def main():
    out = {"generated_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="minutes"),
           "errors": {}}
    for key, name, fn in (("sentry", "snapshot", build_sentry), ("arbitrage", "arb", build_arb),
                          ("es_meanrev", "signal", build_signal)):
        try:
            out[key] = fn(load(name))
        except Exception as e:  # noqa: BLE001
            out[key] = None
            out["errors"][name] = f"{type(e).__name__}: {e}"
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as fh:
        json.dump(out, fh, indent=1)
    print(f"[sentry_brief] wrote {OUT}; errors: {out['errors'] or 'none'}")
    return 0 if out.get("sentry") else 1


if __name__ == "__main__":
    sys.exit(main())
