# Data snapshot 2026-10-26 11:07 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.62), commodities (max |z| 2.36)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.703 | 10-26 11:07 | **LIVE (~0 min old)** | +2.10 bp | 0.34 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.976 | 10-26 11:07 | **LIVE (~0 min old)** | -1.20 bp | -0.19 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.273 | 10-26 11:07 | **LIVE (~0 min old)** | -3.30 bp | -1.02 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.640 | 10-22 close | official value for 2026-10-22 (not live) | -12.00 bp (vs 2026-10-21) | -2.62 | **YES** | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 10-23 close | official value for 2026-10-23 (not live) | +2.00 bp (vs 2026-10-22) | 0.96 |  | fred:T10YIE |
| SOFR | 3.920 | 10-23 close | official value for 2026-10-23 (not live) | +2.00 bp (vs 2026-10-22) | 0.67 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.1s) |
| US dollar index (DXY) | 101.998 | 10-26 10:57 | **LIVE (~11 min old)** | +0.18 % (vs 2026-10-23) | 0.64 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.519 | 10-26 11:07 | **LIVE (~1 min old)** | +0.66 % (vs 2026-10-23) | 1.46 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.118 | 10-26 11:07 | **LIVE (~1 min old)** | -0.33 % (vs 2026-10-23) | -1.30 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.405 | 10-16 close | official value for 2026-10-16 (not live) | -0.14 % (vs 2026-10-15) | -0.48 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,734.250 | 10-26 10:57 | **LIVE (~11 min old)** | +0.97 % (vs 2026-10-23) | 1.53 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,524.500 | 10-26 10:57 | **LIVE (~11 min old)** | +1.40 % (vs 2026-10-23) | 1.17 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,810.600 | 10-26 10:57 | **LIVE (~11 min old)** | +0.94 % (vs 2026-10-23) | 1.03 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,697.060 | 10-26 11:07 | **LIVE (~1 min old)** | +0.96 % (vs 2026-10-23) | 1.46 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,374.557 | 10-26 11:07 | **LIVE (~1 min old)** | +1.44 % (vs 2026-10-23) | 1.15 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,796.552 | 10-26 10:52 | **LIVE (~16 min old)** | +0.74 % (vs 2026-10-23) | 0.83 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.960 | 10-26 10:51 | **LIVE (~16 min old)** | -1.49 pts | -1.20 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s) |
| WTI crude | 101.140 | 10-26 10:57 | **LIVE (~11 min old)** | -2.06 % (vs 2026-10-23) | -0.76 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 110.240 | 10-26 10:57 | **LIVE (~11 min old)** | -5.55 % (vs 2026-10-23) | -2.36 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,039.700 | 10-26 10:57 | **LIVE (~11 min old)** | +0.79 % (vs 2026-10-23) | 0.67 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.527 | 10-26 10:57 | **LIVE (~11 min old)** | +0.78 % (vs 2026-10-23) | 0.59 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 80,307.82, 24h -0.27%, z -0.17
- kraken: funding (raw, units unverified) 1.72257232932375, OI 2783.8901, OI change vs prior snapshot 0.53%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42393.1952, OI change vs prior snapshot 0.36%

**ETH**: price 2,325.47, 24h -0.68%, z -0.34
- kraken: funding (raw, units unverified) 0.047057037690375, OI 32708.22, OI change vs prior snapshot 1.57%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1117241.2558000006, OI change vs prior snapshot 0.04%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s)
