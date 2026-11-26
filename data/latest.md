# Data snapshot 2026-11-26 13:21 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.650 | 11-25 17:05 | not trading now; last trade 11-25 17:05 ET | -2.10 bp | -0.31 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.864 | 11-25 17:05 | not trading now; last trade 11-25 17:05 ET | -3.80 bp | -0.65 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.214 | 11-25 17:05 | not trading now; last trade 11-25 17:05 ET | -1.70 bp | -0.52 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.790 | 11-24 close | official value for 2026-11-24 (not live) | +0.00 bp (vs 2026-11-23) | 0.00 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.120 | 11-25 close | official value for 2026-11-25 (not live) | +0.00 bp (vs 2026-11-24) | 0.00 |  | fred:T10YIE |
| SOFR | 3.940 | 11-24 close | official value for 2026-11-24 (not live) | +2.00 bp (vs 2026-11-23) | 0.96 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.3s) |
| US dollar index (DXY) | 103.810 | 11-25 23:58 | not trading now; last trade 11-25 23:58 ET | +0.00 % (vs 2026-11-24) | 0.00 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.293 | 11-26 13:22 | **LIVE (~0 min old)** | +0.02 % (vs 2026-11-25) | 0.06 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.097 | 11-26 13:21 | **LIVE (~1 min old)** | +0.09 % (vs 2026-11-25) | 0.25 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 123.598 | 11-20 close | official value for 2026-11-20 (not live) | +0.06 % (vs 2026-11-19) | 0.23 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,247.750 | 11-25 23:58 | not trading now; last trade 11-25 23:58 ET | +0.72 % (vs 2026-11-25) | 0.41 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 26,389.750 | 11-25 23:58 | not trading now; last trade 11-25 23:58 ET | +1.11 % (vs 2026-11-25) | 0.42 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,721.700 | 11-25 23:58 | not trading now; last trade 11-25 23:58 ET | +0.58 % (vs 2026-11-25) | 0.35 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,182.780 | 11-25 16:00 | not trading now; last trade 11-25 16:00 ET | -0.25 % (vs 2026-11-24) | -0.14 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 26,046.896 | 11-25 16:00 | not trading now; last trade 11-25 16:00 ET | -0.64 % (vs 2026-11-24) | -0.23 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,704.061 | 11-25 16:00 | not trading now; last trade 11-25 16:00 ET | +0.71 % (vs 2026-11-24) | 0.42 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 26.800 | 11-26 11:30 | not trading now; last trade 11-26 11:30 ET | -1.49 pts (vs 2026-11-25) | -0.39 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (5.2s) |
| WTI crude | 84.420 | 11-25 23:58 | not trading now; last trade 11-25 23:58 ET | +0.88 % (vs 2026-11-25) | 0.31 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 91.170 | 11-25 23:56 | not trading now; last trade 11-25 23:56 ET | -3.64 % (vs 2026-11-25) | -1.15 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,620.400 | 11-25 23:58 | not trading now; last trade 11-25 23:58 ET | +2.39 % (vs 2026-11-25) | 1.16 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.492 | 11-25 23:58 | not trading now; last trade 11-25 23:58 ET | +3.00 % (vs 2026-11-25) | 1.40 |  | yahoo:HG=F (unofficial feed) |

## Row notes

- **US 10-year yield**: fell back after: yahoo:10Y=F -> no prior close before the current session (11.9s)
- **10-year real yield (TIPS)**: official end-of-day series, published with a lag; no free live source
- **10-year breakeven inflation**: official end-of-day series, published with a lag; no free live source
- **SOFR**: NY Fed publishes ~8:00 AM ET for the prior business day; before that, the latest is the previous day's
- **3M SOFR futures implied rate (front)**: 100 minus futures price; forward-looking proxy for SOFR
- **US dollar index (DXY)**: fell back after: yahoo:DX=F -> YFTzMissingError: $DX=F: possibly delisted; no timezone found (5.2s)
- **USD/JPY**: live move vs prior close, scored against full-day volatility (approximate)
- **EUR/USD**: live move vs prior close, scored against full-day volatility (approximate)
- **Broad trade-weighted dollar**: official end-of-day series, published with a lag; no free live source; use DXY / EUR/USD / USD/JPY for the live picture
- **S&P 500 futures (ES)**: roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open
- **Nasdaq 100 futures (NQ)**: roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Russell 2000 futures (RTY)**: roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; fell back after: cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.0s)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **Gold**: roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 60,443.08, 24h 1.33%, z 0.54
- kraken: funding (raw, units unverified) 0.5037600312266882, OI 2066.9819, OI change vs prior snapshot -2.38%
- hyperliquid: funding (raw, units unverified) 0.0000025295, OI 35406.2512399999, OI change vs prior snapshot 0.01%

**ETH**: price 1,690.45, 24h 0.73%, z 0.22
- kraken: funding (raw, units unverified) -0.0107535714075, OI 31035.982, OI change vs prior snapshot -0.12%
- hyperliquid: funding (raw, units unverified) -0.0000060963, OI 664273.1128000002, OI change vs prior snapshot 0.09%


## Source errors

- yahoo:10Y=F -> no prior close before the current session (11.9s)
- yahoo:SR3=F -> no prior close before the current session (9.3s)
- yahoo:DX=F -> YFTzMissingError: $DX=F: possibly delisted; no timezone found (5.2s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (5.2s)
