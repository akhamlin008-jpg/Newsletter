# Data snapshot 2026-10-09 11:14 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.21)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.812 | 10-09 11:14 | **LIVE (~0 min old)** | +5.60 bp | 0.93 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.270 | 10-09 11:14 | **LIVE (~0 min old)** | +3.70 bp | 0.74 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.458 | 10-09 11:14 | **LIVE (~0 min old)** | -1.90 bp | -0.55 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.920 | 10-07 close | official value for 2026-10-07 (not live) | +1.00 bp (vs 2026-10-06) | 0.20 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-08 close | official value for 2026-10-08 (not live) | -1.00 bp (vs 2026-10-07) | -0.61 |  | fred:T10YIE |
| SOFR | 3.870 | 10-08 close | official value for 2026-10-08 (not live) | -1.00 bp (vs 2026-10-07) | -0.26 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.6s) |
| US dollar index (DXY) | 102.286 | 10-09 11:04 | **LIVE (~10 min old)** | +0.14 % (vs 2026-10-08) | 0.47 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.359 | 10-09 11:14 | **LIVE (~0 min old)** | +0.19 % (vs 2026-10-08) | 0.39 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.120 | 10-09 11:13 | **LIVE (~1 min old)** | -0.02 % (vs 2026-10-08) | -0.05 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.385 | 10-02 close | official value for 2026-10-02 (not live) | -0.33 % (vs 2026-10-01) | -1.17 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,849.500 | 10-09 11:04 | **LIVE (~10 min old)** | +0.43 % (vs 2026-10-08) | 0.76 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 31,086.750 | 10-09 11:04 | **LIVE (~10 min old)** | +0.38 % (vs 2026-10-08) | 0.43 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,818.700 | 10-09 11:04 | **LIVE (~10 min old)** | +0.32 % (vs 2026-10-08) | 0.42 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,798.290 | 10-09 11:14 | **LIVE (~0 min old)** | +0.42 % (vs 2026-10-08) | 0.69 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,815.787 | 10-09 11:14 | **LIVE (~0 min old)** | +0.29 % (vs 2026-10-08) | 0.30 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,801.812 | 10-09 10:59 | **LIVE (~15 min old)** | +0.27 % (vs 2026-10-08) | 0.36 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 14.960 | 10-09 10:58 | **LIVE (~16 min old)** | -0.45 pts | -0.53 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.0s) |
| WTI crude | 91.860 | 10-09 11:04 | **LIVE (~10 min old)** | +0.40 % (vs 2026-10-08) | 0.15 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 104.720 | 10-09 11:04 | **LIVE (~10 min old)** | +0.42 % (vs 2026-10-08) | 0.17 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,211.500 | 10-09 11:04 | **LIVE (~10 min old)** | +1.31 % (vs 2026-10-08) | 1.09 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.701 | 10-09 11:04 | **LIVE (~10 min old)** | +2.79 % (vs 2026-10-08) | 2.21 | **YES** | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 82,786.76, 24h 2.25%, z 1.16
- kraken: funding (raw, units unverified) 1.1528130879848193, OI 2345.4604, OI change vs prior snapshot -1.12%
- hyperliquid: funding (raw, units unverified) 0.0000046444, OI 38784.00598, OI change vs prior snapshot -0.71%

**ETH**: price 2,485.17, 24h 2.12%, z 0.86
- kraken: funding (raw, units unverified) 0.01962382505000083, OI 28705.879, OI change vs prior snapshot 0.17%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1123674.3049999995, OI change vs prior snapshot 0.17%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.6s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.0s)
