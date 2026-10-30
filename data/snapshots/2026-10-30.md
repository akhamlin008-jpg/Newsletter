# Data snapshot 2026-10-30 11:00 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** crypto (max |z| 2.81), commodities (max |z| 2.45)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.621 | 10-30 10:59 | **LIVE (~0 min old)** | -3.50 bp | -0.62 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.950 | 10-30 11:00 | **LIVE (~0 min old)** | -3.90 bp | -0.68 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.329 | 10-30 10:59 | **LIVE (~0 min old)** | -0.40 bp | -0.11 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.670 | 10-28 close | official value for 2026-10-28 (not live) | +3.00 bp (vs 2026-10-27) | 0.61 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-29 close | official value for 2026-10-29 (not live) | -3.00 bp (vs 2026-10-28) | -1.46 |  | fred:T10YIE |
| SOFR | 3.940 | 10-29 close | official value for 2026-10-29 (not live) | +0.00 bp (vs 2026-10-28) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.8s) |
| US dollar index (DXY) | 101.976 | 10-30 10:50 | **LIVE (~10 min old)** | -0.06 % (vs 2026-10-29) | -0.23 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.259 | 10-30 11:00 | **LIVE (~0 min old)** | -0.36 % (vs 2026-10-29) | -0.87 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.116 | 10-30 10:59 | **LIVE (~1 min old)** | +0.03 % (vs 2026-10-29) | 0.13 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,657.250 | 10-30 10:50 | **LIVE (~10 min old)** | -1.25 % (vs 2026-10-29) | -2.05 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,803.500 | 10-30 10:50 | **LIVE (~10 min old)** | -2.57 % (vs 2026-10-29) | -2.17 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,831.500 | 10-30 10:50 | **LIVE (~10 min old)** | -1.25 % (vs 2026-10-29) | -1.41 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,622.750 | 10-30 11:00 | **LIVE (~0 min old)** | -1.26 % (vs 2026-10-29) | -2.02 | **YES** | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,636.891 | 10-30 11:00 | **LIVE (~0 min old)** | -2.60 % (vs 2026-10-29) | -2.13 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,822.236 | 10-30 10:45 | **LIVE (~15 min old)** | -1.29 % (vs 2026-10-29) | -1.46 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 19.070 | 10-30 10:44 | **LIVE (~16 min old)** | +1.87 pts | 1.62 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.7s) |
| WTI crude | 104.310 | 10-30 10:50 | **LIVE (~10 min old)** | +2.26 % (vs 2026-10-29) | 0.89 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 113.540 | 10-30 10:50 | **LIVE (~10 min old)** | -1.17 % (vs 2026-10-29) | -0.54 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,923.200 | 10-30 10:50 | **LIVE (~10 min old)** | -2.68 % (vs 2026-10-29) | -2.45 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.529 | 10-30 10:50 | **LIVE (~10 min old)** | -0.80 % (vs 2026-10-29) | -0.63 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 77,079.04, 24h -4.95%, z -2.81 **FLAG**
- kraken: funding (raw, units unverified) 2.2370417011336508, OI 2752.4746, OI change vs prior snapshot 0.23%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41123.19452, OI change vs prior snapshot 1.11%

**ETH**: price 2,233.01, 24h -4.66%, z -2.21 **FLAG**
- kraken: funding (raw, units unverified) 0.01906941371016741, OI 30640.506, OI change vs prior snapshot -0.60%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1029297.4082000003, OI change vs prior snapshot -0.45%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.8s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.7s)
