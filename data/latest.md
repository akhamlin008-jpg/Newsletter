# Data snapshot 2026-11-16 12:24 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.846 | 11-16 12:23 | **LIVE (~1 min old)** | -2.80 bp | -0.37 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.135 | 11-16 12:24 | **LIVE (~0 min old)** | -1.80 bp | -0.29 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.289 | 11-16 12:23 | **LIVE (~1 min old)** | +1.00 bp | 0.26 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.860 | 11-12 close | official value for 2026-11-12 (not live) | +8.00 bp (vs 2026-11-10) | 1.59 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.240 | 11-13 close | official value for 2026-11-13 (not live) | +0.00 bp (vs 2026-11-12) | 0.00 |  | fred:T10YIE |
| SOFR | 3.900 | 11-13 close | official value for 2026-11-13 (not live) | +0.00 bp (vs 2026-11-12) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.4s) |
| US dollar index (DXY) | 103.503 | 11-16 12:14 | **LIVE (~10 min old)** | +0.09 % (vs 2026-11-13) | 0.25 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.543 | 11-16 12:24 | **LIVE (~0 min old)** | -0.21 % (vs 2026-11-13) | -0.52 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.101 | 11-16 12:23 | **LIVE (~1 min old)** | -0.32 % (vs 2026-11-13) | -0.87 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,485.250 | 11-16 12:14 | **LIVE (~10 min old)** | -1.29 % (vs 2026-11-13) | -1.03 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,498.000 | 11-16 12:14 | **LIVE (~10 min old)** | -1.91 % (vs 2026-11-13) | -0.97 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,764.800 | 11-16 12:14 | **LIVE (~10 min old)** | -1.17 % (vs 2026-11-13) | -0.80 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,454.700 | 11-16 12:24 | **LIVE (~0 min old)** | -1.41 % (vs 2026-11-13) | -1.13 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,339.855 | 11-16 12:24 | **LIVE (~0 min old)** | -2.16 % (vs 2026-11-13) | -1.09 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,758.610 | 11-16 12:09 | **LIVE (~15 min old)** | -1.14 % (vs 2026-11-13) | -0.78 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 21.150 | 11-16 12:08 | **LIVE (~16 min old)** | +1.85 pts | 0.61 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.6s) |
| WTI crude | 86.400 | 11-16 12:14 | **LIVE (~10 min old)** | -2.44 % (vs 2026-11-13) | -0.79 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 93.370 | 11-16 12:14 | **LIVE (~10 min old)** | -2.58 % (vs 2026-11-13) | -0.73 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,869.800 | 11-16 12:14 | **LIVE (~10 min old)** | -0.42 % (vs 2026-11-13) | -0.28 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.011 | 11-16 12:14 | **LIVE (~10 min old)** | -1.12 % (vs 2026-11-13) | -0.77 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 64,988.98, 24h 0.71%, z 0.27
- kraken: funding (raw, units unverified) 1.1582464966272716, OI 2259.885, OI change vs prior snapshot 0.57%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 35909.8182599999, OI change vs prior snapshot -0.47%

**ETH**: price 1,830.44, 24h 0.95%, z 0.27
- kraken: funding (raw, units unverified) -0.010078049467583942, OI 27499.602, OI change vs prior snapshot 0.56%
- hyperliquid: funding (raw, units unverified) 0.0000120191, OI 585414.6858000009, OI change vs prior snapshot -0.29%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.4s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.6s)
