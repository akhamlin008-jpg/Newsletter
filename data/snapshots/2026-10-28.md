# Data snapshot 2026-10-28 09:57 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.760 | 10-28 09:57 | **LIVE (~0 min old)** | +2.30 bp | 0.39 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.999 | 10-28 09:57 | **LIVE (~0 min old)** | +0.60 bp | 0.10 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.239 | 10-28 09:57 | **LIVE (~0 min old)** | -1.70 bp | -0.54 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.660 | 10-26 close | official value for 2026-10-26 (not live) | +0.00 bp (vs 2026-10-23) | 0.00 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-27 close | official value for 2026-10-27 (not live) | +1.00 bp (vs 2026-10-26) | 0.50 |  | fred:T10YIE |
| SOFR | 3.950 | 10-27 close | official value for 2026-10-27 (not live) | +2.00 bp (vs 2026-10-26) | 0.70 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.6s) |
| US dollar index (DXY) | 102.321 | 10-28 09:47 | **LIVE (~11 min old)** | +0.00 % (vs 2026-10-27) | 0.00 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.102 | 10-28 09:57 | **LIVE (~1 min old)** | +0.36 % (vs 2026-10-27) | 0.83 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.114 | 10-28 09:57 | **LIVE (~1 min old)** | -0.33 % (vs 2026-10-27) | -1.28 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,761.500 | 10-28 09:47 | **LIVE (~11 min old)** | +0.04 % (vs 2026-10-27) | 0.07 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,829.250 | 10-28 09:47 | **LIVE (~11 min old)** | +0.06 % (vs 2026-10-27) | 0.05 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,830.400 | 10-28 09:47 | **LIVE (~11 min old)** | +0.07 % (vs 2026-10-27) | 0.07 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,729.960 | 10-28 09:57 | **LIVE (~1 min old)** | +0.10 % (vs 2026-10-27) | 0.14 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,685.465 | 10-28 09:57 | **LIVE (~1 min old)** | +0.11 % (vs 2026-10-27) | 0.09 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,822.948 | 10-28 09:42 | **LIVE (~16 min old)** | +0.14 % (vs 2026-10-27) | 0.16 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.530 | 10-28 09:41 | **LIVE (~16 min old)** | +0.01 pts | 0.01 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.6s) |
| WTI crude | 102.030 | 10-28 09:47 | **LIVE (~11 min old)** | +2.13 % (vs 2026-10-27) | 0.82 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 111.410 | 10-28 09:47 | **LIVE (~11 min old)** | -2.17 % (vs 2026-10-27) | -0.96 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,063.100 | 10-28 09:47 | **LIVE (~11 min old)** | -0.28 % (vs 2026-10-27) | -0.25 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.649 | 10-28 09:47 | **LIVE (~11 min old)** | +0.40 % (vs 2026-10-27) | 0.30 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 80,599.99, 24h 0.87%, z 0.58
- kraken: funding (raw, units unverified) 0.9173374248025269, OI 2488.4577, OI change vs prior snapshot -7.32%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 43133.63478, OI change vs prior snapshot 0.33%

**ETH**: price 2,331.59, 24h 0.57%, z 0.30
- kraken: funding (raw, units unverified) 0.027131671673165887, OI 31673.408, OI change vs prior snapshot -3.52%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1127796.8533999999, OI change vs prior snapshot -0.11%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.6s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.6s)
