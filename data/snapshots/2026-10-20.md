# Data snapshot 2026-10-20 09:31 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.765 | 10-20 09:31 | **LIVE (~0 min old)** | +0.40 bp | 0.07 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.104 | 10-20 09:31 | **LIVE (~0 min old)** | -3.20 bp | -0.65 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.339 | 10-20 09:31 | **LIVE (~0 min old)** | -3.60 bp | -1.05 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.740 | 10-16 close | official value for 2026-10-16 (not live) | -4.00 bp (vs 2026-10-15) | -0.84 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-19 close | official value for 2026-10-19 (not live) | +0.00 bp (vs 2026-10-16) | 0.00 |  | fred:T10YIE |
| SOFR | 3.870 | 10-19 close | official value for 2026-10-19 (not live) | -1.00 bp (vs 2026-10-16) | -0.30 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.5s) |
| US dollar index (DXY) | 101.738 | 10-20 09:21 | **LIVE (~11 min old)** | -0.24 % (vs 2026-10-19) | -0.76 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.953 | 10-20 09:31 | **LIVE (~1 min old)** | +0.09 % (vs 2026-10-19) | 0.23 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.123 | 10-20 09:31 | **LIVE (~1 min old)** | +0.04 % (vs 2026-10-19) | 0.13 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.405 | 10-16 close | official value for 2026-10-16 (not live) | -0.14 % (vs 2026-10-15) | -0.48 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,726.750 | 10-20 09:21 | **LIVE (~11 min old)** | -0.10 % (vs 2026-10-19) | -0.17 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,616.500 | 10-20 09:21 | **LIVE (~11 min old)** | -0.36 % (vs 2026-10-19) | -0.33 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,744.700 | 10-20 09:21 | **LIVE (~11 min old)** | +0.09 % (vs 2026-10-19) | 0.09 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,678.030 | 10-20 09:31 | **LIVE (~1 min old)** | -0.17 % (vs 2026-10-19) | -0.26 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,346.590 | 10-20 09:31 | **LIVE (~1 min old)** | -0.62 % (vs 2026-10-19) | -0.54 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,728.298 | 10-19 16:30 | not trading now; last trade 10-19 16:30 ET | +0.25 % (vs 2026-10-16) | 0.27 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 18.640 | 10-20 09:16 | **LIVE (~16 min old)** | +0.20 pts (vs 2026-10-19) | 0.16 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.6s) |
| WTI crude | 99.810 | 10-20 09:21 | **LIVE (~11 min old)** | -3.71 % (vs 2026-10-19) | -1.49 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 110.530 | 10-20 09:21 | **LIVE (~11 min old)** | +0.89 % (vs 2026-10-19) | 0.39 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,138.600 | 10-20 09:21 | **LIVE (~11 min old)** | -0.52 % (vs 2026-10-19) | -0.45 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.577 | 10-20 09:21 | **LIVE (~11 min old)** | +0.60 % (vs 2026-10-19) | 0.51 |  | yahoo:HG=F (unofficial feed) |

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
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 81,283.92, 24h -0.91%, z -0.57
- kraken: funding (raw, units unverified) 1.5863077036824729, OI 2382.5229, OI change vs prior snapshot 0.28%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41146.70062, OI change vs prior snapshot -0.38%

**ETH**: price 2,385.63, 24h -0.52%, z -0.25
- kraken: funding (raw, units unverified) 0.02826537327525, OI 28992.217, OI change vs prior snapshot -0.15%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1063813.4774000004, OI change vs prior snapshot -0.06%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.5s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.6s)
