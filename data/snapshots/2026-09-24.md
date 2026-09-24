# Data snapshot 2026-09-24 08:52 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.66)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.858 | 09-24 08:52 | **LIVE (~0 min old)** | -3.70 bp | -0.66 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.114 | 09-24 08:52 | **LIVE (~0 min old)** | +0.00 bp | 0.00 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.256 | 09-24 08:52 | **LIVE (~0 min old)** | +3.70 bp | 1.15 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.630 | 09-22 close | official value for 2026-09-22 (not live) | +1.00 bp (vs 2026-09-21) | 0.22 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 09-23 close | official value for 2026-09-23 (not live) | +2.00 bp (vs 2026-09-22) | 0.93 |  | fred:T10YIE |
| SOFR | 3.870 | 09-23 close | official value for 2026-09-23 (not live) | +0.00 bp (vs 2026-09-22) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.6s) |
| US dollar index (DXY) | 101.274 | 09-24 08:42 | **LIVE (~11 min old)** | +0.17 % (vs 2026-09-23) | 0.52 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.763 | 09-24 08:52 | **LIVE (~1 min old)** | +0.82 % (vs 2026-09-23) | 1.36 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.137 | 09-24 08:52 | **LIVE (~1 min old)** | -0.68 % (vs 2026-09-23) | -2.66 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 119.513 | 09-18 close | official value for 2026-09-18 (not live) | +0.14 % (vs 2026-09-17) | 0.61 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,732.750 | 09-24 08:42 | **LIVE (~11 min old)** | -0.51 % (vs 2026-09-23) | -0.81 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,468.750 | 09-24 08:42 | **LIVE (~11 min old)** | -0.96 % (vs 2026-09-23) | -0.97 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,849.200 | 09-24 08:42 | **LIVE (~11 min old)** | -0.38 % (vs 2026-09-23) | -0.43 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,706.030 | 09-23 16:36 | not trading now; last trade 09-23 16:36 ET | -0.76 % (vs 2026-09-21) | -1.03 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,470.293 | 09-23 17:16 | not trading now; last trade 09-23 17:16 ET | -0.04 % (vs 2026-09-21) | -0.03 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,838.660 | 09-23 16:30 | not trading now; last trade 09-23 16:30 ET | -1.28 % (vs 2026-09-21) | -1.61 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 16.070 | 09-24 08:37 | **LIVE (~16 min old)** | +0.89 pts (vs 2026-09-23) | 0.85 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.3s) |
| WTI crude | 93.860 | 09-24 08:42 | **LIVE (~11 min old)** | +1.84 % (vs 2026-09-23) | 0.62 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 99.860 | 09-24 08:42 | **LIVE (~11 min old)** | -3.12 % (vs 2026-09-23) | -1.07 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,305.800 | 09-24 08:42 | **LIVE (~11 min old)** | -0.29 % (vs 2026-09-23) | -0.23 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.749 | 09-24 08:42 | **LIVE (~11 min old)** | +1.06 % (vs 2026-09-23) | 0.69 |  | yahoo:HG=F (unofficial feed) |

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
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-18, 2026-09-21)
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 83,431.48, 24h -2.40%, z -0.91
- kraken: funding (raw, units unverified) 0.8587995978494861, OI 2193.0954, OI change vs prior snapshot 0.07%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 37863.43776, OI change vs prior snapshot 0.10%

**ETH**: price 2,641.78, 24h -2.92%, z -0.96
- kraken: funding (raw, units unverified) 0.01845356471345745, OI 27381.286, OI change vs prior snapshot 0.09%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1067950.7721999993, OI change vs prior snapshot -0.01%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.6s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.3s)
