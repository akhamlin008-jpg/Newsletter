# Data snapshot 2026-10-26 10:32 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.62), commodities (max |z| 2.47)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.699 | 10-26 10:31 | **LIVE (~0 min old)** | +1.70 bp | 0.27 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.966 | 10-26 10:31 | **LIVE (~0 min old)** | -2.20 bp | -0.35 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.267 | 10-26 10:31 | **LIVE (~0 min old)** | -3.90 bp | -1.20 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.640 | 10-22 close | official value for 2026-10-22 (not live) | -12.00 bp (vs 2026-10-21) | -2.62 | **YES** | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 10-23 close | official value for 2026-10-23 (not live) | +2.00 bp (vs 2026-10-22) | 0.96 |  | fred:T10YIE |
| SOFR | 3.920 | 10-23 close | official value for 2026-10-23 (not live) | +2.00 bp (vs 2026-10-22) | 0.67 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.3s) |
| US dollar index (DXY) | 101.994 | 10-26 10:22 | **LIVE (~10 min old)** | +0.18 % (vs 2026-10-23) | 0.62 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.434 | 10-26 10:32 | **LIVE (~0 min old)** | +0.60 % (vs 2026-10-23) | 1.34 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.119 | 10-26 10:31 | **LIVE (~1 min old)** | -0.31 % (vs 2026-10-23) | -1.21 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.405 | 10-16 close | official value for 2026-10-16 (not live) | -0.14 % (vs 2026-10-15) | -0.48 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,715.250 | 10-26 10:22 | **LIVE (~10 min old)** | +0.72 % (vs 2026-10-23) | 1.14 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,359.750 | 10-26 10:22 | **LIVE (~10 min old)** | +0.83 % (vs 2026-10-23) | 0.69 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,811.600 | 10-26 10:22 | **LIVE (~10 min old)** | +0.97 % (vs 2026-10-23) | 1.07 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,670.950 | 10-26 10:32 | **LIVE (~0 min old)** | +0.62 % (vs 2026-10-23) | 0.94 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,157.262 | 10-26 10:32 | **LIVE (~0 min old)** | +0.69 % (vs 2026-10-23) | 0.55 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,797.816 | 10-26 10:17 | **LIVE (~15 min old)** | +0.79 % (vs 2026-10-23) | 0.88 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 18.230 | 10-26 10:16 | **LIVE (~16 min old)** | -1.22 pts | -0.98 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.4s) |
| WTI crude | 100.800 | 10-26 10:22 | **LIVE (~10 min old)** | -2.39 % (vs 2026-10-23) | -0.88 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 109.950 | 10-26 10:22 | **LIVE (~10 min old)** | -5.80 % (vs 2026-10-23) | -2.47 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,026.700 | 10-26 10:22 | **LIVE (~10 min old)** | +0.47 % (vs 2026-10-23) | 0.40 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.540 | 10-26 10:22 | **LIVE (~10 min old)** | +0.98 % (vs 2026-10-23) | 0.75 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 79,629.79, 24h -1.14%, z -0.72
- kraken: funding (raw, units unverified) 0.768708422235, OI 2769.2919, OI change vs prior snapshot 0.32%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42242.51182, OI change vs prior snapshot 0.07%

**ETH**: price 2,306.96, 24h -1.42%, z -0.72
- kraken: funding (raw, units unverified) 0.011580535580875, OI 32202.669, OI change vs prior snapshot 0.54%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1116766.2836000002, OI change vs prior snapshot 0.39%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.3s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.4s)
