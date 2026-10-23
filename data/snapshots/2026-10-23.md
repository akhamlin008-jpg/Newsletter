# Data snapshot 2026-10-23 08:50 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.87), dollar (max |z| 2.83)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.660 | 10-23 08:50 | **LIVE (~0 min old)** | +2.50 bp | 0.50 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.970 | 10-23 08:50 | **LIVE (~0 min old)** | +1.70 bp | 0.36 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.310 | 10-23 08:50 | **LIVE (~0 min old)** | -0.80 bp | -0.24 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.760 | 10-21 close | official value for 2026-10-21 (not live) | -1.00 bp (vs 2026-10-20) | -0.21 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.320 | 10-22 close | official value for 2026-10-22 (not live) | -5.00 bp (vs 2026-10-21) | -2.87 | **YES** | fred:T10YIE |
| SOFR | 3.900 | 10-22 close | official value for 2026-10-22 (not live) | +2.00 bp (vs 2026-10-21) | 0.66 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.1s) |
| US dollar index (DXY) | 101.724 | 10-23 08:40 | **LIVE (~11 min old)** | +0.11 % (vs 2026-10-22) | 0.38 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 156.419 | 10-23 08:50 | **LIVE (~1 min old)** | -1.08 % (vs 2026-10-22) | -2.83 | **YES** | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.121 | 10-23 08:50 | **LIVE (~1 min old)** | -0.26 % (vs 2026-10-22) | -0.99 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.405 | 10-16 close | official value for 2026-10-16 (not live) | -0.14 % (vs 2026-10-15) | -0.48 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,670.750 | 10-23 08:40 | **LIVE (~11 min old)** | -0.44 % (vs 2026-10-22) | -0.68 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,060.500 | 10-23 08:40 | **LIVE (~11 min old)** | -0.28 % (vs 2026-10-22) | -0.23 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,779.000 | 10-23 08:40 | **LIVE (~11 min old)** | -0.61 % (vs 2026-10-22) | -0.66 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,663.430 | 10-22 16:00 | not trading now; last trade 10-22 16:00 ET | -1.21 % (vs 2026-10-21) | -1.96 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,958.688 | 10-22 16:00 | not trading now; last trade 10-22 16:00 ET | -2.90 % (vs 2026-10-21) | -2.61 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,784.026 | 10-22 16:00 | not trading now; last trade 10-22 16:00 ET | +0.11 % (vs 2026-10-21) | 0.11 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 20.010 | 10-23 08:35 | **LIVE (~16 min old)** | +0.98 pts (vs 2026-10-22) | 0.76 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.4s) |
| WTI crude | 101.190 | 10-23 08:40 | **LIVE (~11 min old)** | +1.73 % (vs 2026-10-22) | 0.66 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 110.160 | 10-23 08:40 | **LIVE (~11 min old)** | -2.66 % (vs 2026-10-22) | -1.16 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,038.300 | 10-23 08:40 | **LIVE (~11 min old)** | -0.54 % (vs 2026-10-22) | -0.46 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.476 | 10-23 08:40 | **LIVE (~11 min old)** | +1.78 % (vs 2026-10-22) | 1.39 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 81,630.23, 24h 0.03%, z 0.02
- kraken: funding (raw, units unverified) 1.0052631834668062, OI 2602.8458, OI change vs prior snapshot 0.09%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 45266.79594, OI change vs prior snapshot 2.52%

**ETH**: price 2,397.40, 24h -0.04%, z -0.02
- kraken: funding (raw, units unverified) 0.01539551861475, OI 28898.161, OI change vs prior snapshot 0.07%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1088683.5204, OI change vs prior snapshot -0.10%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.4s)
