# Data snapshot 2026-11-06 09:56 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.81)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.543 | 11-06 09:56 | **LIVE (~0 min old)** | +6.60 bp | 1.26 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.880 | 11-06 09:56 | **LIVE (~0 min old)** | +4.30 bp | 0.78 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.337 | 11-06 09:56 | **LIVE (~0 min old)** | -2.30 bp | -0.61 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.640 | 11-04 close | official value for 2026-11-04 (not live) | -1.00 bp (vs 2026-11-03) | -0.22 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.240 | 11-05 close | official value for 2026-11-05 (not live) | -2.00 bp (vs 2026-11-04) | -0.82 |  | fred:T10YIE |
| SOFR | 3.920 | 11-05 close | official value for 2026-11-05 (not live) | -2.00 bp (vs 2026-11-04) | -0.79 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.6s) |
| US dollar index (DXY) | 102.240 | 11-06 09:46 | **LIVE (~11 min old)** | +0.68 % (vs 2026-11-05) | 2.66 | **YES** | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.342 | 11-06 09:56 | **LIVE (~1 min old)** | -0.01 % (vs 2026-11-05) | -0.03 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.115 | 11-06 09:56 | **LIVE (~1 min old)** | -0.73 % (vs 2026-11-05) | -2.81 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,447.250 | 11-06 09:46 | **LIVE (~11 min old)** | +0.87 % (vs 2026-11-05) | 0.66 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,363.750 | 11-06 09:46 | **LIVE (~11 min old)** | +2.29 % (vs 2026-11-05) | 1.12 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,746.900 | 11-06 09:46 | **LIVE (~11 min old)** | +0.42 % (vs 2026-11-05) | 0.29 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,424.720 | 11-06 09:56 | **LIVE (~1 min old)** | +0.97 % (vs 2026-11-05) | 0.73 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,196.145 | 11-06 09:56 | **LIVE (~1 min old)** | +2.13 % (vs 2026-11-05) | 1.03 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,732.425 | 11-06 09:41 | **LIVE (~16 min old)** | +0.09 % (vs 2026-11-05) | 0.07 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 25.170 | 11-06 09:40 | **LIVE (~16 min old)** | -3.01 pts | -0.93 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.6s) |
| WTI crude | 90.570 | 11-06 09:47 | **LIVE (~10 min old)** | +0.06 % (vs 2026-11-05) | 0.02 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 97.800 | 11-06 09:47 | **LIVE (~10 min old)** | -0.50 % (vs 2026-11-05) | -0.13 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,054.900 | 11-06 09:47 | **LIVE (~10 min old)** | -1.42 % (vs 2026-11-05) | -0.94 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.277 | 11-06 09:47 | **LIVE (~10 min old)** | +0.45 % (vs 2026-11-05) | 0.31 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 75,425.13, 24h -3.56%, z -1.58
- kraken: funding (raw, units unverified) -0.34367292667255805, OI 2648.0569, OI change vs prior snapshot -10.70%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42271.30618, OI change vs prior snapshot 2.13%

**ETH**: price 2,222.51, 24h -5.08%, z -1.68
- kraken: funding (raw, units unverified) -0.03189195048599926, OI 32540.082, OI change vs prior snapshot -4.44%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 969934.6331999995, OI change vs prior snapshot 0.94%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.6s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.6s)
