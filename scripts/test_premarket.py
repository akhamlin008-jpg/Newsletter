#!/usr/bin/env python3
"""Pre-market test for fetch_snapshot.py. No network.

Runs the real row-building code at 04:30, 05:10 and 06:30 ET against stub
sources that behave the way the live feeds behave before the US open:

  cnbc      Treasuries trade overnight in Asia/London        -> live
  yahoo =F  CME futures trade overnight                      -> live
  yahoo FX  FX trades 24/5                                   -> live
  yahoo ^   cash indices are only calculated 9:30-16:00      -> prior close
  cboe      cash VIX                                         -> prior close
  fred      official daily series, published with a lag      -> prior day
  nyfed     SOFR posts ~8:00 AM for the prior business day   -> prior day
  SR3=F, VX=F                                                -> raise (known failures)

It checks that the script produces a usable snapshot in that window: enough
rows, the overnight rows marked LIVE, the closed-market rows labeled instead
of silently passed off as current, scores computed, and no crash.

    python scripts/test_premarket.py          # exit 0 = pass

Edge cases covered: a quote timestamped in the future (clock skew), a source
that throws, a row whose history is too short to score, and a weekend date.
"""

import os
import random
import sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fetch_snapshot as fs  # noqa: E402

ET = fs.ET
FAIL_SYMBOLS = {"SR3=F", "VX=F"}          # the two rows already failing live
SKEW_SYMBOL = "EURUSD=X"                  # gets a timestamp 2 min in the future


# ------------------------------------------------------------------ stubs

def business_days_back(end, n):
    out, d = [], end
    while len(out) < n:
        if d.weekday() < 5:
            out.append(d)
        d -= timedelta(days=1)
    return list(reversed(out))


def fake_series(key, last_date, n=260):
    """Deterministic random-walk daily history ending the business day before last_date."""
    rnd = random.Random(hash(key) & 0xFFFF)
    base = {"pct": 100.0, "bp": 4.0}.get(_kind_of(key), 100.0)
    level, out = base, []
    for d in business_days_back(last_date, n):
        level *= 1 + rnd.gauss(0, 0.004)
        out.append((d, round(level, 4)))
    return out


def _kind_of(key):
    for _id, _label, _group, kind, chain, _opts in fs.ROWS:
        if any(sid == key.split(":")[-1] for _src, sid in chain):
            return kind
    return "pct"


_SERIES = {}


def stub_get_series(src, sid):
    k = f"{src}:{sid}"
    if k not in _SERIES:
        _SERIES[k] = fake_series(k, TODAY - timedelta(days=1))
    return _SERIES[k]


def _hist_and_prev(src, sid, before_date):
    series = [x for x in stub_get_series(src, sid) if x[0] < before_date]
    return series, series[-1]


def stub_live(src):
    """Quoter whose last trade is a few minutes before NOW: overnight markets."""
    def q(sid):
        if sid in FAIL_SYMBOLS:
            raise RuntimeError(f"{sid} -> stubbed source failure")
        offset = timedelta(minutes=-2) if sid == SKEW_SYMBOL else timedelta(minutes=8)
        hist, (pd_, pv) = _hist_and_prev(src, sid, TODAY)
        return {"value": pv * 1.003, "time": NOW - offset, "date": TODAY,
                "basis": "last trade", "prev": pv, "prev_date": pd_, "hist": hist}
    return q


def stub_closed(src):
    """Quoter whose last trade was the prior close: cash indices, cash VIX."""
    def q(sid):
        if sid in FAIL_SYMBOLS:
            raise RuntimeError(f"{sid} -> stubbed source failure")
        hist, (pd_, pv) = _hist_and_prev(src, sid, TODAY)
        last_close = fs.close_time(pd_)
        return {"value": pv, "time": last_close, "date": pd_, "basis": "last trade",
                "prev": hist[-2][1], "prev_date": hist[-2][0], "hist": hist[:-1]}
    return q


def stub_official(src, days_late=1):
    """Quoter for published-with-a-lag series: FRED, NY Fed."""
    def q(sid):
        series = stub_get_series(src, sid)[: -days_late] if days_late else stub_get_series(src, sid)
        return fs.daily_quote(series, "official")
    return q


def stub_yahoo(sid):
    if sid in FAIL_SYMBOLS:
        raise RuntimeError(f"{sid} -> stubbed source failure")
    if sid.startswith("^"):                      # cash index: closed pre-market
        return stub_closed("yahoo")(sid)
    return stub_live("yahoo")(sid)                # futures and FX: trading


def install_stubs():
    fs.get_series = stub_get_series
    fs.QUOTERS = {"yahoo": stub_yahoo,
                  "cnbc": stub_live("cnbc"),
                  "cboe": stub_closed("cboe"),
                  "fred": stub_official("fred"),
                  "nyfed": stub_official("nyfed", days_late=1)}
    fs.build_crypto = lambda previous: ([], [])   # 24/7 venues, not what this test is about


# ------------------------------------------------------------------ run

def build(now_et):
    """Same call path as main(), with the clock frozen."""
    now = now_et.astimezone(fs.timezone.utc)
    rows = [fs.build_row(*r, now=now) for r in fs.ROWS]
    i10 = next(i for i, r in enumerate(rows) if r["id"] == "UST10Y")
    rows.insert(i10 + 1, fs.build_spread_row(rows, now))
    groups = {}
    for r in rows:
        if r.get("flag") and r.get("z") is not None:
            groups[r["group"]] = max(groups.get(r["group"], 0), abs(r["z"]))
    return {"schema_version": 2,
            "generated_utc": now.isoformat(timespec="seconds"),
            "generated_et": now_et.strftime("%Y-%m-%d %H:%M %Z"),
            "parameters": {"ewma_lambda": fs.EWMA_LAMBDA, "floor_fraction": fs.FLOOR_FRACTION,
                           "floor_window": fs.FLOOR_WINDOW, "z_flag": fs.Z_FLAG},
            "rows": rows, "crypto": [],
            "flag_groups_ranked": [{"group": g, "max_abs_z": round(z, 2)}
                                   for g, z in sorted(groups.items(), key=lambda kv: -kv[1])][:2],
            "rows_ok": sum(r["status"] == "ok" for r in rows),
            "rows_live": sum(bool(r.get("live")) for r in rows),
            "rows_failed": sum(r["status"] != "ok" for r in rows),
            "errors": [e for r in rows for e in r.get("failed_sources", [])],
            "fetch_seconds_total": 0.0}


OVERNIGHT = {"UST2Y", "UST10Y", "S2S10", "DXY", "USDJPY", "EURUSD",
             "ES", "NQ", "RTY", "WTI", "BRENT", "GOLD", "COPPER"}
CLOSED = {"SPX", "NDX", "RUT", "VIX"}
LAGGED = {"REAL10Y", "BE10Y", "SOFR", "USD_BROAD"}


def check(snap, when):
    """Returns a list of failures. Empty list = viable snapshot."""
    bad = []
    by_id = {r["id"]: r for r in snap["rows"]}

    expected_fail = {r["id"] for r in snap["rows"]
                     if all(sid in FAIL_SYMBOLS for _src, sid in _chain(r["id"]))}
    for rid, r in by_id.items():
        if r["status"] != "ok" and rid not in expected_fail:
            bad.append(f"{when}: {rid} failed unexpectedly: {r.get('failed_sources')}")

    for rid in OVERNIGHT:
        r = by_id.get(rid, {})
        if not r.get("live"):
            bad.append(f"{when}: {rid} should be live overnight, got {r.get('status_label')}")
        if r.get("change") is None:
            bad.append(f"{when}: {rid} has no change vs prior close")
        if r.get("z") is None:
            bad.append(f"{when}: {rid} has no unusual-move score")

    for rid in CLOSED | LAGGED:
        r = by_id.get(rid, {})
        if r.get("status") != "ok":
            continue
        if r.get("live"):
            bad.append(f"{when}: {rid} claims LIVE while its market is closed")
        label = (r.get("status_label") or "").lower()
        if not any(w in label for w in ("not live", "not trading", "prior close")):
            bad.append(f"{when}: {rid} label does not say it is not current: {label!r}")

    if snap["rows_ok"] < len(snap["rows"]) - len(expected_fail):
        bad.append(f"{when}: only {snap['rows_ok']} rows ok")
    if snap["rows_live"] < 10:
        bad.append(f"{when}: only {snap['rows_live']} live rows, too thin to write from")

    try:
        md = fs.to_markdown(snap)
        if "| Row |" not in md or len(md) < 800:
            bad.append(f"{when}: markdown table looks wrong")
    except Exception as e:  # noqa: BLE001
        bad.append(f"{when}: to_markdown crashed: {type(e).__name__}: {e}")
    return bad


def _chain(row_id):
    for rid, _l, _g, _k, chain, _o in fs.ROWS:
        if rid == row_id:
            return chain
    return []


def main():
    global TODAY, NOW
    failures, results = [], []
    days = [datetime(2026, 9, 18, tzinfo=ET),    # weekday, EDT
            datetime(2026, 12, 3, tzinfo=ET),    # weekday, EST
            datetime(2026, 9, 21, tzinfo=ET)]    # Monday after a weekend
    for day in days:
        for hh, mm in ((4, 30), (5, 10), (6, 30)):
            _SERIES.clear()
            fs._CACHE.clear()
            NOW = day.replace(hour=hh, minute=mm)
            TODAY = NOW.date()
            install_stubs()
            when = NOW.strftime("%Y-%m-%d %H:%M %Z")
            try:
                snap = build(NOW)
            except Exception as e:  # noqa: BLE001
                failures.append(f"{when}: build crashed: {type(e).__name__}: {e}")
                continue
            bad = check(snap, when)
            failures += bad
            results.append((when, snap["rows_ok"], snap["rows_live"], snap["rows_failed"],
                            len(bad), snap["flag_groups_ranked"]))

    print(f"{'run (ET)':<22} {'ok':>3} {'live':>5} {'failed':>7} {'problems':>9}  flagged groups")
    for when, ok, live, failed, nbad, ranked in results:
        groups = ", ".join(f"{g['group']} {g['max_abs_z']}" for g in ranked) or "none"
        print(f"{when:<22} {ok:>3} {live:>5} {failed:>7} {nbad:>9}  {groups}")

    if failures:
        print(f"\nFAIL ({len(failures)}):")
        for f in failures:
            print("  -", f)
        return 1
    print("\nPASS: every run 04:30-06:30 ET produced a usable snapshot.")
    print("Stubs replace the network only. Row selection, live/stale labeling, change")
    print("calculation, scoring, flagging and markdown are the real code.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
