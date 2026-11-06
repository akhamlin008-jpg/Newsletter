# Data snapshot 2026-11-06 10:52 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.76)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.534 | 11-06 10:52 | **LIVE (~0 min old)** | +5.70 bp | 1.08 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.866 | 11-06 10:52 | **LIVE (~0 min old)** | +2.90 bp | 0.53 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.332 | 11-06 10:52 | **LIVE (~0 min old)** | -2.80 bp | -0.74 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.640 | 11-04 close | official value for 2026-11-04 (not live) | -1.00 bp (vs 2026-11-03) | -0.22 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.240 | 11-05 close | official value for 2026-11-05 (not live) | -2.00 bp (vs 2026-11-04) | -0.82 |  | fred:T10YIE |
| SOFR | 3.920 | 11-05 close | official value for 2026-11-05 (not live) | -2.00 bp (vs 2026-11-04) | -0.79 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.4s) |
| US dollar index (DXY) | 102.160 | 11-06 10:42 | **LIVE (~10 min old)** | +0.60 % (vs 2026-11-05) | 2.35 | **YES** | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.320 | 11-06 10:52 | **LIVE (~0 min old)** | -0.02 % (vs 2026-11-05) | -0.06 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.115 | 11-06 10:52 | **LIVE (~0 min old)** | -0.72 % (vs 2026-11-05) | -2.76 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,431.250 | 11-06 10:42 | **LIVE (~10 min old)** | +0.65 % (vs 2026-11-05) | 0.50 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,141.750 | 11-06 10:42 | **LIVE (~10 min old)** | +1.46 % (vs 2026-11-05) | 0.71 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,745.500 | 11-06 10:42 | **LIVE (~10 min old)** | +0.37 % (vs 2026-11-05) | 0.26 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,435.280 | 11-06 10:52 | **LIVE (~0 min old)** | +1.11 % (vs 2026-11-05) | 0.84 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,201.000 | 11-06 10:52 | **LIVE (~0 min old)** | +2.14 % (vs 2026-11-05) | 1.04 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,733.317 | 11-06 10:37 | **LIVE (~15 min old)** | +0.13 % (vs 2026-11-05) | 0.09 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 25.400 | 11-06 10:36 | **LIVE (~16 min old)** | -2.78 pts | -0.86 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.0s) |
| WTI crude | 90.180 | 11-06 10:42 | **LIVE (~10 min old)** | -0.38 % (vs 2026-11-05) | -0.11 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 97.160 | 11-06 10:42 | **LIVE (~10 min old)** | -1.15 % (vs 2026-11-05) | -0.30 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,060.400 | 11-06 10:42 | **LIVE (~10 min old)** | -1.29 % (vs 2026-11-05) | -0.86 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.258 | 11-06 10:42 | **LIVE (~10 min old)** | +0.15 % (vs 2026-11-05) | 0.10 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 75,765.08, 24h -0.21%, z -0.09
- kraken: funding (raw, units unverified) 0.3965228917705, OI 2749.134, OI change vs prior snapshot 0.27%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42675.26884, OI change vs prior snapshot 0.09%

**ETH**: price 2,228.71, 24h -0.93%, z -0.31
- kraken: funding (raw, units unverified) -0.026075731463375, OI 32445.077, OI change vs prior snapshot -0.37%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 995588.4243999998, OI change vs prior snapshot 2.06%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.4s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.0s)
