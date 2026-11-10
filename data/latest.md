# Data snapshot 2026-11-10 10:45 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 3.19), crypto (max |z| 2.15)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.733 | 11-10 10:45 | **LIVE (~0 min old)** | +18.60 bp | 3.19 | **YES** | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.992 | 11-10 10:45 | **LIVE (~0 min old)** | +13.00 bp | 2.41 | **YES** | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.259 | 11-10 10:45 | **LIVE (~0 min old)** | -5.60 bp | -1.52 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.630 | 11-06 close | official value for 2026-11-06 (not live) | +3.00 bp (vs 2026-11-05) | 0.69 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.220 | 11-09 close | official value for 2026-11-09 (not live) | -1.00 bp (vs 2026-11-06) | -0.43 |  | fred:T10YIE |
| SOFR | 3.880 | 11-09 close | official value for 2026-11-09 (not live) | -1.00 bp (vs 2026-11-06) | -0.40 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.4s) |
| US dollar index (DXY) | 102.178 | 11-10 10:35 | **LIVE (~10 min old)** | +0.52 % (vs 2026-11-09) | 1.55 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.626 | 11-10 10:45 | **LIVE (~0 min old)** | +0.21 % (vs 2026-11-09) | 0.54 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.117 | 11-10 10:45 | **LIVE (~0 min old)** | +0.22 % (vs 2026-11-09) | 0.73 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,544.500 | 11-10 10:35 | **LIVE (~10 min old)** | -0.39 % (vs 2026-11-09) | -0.29 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,933.500 | 11-10 10:35 | **LIVE (~10 min old)** | -0.29 % (vs 2026-11-09) | -0.14 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,821.500 | 11-10 10:35 | **LIVE (~10 min old)** | -0.95 % (vs 2026-11-09) | -0.61 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,498.870 | 11-10 10:45 | **LIVE (~0 min old)** | -0.68 % (vs 2026-11-09) | -0.49 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,701.838 | 11-10 10:45 | **LIVE (~0 min old)** | -0.74 % (vs 2026-11-09) | -0.35 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,815.031 | 11-10 10:30 | **LIVE (~15 min old)** | -0.91 % (vs 2026-11-09) | -0.58 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 20.460 | 11-10 10:29 | **LIVE (~16 min old)** | +0.54 pts | 0.16 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s) |
| WTI crude | 85.270 | 11-10 10:35 | **LIVE (~10 min old)** | -1.82 % (vs 2026-11-09) | -0.53 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 90.400 | 11-10 10:35 | **LIVE (~10 min old)** | -2.34 % (vs 2026-11-09) | -0.60 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,056.700 | 11-10 10:35 | **LIVE (~10 min old)** | -1.40 % (vs 2026-11-09) | -0.97 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.282 | 11-10 10:35 | **LIVE (~10 min old)** | -0.73 % (vs 2026-11-09) | -0.51 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 72,926.14, 24h -3.32%, z -1.64
- kraken: funding (raw, units unverified) 0.694230678087358, OI 2467.2896, OI change vs prior snapshot -1.92%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41816.24764, OI change vs prior snapshot -1.22%

**ETH**: price 2,010.13, 24h -6.28%, z -2.15 **FLAG**
- kraken: funding (raw, units unverified) -0.01581160784875, OI 30108.274, OI change vs prior snapshot 0.48%
- hyperliquid: funding (raw, units unverified) 0.000000738, OI 795720.3131999996, OI change vs prior snapshot -0.14%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.4s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s)
