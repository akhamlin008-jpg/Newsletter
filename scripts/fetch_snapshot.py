"""
Morning Letter: free data snapshot.

Pulls free public market data, computes unusual-move scores (charter Section 5),
and writes:
  data/latest.json              machine-readable snapshot (read by the analyst)
  data/latest.md                human-readable table
  data/snapshots/YYYY-MM-DD.json  daily archive (later run of the day overwrites)

Standard library only, so there is nothing to install.
Every source is tried independently. A failed source is recorded in the output,
never hidden, and never replaced with a guessed number.

Sources marked EXPERIMENTAL have not been confirmed to work from GitHub's servers.
The first run will show which ones work.
"""

import csv
import io
import json
import math
import os
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

ET = ZoneInfo("America/New_York")
DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
HISTORY_START = (date.today() - timedelta(days=800)).isoformat()

# Charter parameters (Section 5). [TUNE] values, frozen before live use.
EWMA_LAMBDA = 0.94
FLOOR_FRACTION = 0.5       # floor = 0.5 x one-year realized volatility
FLOOR_WINDOW = 252         # trading days
Z_FLAG = 2.0
MIN_CHANGES = 60           # minimum history to compute a score

# change types:
#   "bp"   level difference x 100 (yields quoted in percent -> basis points)
#   "pct"  percent change
#   "diff" level difference in the series' own units
ROWS = [
    # id, label, group, change type, [sources in order of preference]
    ("UST2Y", "US 2-year yield", "rates", "bp", [("fred", "DGS2")]),
    ("UST10Y", "US 10-year yield", "rates", "bp", [("fred", "DGS10")]),
    ("S2S10", "2s10s spread", "rates", "bp", [("fred", "T10Y2Y")]),
    ("REAL10Y", "10-year real yield (TIPS)", "rates", "bp", [("fred", "DFII10")]),
    ("BE10Y", "10-year breakeven inflation", "rates", "bp", [("fred", "T10YIE")]),
    ("SOFR", "SOFR", "rates", "bp", [("fred", "SOFR")]),
    ("USD_BROAD", "Broad trade-weighted dollar", "dollar", "pct", [("fred", "DTWEXBGS")]),
    ("USDJPY", "USD/JPY", "dollar", "pct", [("fred", "DEXJPUS")]),
    ("EURUSD", "EUR/USD", "dollar", "pct", [("fred", "DEXUSEU")]),
    ("SPX", "S&P 500 index", "equity", "pct", [("fred", "SP500"), ("stooq", "^spx")]),
    ("NDX", "Nasdaq 100 index", "equity", "pct", [("fred", "NASDAQ100"), ("stooq", "^ndx")]),
    ("RUT", "Russell 2000 index", "equity", "pct", [("stooq", "^rut")]),
    ("ES", "S&P 500 futures", "equity", "pct", [("stooq", "es.f")]),
    ("NQ", "Nasdaq 100 futures", "equity", "pct", [("stooq", "nq.f")]),
    ("VIX", "VIX", "vol", "diff", [("fred", "VIXCLS"), ("cboe_vix", "VIX")]),
    ("WTI", "WTI crude", "commodities", "pct", [("fred", "DCOILWTICO"), ("stooq", "cl.f")]),
    ("BRENT", "Brent crude", "commodities", "pct", [("fred", "DCOILBRENTEU"), ("stooq", "cb.f")]),
    ("GOLD", "Gold", "commodities", "pct", [("stooq", "xauusd"), ("stooq", "gc.f")]),
    ("COPPER", "Copper", "commodities", "pct", [("stooq", "hg.f")]),
]

EXPERIMENTAL_SOURCES = {"stooq"}

CRYPTO = [("BTC", "BTC-USD", "PF_XBTUSD", "BTC"), ("ETH", "ETH-USD", "PF_ETHUSD", "ETH")]


# ---------------------------------------------------------------- HTTP

REQUEST_TIMEOUT = 8   # seconds per attempt
TRIES = 2             # one retry, and only for timeouts or server errors
CUSTOM_UA = "MorningLetterSnapshot/0.2 (personal research project)"


def http_get(url, data=None, headers=None, custom_ua=True):
    # custom_ua=False sends urllib's default agent (Python-urllib/3.x).
    # FRED needs this: from GitHub-hosted runners, requests with a custom
    # User-Agent have been reported to stall until the read times out.
    hdrs = {"User-Agent": CUSTOM_UA} if custom_ua else {}
    if headers:
        hdrs.update(headers)
    last_err = None
    for attempt in range(TRIES):
        try:
            req = urllib.request.Request(url, data=data, headers=hdrs)
            with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as e:
            last_err = e
            if 400 <= e.code < 500:  # blocked or not found: retrying won't help
                break
        except Exception as e:  # noqa: BLE001 - timeouts, connection errors
            last_err = e
        if attempt < TRIES - 1:
            time.sleep(1)
    raise RuntimeError(f"{type(last_err).__name__}: {last_err}")


# ---------------------------------------------------------------- sources
# Each returns a chronological list of (date, float).

def parse_date(s):
    s = s.strip()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%Y%m%d"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            pass
    raise ValueError(f"unrecognized date {s!r}")


FRED_SLOTS = threading.Semaphore(4)   # don't open 14 connections to FRED at once


def fetch_fred(series_id):
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}&cosd={HISTORY_START}"
    with FRED_SLOTS:
        text = http_get(url, custom_ua=False)
    rows = list(csv.reader(io.StringIO(text)))
    if not rows or len(rows[0]) < 2:
        raise RuntimeError(f"unexpected FRED response: {snippet(text)}")
    out = []
    for r in rows[1:]:
        if len(r) < 2 or r[1].strip() in ("", "."):
            continue
        out.append((parse_date(r[0]), float(r[1])))
    return out


def snippet(text, n=100):
    return repr(" ".join(text.split())[:n])


def fetch_stooq(symbol):
    # Since about April 2026 Stooq has returned an API-key instructions page
    # (HTTP 200) instead of CSV to requests without a key. The key is optional
    # here so a keyless run still records exactly what Stooq sent back.
    key = os.environ.get("STOOQ_APIKEY", "").strip()
    url = f"https://stooq.com/q/d/l/?s={urllib.parse.quote(symbol)}&i=d"
    if key:
        url += f"&apikey={urllib.parse.quote(key)}"

    def redact(msg):  # error text is committed to a public repo
        if not key:
            return msg
        return msg.replace(key, "[key]").replace(urllib.parse.quote(key), "[key]")

    try:
        text = http_get(url)
    except RuntimeError as e:
        raise RuntimeError(redact(str(e))) from None
    reader = csv.DictReader(io.StringIO(text))
    if not reader.fieldnames or "Close" not in reader.fieldnames:
        tag = "" if key else " [no STOOQ_APIKEY set]"
        raise RuntimeError(f"unexpected Stooq response{tag} (no Close column): {snippet(redact(text), 160)}")
    out = []
    for r in reader:
        try:
            out.append((parse_date(r["Date"]), float(r["Close"])))
        except (ValueError, KeyError, TypeError):
            continue
    out.sort()
    cutoff = date.fromisoformat(HISTORY_START)
    return [x for x in out if x[0] >= cutoff]


def fetch_cboe_vix(_):
    url = "https://cdn.cboe.com/api/global/us_indices/daily_prices/VIX_History.csv"
    text = http_get(url)
    reader = csv.DictReader(io.StringIO(text))
    out = []
    for r in reader:
        try:
            out.append((parse_date(r["DATE"]), float(r["CLOSE"])))
        except (ValueError, KeyError, TypeError):
            continue
    out.sort()
    cutoff = date.fromisoformat(HISTORY_START)
    return [x for x in out if x[0] >= cutoff]


FETCHERS = {"fred": fetch_fred, "stooq": fetch_stooq, "cboe_vix": fetch_cboe_vix}


# ---------------------------------------------------------------- math

def changes(series, kind):
    out = []
    for (d0, v0), (d1, v1) in zip(series, series[1:]):
        if kind == "bp":
            out.append((d1, (v1 - v0) * 100.0))
        elif kind == "diff":
            out.append((d1, v1 - v0))
        else:  # pct
            if v0 <= 0:
                continue  # percent change undefined (e.g. negative oil in 2020)
            out.append((d1, (v1 / v0 - 1.0) * 100.0))
    return out


def unusual_move_score(chg_values, latest_change):
    """z = latest change / max(EWMA vol through the prior day, floor). Charter Section 5."""
    hist = chg_values
    if len(hist) < MIN_CHANGES:
        return None, None, None
    seed = hist[:20]
    var = sum(x * x for x in seed) / len(seed)
    for x in hist[20:]:
        var = EWMA_LAMBDA * var + (1 - EWMA_LAMBDA) * x * x
    ewma_sigma = math.sqrt(var)
    window = hist[-FLOOR_WINDOW:]
    mean = sum(window) / len(window)
    sd = math.sqrt(sum((x - mean) ** 2 for x in window) / (len(window) - 1))
    floor = FLOOR_FRACTION * sd
    sigma = max(ewma_sigma, floor)
    if sigma == 0:
        return None, ewma_sigma, floor
    return latest_change / sigma, ewma_sigma, floor


def weekdays_between(d_from, d_to):
    """Weekdays after d_from up to and including d_to. Ignores market holidays."""
    n, d = 0, d_from
    while d < d_to:
        d += timedelta(days=1)
        if d.weekday() < 5:
            n += 1
    return n


# ---------------------------------------------------------------- rows

def build_row(row_id, label, group, kind, sources, today_et):
    errors = []
    for src, sid in sources:
        t0 = time.monotonic()
        try:
            series = FETCHERS[src](sid)
            if len(series) < 2:
                raise RuntimeError("fewer than 2 observations")
            chg = changes(series, kind)
            last_date, last_val = series[-1]
            latest = chg[-1][1] if chg and chg[-1][0] == last_date else None
            z = ewma = floor = None
            if latest is not None:
                z, ewma, floor = unusual_move_score([c for _, c in chg[:-1]], latest)
            age = weekdays_between(last_date, today_et)
            return {
                "id": row_id, "label": label, "group": group,
                "source": f"{src}:{sid}",
                "experimental_source": src in EXPERIMENTAL_SOURCES,
                "last_date": last_date.isoformat(),
                "value": round(last_val, 6),
                "change": None if latest is None else round(latest, 4),
                "change_unit": {"bp": "bp", "pct": "%", "diff": "pts"}[kind],
                "ewma_sigma": None if ewma is None else round(ewma, 4),
                "floor_sigma": None if floor is None else round(floor, 4),
                "z": None if z is None else round(z, 2),
                "flag": z is not None and abs(z) >= Z_FLAG,
                "age_weekdays": age,
                "stale": age > 1,
                "status": "ok",
                "fetch_seconds": round(time.monotonic() - t0, 1),
                "failed_sources": errors,
            }
        except Exception as e:  # noqa: BLE001
            errors.append(f"{src}:{sid} -> {e} ({time.monotonic() - t0:.1f}s)")
    return {"id": row_id, "label": label, "group": group, "status": "failed",
            "failed_sources": errors, "flag": False}


# ---------------------------------------------------------------- crypto

def coinbase_daily_closes(product):
    url = f"https://api.exchange.coinbase.com/products/{product}/candles?granularity=86400"
    candles = json.loads(http_get(url))  # [time, low, high, open, close, volume], newest first
    today_utc = datetime.now(timezone.utc).date()
    closes = []
    for c in sorted(candles, key=lambda c: c[0]):
        d = datetime.fromtimestamp(c[0], tz=timezone.utc).date()
        if d < today_utc:  # completed days only
            closes.append((d, float(c[4])))
    return closes


def coinbase_24h(product):
    stats = json.loads(http_get(f"https://api.exchange.coinbase.com/products/{product}/stats"))
    last, open_ = float(stats["last"]), float(stats["open"])
    return last, (last / open_ - 1.0) * 100.0


def kraken_futures_tickers():
    data = json.loads(http_get("https://futures.kraken.com/derivatives/api/v3/tickers"))
    return {t.get("symbol"): t for t in data.get("tickers", [])}


def hyperliquid_ctxs():
    body = json.dumps({"type": "metaAndAssetCtxs"}).encode()
    data = json.loads(http_get("https://api.hyperliquid.xyz/info", data=body,
                               headers={"Content-Type": "application/json"}))
    meta, ctxs = data[0], data[1]
    return {a["name"]: c for a, c in zip(meta["universe"], ctxs)}


def build_crypto(previous):
    out, errors = [], []
    def attempt(fn):
        t0 = time.monotonic()
        try:
            return fn(), None
        except Exception as e:  # noqa: BLE001
            return None, f"{e} ({time.monotonic() - t0:.1f}s)"

    with ThreadPoolExecutor(max_workers=2) as pool:
        fk, fh = pool.submit(attempt, kraken_futures_tickers), pool.submit(attempt, hyperliquid_ctxs)
        kraken, err_k = fk.result()
        hyper, err_h = fh.result()
    if err_k:
        errors.append(f"kraken_futures -> {err_k}")
    if err_h:
        errors.append(f"hyperliquid -> {err_h}")

    prev_by_id = {r["id"]: r for r in (previous or {}).get("crypto", []) if "id" in r}

    for cid, product, kraken_sym, hl_name in CRYPTO:
        row = {"id": cid, "group": "crypto", "status": "ok", "errors": []}
        try:
            with ThreadPoolExecutor(max_workers=2) as pool:
                f24 = pool.submit(coinbase_24h, product)
                fcl = pool.submit(coinbase_daily_closes, product)
                last, chg24 = f24.result()
                closes = fcl.result()
            daily = [c for _, c in changes(closes, "pct")]
            z, ewma, floor = unusual_move_score(daily, chg24)
            row.update({
                "price": last, "price_source": f"coinbase:{product}",
                "change_24h_pct": round(chg24, 3),
                "z": None if z is None else round(z, 2),
                "flag": z is not None and abs(z) >= Z_FLAG,
                "note": "z compares a rolling 24h change with daily-close volatility; approximate",
            })
        except Exception as e:  # noqa: BLE001
            row["errors"].append(f"coinbase:{product} -> {e}")
            row["flag"] = False

        perps = {}
        if kraken and kraken_sym in kraken:
            t = kraken[kraken_sym]
            perps["kraken"] = {
                "symbol": kraken_sym,
                "funding_rate_raw": t.get("fundingRate"),
                "funding_rate_prediction_raw": t.get("fundingRatePrediction"),
                "open_interest": t.get("openInterest"),
                "mark_price": t.get("markPrice"),
                "units_note": "funding field units UNVERIFIED; do not interpret until confirmed",
            }
        if hyper and hl_name in hyper:
            c = hyper[hl_name]
            perps["hyperliquid"] = {
                "funding_rate_raw": c.get("funding"),
                "open_interest": c.get("openInterest"),
                "mark_price": c.get("markPx"),
                "units_note": "funding believed to be an hourly fraction; UNVERIFIED",
            }
        # open interest change vs the previous snapshot, same venue
        prev = prev_by_id.get(cid, {}).get("perps", {})
        for venue, p in perps.items():
            try:
                now_oi = float(p["open_interest"])
                old_oi = float(prev[venue]["open_interest"])
                p["oi_change_pct_vs_prev_snapshot"] = round((now_oi / old_oi - 1) * 100, 2)
                p["prev_snapshot_utc"] = previous.get("generated_utc")
            except (KeyError, TypeError, ValueError, ZeroDivisionError):
                p["oi_change_pct_vs_prev_snapshot"] = None
        row["perps"] = perps
        if not perps:
            row["errors"].append("no perpetual data from any venue")
        if row["errors"] and "price" not in row:
            row["status"] = "failed"
        out.append(row)
    return out, errors


# ---------------------------------------------------------------- output

def fmt(v, nd=2):
    return "n/a" if v is None else f"{v:,.{nd}f}"


def to_markdown(snap):
    L = [f"# Data snapshot {snap['generated_et']}", "",
         "Machine-generated. Numbers here are the only numbers the letter may use.", ""]
    ranked = snap["flag_groups_ranked"]
    L.append("**Flagged groups (top two get commentary):** " +
             (", ".join(f"{g['group']} (max |z| {g['max_abs_z']})" for g in ranked) if ranked else "none"))
    L += ["", "| Row | Value | As of | Change | z | Flag | Stale | Source |",
          "|---|---|---|---|---|---|---|---|"]
    for r in snap["rows"]:
        if r["status"] != "ok":
            L.append(f"| {r['label']} | FAILED | | | | | | {'; '.join(r['failed_sources'])[:120]} |")
            continue
        chg = "n/a" if r["change"] is None else f"{r['change']:+.2f} {r['change_unit']}"
        src = r["source"] + (" (experimental)" if r["experimental_source"] else "")
        L.append(f"| {r['label']} | {fmt(r['value'], 3)} | {r['last_date']} | {chg} | "
                 f"{fmt(r['z'])} | {'**YES**' if r['flag'] else ''} | {'yes' if r['stale'] else ''} | {src} |")
    L += ["", "## Crypto", ""]
    for c in snap["crypto"]:
        L.append(f"**{c['id']}**: price {fmt(c.get('price'))}, 24h {fmt(c.get('change_24h_pct'))}%, "
                 f"z {fmt(c.get('z'))}{' **FLAG**' if c.get('flag') else ''}")
        for venue, p in c.get("perps", {}).items():
            L.append(f"- {venue}: funding (raw, units unverified) {p.get('funding_rate_raw')}, "
                     f"OI {p.get('open_interest')}, OI change vs prior snapshot "
                     f"{fmt(p.get('oi_change_pct_vs_prev_snapshot'))}%")
        for e in c.get("errors", []):
            L.append(f"- error: {e}")
        L.append("")
    if snap["errors"]:
        L += ["", "## Source errors", ""] + [f"- {e}" for e in snap["errors"]]
    L += ["", "Stale = more than one weekday old (market holidays not yet accounted for)."]
    return "\n".join(L) + "\n"


def main():
    now_utc = datetime.now(timezone.utc)
    now_et = now_utc.astimezone(ET)
    os.makedirs(os.path.join(DATA_DIR, "snapshots"), exist_ok=True)

    previous = None
    latest_path = os.path.join(DATA_DIR, "latest.json")
    if os.path.exists(latest_path):
        try:
            with open(latest_path) as f:
                previous = json.load(f)
        except (OSError, json.JSONDecodeError):
            previous = None

    t_start = time.monotonic()
    with ThreadPoolExecutor(max_workers=12) as pool:
        row_futures = [pool.submit(build_row, *r, today_et=now_et.date()) for r in ROWS]
        crypto_future = pool.submit(build_crypto, previous)
        rows = [f.result() for f in row_futures]
        crypto, crypto_errors = crypto_future.result()
    elapsed = round(time.monotonic() - t_start, 1)

    groups = {}
    for r in rows + crypto:
        if r.get("flag") and r.get("z") is not None:
            groups[r["group"]] = max(groups.get(r["group"], 0), abs(r["z"]))
    ranked = [{"group": g, "max_abs_z": round(z, 2)}
              for g, z in sorted(groups.items(), key=lambda kv: -kv[1])][:2]

    errors = [e for r in rows for e in r.get("failed_sources", [])] + crypto_errors
    snap = {
        "schema_version": 1,
        "generated_utc": now_utc.isoformat(timespec="seconds"),
        "generated_et": now_et.strftime("%Y-%m-%d %H:%M %Z"),
        "parameters": {"ewma_lambda": EWMA_LAMBDA, "floor_fraction": FLOOR_FRACTION,
                       "floor_window": FLOOR_WINDOW, "z_flag": Z_FLAG},
        "rows": rows,
        "crypto": crypto,
        "flag_groups_ranked": ranked,
        "rows_ok": sum(r["status"] == "ok" for r in rows),
        "rows_failed": sum(r["status"] != "ok" for r in rows),
        "errors": errors,
        "fetch_seconds_total": elapsed,
    }

    with open(latest_path, "w") as f:
        json.dump(snap, f, indent=2)
    with open(os.path.join(DATA_DIR, "snapshots", f"{now_et.date().isoformat()}.json"), "w") as f:
        json.dump(snap, f, indent=2)
    with open(os.path.join(DATA_DIR, "latest.md"), "w") as f:
        f.write(to_markdown(snap))

    print(f"fetch time: {elapsed}s")
    print(f"rows ok: {snap['rows_ok']}, rows failed: {snap['rows_failed']}, "
          f"crypto ok: {sum(c['status'] == 'ok' for c in crypto)}")
    for e in errors:
        print("  error:", e)

    if snap["rows_failed"]:
        # Shows on the Actions run page; does not change the exit rule below.
        print(f"::warning::{snap['rows_failed']} of {len(rows)} dashboard rows failed")
    ok_anything = snap["rows_ok"] > 0 or any(c["status"] == "ok" for c in crypto)
    sys.exit(0 if ok_anything else 1)


if __name__ == "__main__":
    main()
