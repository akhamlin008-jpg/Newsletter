# Data snapshot 2026-11-23 15:05 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** equity (max |z| 3.07), vol (max |z| 2.41)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.662 | 11-23 15:05 | **LIVE (~0 min old)** | +4.90 bp | 0.74 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.920 | 11-23 15:05 | **LIVE (~0 min old)** | +0.80 bp | 0.14 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.258 | 11-23 15:05 | **LIVE (~0 min old)** | -4.10 bp | -1.21 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.880 | 11-19 close | official value for 2026-11-19 (not live) | +0.00 bp (vs 2026-11-18) | 0.00 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.150 | 11-20 close | official value for 2026-11-20 (not live) | -1.00 bp (vs 2026-11-19) | -0.41 |  | fred:T10YIE |
| SOFR | 3.920 | 11-20 close | official value for 2026-11-20 (not live) | +1.00 bp (vs 2026-11-19) | 0.46 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.8s) |
| US dollar index (DXY) | 104.341 | 11-23 14:55 | **LIVE (~11 min old)** | +0.51 % (vs 2026-11-20) | 1.56 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.889 | 11-23 15:05 | **LIVE (~1 min old)** | -0.51 % (vs 2026-11-20) | -1.48 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.091 | 11-23 15:05 | **LIVE (~1 min old)** | -0.58 % (vs 2026-11-20) | -1.74 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 122.650 | 11-13 close | official value for 2026-11-13 (not live) | +0.09 % (vs 2026-11-12) | 0.34 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,251.750 | 11-23 14:55 | **LIVE (~11 min old)** | +4.57 % (vs 2026-11-20) | 2.95 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 26,759.750 | 11-23 14:55 | **LIVE (~11 min old)** | +6.50 % (vs 2026-11-20) | 2.81 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,668.400 | 11-23 14:55 | **LIVE (~11 min old)** | +3.13 % (vs 2026-11-20) | 1.95 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,241.310 | 11-23 15:05 | **LIVE (~1 min old)** | +4.79 % (vs 2026-11-20) | 3.07 | **YES** | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 26,707.002 | 11-23 15:05 | **LIVE (~1 min old)** | +6.70 % (vs 2026-11-20) | 2.88 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,663.048 | 11-23 14:50 | **LIVE (~16 min old)** | +3.15 % (vs 2026-11-20) | 1.97 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 27.540 | 11-23 14:50 | **LIVE (~16 min old)** | -8.35 pts (vs 2026-11-20) | -2.41 | **YES** | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.8s) |
| WTI crude | 80.020 | 11-23 14:55 | **LIVE (~11 min old)** | -4.72 % (vs 2026-11-20) | -1.65 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 86.510 | 11-23 14:55 | **LIVE (~11 min old)** | -6.55 % (vs 2026-11-20) | -2.07 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 3,641.300 | 11-23 14:55 | **LIVE (~11 min old)** | +3.58 % (vs 2026-11-20) | 1.86 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.620 | 11-23 14:55 | **LIVE (~11 min old)** | +2.61 % (vs 2026-11-20) | 1.39 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate); fell back after: cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.1s)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 61,160.27, 24h 0.56%, z 0.21
- kraken: funding (raw, units unverified) 0.9446226340344788, OI 2247.2258, OI change vs prior snapshot -2.33%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 37152.9542, OI change vs prior snapshot -0.19%

**ETH**: price 1,727.39, 24h 0.52%, z 0.15
- kraken: funding (raw, units unverified) 0.000658786176167243, OI 33409.514, OI change vs prior snapshot -1.97%
- hyperliquid: funding (raw, units unverified) -0.0000140801, OI 607677.6764, OI change vs prior snapshot -1.57%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.8s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.8s)
