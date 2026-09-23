# Data snapshot 2026-09-23 08:59 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.796 | 09-23 08:57 | **LIVE (~2 min old)** | +1.90 bp | 0.34 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.988 | 09-23 08:58 | **LIVE (~1 min old)** | +2.10 bp | 0.45 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.192 | 09-23 08:57 | **LIVE (~2 min old)** | +0.20 bp | 0.06 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.620 | 09-21 close | official value for 2026-09-21 (not live) | -6.00 bp (vs 2026-09-18) | -1.38 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 09-22 close | official value for 2026-09-22 (not live) | -1.00 bp (vs 2026-09-21) | -0.45 |  | fred:T10YIE |
| SOFR | 3.870 | 09-22 close | official value for 2026-09-22 (not live) | +2.00 bp (vs 2026-09-21) | 0.37 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.3s) |
| US dollar index (DXY) | 100.939 | 09-23 08:49 | **LIVE (~10 min old)** | +0.51 % (vs 2026-09-21) | 1.69 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.889 | 09-23 08:59 | **LIVE (~0 min old)** | +0.33 % (vs 2026-09-22) | 0.53 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.141 | 09-23 08:59 | **LIVE (~0 min old)** | -0.46 % (vs 2026-09-22) | -1.77 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 119.513 | 09-18 close | official value for 2026-09-18 (not live) | +0.14 % (vs 2026-09-17) | 0.61 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,821.000 | 09-23 08:49 | **LIVE (~10 min old)** | -0.14 % (vs 2026-09-22) | -0.22 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,955.000 | 09-23 08:49 | **LIVE (~10 min old)** | -0.24 % (vs 2026-09-22) | -0.24 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,898.800 | 09-23 08:49 | **LIVE (~10 min old)** | -0.53 % (vs 2026-09-22) | -0.66 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,764.640 | 09-22 16:36 | not trading now; last trade 09-22 16:36 ET | -0.00 % (vs 2026-09-21) | -0.00 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,732.396 | 09-22 17:16 | not trading now; last trade 09-22 17:16 ET | +0.82 % (vs 2026-09-21) | 0.68 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,889.919 | 09-22 16:30 | not trading now; last trade 09-22 16:30 ET | +0.51 % (vs 2026-09-21) | 0.64 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 14.310 | 09-23 08:44 | **LIVE (~15 min old)** | -0.56 pts (vs 2026-09-21) | -0.52 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.7s) |
| WTI crude | 91.080 | 09-23 08:49 | **LIVE (~10 min old)** | -3.71 % (vs 2026-09-22) | -1.24 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 96.460 | 09-23 08:49 | **LIVE (~10 min old)** | -2.81 % (vs 2026-09-22) | -0.99 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,340.300 | 09-23 08:49 | **LIVE (~10 min old)** | -0.82 % (vs 2026-09-22) | -0.66 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.796 | 09-23 08:49 | **LIVE (~10 min old)** | +0.55 % (vs 2026-09-22) | 0.35 |  | yahoo:HG=F (unofficial feed) |

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
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 85,443.17, 24h -0.67%, z -0.25
- kraken: funding (raw, units unverified) 1.2362652324701797, OI 2282.8828, OI change vs prior snapshot -0.21%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 45961.5350399999, OI change vs prior snapshot 0.11%

**ETH**: price 2,719.94, 24h -1.31%, z -0.42
- kraken: funding (raw, units unverified) 0.04491563130183424, OI 30259.184, OI change vs prior snapshot -0.08%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1131657.0101999976, OI change vs prior snapshot -0.08%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.3s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.7s)
