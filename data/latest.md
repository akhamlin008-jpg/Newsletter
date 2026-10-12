# Data snapshot 2026-10-12 13:47 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.791 | 10-09 17:05 | not trading now; last trade 10-09 17:05 ET | +3.50 bp | 0.60 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.240 | 10-12 13:33 | **LIVE (~15 min old)** | -0.40 bp (vs 2026-10-09) | -0.09 |  | yahoo:^TNX (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.449 | 10-09 17:05 | not trading now; last trade 10-09 17:05 ET | -3.90 bp | -1.14 |  | calc: yahoo:^TNX minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.870 | 10-08 close | official value for 2026-10-08 (not live) | -5.00 bp (vs 2026-10-07) | -1.03 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 10-09 close | official value for 2026-10-09 (not live) | -2.00 bp (vs 2026-10-08) | -1.23 |  | fred:T10YIE |
| SOFR | 3.870 | 10-08 close | official value for 2026-10-08 (not live) | -1.00 bp (vs 2026-10-07) | -0.26 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (7.9s) |
| US dollar index (DXY) | 102.559 | 10-12 13:37 | **LIVE (~11 min old)** | +0.34 % (vs 2026-10-09) | 1.15 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.659 | 10-12 13:47 | **LIVE (~1 min old)** | +0.38 % (vs 2026-10-09) | 0.80 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.116 | 10-12 13:47 | **LIVE (~1 min old)** | -0.46 % (vs 2026-10-09) | -1.52 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.385 | 10-02 close | official value for 2026-10-02 (not live) | -0.33 % (vs 2026-10-01) | -1.17 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,851.000 | 10-12 13:37 | **LIVE (~11 min old)** | -0.11 % (vs 2026-10-09) | -0.20 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,873.250 | 10-12 13:37 | **LIVE (~11 min old)** | -0.76 % (vs 2026-10-09) | -0.89 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,814.000 | 10-12 13:37 | **LIVE (~11 min old)** | -0.29 % (vs 2026-10-09) | -0.38 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,804.950 | 10-12 13:47 | **LIVE (~1 min old)** | -0.08 % (vs 2026-10-09) | -0.14 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,662.998 | 10-12 13:48 | **LIVE (~0 min old)** | -0.71 % (vs 2026-10-09) | -0.74 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,798.586 | 10-12 13:32 | **LIVE (~16 min old)** | -0.30 % (vs 2026-10-09) | -0.40 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.210 | 10-12 13:32 | **LIVE (~15 min old)** | +0.37 pts | 0.44 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (5.8s) |
| WTI crude | 93.800 | 10-12 13:38 | **LIVE (~10 min old)** | +2.12 % (vs 2026-10-09) | 0.83 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 106.800 | 10-12 13:38 | **LIVE (~10 min old)** | +1.99 % (vs 2026-10-09) | 0.81 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,193.700 | 10-12 13:38 | **LIVE (~10 min old)** | -0.54 % (vs 2026-10-09) | -0.44 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.751 | 10-12 13:37 | **LIVE (~11 min old)** | +1.63 % (vs 2026-10-09) | 1.24 |  | yahoo:HG=F (unofficial feed) |

## Row notes

- **US 10-year yield**: live move vs prior close, scored against full-day volatility (approximate); fell back after: yahoo:10Y=F -> no prior close before the current session (12.5s)
- **2s10s spread (10Y minus 2Y)**: legs come from different sources; spread is approximate
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

**BTC**: price 82,388.29, 24h -1.61%, z -0.90
- kraken: funding (raw, units unverified) 0.5232475115968608, OI 2389.4222, OI change vs prior snapshot 0.45%
- hyperliquid: funding (raw, units unverified) 0.0000043447, OI 37983.57854, OI change vs prior snapshot -0.04%

**ETH**: price 2,504.86, 24h -1.21%, z -0.53
- kraken: funding (raw, units unverified) 0.021399341940625, OI 30582.947, OI change vs prior snapshot -0.55%
- hyperliquid: funding (raw, units unverified) 0.0000094128, OI 1103171.8882000009, OI change vs prior snapshot -0.02%


## Source errors

- yahoo:10Y=F -> no prior close before the current session (12.5s)
- yahoo:SR3=F -> no prior close before the current session (7.9s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (5.8s)
