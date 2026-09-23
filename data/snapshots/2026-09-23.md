# Data snapshot 2026-09-23 09:35 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.802 | 09-23 09:35 | **LIVE (~0 min old)** | +2.50 bp | 0.44 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.994 | 09-23 09:35 | **LIVE (~0 min old)** | +2.70 bp | 0.58 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.192 | 09-23 09:35 | **LIVE (~0 min old)** | +0.20 bp | 0.06 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.620 | 09-21 close | official value for 2026-09-21 (not live) | -6.00 bp (vs 2026-09-18) | -1.38 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 09-22 close | official value for 2026-09-22 (not live) | -1.00 bp (vs 2026-09-21) | -0.45 |  | fred:T10YIE |
| SOFR | 3.870 | 09-22 close | official value for 2026-09-22 (not live) | +2.00 bp (vs 2026-09-21) | 0.37 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.6s) |
| US dollar index (DXY) | 100.903 | 09-23 09:25 | **LIVE (~11 min old)** | +0.47 % (vs 2026-09-21) | 1.57 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.882 | 09-23 09:35 | **LIVE (~1 min old)** | +0.33 % (vs 2026-09-22) | 0.52 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.142 | 09-23 09:35 | **LIVE (~1 min old)** | -0.42 % (vs 2026-09-22) | -1.59 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 119.513 | 09-18 close | official value for 2026-09-18 (not live) | +0.14 % (vs 2026-09-17) | 0.61 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,823.250 | 09-23 09:25 | **LIVE (~11 min old)** | -0.11 % (vs 2026-09-22) | -0.17 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,986.750 | 09-23 09:25 | **LIVE (~11 min old)** | -0.13 % (vs 2026-09-22) | -0.13 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,898.800 | 09-23 09:25 | **LIVE (~11 min old)** | -0.53 % (vs 2026-09-22) | -0.66 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,751.460 | 09-23 09:35 | **LIVE (~1 min old)** | -0.17 % (vs 2026-09-21) | -0.23 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,645.717 | 09-23 09:35 | **LIVE (~1 min old)** | +0.54 % (vs 2026-09-21) | 0.44 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,889.919 | 09-22 16:30 | not trading now; last trade 09-22 16:30 ET | +0.51 % (vs 2026-09-21) | 0.64 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 14.260 | 09-23 09:20 | **LIVE (~16 min old)** | -0.61 pts (vs 2026-09-21) | -0.57 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.7s) |
| WTI crude | 91.240 | 09-23 09:25 | **LIVE (~11 min old)** | -3.54 % (vs 2026-09-22) | -1.18 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 96.510 | 09-23 09:25 | **LIVE (~11 min old)** | -2.76 % (vs 2026-09-22) | -0.97 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,344.800 | 09-23 09:26 | **LIVE (~10 min old)** | -0.72 % (vs 2026-09-22) | -0.58 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.800 | 09-23 09:26 | **LIVE (~10 min old)** | +0.59 % (vs 2026-09-22) | 0.38 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 85,545.93, 24h -0.91%, z -0.34
- kraken: funding (raw, units unverified) 1.1165409566865, OI 2295.7953, OI change vs prior snapshot 0.57%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 45948.89942, OI change vs prior snapshot -0.03%

**ETH**: price 2,713.64, 24h -1.62%, z -0.53
- kraken: funding (raw, units unverified) 0.0551532816, OI 29028.628, OI change vs prior snapshot -4.07%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1119112.9595999995, OI change vs prior snapshot -1.11%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.6s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.7s)
