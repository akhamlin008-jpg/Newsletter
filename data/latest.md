# Data snapshot 2026-10-19 10:36 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.757 | 10-19 10:35 | **LIVE (~1 min old)** | +2.10 bp | n/a |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.123 | 10-19 10:36 | **LIVE (~0 min old)** | +2.50 bp | 0.49 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.366 | 10-19 10:35 | **LIVE (~1 min old)** | +0.40 bp | 0.12 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.780 | 10-15 close | official value for 2026-10-15 (not live) | -6.00 bp (vs 2026-10-14) | -1.28 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-16 close | official value for 2026-10-16 (not live) | +3.00 bp (vs 2026-10-15) | 1.73 |  | fred:T10YIE |
| SOFR | 3.880 | 10-16 close | official value for 2026-10-16 (not live) | -1.00 bp (vs 2026-10-15) | -0.30 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.1s) |
| US dollar index (DXY) | 101.941 | 10-19 10:26 | **LIVE (~10 min old)** | +0.10 % (vs 2026-10-16) | 0.31 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.434 | 10-19 10:36 | **LIVE (~0 min old)** | +0.18 % (vs 2026-10-16) | 0.45 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.121 | 10-19 10:35 | **LIVE (~1 min old)** | +0.01 % (vs 2026-10-16) | 0.04 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.602 | 10-09 close | official value for 2026-10-09 (not live) | +0.13 % (vs 2026-10-08) | 0.46 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,754.500 | 10-19 10:26 | **LIVE (~10 min old)** | +0.65 % (vs 2026-10-16) | 1.07 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,849.500 | 10-19 10:26 | **LIVE (~10 min old)** | +1.56 % (vs 2026-10-16) | 1.46 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,745.000 | 10-19 10:26 | **LIVE (~10 min old)** | +0.35 % (vs 2026-10-16) | 0.36 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,702.300 | 10-19 10:36 | **LIVE (~0 min old)** | +0.56 % (vs 2026-10-16) | 0.87 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,603.957 | 10-19 10:36 | **LIVE (~0 min old)** | +1.43 % (vs 2026-10-16) | 1.25 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,732.275 | 10-19 10:21 | **LIVE (~15 min old)** | +0.40 % (vs 2026-10-16) | 0.42 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.670 | 10-19 10:20 | **LIVE (~16 min old)** | -2.32 pts | -1.96 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.2s) |
| WTI crude | 97.610 | 10-19 10:26 | **LIVE (~10 min old)** | -3.75 % (vs 2026-10-16) | -1.49 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 108.170 | 10-19 10:26 | **LIVE (~10 min old)** | -1.54 % (vs 2026-10-16) | -0.66 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,167.400 | 10-19 10:26 | **LIVE (~10 min old)** | -0.33 % (vs 2026-10-16) | -0.28 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.546 | 10-19 10:26 | **LIVE (~10 min old)** | +0.23 % (vs 2026-10-16) | 0.19 |  | yahoo:HG=F (unofficial feed) |

## Row notes

- **US 2-year yield**: fell back after: history fred:DGS2 -> TimeoutError: The read operation timed out
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
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 81,875.28, 24h 1.09%, z 0.67
- kraken: funding (raw, units unverified) 0.637107177892, OI 2295.6068, OI change vs prior snapshot 1.31%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 39681.98744, OI change vs prior snapshot -5.59%

**ETH**: price 2,390.03, 24h 0.68%, z 0.31
- kraken: funding (raw, units unverified) 0.010462801648, OI 28188.291, OI change vs prior snapshot 1.73%
- hyperliquid: funding (raw, units unverified) 0.0000068578, OI 1081158.209, OI change vs prior snapshot -0.82%


## Source errors

- history fred:DGS2 -> TimeoutError: The read operation timed out
- yahoo:SR3=F -> no prior close before the current session (10.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.2s)
