# Data snapshot 2026-10-15 09:21 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.75), equity (max |z| 2.69)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.728 | 10-15 09:21 | **LIVE (~0 min old)** | -7.40 bp | -1.31 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.056 | 10-15 09:21 | **LIVE (~0 min old)** | -13.40 bp | -2.75 | **YES** | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.328 | 10-15 09:21 | **LIVE (~0 min old)** | -6.00 bp | -1.72 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.880 | 10-13 close | official value for 2026-10-13 (not live) | -3.00 bp (vs 2026-10-09) | -0.62 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-14 close | official value for 2026-10-14 (not live) | +2.00 bp (vs 2026-10-13) | 1.25 |  | fred:T10YIE |
| SOFR | 3.880 | 10-14 close | official value for 2026-10-14 (not live) | -1.00 bp (vs 2026-10-13) | -0.28 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.1s) |
| US dollar index (DXY) | 102.126 | 10-15 09:11 | **LIVE (~10 min old)** | -0.41 % (vs 2026-10-14) | -1.33 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.742 | 10-15 09:21 | **LIVE (~0 min old)** | -0.37 % (vs 2026-10-14) | -0.85 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.121 | 10-15 09:21 | **LIVE (~0 min old)** | +0.06 % (vs 2026-10-14) | 0.18 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.602 | 10-09 close | official value for 2026-10-09 (not live) | +0.13 % (vs 2026-10-08) | 0.46 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,742.000 | 10-15 09:11 | **LIVE (~10 min old)** | -0.36 % (vs 2026-10-14) | -0.63 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,778.000 | 10-15 09:11 | **LIVE (~10 min old)** | -1.34 % (vs 2026-10-14) | -1.44 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,748.900 | 10-15 09:11 | **LIVE (~10 min old)** | +0.14 % (vs 2026-10-14) | 0.17 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,718.940 | 10-14 16:36 | not trading now; last trade 10-14 16:36 ET | -1.11 % (vs 2026-10-13) | -1.93 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,950.816 | 10-14 17:16 | not trading now; last trade 10-14 17:16 ET | -2.02 % (vs 2026-10-13) | -2.19 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,729.531 | 10-14 16:30 | not trading now; last trade 10-14 16:30 ET | -1.93 % (vs 2026-10-13) | -2.69 | **YES** | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.410 | 10-15 09:06 | **LIVE (~15 min old)** | +0.54 pts (vs 2026-10-14) | 0.63 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.3s) |
| WTI crude | 94.440 | 10-15 09:11 | **LIVE (~10 min old)** | -0.68 % (vs 2026-10-14) | -0.29 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 104.850 | 10-15 09:11 | **LIVE (~10 min old)** | -1.14 % (vs 2026-10-14) | -0.50 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,170.400 | 10-15 09:11 | **LIVE (~10 min old)** | +1.52 % (vs 2026-10-14) | 1.28 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.549 | 10-15 09:11 | **LIVE (~10 min old)** | -0.95 % (vs 2026-10-14) | -0.76 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 80,301.67, 24h -2.36%, z -1.29
- kraken: funding (raw, units unverified) 0.6254905201533065, OI 2396.4545, OI change vs prior snapshot -0.58%
- hyperliquid: funding (raw, units unverified) 0.000002389, OI 39139.47816, OI change vs prior snapshot -0.35%

**ETH**: price 2,343.60, 24h -4.34%, z -1.80
- kraken: funding (raw, units unverified) 0.002953061168915884, OI 29548.079, OI change vs prior snapshot -2.72%
- hyperliquid: funding (raw, units unverified) 0.0000041701, OI 1062812.9758000004, OI change vs prior snapshot -0.34%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.3s)
