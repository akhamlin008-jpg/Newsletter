# Data snapshot 2026-10-29 10:37 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.04)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.650 | 10-29 10:37 | **LIVE (~0 min old)** | -8.50 bp | -1.47 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.978 | 10-29 10:37 | **LIVE (~0 min old)** | -6.70 bp | -1.16 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.328 | 10-29 10:37 | **LIVE (~0 min old)** | +1.80 bp | 0.48 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.640 | 10-27 close | official value for 2026-10-27 (not live) | -2.00 bp (vs 2026-10-26) | -0.40 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.380 | 10-28 close | official value for 2026-10-28 (not live) | +3.00 bp (vs 2026-10-27) | 1.52 |  | fred:T10YIE |
| SOFR | 3.940 | 10-28 close | official value for 2026-10-28 (not live) | -1.00 bp (vs 2026-10-27) | -0.36 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.2s) |
| US dollar index (DXY) | 102.113 | 10-29 10:27 | **LIVE (~11 min old)** | -0.08 % (vs 2026-10-28) | -0.27 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.948 | 10-29 10:34 | **LIVE (~4 min old)** | -0.03 % (vs 2026-10-28) | -0.07 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.115 | 10-29 10:34 | **LIVE (~4 min old)** | +0.17 % (vs 2026-10-28) | 0.63 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,752.000 | 10-29 10:24 | **LIVE (~14 min old)** | -0.40 % (vs 2026-10-28) | -0.64 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,580.500 | 10-29 10:24 | **LIVE (~14 min old)** | -1.33 % (vs 2026-10-28) | -1.14 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,871.900 | 10-29 10:24 | **LIVE (~14 min old)** | +1.14 % (vs 2026-10-28) | 1.30 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,723.350 | 10-29 10:37 | **LIVE (~1 min old)** | -0.27 % (vs 2026-10-28) | -0.42 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,439.824 | 10-29 10:37 | **LIVE (~1 min old)** | -1.25 % (vs 2026-10-28) | -1.03 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,860.502 | 10-29 10:19 | **LIVE (~19 min old)** | +1.06 % (vs 2026-10-28) | 1.21 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 16.690 | 10-29 10:22 | **LIVE (~16 min old)** | -0.22 pts | -0.19 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.2s) |
| WTI crude | 100.780 | 10-29 10:24 | **LIVE (~14 min old)** | -1.95 % (vs 2026-10-28) | -0.74 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 110.120 | 10-29 10:24 | **LIVE (~14 min old)** | -4.51 % (vs 2026-10-28) | -2.04 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,035.100 | 10-29 10:24 | **LIVE (~14 min old)** | -0.41 % (vs 2026-10-28) | -0.36 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.569 | 10-29 10:24 | **LIVE (~14 min old)** | -1.08 % (vs 2026-10-28) | -0.85 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 81,411.64, 24h 1.16%, z 0.79
- kraken: funding (raw, units unverified) 0.52344273058564, OI 2433.5129, OI change vs prior snapshot -1.78%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42988.95176, OI change vs prior snapshot -1.25%

**ETH**: price 2,350.35, 24h 0.87%, z 0.47
- kraken: funding (raw, units unverified) -0.01293087684579244, OI 32374.382, OI change vs prior snapshot 0.40%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1132178.5606000002, OI change vs prior snapshot 0.02%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.2s)
