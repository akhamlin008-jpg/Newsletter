# Data snapshot 2026-09-30 13:17 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.893 | 09-30 13:16 | **LIVE (~1 min old)** | +0.40 bp | 0.06 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.302 | 09-30 13:16 | **LIVE (~0 min old)** | +4.70 bp | 0.82 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.409 | 09-30 13:16 | **LIVE (~1 min old)** | +4.30 bp | 1.19 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.900 | 09-28 close | official value for 2026-09-28 (not live) | +7.00 bp (vs 2026-09-25) | 1.29 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 09-29 close | official value for 2026-09-29 (not live) | +1.00 bp (vs 2026-09-28) | 0.50 |  | fred:T10YIE |
| SOFR | 3.880 | 09-29 close | official value for 2026-09-29 (not live) | -2.00 bp (vs 2026-09-28) | -0.43 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.0s) |
| US dollar index (DXY) | 101.402 | 09-30 13:07 | **LIVE (~10 min old)** | +0.03 % (vs 2026-09-29) | 0.11 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.242 | 09-30 13:17 | **LIVE (~0 min old)** | -0.08 % (vs 2026-09-29) | -0.13 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.134 | 09-30 13:16 | **LIVE (~1 min old)** | -0.26 % (vs 2026-09-29) | -1.00 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,771.250 | 09-30 13:07 | **LIVE (~10 min old)** | +0.51 % (vs 2026-09-29) | 0.85 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,866.750 | 09-30 13:07 | **LIVE (~10 min old)** | +0.83 % (vs 2026-09-29) | 0.90 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,831.600 | 09-30 13:07 | **LIVE (~10 min old)** | +0.08 % (vs 2026-09-29) | 0.10 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,700.800 | 09-30 13:17 | **LIVE (~0 min old)** | +0.39 % (vs 2026-09-29) | 0.58 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,538.473 | 09-30 13:17 | **LIVE (~0 min old)** | +0.66 % (vs 2026-09-29) | 0.61 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,812.543 | 09-30 13:02 | **LIVE (~15 min old)** | +0.16 % (vs 2026-09-29) | 0.21 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.830 | 09-30 13:01 | **LIVE (~16 min old)** | -0.21 pts | -0.21 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.4s) |
| WTI crude | 90.910 | 09-30 13:07 | **LIVE (~10 min old)** | +1.71 % (vs 2026-09-29) | 0.60 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 98.260 | 09-30 13:07 | **LIVE (~10 min old)** | -4.22 % (vs 2026-09-29) | -1.50 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,185.900 | 09-30 13:07 | **LIVE (~10 min old)** | +0.15 % (vs 2026-09-29) | 0.11 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.628 | 09-30 13:07 | **LIVE (~10 min old)** | +1.28 % (vs 2026-09-29) | 0.89 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-21)
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-21)
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-18, 2026-09-21)
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 84,135.04, 24h 1.31%, z 0.59
- kraken: funding (raw, units unverified) 1.4728503843816385, OI 2423.9684, OI change vs prior snapshot -1.50%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 36112.80668, OI change vs prior snapshot 2.59%

**ETH**: price 2,688.69, 24h 0.59%, z 0.23
- kraken: funding (raw, units unverified) 0.018581289512500897, OI 26640.292, OI change vs prior snapshot 0.85%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1184084.818999999, OI change vs prior snapshot 0.09%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.4s)
