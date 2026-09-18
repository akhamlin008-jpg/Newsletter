# Data snapshot 2026-09-18 06:15 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.713 | 09-18 06:14 | **LIVE (~1 min old)** | +2.30 bp | 0.42 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.957 | 09-18 06:14 | **LIVE (~1 min old)** | +1.00 bp | 0.24 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.244 | 09-18 06:14 | **LIVE (~1 min old)** | -1.30 bp | -0.43 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.680 | 09-16 close | official value for 2026-09-16 (not live) | +6.00 bp (vs 2026-09-15) | 1.63 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 09-17 close | official value for 2026-09-17 (not live) | +0.00 bp (vs 2026-09-16) | 0.00 |  | fred:T10YIE |
| SOFR | 3.620 | 09-16 close | official value for 2026-09-16 (not live) | -2.00 bp (vs 2026-09-15) | -0.89 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.0s) |
| US dollar index (DXY) | 100.361 | 09-18 06:05 | **LIVE (~10 min old)** | +0.14 % (vs 2026-09-17) | 0.45 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.889 | 09-18 06:15 | **LIVE (~0 min old)** | +1.20 % (vs 2026-09-17) | 1.80 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.149 | 09-18 06:14 | **LIVE (~1 min old)** | +0.16 % (vs 2026-09-17) | 0.55 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 118.213 | 09-11 close | official value for 2026-09-11 (not live) | +0.11 % (vs 2026-09-10) | 0.54 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,716.750 | 09-18 06:05 | **LIVE (~10 min old)** | +1.00 % (vs 2026-09-17) | 1.51 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,846.750 | 09-18 06:05 | **LIVE (~10 min old)** | +1.36 % (vs 2026-09-17) | 1.31 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,894.700 | 09-18 06:04 | **LIVE (~11 min old)** | +0.65 % (vs 2026-09-17) | 0.81 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,637.760 | 09-17 16:34 | not trading now; last trade 09-17 16:34 ET | +1.14 % (vs 2026-09-16) | 1.79 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,446.980 | 09-17 17:16 | not trading now; last trade 09-17 17:16 ET | +1.73 % (vs 2026-09-16) | 1.76 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,874.630 | 09-17 16:30 | not trading now; last trade 09-17 16:30 ET | +0.55 % (vs 2026-09-16) | 0.66 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.350 | 09-18 06:00 | **LIVE (~15 min old)** | -0.09 pts (vs 2026-09-17) | -0.08 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.5s) |
| WTI crude | 96.360 | 09-18 06:05 | **LIVE (~10 min old)** | -5.45 % (vs 2026-09-17) | -1.80 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 98.850 | 09-18 06:03 | **LIVE (~12 min old)** | -5.70 % (vs 2026-09-17) | -1.92 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,417.000 | 09-18 06:05 | **LIVE (~10 min old)** | +0.39 % (vs 2026-09-17) | 0.29 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.644 | 09-18 06:05 | **LIVE (~10 min old)** | +0.88 % (vs 2026-09-17) | 0.53 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); quarterly roll window: roll date 2026-09-10, expiry 2026-09-18; a jump may be the contract switch; roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); quarterly roll window: roll date 2026-09-10, expiry 2026-09-18; a jump may be the contract switch; roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); quarterly roll window: roll date 2026-09-10, expiry 2026-09-18; a jump may be the contract switch; roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 78,049.69, 24h 2.25%, z 1.14
- kraken: funding (raw, units unverified) 0.92988381849725, OI 2249.666, OI change vs prior snapshot 0.54%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 36515.23746, OI change vs prior snapshot 0.09%

**ETH**: price 2,509.21, 24h 3.11%, z 1.10
- kraken: funding (raw, units unverified) 0.07623936777925, OI 35364.149, OI change vs prior snapshot 0.15%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1041207.6976000001, OI change vs prior snapshot 0.53%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.5s)
