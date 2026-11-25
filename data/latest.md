# Data snapshot 2026-11-25 13:37 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.1)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.629 | 11-25 13:36 | **LIVE (~0 min old)** | -4.20 bp | -0.60 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.836 | 11-25 13:36 | **LIVE (~0 min old)** | -6.60 bp | -1.10 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.207 | 11-25 13:36 | **LIVE (~0 min old)** | -2.40 bp | -0.75 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.790 | 11-23 close | official value for 2026-11-23 (not live) | +2.00 bp (vs 2026-11-20) | 0.38 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.120 | 11-24 close | official value for 2026-11-24 (not live) | -1.00 bp (vs 2026-11-23) | -0.43 |  | fred:T10YIE |
| SOFR | 3.940 | 11-24 close | official value for 2026-11-24 (not live) | +2.00 bp (vs 2026-11-23) | 0.96 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.4s) |
| US dollar index (DXY) | 103.615 | 11-25 13:27 | **LIVE (~10 min old)** | -0.19 % (vs 2026-11-24) | -0.54 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.113 | 11-25 13:37 | **LIVE (~0 min old)** | +0.07 % (vs 2026-11-24) | 0.19 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.099 | 11-25 13:36 | **LIVE (~1 min old)** | +0.72 % (vs 2026-11-24) | 2.10 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 123.598 | 11-20 close | official value for 2026-11-20 (not live) | +0.06 % (vs 2026-11-19) | 0.23 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,176.500 | 11-25 13:27 | **LIVE (~10 min old)** | -0.57 % (vs 2026-11-24) | -0.31 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 25,899.500 | 11-25 13:27 | **LIVE (~10 min old)** | -1.43 % (vs 2026-11-24) | -0.52 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,702.300 | 11-25 13:27 | **LIVE (~10 min old)** | +0.48 % (vs 2026-11-24) | 0.28 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,164.390 | 11-25 13:37 | **LIVE (~0 min old)** | -0.51 % (vs 2026-11-24) | -0.28 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 25,861.438 | 11-25 13:37 | **LIVE (~0 min old)** | -1.35 % (vs 2026-11-24) | -0.49 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,696.596 | 11-25 13:22 | **LIVE (~15 min old)** | +0.43 % (vs 2026-11-24) | 0.25 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 28.540 | 11-25 13:22 | **LIVE (~15 min old)** | +2.18 pts (vs 2026-11-24) | 0.55 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.8s) |
| WTI crude | 83.510 | 11-25 13:27 | **LIVE (~10 min old)** | +1.78 % (vs 2026-11-24) | 0.60 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 90.160 | 11-25 13:27 | **LIVE (~10 min old)** | -1.36 % (vs 2026-11-24) | -0.43 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,558.300 | 11-25 13:27 | **LIVE (~10 min old)** | -0.10 % (vs 2026-11-24) | -0.05 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.458 | 11-25 13:27 | **LIVE (~10 min old)** | +1.79 % (vs 2026-11-24) | 0.81 |  | yahoo:HG=F (unofficial feed) |

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
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate); fell back after: cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.2s)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 59,664.99, 24h -0.23%, z -0.09
- kraken: funding (raw, units unverified) 1.0554802509078134, OI 2035.7398, OI change vs prior snapshot 0.28%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 35946.21306, OI change vs prior snapshot 1.01%

**ETH**: price 1,683.72, 24h 0.42%, z 0.12
- kraken: funding (raw, units unverified) -0.02399093522, OI 36288.19, OI change vs prior snapshot 1.52%
- hyperliquid: funding (raw, units unverified) 0.0000105477, OI 637460.0717999997, OI change vs prior snapshot -0.65%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.4s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.8s)
