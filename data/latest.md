# Data snapshot 2026-11-05 11:24 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** vol (max |z| 5.75), equity (max |z| 3.7)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.523 | 11-05 11:24 | **LIVE (~0 min old)** | -5.80 bp | -1.08 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.843 | 11-05 11:24 | **LIVE (~0 min old)** | -4.90 bp | -0.88 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.320 | 11-05 11:24 | **LIVE (~0 min old)** | +0.90 bp | 0.25 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.650 | 11-03 close | official value for 2026-11-03 (not live) | +3.00 bp (vs 2026-11-02) | 0.66 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.260 | 11-04 close | official value for 2026-11-04 (not live) | -4.00 bp (vs 2026-11-03) | -1.75 |  | fred:T10YIE |
| SOFR | 3.940 | 11-04 close | official value for 2026-11-04 (not live) | -3.00 bp (vs 2026-11-03) | -1.18 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.3s) |
| US dollar index (DXY) | 101.587 | 11-05 11:14 | **LIVE (~11 min old)** | +0.08 % (vs 2026-11-04) | 0.29 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.917 | 11-05 11:24 | **LIVE (~1 min old)** | -0.35 % (vs 2026-11-04) | -0.91 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.123 | 11-05 11:24 | **LIVE (~1 min old)** | +0.17 % (vs 2026-11-04) | 0.64 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,493.000 | 11-05 11:14 | **LIVE (~11 min old)** | -2.95 % (vs 2026-11-04) | -3.70 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,160.250 | 11-05 11:14 | **LIVE (~11 min old)** | -4.92 % (vs 2026-11-04) | -3.59 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,782.000 | 11-05 11:14 | **LIVE (~11 min old)** | -2.93 % (vs 2026-11-04) | -3.14 | **YES** | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,476.420 | 11-05 11:24 | **LIVE (~1 min old)** | -2.76 % (vs 2026-11-04) | -3.44 | **YES** | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,172.230 | 11-05 11:24 | **LIVE (~1 min old)** | -4.45 % (vs 2026-11-04) | -3.19 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,768.016 | 11-05 11:09 | **LIVE (~16 min old)** | -3.11 % (vs 2026-11-04) | -3.27 | **YES** | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 25.740 | 11-05 11:08 | **LIVE (~16 min old)** | +9.13 pts | 5.75 | **YES** | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.5s) |
| WTI crude | 90.610 | 11-05 11:14 | **LIVE (~11 min old)** | +2.83 % (vs 2026-11-04) | 0.81 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 97.120 | 11-05 11:14 | **LIVE (~11 min old)** | +2.64 % (vs 2026-11-04) | 0.69 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,106.200 | 11-05 11:14 | **LIVE (~11 min old)** | +0.82 % (vs 2026-11-04) | 0.53 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.292 | 11-05 11:14 | **LIVE (~11 min old)** | -1.74 % (vs 2026-11-04) | -1.27 |  | yahoo:HG=F (unofficial feed) |

## Row notes

- **US 2-year yield**: live move vs prior close, scored against full-day volatility (approximate)
- **US 10-year yield**: live move vs prior close, scored against full-day volatility (approximate)
- **10-year real yield (TIPS)**: official end-of-day series, published with a lag; no free live source
- **10-year breakeven inflation**: official end-of-day series, published with a lag; no free live source
- **SOFR**: NY Fed publishes ~8:00 AM ET for the prior business day; before that, the latest is the previous day's
- **3M SOFR futures implied rate (front)**: 100 minus futures price; forward-looking proxy for SOFR
- **US dollar index (DXY)**: live move vs prior close, scored against full-day volatility (approximate)
- **USD/JPY**: live move vs prior close, scored against full-day volatility (approximate)
- **EUR/USD**: live move vs prior close, scored against full-day volatility (approximate)
- **Broad trade-weighted dollar**: official end-of-day series, published with a lag; no free live source; use DXY / EUR/USD / USD/JPY for the live picture
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 76,777.94, 24h -4.58%, z -2.47 **FLAG**
- kraken: funding (raw, units unverified) 2.4453034087185, OI 2965.2474, OI change vs prior snapshot 2.83%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41390.4094600001, OI change vs prior snapshot 6.63%

**ETH**: price 2,279.79, 24h -6.29%, z -2.60 **FLAG**
- kraken: funding (raw, units unverified) 0.02266795041875075, OI 34053.645, OI change vs prior snapshot -9.00%
- hyperliquid: funding (raw, units unverified) 0.0000062012, OI 960868.0142000009, OI change vs prior snapshot -1.63%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.3s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.5s)
