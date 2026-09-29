# Data snapshot 2026-09-29 10:49 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.87)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.931 | 09-29 10:49 | **LIVE (~0 min old)** | +0.70 bp | 0.11 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.257 | 09-29 10:49 | **LIVE (~0 min old)** | +1.50 bp | 0.27 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.326 | 09-29 10:49 | **LIVE (~0 min old)** | +0.80 bp | 0.23 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.830 | 09-25 close | official value for 2026-09-25 (not live) | -2.00 bp (vs 2026-09-24) | -0.36 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 09-28 close | official value for 2026-09-28 (not live) | +0.00 bp (vs 2026-09-25) | 0.00 |  | fred:T10YIE |
| SOFR | 3.900 | 09-28 close | official value for 2026-09-28 (not live) | +0.00 bp (vs 2026-09-25) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.8s) |
| US dollar index (DXY) | 101.392 | 09-29 10:39 | **LIVE (~10 min old)** | +0.19 % (vs 2026-09-28) | 0.63 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.400 | 09-29 10:49 | **LIVE (~0 min old)** | -0.04 % (vs 2026-09-28) | -0.07 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.134 | 09-29 10:48 | **LIVE (~1 min old)** | -0.31 % (vs 2026-09-28) | -1.14 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,743.250 | 09-29 10:39 | **LIVE (~10 min old)** | -0.05 % (vs 2026-09-28) | -0.07 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,685.000 | 09-29 10:39 | **LIVE (~10 min old)** | +0.39 % (vs 2026-09-28) | 0.41 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,829.300 | 09-29 10:39 | **LIVE (~10 min old)** | -0.38 % (vs 2026-09-28) | -0.46 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,676.210 | 09-29 10:49 | **LIVE (~0 min old)** | -0.10 % (vs 2026-09-28) | -0.14 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,382.387 | 09-29 10:49 | **LIVE (~0 min old)** | +0.35 % (vs 2026-09-28) | 0.31 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,811.131 | 09-29 10:34 | **LIVE (~15 min old)** | -0.24 % (vs 2026-09-28) | -0.30 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.900 | 09-29 10:33 | **LIVE (~16 min old)** | -0.17 pts | -0.17 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s) |
| WTI crude | 91.390 | 09-29 10:39 | **LIVE (~10 min old)** | -1.31 % (vs 2026-09-28) | -0.46 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 96.720 | 09-29 10:39 | **LIVE (~10 min old)** | -8.13 % (vs 2026-09-28) | -2.87 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,196.700 | 09-29 10:39 | **LIVE (~10 min old)** | -2.88 % (vs 2026-09-25) | -2.41 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.635 | 09-29 10:39 | **LIVE (~10 min old)** | +1.05 % (vs 2026-09-28) | 0.71 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 83,863.50, 24h 1.04%, z 0.46
- kraken: funding (raw, units unverified) 0.706451560540875, OI 2335.8749, OI change vs prior snapshot -0.22%
- hyperliquid: funding (raw, units unverified) 0.0000104278, OI 34553.80514, OI change vs prior snapshot -0.13%

**ETH**: price 2,715.72, 24h 1.84%, z 0.70
- kraken: funding (raw, units unverified) 0.016293114031582425, OI 26371.141, OI change vs prior snapshot 0.60%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1204494.0642000022, OI change vs prior snapshot 0.05%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.8s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s)
