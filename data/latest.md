# Data snapshot 2026-10-08 11:32 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.17)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.814 | 10-08 11:32 | **LIVE (~0 min old)** | +5.00 bp | 0.81 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.299 | 10-08 11:32 | **LIVE (~0 min old)** | +2.20 bp | 0.42 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.485 | 10-08 11:32 | **LIVE (~0 min old)** | -2.80 bp | -0.82 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.910 | 10-06 close | official value for 2026-10-06 (not live) | -4.00 bp (vs 2026-10-05) | -0.79 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 10-07 close | official value for 2026-10-07 (not live) | +0.00 bp (vs 2026-10-06) | 0.00 |  | fred:T10YIE |
| SOFR | 3.880 | 10-07 close | official value for 2026-10-07 (not live) | -2.00 bp (vs 2026-10-06) | -0.50 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.7s) |
| US dollar index (DXY) | 102.253 | 10-08 11:22 | **LIVE (~10 min old)** | +0.01 % (vs 2026-10-07) | 0.04 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.275 | 10-08 11:32 | **LIVE (~0 min old)** | -0.01 % (vs 2026-10-07) | -0.03 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.120 | 10-08 11:31 | **LIVE (~1 min old)** | -0.47 % (vs 2026-10-07) | -1.59 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.385 | 10-02 close | official value for 2026-10-02 (not live) | -0.33 % (vs 2026-10-01) | -1.17 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,823.750 | 10-08 11:22 | **LIVE (~10 min old)** | -0.37 % (vs 2026-10-07) | -0.65 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 31,239.500 | 10-08 11:22 | **LIVE (~10 min old)** | -0.52 % (vs 2026-10-07) | -0.63 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,781.900 | 10-08 11:22 | **LIVE (~10 min old)** | -1.08 % (vs 2026-10-07) | -1.34 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,773.630 | 10-08 11:32 | **LIVE (~0 min old)** | -0.36 % (vs 2026-10-07) | -0.58 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,988.375 | 10-08 11:32 | **LIVE (~0 min old)** | -0.55 % (vs 2026-10-07) | -0.58 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,766.323 | 10-08 11:17 | **LIVE (~15 min old)** | -0.96 % (vs 2026-10-07) | -1.22 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.550 | 10-08 11:16 | **LIVE (~16 min old)** | +0.47 pts | 0.54 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s) |
| WTI crude | 92.820 | 10-08 11:22 | **LIVE (~10 min old)** | +5.14 % (vs 2026-10-07) | 2.01 | **YES** | yahoo:CL=F (unofficial feed) |
| Brent crude | 105.420 | 10-08 11:22 | **LIVE (~10 min old)** | +5.21 % (vs 2026-10-07) | 2.17 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,140.100 | 10-08 11:22 | **LIVE (~10 min old)** | -0.01 % (vs 2026-10-07) | -0.01 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.592 | 10-08 11:22 | **LIVE (~10 min old)** | -0.07 % (vs 2026-10-07) | -0.05 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 81,338.59, 24h -2.49%, z -1.28
- kraken: funding (raw, units unverified) 1.3746085662600276, OI 2418.3551, OI change vs prior snapshot -3.37%
- hyperliquid: funding (raw, units unverified) 0.0000112867, OI 40248.1793, OI change vs prior snapshot -2.26%

**ETH**: price 2,460.20, 24h -4.25%, z -1.82
- kraken: funding (raw, units unverified) 0.016631261885334175, OI 29260.017, OI change vs prior snapshot -2.39%
- hyperliquid: funding (raw, units unverified) -0.0000094569, OI 1139472.8228000016, OI change vs prior snapshot -0.96%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.7s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s)
