# Data snapshot 2026-10-22 09:10 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.28)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.723 | 10-22 09:10 | **LIVE (~0 min old)** | -10.00 bp | -1.95 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.034 | 10-22 09:10 | **LIVE (~0 min old)** | -11.20 bp | -2.28 | **YES** | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.311 | 10-22 09:10 | **LIVE (~0 min old)** | -1.20 bp | -0.35 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.770 | 10-20 close | official value for 2026-10-20 (not live) | -3.00 bp (vs 2026-10-19) | -0.62 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.370 | 10-21 close | official value for 2026-10-21 (not live) | +2.00 bp (vs 2026-10-20) | 1.16 |  | fred:T10YIE |
| SOFR | 3.880 | 10-21 close | official value for 2026-10-21 (not live) | +0.00 bp (vs 2026-10-20) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.8s) |
| US dollar index (DXY) | 101.770 | 10-22 09:00 | **LIVE (~10 min old)** | -0.01 % (vs 2026-10-21) | -0.03 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.111 | 10-22 09:10 | **LIVE (~0 min old)** | -0.73 % (vs 2026-10-21) | -1.85 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.121 | 10-22 09:10 | **LIVE (~0 min old)** | -0.18 % (vs 2026-10-21) | -0.66 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.405 | 10-16 close | official value for 2026-10-16 (not live) | -0.14 % (vs 2026-10-15) | -0.48 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,725.250 | 10-22 09:00 | **LIVE (~10 min old)** | -0.96 % (vs 2026-10-21) | -1.65 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,499.500 | 10-22 09:00 | **LIVE (~10 min old)** | -1.69 % (vs 2026-10-21) | -1.62 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,777.600 | 10-22 09:00 | **LIVE (~10 min old)** | -0.59 % (vs 2026-10-21) | -0.62 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,757.170 | 10-21 16:00 | not trading now; last trade 10-21 16:00 ET | +0.58 % (vs 2026-10-20) | 0.93 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,822.518 | 10-21 16:00 | not trading now; last trade 10-21 16:00 ET | +1.13 % (vs 2026-10-20) | 1.02 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,781.021 | 10-21 16:00 | not trading now; last trade 10-21 16:00 ET | +0.27 % (vs 2026-10-20) | 0.28 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 18.090 | 10-22 08:55 | **LIVE (~15 min old)** | +1.41 pts (vs 2026-10-21) | 1.19 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.8s) |
| WTI crude | 99.610 | 10-22 09:00 | **LIVE (~10 min old)** | +2.53 % (vs 2026-10-21) | 0.96 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 112.140 | 10-22 09:00 | **LIVE (~10 min old)** | +3.05 % (vs 2026-10-21) | 1.43 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,098.000 | 10-22 09:00 | **LIVE (~10 min old)** | -1.25 % (vs 2026-10-21) | -1.15 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.419 | 10-22 09:00 | **LIVE (~10 min old)** | -1.90 % (vs 2026-10-21) | -1.69 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 81,593.64, 24h -2.55%, z -1.63
- kraken: funding (raw, units unverified) 0.4241451009591939, OI 2420.4287, OI change vs prior snapshot -0.32%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42036.00464, OI change vs prior snapshot 0.24%

**ETH**: price 2,394.89, 24h -3.06%, z -1.51
- kraken: funding (raw, units unverified) 0.004746154182, OI 27217.65, OI change vs prior snapshot -0.06%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1097380.2423999999, OI change vs prior snapshot -0.27%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.8s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.8s)
