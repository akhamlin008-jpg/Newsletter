# Data snapshot 2026-11-16 11:56 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.859 | 11-16 11:55 | **LIVE (~1 min old)** | -1.50 bp | -0.20 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.145 | 11-16 11:54 | **LIVE (~1 min old)** | -0.80 bp | -0.13 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.286 | 11-16 11:54 | **LIVE (~1 min old)** | +0.70 bp | 0.18 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.860 | 11-12 close | official value for 2026-11-12 (not live) | +8.00 bp (vs 2026-11-10) | 1.59 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.240 | 11-13 close | official value for 2026-11-13 (not live) | +0.00 bp (vs 2026-11-12) | 0.00 |  | fred:T10YIE |
| SOFR | 3.900 | 11-13 close | official value for 2026-11-13 (not live) | +0.00 bp (vs 2026-11-12) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.4s) |
| US dollar index (DXY) | 103.532 | 11-16 11:46 | **LIVE (~10 min old)** | +0.12 % (vs 2026-11-13) | 0.32 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.625 | 11-16 11:56 | **LIVE (~0 min old)** | -0.16 % (vs 2026-11-13) | -0.39 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.101 | 11-16 11:55 | **LIVE (~1 min old)** | -0.37 % (vs 2026-11-13) | -0.98 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,496.250 | 11-16 11:46 | **LIVE (~10 min old)** | -1.14 % (vs 2026-11-13) | -0.91 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,539.500 | 11-16 11:46 | **LIVE (~10 min old)** | -1.77 % (vs 2026-11-13) | -0.89 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,765.800 | 11-16 11:46 | **LIVE (~10 min old)** | -1.13 % (vs 2026-11-13) | -0.77 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,472.200 | 11-16 11:56 | **LIVE (~0 min old)** | -1.18 % (vs 2026-11-13) | -0.94 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,446.818 | 11-16 11:56 | **LIVE (~0 min old)** | -1.78 % (vs 2026-11-13) | -0.90 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,761.478 | 11-16 11:41 | **LIVE (~15 min old)** | -1.04 % (vs 2026-11-13) | -0.71 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 21.010 | 11-16 11:40 | **LIVE (~16 min old)** | +1.71 pts | 0.56 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.6s) |
| WTI crude | 86.700 | 11-16 11:46 | **LIVE (~10 min old)** | -2.10 % (vs 2026-11-13) | -0.68 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 93.660 | 11-16 11:46 | **LIVE (~10 min old)** | -2.27 % (vs 2026-11-13) | -0.64 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,863.100 | 11-16 11:46 | **LIVE (~10 min old)** | -0.60 % (vs 2026-11-13) | -0.39 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.026 | 11-16 11:46 | **LIVE (~10 min old)** | -0.89 % (vs 2026-11-13) | -0.62 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 64,685.89, 24h 0.02%, z 0.01
- kraken: funding (raw, units unverified) 1.021012442673, OI 2247.132, OI change vs prior snapshot -10.91%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 36080.4191, OI change vs prior snapshot -8.40%

**ETH**: price 1,822.92, 24h 0.50%, z 0.14
- kraken: funding (raw, units unverified) -0.037530384609375, OI 27345.493, OI change vs prior snapshot -5.52%
- hyperliquid: funding (raw, units unverified) 0.0000097325, OI 587121.4078000002, OI change vs prior snapshot -19.18%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.4s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.6s)
