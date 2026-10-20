# Data snapshot 2026-10-20 08:56 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.768 | 10-20 08:56 | **LIVE (~1 min old)** | +0.70 bp | 0.13 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.106 | 10-20 08:56 | **LIVE (~0 min old)** | -3.00 bp | -0.61 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.338 | 10-20 08:56 | **LIVE (~1 min old)** | -3.70 bp | -1.08 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.740 | 10-16 close | official value for 2026-10-16 (not live) | -4.00 bp (vs 2026-10-15) | -0.84 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-19 close | official value for 2026-10-19 (not live) | +0.00 bp (vs 2026-10-16) | 0.00 |  | fred:T10YIE |
| SOFR | 3.870 | 10-19 close | official value for 2026-10-19 (not live) | -1.00 bp (vs 2026-10-16) | -0.30 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.9s) |
| US dollar index (DXY) | 101.718 | 10-20 08:46 | **LIVE (~11 min old)** | -0.26 % (vs 2026-10-19) | -0.82 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.057 | 10-20 08:56 | **LIVE (~1 min old)** | +0.16 % (vs 2026-10-19) | 0.40 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.123 | 10-20 08:56 | **LIVE (~1 min old)** | +0.04 % (vs 2026-10-19) | 0.13 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.405 | 10-16 close | official value for 2026-10-16 (not live) | -0.14 % (vs 2026-10-15) | -0.48 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,722.750 | 10-20 08:46 | **LIVE (~11 min old)** | -0.15 % (vs 2026-10-19) | -0.25 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,594.250 | 10-20 08:46 | **LIVE (~11 min old)** | -0.43 % (vs 2026-10-19) | -0.40 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,743.500 | 10-20 08:46 | **LIVE (~11 min old)** | +0.04 % (vs 2026-10-19) | 0.05 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,690.730 | 10-19 16:44 | not trading now; last trade 10-19 16:44 ET | +0.41 % (vs 2026-10-16) | 0.63 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,529.344 | 10-19 17:16 | not trading now; last trade 10-19 17:16 ET | +1.17 % (vs 2026-10-16) | 1.03 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,728.298 | 10-19 16:30 | not trading now; last trade 10-19 16:30 ET | +0.25 % (vs 2026-10-16) | 0.27 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 18.890 | 10-20 08:41 | **LIVE (~16 min old)** | +0.45 pts (vs 2026-10-19) | 0.37 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s) |
| WTI crude | 99.360 | 10-20 08:46 | **LIVE (~11 min old)** | -4.15 % (vs 2026-10-19) | -1.66 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 110.090 | 10-20 08:46 | **LIVE (~11 min old)** | +0.49 % (vs 2026-10-19) | 0.22 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,143.200 | 10-20 08:46 | **LIVE (~11 min old)** | -0.41 % (vs 2026-10-19) | -0.35 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.585 | 10-20 08:46 | **LIVE (~11 min old)** | +0.71 % (vs 2026-10-19) | 0.60 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 81,576.50, 24h -1.13%, z -0.71
- kraken: funding (raw, units unverified) 1.1913952709488063, OI 2375.9072, OI change vs prior snapshot 0.06%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41305.02674, OI change vs prior snapshot 0.24%

**ETH**: price 2,394.78, 24h -1.09%, z -0.52
- kraken: funding (raw, units unverified) 0.008244878859, OI 29035.342, OI change vs prior snapshot -0.03%
- hyperliquid: funding (raw, units unverified) 0.0000114019, OI 1064418.1200000003, OI change vs prior snapshot -0.70%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.9s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s)
