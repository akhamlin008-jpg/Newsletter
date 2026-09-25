# Data snapshot 2026-09-25 08:57 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 3.0), commodities (max |z| 2.65)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.897 | 09-25 08:56 | **LIVE (~0 min old)** | +0.20 bp | 0.03 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.179 | 09-25 08:57 | **LIVE (~0 min old)** | +1.70 bp | 0.30 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.282 | 09-25 08:56 | **LIVE (~0 min old)** | +1.50 bp | 0.45 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.760 | 09-23 close | official value for 2026-09-23 (not live) | +13.00 bp (vs 2026-09-22) | 3.00 | **YES** | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 09-24 close | official value for 2026-09-24 (not live) | -2.00 bp (vs 2026-09-23) | -0.93 |  | fred:T10YIE |
| SOFR | 3.880 | 09-24 close | official value for 2026-09-24 (not live) | +1.00 bp (vs 2026-09-23) | 0.20 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.5s) |
| US dollar index (DXY) | 101.004 | 09-25 08:47 | **LIVE (~10 min old)** | -0.28 % (vs 2026-09-24) | -0.93 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.525 | 09-25 08:57 | **LIVE (~0 min old)** | -0.47 % (vs 2026-09-24) | -0.78 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.141 | 09-25 08:57 | **LIVE (~0 min old)** | +0.20 % (vs 2026-09-24) | 0.71 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 119.513 | 09-18 close | official value for 2026-09-18 (not live) | +0.14 % (vs 2026-09-17) | 0.61 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,786.250 | 09-25 08:47 | **LIVE (~10 min old)** | +0.25 % (vs 2026-09-24) | 0.40 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,885.250 | 09-25 08:47 | **LIVE (~10 min old)** | +0.39 % (vs 2026-09-24) | 0.40 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,863.300 | 09-25 08:47 | **LIVE (~10 min old)** | +0.23 % (vs 2026-09-24) | 0.26 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,704.130 | 09-24 16:36 | not trading now; last trade 09-24 16:36 ET | -0.02 % (vs 2026-09-23) | -0.03 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,478.855 | 09-24 17:16 | not trading now; last trade 09-24 17:16 ET | +0.03 % (vs 2026-09-23) | 0.02 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,835.574 | 09-24 16:30 | not trading now; last trade 09-24 16:30 ET | -0.11 % (vs 2026-09-23) | -0.13 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.190 | 09-25 08:42 | **LIVE (~15 min old)** | -0.48 pts (vs 2026-09-24) | -0.47 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.8s) |
| WTI crude | 92.510 | 09-25 08:47 | **LIVE (~10 min old)** | -2.22 % (vs 2026-09-24) | -0.75 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 98.250 | 09-25 08:47 | **LIVE (~10 min old)** | -7.83 % (vs 2026-09-24) | -2.65 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,338.800 | 09-25 08:47 | **LIVE (~10 min old)** | +0.95 % (vs 2026-09-24) | 0.77 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.762 | 09-25 08:47 | **LIVE (~10 min old)** | +0.65 % (vs 2026-09-24) | 0.43 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 84,461.52, 24h 1.06%, z 0.41
- kraken: funding (raw, units unverified) -0.175647555526, OI 2237.1516, OI change vs prior snapshot -0.13%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40285.9587400001, OI change vs prior snapshot -0.04%

**ETH**: price 2,719.31, 24h 2.66%, z 0.90
- kraken: funding (raw, units unverified) 0.023456816182832428, OI 26322.64, OI change vs prior snapshot -0.25%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1102787.2606000011, OI change vs prior snapshot 0.08%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.5s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.8s)
