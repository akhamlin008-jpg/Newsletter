# Data snapshot 2026-10-23 09:20 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.87), dollar (max |z| 2.72)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.663 | 10-23 09:20 | **LIVE (~0 min old)** | +2.80 bp | 0.56 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.974 | 10-23 09:20 | **LIVE (~0 min old)** | +2.10 bp | 0.44 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.311 | 10-23 09:20 | **LIVE (~0 min old)** | -0.70 bp | -0.21 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.760 | 10-21 close | official value for 2026-10-21 (not live) | -1.00 bp (vs 2026-10-20) | -0.21 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.320 | 10-22 close | official value for 2026-10-22 (not live) | -5.00 bp (vs 2026-10-21) | -2.87 | **YES** | fred:T10YIE |
| SOFR | 3.900 | 10-22 close | official value for 2026-10-22 (not live) | +2.00 bp (vs 2026-10-21) | 0.66 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.9s) |
| US dollar index (DXY) | 101.704 | 10-23 09:10 | **LIVE (~10 min old)** | +0.09 % (vs 2026-10-22) | 0.31 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 156.483 | 10-23 09:20 | **LIVE (~0 min old)** | -1.04 % (vs 2026-10-22) | -2.72 | **YES** | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.120 | 10-23 09:20 | **LIVE (~0 min old)** | -0.30 % (vs 2026-10-22) | -1.16 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.405 | 10-16 close | official value for 2026-10-16 (not live) | -0.14 % (vs 2026-10-15) | -0.48 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,668.250 | 10-23 09:10 | **LIVE (~10 min old)** | -0.47 % (vs 2026-10-22) | -0.73 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,051.000 | 10-23 09:10 | **LIVE (~10 min old)** | -0.31 % (vs 2026-10-22) | -0.25 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,777.800 | 10-23 09:10 | **LIVE (~10 min old)** | -0.65 % (vs 2026-10-22) | -0.71 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,663.430 | 10-22 16:00 | not trading now; last trade 10-22 16:00 ET | -1.21 % (vs 2026-10-21) | -1.96 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,958.688 | 10-22 16:00 | not trading now; last trade 10-22 16:00 ET | -2.90 % (vs 2026-10-21) | -2.61 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,784.026 | 10-22 16:00 | not trading now; last trade 10-22 16:00 ET | +0.11 % (vs 2026-10-21) | 0.11 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 20.120 | 10-23 09:05 | **LIVE (~15 min old)** | +1.09 pts (vs 2026-10-22) | 0.85 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.5s) |
| WTI crude | 101.270 | 10-23 09:10 | **LIVE (~10 min old)** | +1.81 % (vs 2026-10-22) | 0.69 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 110.350 | 10-23 09:10 | **LIVE (~10 min old)** | -2.49 % (vs 2026-10-22) | -1.09 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,042.500 | 10-23 09:10 | **LIVE (~10 min old)** | -0.44 % (vs 2026-10-22) | -0.37 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.467 | 10-23 09:10 | **LIVE (~10 min old)** | +1.64 % (vs 2026-10-22) | 1.28 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 81,564.67, 24h -0.06%, z -0.03
- kraken: funding (raw, units unverified) 0.9550855376936106, OI 2602.7252, OI change vs prior snapshot -0.00%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 45125.7025, OI change vs prior snapshot -0.31%

**ETH**: price 2,395.79, 24h -0.49%, z -0.23
- kraken: funding (raw, units unverified) 0.016729216781082534, OI 28945.894, OI change vs prior snapshot 0.17%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1090547.9535999999, OI change vs prior snapshot 0.17%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.9s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.5s)
