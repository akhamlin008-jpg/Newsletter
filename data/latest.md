# Data snapshot 2026-11-17 12:02 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.793 | 11-17 12:01 | **LIVE (~0 min old)** | -3.40 bp | -0.47 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.099 | 11-17 12:02 | **LIVE (~0 min old)** | -2.20 bp | -0.36 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.306 | 11-17 12:01 | **LIVE (~0 min old)** | +1.20 bp | 0.32 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.910 | 11-13 close | official value for 2026-11-13 (not live) | +5.00 bp (vs 2026-11-12) | 0.95 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.200 | 11-16 close | official value for 2026-11-16 (not live) | -4.00 bp (vs 2026-11-13) | -1.71 |  | fred:T10YIE |
| SOFR | 3.930 | 11-16 close | official value for 2026-11-16 (not live) | +3.00 bp (vs 2026-11-13) | 1.28 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.5s) |
| US dollar index (DXY) | 103.431 | 11-17 11:52 | **LIVE (~10 min old)** | -0.11 % (vs 2026-11-16) | -0.32 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.248 | 11-17 12:02 | **LIVE (~0 min old)** | -0.33 % (vs 2026-11-16) | -0.87 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.102 | 11-17 12:01 | **LIVE (~1 min old)** | -0.07 % (vs 2026-11-16) | -0.20 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 122.650 | 11-13 close | official value for 2026-11-13 (not live) | +0.09 % (vs 2026-11-12) | 0.34 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,325.250 | 11-17 11:52 | **LIVE (~10 min old)** | -1.53 % (vs 2026-11-16) | -1.18 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 26,821.500 | 11-17 11:52 | **LIVE (~10 min old)** | -1.70 % (vs 2026-11-16) | -0.84 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,709.900 | 11-17 11:52 | **LIVE (~10 min old)** | -1.51 % (vs 2026-11-16) | -1.02 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,325.190 | 11-17 12:02 | **LIVE (~0 min old)** | -1.23 % (vs 2026-11-16) | -0.94 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 26,819.104 | 11-17 12:02 | **LIVE (~0 min old)** | -1.39 % (vs 2026-11-16) | -0.68 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,704.333 | 11-17 11:47 | **LIVE (~15 min old)** | -1.41 % (vs 2026-11-16) | -0.95 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 26.900 | 11-17 11:46 | **LIVE (~16 min old)** | +3.99 pts | 1.29 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.7s) |
| WTI crude | 86.440 | 11-17 11:52 | **LIVE (~10 min old)** | +0.84 % (vs 2026-11-16) | 0.27 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 93.130 | 11-17 11:52 | **LIVE (~10 min old)** | +0.75 % (vs 2026-11-16) | 0.21 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,867.700 | 11-17 11:52 | **LIVE (~10 min old)** | +0.38 % (vs 2026-11-16) | 0.25 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.979 | 11-17 11:52 | **LIVE (~10 min old)** | -0.32 % (vs 2026-11-16) | -0.22 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 63,598.55, 24h -1.91%, z -0.75
- kraken: funding (raw, units unverified) 0.994702749942, OI 2237.0331, OI change vs prior snapshot 0.60%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 37563.09604, OI change vs prior snapshot -0.57%

**ETH**: price 1,773.76, 24h -2.50%, z -0.73
- kraken: funding (raw, units unverified) 0.013606225610833925, OI 28762.593, OI change vs prior snapshot -0.22%
- hyperliquid: funding (raw, units unverified) -0.000023099, OI 623613.4411999999, OI change vs prior snapshot 0.24%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.5s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.7s)
