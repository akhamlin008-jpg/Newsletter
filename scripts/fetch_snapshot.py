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
#
# Each row lists sources newest-first. The first source whose quote is live
# (a trade within LIVE_MAX_AGE_MIN) is used; if none is live, the most recent
# quote is used and labeled as a prior close / official value with its date.
LIVE_MAX_AGE_MIN = 60

LAGGED = "official end-of-day series, published with a lag; no free live source"
CASH = "cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)"

ROWS = [
    # id, label, group, change type, [sources], options
    ("UST2Y", "US 2-year yield", "rates", "bp",
     [("cnbc", "US2Y"), ("yahoo", "2YY=F"), ("fred", "DGS2")], {"hist": ("fred", "DGS2")}),
    ("UST10Y", "US 10-year yield", "rates", "bp",
     [("cnbc", "US10Y"), ("yahoo", "10Y=F"), ("yahoo", "^TNX"), ("fred", "DGS10")], {"hist": ("fred", "DGS10")}),
    # S2S10 (2s10s) is computed from the two rows above; see build_spread_row.
    ("REAL10Y", "10-year real yield (TIPS)", "rates", "bp", [("fred", "DFII10")], {"note": LAGGED}),
    ("BE10Y", "10-year breakeven inflation", "rates", "bp", [("fred", "T10YIE")], {"note": LAGGED}),
    ("SOFR", "SOFR", "rates", "bp", [("nyfed", "SOFR"), ("fred", "SOFR")],
     {"hist": ("fred", "SOFR"),
      "note": "NY Fed publishes ~8:00 AM ET for the prior business day; before that, the latest is the previous day's"}),
    ("SOFR_FUT", "3M SOFR futures implied rate (front)", "rates", "bp", [("yahoo", "SR3=F")],
     {"transform": "100-minus", "note": "100 minus futures price; forward-looking proxy for SOFR"}),
    ("DXY", "US dollar index (DXY)", "dollar", "pct", [("yahoo", "DX-Y.NYB"), ("yahoo", "DX=F")], {}),
    ("USDJPY", "USD/JPY", "dollar", "pct", [("yahoo", "JPY=X"), ("fred", "DEXJPUS")], {}),
    ("EURUSD", "EUR/USD", "dollar", "pct", [("yahoo", "EURUSD=X"), ("fred", "DEXUSEU")], {}),
    ("USD_BROAD", "Broad trade-weighted dollar", "dollar", "pct", [("fred", "DTWEXBGS")],
     {"note": LAGGED + "; use DXY / EUR/USD / USD/JPY for the live picture"}),
    ("ES", "S&P 500 futures (ES)", "equity", "pct", [("yahoo", "ES=F")], {}),
    ("NQ", "Nasdaq 100 futures (NQ)", "equity", "pct", [("yahoo", "NQ=F")], {}),
    ("RTY", "Russell 2000 futures (RTY)", "equity", "pct", [("yahoo", "RTY=F")], {}),
    ("SPX", "S&P 500 index (cash)", "equity", "pct", [("yahoo", "^GSPC"), ("fred", "SP500")], {"note": CASH}),
    ("NDX", "Nasdaq 100 index (cash)", "equity", "pct", [("yahoo", "^NDX"), ("fred", "NASDAQ100")], {"note": CASH}),
    ("RUT", "Russell 2000 index (cash)", "equity", "pct", [("yahoo", "^RUT")], {"note": CASH}),
    ("VIX", "VIX (spot)", "vol", "diff", [("cboe", "VIX"), ("yahoo", "^VIX"), ("fred", "VIXCLS")],
     {"hist": ("cboe_vix", "VIX"),
      "note": "Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close"}),
    ("VX", "VIX futures (front month)", "vol", "diff", [("yahoo", "VX=F")],
     {"note": "futures price, not the same number as spot VIX"}),
    ("WTI", "WTI crude", "commodities", "pct", [("yahoo", "CL=F"), ("fred", "DCOILWTICO")], {}),
    ("BRENT", "Brent crude", "commodities", "pct", [("yahoo", "BZ=F"), ("fred", "DCOILBRENTEU")], {}),
    ("GOLD", "Gold", "commodities", "pct", [("yahoo", "GC=F")], {}),
    ("COPPER", "Copper", "commodities", "pct", [("yahoo", "HG=F")], {}),
]

EXPERIMENTAL_SOURCES = {"yahoo"}   # unofficial endpoint; can break without notice

# Futures roll check (#1). Yahoo's =F series splice contracts without adjustment,
# so a contract switch shows up as a one-day jump against the underlying.
# Each futures row is compared with a reference that has no roll.
ROLL_REFS = {
    "ES": [("fred", "SP500"), ("yahoo", "^GSPC")],
    "RTY": [("yahoo", "^RUT")],
    "NQ": [("fred", "NASDAQ100"), ("yahoo", "^NDX")],
    "GOLD": [("yahoo", "GLD")],
    "COPPER": [("yahoo", "CPER")],
}
QUARTERLY_ROLL_ROWS = {"ES", "NQ", "RTY"}   # CME equity index futures: Mar/Jun/Sep/Dec
ROLL_Z = 4.0          # [TUNE] robust z of (futures change - reference change) that marks a roll
ROLL_MIN_GAP = 0.25   # [TUNE] percent; smaller gaps are never called a roll
ROLL_LOOKBACK = 10    # recent observations listed in possible_roll_dates

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


YF_LOCK = threading.Lock()   # one Yahoo request at a time to avoid rate limits


def fetch_yahoo(symbol):
    """Daily closes from Yahoo Finance via yfinance, as [(date, close)].

    For futures (=F), the newest bar during the overnight session is the
    in-progress session, so its close is the latest traded price.
    """
    try:
        import yfinance as yf
    except ImportError:
        raise RuntimeError("yfinance not installed (pip install yfinance)") from None
    with YF_LOCK:
        try:
            df = yf.Ticker(symbol).history(start=HISTORY_START, interval="1d",
                                           auto_adjust=False, raise_errors=True)
        except Exception as e:
            raise RuntimeError(f"{type(e).__name__}: {str(e)[:150]}") from None
        time.sleep(0.5)
    if df is None or df.empty or "Close" not in df.columns:
        raise RuntimeError("Yahoo returned no data")
    out = []
    for ts, close in df["Close"].items():
        if close is None or math.isnan(close):
            continue
        out.append((ts.date(), float(close)))
    if not out:
        raise RuntimeError("Yahoo returned no usable closes")
    return sorted(out)


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


FETCHERS = {"fred": fetch_fred, "yahoo": fetch_yahoo, "cboe_vix": fetch_cboe_vix}


# ---------------------------------------------------------------- math

_CACHE = {}
_CACHE_LOCK = threading.Lock()


def get_series(src, sid):
    """Fetch once per run; concurrent callers wait for the first fetch."""
    with _CACHE_LOCK:
        entry = _CACHE.get((src, sid))
        owner = entry is None
        if owner:
            entry = _CACHE[(src, sid)] = {"done": threading.Event()}
    if owner:
        try:
            entry["value"] = FETCHERS[src](sid)
        except Exception as e:  # noqa: BLE001
            entry["error"] = e
        finally:
            entry["done"].set()
    else:
        entry["done"].wait()
    if "error" in entry:
        raise RuntimeError(str(entry["error"]))
    return entry["value"]


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

def third_friday(y, m):
    d = date(y, m, 15)
    return d + timedelta(days=(4 - d.weekday()) % 7)


def equity_roll_window(today):
    """(roll_date, expiry) if today is in a quarterly equity-futures roll window.

    CME's roll date is 8 days before expiry (third Friday). Yahoo's switch date
    is not documented, so the window runs from the roll date to 3 days after expiry.
    """
    for y in (today.year - 1, today.year, today.year + 1):
        for m in (3, 6, 9, 12):
            expiry = third_friday(y, m)
            roll = expiry - timedelta(days=8)
            if roll <= today <= expiry + timedelta(days=3):
                return roll, expiry
    return None


def roll_suspects(fut, ref):
    """Dates where the futures daily % change departs sharply from the reference's.

    Only compares days where both series have the same previous date, so
    holidays and missing bars don't create false jumps.
    Returns (suspect_dates, threshold_pct, compared_dates) or None if too little overlap.
    """
    ref_pos = {d: i for i, (d, _) in enumerate(ref)}
    diffs = []
    for (d0, f0), (d1, f1) in zip(fut, fut[1:]):
        i0, i1 = ref_pos.get(d0), ref_pos.get(d1)
        if i0 is None or i1 is None or i1 != i0 + 1 or f0 <= 0 or ref[i0][1] <= 0:
            continue
        fchg = (f1 / f0 - 1) * 100
        rchg = (ref[i1][1] / ref[i0][1] - 1) * 100
        diffs.append((d1, fchg - rchg))
    if len(diffs) < MIN_CHANGES:
        return None
    vals = sorted(x for _, x in diffs)
    med = vals[len(vals) // 2]
    mad = sorted(abs(x - med) for x in vals)[len(vals) // 2]
    thr = max(ROLL_Z * 1.4826 * mad, ROLL_MIN_GAP)
    return {d for d, x in diffs if abs(x - med) > thr}, thr, {d for d, _ in diffs}


def check_roll(row_id, fut_series, today_et):
    """Returns (info dict, set of dates to leave out of the volatility history)."""
    info, exclude = {}, set()
    last_date = fut_series[-1][0]
    ref_errors = []
    result = ref_used = None
    for src, sid in ROLL_REFS[row_id]:
        try:
            result = roll_suspects(fut_series, get_series(src, sid))
            ref_used = f"{src}:{sid}"
            if result is not None:
                break
        except Exception as e:  # noqa: BLE001
            ref_errors.append(f"{src}:{sid} -> {e}")
    if result is None:
        why = "; ".join(ref_errors) or "too little overlap with reference"
        info["roll_check"] = f"unavailable ({why})"
    else:
        suspects, thr, compared = result
        exclude = suspects
        recent = sorted(d for d, _ in fut_series[-ROLL_LOOKBACK:] if d in suspects)
        info["roll_reference"] = ref_used
        info["roll_threshold_pct"] = round(thr, 3)
        info["possible_roll_dates"] = [d.isoformat() for d in recent]
        if last_date in suspects:
            info["roll_check"] = "POSSIBLE ROLL on latest change; flag suppressed"
        elif last_date in compared:
            info["roll_check"] = "ok"
        else:
            info["roll_check"] = "latest change not checkable (reference has no close for that date yet)"
    if row_id in QUARTERLY_ROLL_ROWS:
        win = equity_roll_window(today_et)
        if win:
            info["roll_window"] = (f"quarterly roll window: roll date {win[0].isoformat()}, "
                                   f"expiry {win[1].isoformat()}; a jump may be the contract switch")
    return info, exclude


# ---------------------------------------------------------------- live quotes
# Every quoter returns a dict:
#   value, time (tz-aware), basis ("last trade" | "close" | "official"),
#   prev (previous session's close/official value), prev_date,
#   hist (daily [(date, value)] ending at prev; may be None -> row's "hist" option)

def close_time(d):
    return datetime(d.year, d.month, d.day, 16, 0, tzinfo=ET)


def daily_quote(series, basis):
    if len(series) < 2:
        raise RuntimeError("fewer than 2 observations")
    (pd_, pv), (d, v) = series[-2], series[-1]
    return {"value": v, "time": close_time(d), "date": d, "basis": basis,
            "prev": pv, "prev_date": pd_, "hist": series[:-1]}


def session_date(symbol, ts):
    """Trading date a quote belongs to. CME futures sessions open ~6 PM ET for the next day."""
    t = ts.astimezone(ET)
    d = t.date()
    if symbol.endswith("=F") and t.hour >= 18:
        d += timedelta(days=1)
    return d


def quote_yahoo(symbol):
    daily = get_series("yahoo", symbol)
    import yfinance as yf  # installed by the workflow; fetch_yahoo already checked it
    with YF_LOCK:
        try:
            df = yf.Ticker(symbol).history(period="5d", interval="1m", prepost=True,
                                           auto_adjust=False, raise_errors=True)
            intraday_error = None
        except Exception as e:  # noqa: BLE001
            df, intraday_error = None, f"{type(e).__name__}: {str(e)[:100]}"
        time.sleep(0.3)
    closes = None if df is None or df.empty or "Close" not in df.columns else df["Close"].dropna()
    if closes is None or len(closes) == 0:
        q = daily_quote(daily, "close")
        q["note_intraday"] = f"no intraday data ({intraday_error or 'empty'}); showing daily close"
        return q
    ts = closes.index[-1].to_pydatetime()
    value = float(closes.iloc[-1])
    sess = session_date(symbol, ts)
    before = [x for x in daily if x[0] < sess]
    if not before:
        raise RuntimeError("no prior close before the current session")
    return {"value": value, "time": ts, "date": sess, "basis": "last trade",
            "prev": before[-1][1], "prev_date": before[-1][0], "hist": before}


def quote_fred(series_id):
    return daily_quote(get_series("fred", series_id), "official")


def _num(x):
    if x is None:
        raise ValueError("missing")
    return float(str(x).replace("%", "").replace(",", "").replace("+", "").strip())


def _parse_time(text):
    text = str(text).strip()
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S.%f",
                "%Y-%m-%dT%H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            t = datetime.strptime(text, fmt)
        except ValueError:
            continue
        # Naive timestamps are read as ET. If the feed actually uses Central time,
        # the quote looks an hour older than it is (never newer).
        return t if t.tzinfo else t.replace(tzinfo=ET)
    raise ValueError(f"unrecognized timestamp {text!r}")


def fetch_cnbc_all(_):
    # CNBC's public quote feed (Tradeweb cash Treasury yields, updated overnight).
    url = ("https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol"
           "?symbols=US2Y%7CUS10Y&requestMethod=itv&noform=1&partnerId=2&fund=1"
           "&exthrs=1&output=json&events=1")
    text = http_get(url)
    try:
        quotes = json.loads(text)["FormattedQuoteResult"]["FormattedQuote"]
    except (ValueError, KeyError, TypeError):
        raise RuntimeError(f"unexpected CNBC response: {snippet(text)}") from None
    return {q.get("symbol"): q for q in quotes}


def quote_cnbc(symbol):
    q = get_series("cnbc_all", "").get(symbol)
    if q is None:
        raise RuntimeError(f"{symbol} missing from CNBC response")
    try:
        value = _num(q.get("last"))
        ts = _parse_time(q.get("last_time") or q.get("last_timedate"))
    except ValueError as e:
        raise RuntimeError(f"CNBC {symbol}: {e}; keys={sorted(q)[:12]}") from None
    if not 0 < value < 20:
        raise RuntimeError(f"CNBC {symbol}: implausible yield {value}")
    try:
        prev = _num(q.get("previous_day_closing"))
    except ValueError:
        prev = None
    return {"value": value, "time": ts, "date": ts.astimezone(ET).date(), "basis": "last trade",
            "prev": prev, "prev_date": None, "hist": None}


def fetch_cboe_quote(_):
    return json.loads(http_get("https://cdn.cboe.com/api/global/delayed_quotes/quotes/_VIX.json"))


def quote_cboe(_):
    j = get_series("cboe_quote", "VIX")
    d = j.get("data") or {}
    try:
        value = _num(d.get("current_price") if d.get("current_price") is not None else d.get("close"))
        ts = _parse_time(d.get("last_trade_time") or j.get("timestamp"))
    except ValueError as e:
        raise RuntimeError(f"Cboe VIX quote: {e}; keys={sorted(d)[:12]}") from None
    try:
        prev = _num(d.get("prev_day_close"))
    except ValueError:
        prev = None
    return {"value": value, "time": ts, "date": ts.astimezone(ET).date(), "basis": "last trade",
            "prev": prev, "prev_date": None, "hist": None}


def fetch_nyfed_sofr(_):
    data = json.loads(http_get("https://markets.newyorkfed.org/api/rates/secured/sofr/last/2.json"))
    rows = sorted(((parse_date(r["effectiveDate"]), float(r["percentRate"]))
                   for r in data.get("refRates", [])))
    if len(rows) < 2:
        raise RuntimeError("NY Fed returned fewer than 2 SOFR values")
    return rows


def quote_nyfed(_):
    q = daily_quote(get_series("nyfed_sofr", "SOFR"), "official")
    q["hist"] = None  # only 2 values; the row uses FRED history for volatility
    return q


FETCHERS.update({"cnbc_all": fetch_cnbc_all, "cboe_quote": fetch_cboe_quote,
                 "nyfed_sofr": fetch_nyfed_sofr})
QUOTERS = {"yahoo": quote_yahoo, "fred": quote_fred, "cnbc": quote_cnbc,
           "cboe": quote_cboe, "nyfed": quote_nyfed}


def one_change(prev, value, kind):
    if prev is None:
        return None
    if kind == "bp":
        return (value - prev) * 100.0
    if kind == "diff":
        return value - prev
    return None if prev <= 0 else (value / prev - 1.0) * 100.0


def age_minutes(q, now):
    return (now - q["time"]).total_seconds() / 60.0


def is_live(q, now):
    return q["basis"] == "last trade" and -5 <= age_minutes(q, now) <= LIVE_MAX_AGE_MIN


def status_label(q, now):
    t = q["time"].astimezone(ET)
    if is_live(q, now):
        return f"LIVE (~{max(0, round(age_minutes(q, now)))} min old)"
    if q["basis"] == "last trade":
        return f"not trading now; last trade {t:%m-%d %H:%M} ET"
    if q["basis"] == "official":
        return f"official value for {q['date'].isoformat()} (not live)"
    return f"prior close {q['date'].isoformat()} (not live)"


def apply_transform(q, how):
    if how != "100-minus":
        return q
    f = lambda v: None if v is None else 100.0 - v  # noqa: E731
    q = dict(q)
    q["value"], q["prev"] = f(q["value"]), f(q["prev"])
    if q.get("hist"):
        q["hist"] = [(d, 100.0 - v) for d, v in q["hist"]]
    return q


def build_row(row_id, label, group, kind, chain, opts, now):
    errors, quotes = [], []
    t0 = time.monotonic()
    for src, sid in chain:
        t1 = time.monotonic()
        try:
            q = apply_transform(QUOTERS[src](sid), opts.get("transform"))
            q["src"], q["sid"] = src, sid
            quotes.append(q)
            if is_live(q, now):
                break
        except Exception as e:  # noqa: BLE001
            errors.append(f"{src}:{sid} -> {e} ({time.monotonic() - t1:.1f}s)")
    if not quotes:
        return {"id": row_id, "label": label, "group": group, "status": "failed",
                "failed_sources": errors, "flag": False, "note": opts.get("note")}

    live = [q for q in quotes if is_live(q, now)]
    q = live[0] if live else max(quotes, key=lambda x: x["time"])  # max keeps chain order on ties
    skipped = [f"{x['src']}:{x['sid']} ({status_label(x, now)})" for x in quotes if x is not q]

    hist = q.get("hist")
    if not hist and opts.get("hist"):
        try:
            hist = apply_transform({"value": 0, "prev": None, "hist": get_series(*opts["hist"])},
                                   opts.get("transform"))["hist"]
        except Exception as e:  # noqa: BLE001
            errors.append(f"history {opts['hist'][0]}:{opts['hist'][1]} -> {e}")
            hist = None
    if q["prev"] is None and hist:
        q["prev"], q["prev_date"] = hist[-1][1], hist[-1][0]

    row = {}
    exclude = set()
    if q["src"] == "yahoo" and row_id in ROLL_REFS and hist:
        full = hist if q["basis"] == "last trade" else hist + [(q["date"], q["value"])]
        row, exclude = check_roll(row_id, full, now.astimezone(ET).date())
        if q["basis"] == "last trade":
            row["roll_check"] = ("last completed session: " + row.get("roll_check", "n/a")
                                 + "; the live move vs prior close can't be checked before the cash open")

    latest = one_change(q["prev"], q["value"], kind)
    z = ewma = floor = None
    if latest is not None and hist:
        history = [c for d, c in changes(hist, kind) if d not in exclude]
        z, ewma, floor = unusual_move_score(history, latest)
    flag = z is not None and abs(z) >= Z_FLAG
    if flag and q["basis"] != "last trade" and q["date"] in exclude:
        flag = False

    row.update({
        "id": row_id, "label": label, "group": group,
        "source": f"{q['src']}:{q['sid']}",
        "experimental_source": q["src"] in EXPERIMENTAL_SOURCES or q["src"] in {"cnbc", "cboe"},
        "live": is_live(q, now),
        "status_label": status_label(q, now),
        "value": round(q["value"], 6),
        "value_time_et": q["time"].astimezone(ET).isoformat(timespec="minutes"),
        "basis": q["basis"],
        "prev_value": None if q["prev"] is None else round(q["prev"], 6),
        "prev_date": None if q.get("prev_date") is None else q["prev_date"].isoformat(),
        "change": None if latest is None else round(latest, 4),
        "change_unit": {"bp": "bp", "pct": "%", "diff": "pts"}[kind],
        "ewma_sigma": None if ewma is None else round(ewma, 4),
        "floor_sigma": None if floor is None else round(floor, 4),
        "z": None if z is None else round(z, 2),
        "flag": flag,
        "status": "ok",
        "fetch_seconds": round(time.monotonic() - t0, 1),
        "failed_sources": errors,
        "other_sources_checked": skipped,
    })
    if opts.get("note"):
        row["note"] = opts["note"]
    if q.get("note_intraday"):
        row["intraday_note"] = q["note_intraday"]
    if row["live"] and z is not None:
        row["z_note"] = "live move vs prior close, scored against full-day volatility (approximate)"
    return row


def build_spread_row(rows, now):
    """2s10s = live 10Y minus live 2Y; falls back to FRED T10Y2Y if either leg failed."""
    r2 = next(r for r in rows if r["id"] == "UST2Y")
    r10 = next(r for r in rows if r["id"] == "UST10Y")
    label = "2s10s spread (10Y minus 2Y)"
    if r2["status"] != "ok" or r10["status"] != "ok":
        row = build_row("S2S10", label, "rates", "bp", [("fred", "T10Y2Y")],
                        {"note": "a yield leg failed; showing FRED's end-of-day spread"}, now)
        return row
    value = r10["value"] - r2["value"]
    prev = (None if r10["prev_value"] is None or r2["prev_value"] is None
            else r10["prev_value"] - r2["prev_value"])
    latest = one_change(prev, value, "bp")
    z = ewma = floor = None
    errors = []
    try:
        hist = get_series("fred", "T10Y2Y")
        if latest is not None:
            z, ewma, floor = unusual_move_score([c for _, c in changes(hist, "bp")], latest)
    except Exception as e:  # noqa: BLE001
        errors.append(f"history fred:T10Y2Y -> {e}")
    older = min((r2, r10), key=lambda r: r["value_time_et"])
    row = {
        "id": "S2S10", "label": label, "group": "rates",
        "source": f"calc: {r10['source']} minus {r2['source']}",
        "experimental_source": r2["experimental_source"] or r10["experimental_source"],
        "live": r2["live"] and r10["live"],
        "status_label": (r2["status_label"] if older is r2 else r10["status_label"])
        if not (r2["live"] and r10["live"]) else older["status_label"],
        "value": round(value, 6), "value_time_et": older["value_time_et"],
        "basis": "calculated", "prev_value": None if prev is None else round(prev, 6),
        "prev_date": None,
        "change": None if latest is None else round(latest, 4), "change_unit": "bp",
        "ewma_sigma": None if ewma is None else round(ewma, 4),
        "floor_sigma": None if floor is None else round(floor, 4),
        "z": None if z is None else round(z, 2),
        "flag": z is not None and abs(z) >= Z_FLAG,
        "status": "ok", "failed_sources": errors,
    }
    if r2["source"].split(":")[0] != r10["source"].split(":")[0]:
        row["note"] = "legs come from different sources; spread is approximate"
    return row


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
    L += ["", "Status: LIVE = a trade within the last "
          f"{LIVE_MAX_AGE_MIN} min (free feeds are typically ~10-15 min delayed). "
          "Anything else is labeled with the date it refers to.",
          "", "| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |",
          "|---|---|---|---|---|---|---|---|"]
    for r in snap["rows"]:
        if r["status"] != "ok":
            L.append(f"| {r['label']} | FAILED | | | | | | {'; '.join(r['failed_sources'])[:160]} |")
            continue
        chg = "n/a" if r["change"] is None else f"{r['change']:+.2f} {r['change_unit']}"
        if r.get("prev_date"):
            chg += f" (vs {r['prev_date']})"
        src = r["source"] + (" (unofficial feed)" if r["experimental_source"] else "")
        if r.get("roll_check", "").startswith("POSSIBLE ROLL"):
            src += " **possible roll**"
        status = f"**{r['status_label']}**" if r["live"] else r["status_label"]
        t = r["value_time_et"].replace("T", " ")[5:16]
        if r["basis"] in ("close", "official"):
            t = t[:5] + " close"
        L.append(f"| {r['label']} | {fmt(r['value'], 3)} | {t} | {status} | {chg} | "
                 f"{fmt(r['z'])} | {'**YES**' if r['flag'] else ''} | {src} |")
    notes = []
    for r in snap["rows"]:
        parts = [r[k] for k in ("note", "intraday_note", "z_note", "roll_window") if r.get(k)]
        if "roll_check" in r:
            rc = f"roll check: {r['roll_check']}"
            if r.get("possible_roll_dates"):
                rc += f" (possible rolls in recent history: {', '.join(r['possible_roll_dates'])})"
            parts.append(rc)
        if r.get("status") == "ok" and r.get("failed_sources"):
            parts.append("fell back after: " + "; ".join(r["failed_sources"])[:200])
        if parts:
            notes.append(f"- **{r['label']}**: " + "; ".join(parts))
    if notes:
        L += ["", "## Row notes", ""] + notes
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
        row_futures = [pool.submit(build_row, *r, now=now_utc) for r in ROWS]
        crypto_future = pool.submit(build_crypto, previous)
        rows = [f.result() for f in row_futures]
        i10 = next(i for i, r in enumerate(rows) if r["id"] == "UST10Y")
        rows.insert(i10 + 1, build_spread_row(rows, now_utc))
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
        "schema_version": 2,
        "generated_utc": now_utc.isoformat(timespec="seconds"),
        "generated_et": now_et.strftime("%Y-%m-%d %H:%M %Z"),
        "parameters": {"ewma_lambda": EWMA_LAMBDA, "floor_fraction": FLOOR_FRACTION,
                       "floor_window": FLOOR_WINDOW, "z_flag": Z_FLAG},
        "rows": rows,
        "crypto": crypto,
        "flag_groups_ranked": ranked,
        "rows_ok": sum(r["status"] == "ok" for r in rows),
        "rows_live": sum(bool(r.get("live")) for r in rows),
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
    print(f"rows ok: {snap['rows_ok']} (live: {snap['rows_live']}), rows failed: {snap['rows_failed']}, "
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
