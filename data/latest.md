# Data snapshot 2026-10-13 10:57 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.804 | 10-13 10:57 | **LIVE (~0 min old)** | +1.30 bp | 0.22 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.215 | 10-13 10:57 | **LIVE (~0 min old)** | -2.90 bp | -0.57 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.411 | 10-13 10:57 | **LIVE (~0 min old)** | -4.20 bp | -1.22 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.870 | 10-08 close | official value for 2026-10-08 (not live) | -5.00 bp (vs 2026-10-07) | -1.03 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 10-09 close | official value for 2026-10-09 (not live) | -2.00 bp (vs 2026-10-08) | -1.23 |  | fred:T10YIE |
| SOFR | 3.870 | 10-09 close | official value for 2026-10-09 (not live) | +0.00 bp (vs 2026-10-08) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.9s) |
| US dollar index (DXY) | 102.261 | 10-13 10:47 | **LIVE (~11 min old)** | -0.31 % (vs 2026-10-12) | -1.03 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.346 | 10-13 10:57 | **LIVE (~1 min old)** | +0.18 % (vs 2026-10-09) | 0.38 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.120 | 10-13 10:57 | **LIVE (~1 min old)** | -0.15 % (vs 2026-10-09) | -0.52 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.385 | 10-02 close | official value for 2026-10-02 (not live) | -0.33 % (vs 2026-10-01) | -1.17 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,851.250 | 10-13 10:47 | **LIVE (~11 min old)** | -0.09 % (vs 2026-10-12) | -0.16 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,752.250 | 10-13 10:47 | **LIVE (~11 min old)** | -0.47 % (vs 2026-10-12) | -0.56 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,796.200 | 10-13 10:47 | **LIVE (~11 min old)** | -0.57 % (vs 2026-10-12) | -0.76 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,796.540 | 10-13 10:57 | **LIVE (~1 min old)** | -0.14 % (vs 2026-10-12) | -0.23 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,483.152 | 10-13 10:57 | **LIVE (~1 min old)** | -0.59 % (vs 2026-10-12) | -0.62 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,781.264 | 10-13 10:42 | **LIVE (~16 min old)** | -0.47 % (vs 2026-10-12) | -0.64 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.240 | 10-13 10:41 | **LIVE (~16 min old)** | +0.03 pts | 0.04 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.8s) |
| WTI crude | 93.680 | 10-13 10:47 | **LIVE (~11 min old)** | -0.06 % (vs 2026-10-12) | -0.03 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 105.590 | 10-13 10:47 | **LIVE (~11 min old)** | -0.99 % (vs 2026-10-12) | -0.41 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,193.900 | 10-13 10:47 | **LIVE (~11 min old)** | +0.08 % (vs 2026-10-12) | 0.07 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.738 | 10-13 10:47 | **LIVE (~11 min old)** | +0.59 % (vs 2026-10-12) | 0.46 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 83,492.31, 24h 1.21%, z 0.66
- kraken: funding (raw, units unverified) 1.28076954413032, OI 2130.7388, OI change vs prior snapshot -10.83%
- hyperliquid: funding (raw, units unverified) 0.0000095579, OI 38441.48394, OI change vs prior snapshot 1.21%

**ETH**: price 2,516.29, 24h -0.19%, z -0.08
- kraken: funding (raw, units unverified) 0.020390510440160402, OI 31875.648, OI change vs prior snapshot 4.23%
- hyperliquid: funding (raw, units unverified) 0.0000070241, OI 1086359.4227999998, OI change vs prior snapshot -1.52%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.9s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.8s)
