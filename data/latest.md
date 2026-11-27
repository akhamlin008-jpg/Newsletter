# Data snapshot 2026-11-27 12:24 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.38)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.697 | 11-27 12:24 | **LIVE (~0 min old)** | +6.20 bp | 0.92 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.936 | 11-27 12:24 | **LIVE (~0 min old)** | +8.80 bp | 1.52 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.239 | 11-27 12:24 | **LIVE (~0 min old)** | +2.60 bp | 0.80 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.790 | 11-24 close | official value for 2026-11-24 (not live) | +0.00 bp (vs 2026-11-23) | 0.00 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.120 | 11-25 close | official value for 2026-11-25 (not live) | +0.00 bp (vs 2026-11-24) | 0.00 |  | fred:T10YIE |
| SOFR | 3.950 | 11-25 close | official value for 2026-11-25 (not live) | +1.00 bp (vs 2026-11-24) | 0.49 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.8s) |
| US dollar index (DXY) | 104.001 | 11-27 12:14 | **LIVE (~10 min old)** | +0.32 % (vs 2026-11-25) | 0.94 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.519 | 11-27 12:24 | **LIVE (~0 min old)** | +0.19 % (vs 2026-11-26) | 0.58 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.094 | 11-27 12:23 | **LIVE (~1 min old)** | -0.26 % (vs 2026-11-26) | -0.74 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 123.598 | 11-20 close | official value for 2026-11-20 (not live) | +0.06 % (vs 2026-11-19) | 0.23 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,288.500 | 11-27 12:14 | **LIVE (~10 min old)** | +1.29 % (vs 2026-11-25) | 0.73 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 26,612.250 | 11-27 12:14 | **LIVE (~10 min old)** | +1.96 % (vs 2026-11-25) | 0.74 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,746.700 | 11-27 12:14 | **LIVE (~10 min old)** | +1.50 % (vs 2026-11-25) | 0.90 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,285.670 | 11-27 12:24 | **LIVE (~0 min old)** | +1.43 % (vs 2026-11-25) | 0.80 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 26,592.900 | 11-27 12:24 | **LIVE (~0 min old)** | +2.10 % (vs 2026-11-25) | 0.78 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,744.148 | 11-27 12:09 | **LIVE (~15 min old)** | +1.48 % (vs 2026-11-25) | 0.89 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 24.860 | 11-27 12:09 | **LIVE (~15 min old)** | -1.94 pts (vs 2026-11-26) | -0.52 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.6s) |
| WTI crude | 83.000 | 11-27 12:14 | **LIVE (~10 min old)** | -0.81 % (vs 2026-11-25) | -0.28 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 90.250 | 11-27 12:14 | **LIVE (~10 min old)** | -4.61 % (vs 2026-11-25) | -1.46 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,661.800 | 11-27 12:14 | **LIVE (~10 min old)** | +3.56 % (vs 2026-11-25) | 1.73 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.604 | 11-27 12:14 | **LIVE (~10 min old)** | +5.10 % (vs 2026-11-25) | 2.38 | **YES** | yahoo:HG=F (unofficial feed) |

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
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate); fell back after: cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.1s)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 59,821.56, 24h -1.05%, z -0.44
- kraken: funding (raw, units unverified) -0.71135114015248, OI 2085.2404, OI change vs prior snapshot 0.88%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 35997.49484, OI change vs prior snapshot 1.67%

**ETH**: price 1,669.11, 24h -1.37%, z -0.43
- kraken: funding (raw, units unverified) -0.025401703574, OI 34048.363, OI change vs prior snapshot 9.71%
- hyperliquid: funding (raw, units unverified) 0.0000051975, OI 599046.0122000005, OI change vs prior snapshot -9.82%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.8s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.6s)
