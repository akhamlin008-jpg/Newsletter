# Data snapshot 2026-11-17 11:49 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.787 | 11-17 11:49 | **LIVE (~0 min old)** | -4.00 bp | -0.55 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.097 | 11-17 11:49 | **LIVE (~0 min old)** | -2.40 bp | -0.39 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.310 | 11-17 11:49 | **LIVE (~0 min old)** | +1.60 bp | 0.43 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.910 | 11-13 close | official value for 2026-11-13 (not live) | +5.00 bp (vs 2026-11-12) | 0.95 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.200 | 11-16 close | official value for 2026-11-16 (not live) | -4.00 bp (vs 2026-11-13) | -1.71 |  | fred:T10YIE |
| SOFR | 3.930 | 11-16 close | official value for 2026-11-16 (not live) | +3.00 bp (vs 2026-11-13) | 1.28 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.7s) |
| US dollar index (DXY) | 103.435 | 11-17 11:40 | **LIVE (~10 min old)** | -0.11 % (vs 2026-11-16) | -0.31 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.246 | 11-17 11:50 | **LIVE (~0 min old)** | -0.33 % (vs 2026-11-16) | -0.87 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.102 | 11-17 11:49 | **LIVE (~1 min old)** | -0.06 % (vs 2026-11-16) | -0.17 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 122.650 | 11-13 close | official value for 2026-11-13 (not live) | +0.09 % (vs 2026-11-12) | 0.34 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,342.250 | 11-17 11:40 | **LIVE (~10 min old)** | -1.30 % (vs 2026-11-16) | -1.00 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 26,907.750 | 11-17 11:40 | **LIVE (~10 min old)** | -1.38 % (vs 2026-11-16) | -0.68 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,710.300 | 11-17 11:40 | **LIVE (~10 min old)** | -1.49 % (vs 2026-11-16) | -1.01 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,311.220 | 11-17 11:50 | **LIVE (~0 min old)** | -1.42 % (vs 2026-11-16) | -1.09 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 26,765.807 | 11-17 11:50 | **LIVE (~0 min old)** | -1.59 % (vs 2026-11-16) | -0.78 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,703.269 | 11-17 11:35 | **LIVE (~15 min old)** | -1.45 % (vs 2026-11-16) | -0.98 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 26.370 | 11-17 11:34 | **LIVE (~16 min old)** | +3.46 pts | 1.12 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.7s) |
| WTI crude | 86.530 | 11-17 11:40 | **LIVE (~10 min old)** | +0.94 % (vs 2026-11-16) | 0.30 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 93.130 | 11-17 11:40 | **LIVE (~10 min old)** | +0.75 % (vs 2026-11-16) | 0.21 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,872.700 | 11-17 11:40 | **LIVE (~10 min old)** | +0.51 % (vs 2026-11-16) | 0.34 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.986 | 11-17 11:40 | **LIVE (~10 min old)** | -0.19 % (vs 2026-11-16) | -0.13 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 63,712.64, 24h -1.77%, z -0.69
- kraken: funding (raw, units unverified) 0.8051833446475203, OI 2223.5904, OI change vs prior snapshot -2.11%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 37779.22204, OI change vs prior snapshot 3.67%

**ETH**: price 1,777.68, 24h -2.70%, z -0.79
- kraken: funding (raw, units unverified) -0.021220826451, OI 28826.9, OI change vs prior snapshot 3.86%
- hyperliquid: funding (raw, units unverified) -0.0000166124, OI 622118.1679999999, OI change vs prior snapshot 4.07%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.7s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.7s)
