# Data snapshot 2026-10-01 10:25 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.854 | 10-01 10:24 | **LIVE (~0 min old)** | -3.30 bp | -0.51 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.317 | 10-01 10:25 | **LIVE (~0 min old)** | +2.40 bp | 0.43 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.463 | 10-01 10:24 | **LIVE (~0 min old)** | +5.70 bp | 1.57 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.910 | 09-29 close | official value for 2026-09-29 (not live) | +1.00 bp (vs 2026-09-28) | 0.18 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 09-30 close | official value for 2026-09-30 (not live) | +1.00 bp (vs 2026-09-29) | 0.51 |  | fred:T10YIE |
| SOFR | 3.900 | 09-30 close | official value for 2026-09-30 (not live) | +2.00 bp (vs 2026-09-29) | 0.44 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.7s) |
| US dollar index (DXY) | 101.796 | 10-01 10:15 | **LIVE (~10 min old)** | +0.34 % (vs 2026-09-30) | 1.19 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.957 | 10-01 10:25 | **LIVE (~0 min old)** | +0.35 % (vs 2026-09-30) | 0.61 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.129 | 10-01 10:24 | **LIVE (~1 min old)** | -0.45 % (vs 2026-09-30) | -1.73 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,694.750 | 10-01 10:15 | **LIVE (~10 min old)** | -0.27 % (vs 2026-09-30) | -0.46 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,652.250 | 10-01 10:15 | **LIVE (~10 min old)** | -0.15 % (vs 2026-09-30) | -0.17 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,803.100 | 10-01 10:15 | **LIVE (~10 min old)** | -0.51 % (vs 2026-09-30) | -0.64 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,632.410 | 10-01 10:25 | **LIVE (~0 min old)** | -0.25 % (vs 2026-09-30) | -0.38 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,343.797 | 10-01 10:25 | **LIVE (~0 min old)** | -0.21 % (vs 2026-09-30) | -0.20 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,781.006 | 10-01 10:10 | **LIVE (~15 min old)** | -0.57 % (vs 2026-09-30) | -0.73 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.210 | 10-01 10:09 | **LIVE (~16 min old)** | +0.87 pts | 0.90 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s) |
| WTI crude | 91.620 | 10-01 10:15 | **LIVE (~10 min old)** | +1.33 % (vs 2026-09-30) | 0.47 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 101.080 | 10-01 10:15 | **LIVE (~10 min old)** | -2.37 % (vs 2026-09-30) | -0.86 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,184.500 | 10-01 10:15 | **LIVE (~10 min old)** | -0.05 % (vs 2026-09-30) | -0.04 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.567 | 10-01 10:15 | **LIVE (~10 min old)** | +0.13 % (vs 2026-09-30) | 0.09 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 83,975.79, 24h 0.26%, z 0.12
- kraken: funding (raw, units unverified) 0.7941137522130137, OI 2388.2587, OI change vs prior snapshot 1.83%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 34240.98776, OI change vs prior snapshot 0.25%

**ETH**: price 2,691.33, 24h 0.54%, z 0.22
- kraken: funding (raw, units unverified) 0.025185023792499102, OI 25996.42, OI change vs prior snapshot -2.45%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1198320.3879999998, OI change vs prior snapshot -0.29%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.7s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s)
