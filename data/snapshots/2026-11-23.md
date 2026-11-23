# Data snapshot 2026-11-23 14:10 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** equity (max |z| 3.09), vol (max |z| 2.47)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.679 | 11-23 14:10 | **LIVE (~0 min old)** | +6.60 bp | 1.00 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.932 | 11-23 14:09 | **LIVE (~0 min old)** | +2.00 bp | 0.36 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.253 | 11-23 14:09 | **LIVE (~0 min old)** | -4.60 bp | -1.36 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.880 | 11-19 close | official value for 2026-11-19 (not live) | +0.00 bp (vs 2026-11-18) | 0.00 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.150 | 11-20 close | official value for 2026-11-20 (not live) | -1.00 bp (vs 2026-11-19) | -0.41 |  | fred:T10YIE |
| SOFR | 3.920 | 11-20 close | official value for 2026-11-20 (not live) | +1.00 bp (vs 2026-11-19) | 0.46 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.7s) |
| US dollar index (DXY) | 104.425 | 11-23 14:00 | **LIVE (~10 min old)** | +0.59 % (vs 2026-11-20) | 1.81 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.083 | 11-23 14:10 | **LIVE (~0 min old)** | -0.39 % (vs 2026-11-20) | -1.13 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.090 | 11-23 14:09 | **LIVE (~1 min old)** | -0.66 % (vs 2026-11-20) | -2.00 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 122.650 | 11-13 close | official value for 2026-11-13 (not live) | +0.09 % (vs 2026-11-12) | 0.34 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,243.500 | 11-23 14:00 | **LIVE (~10 min old)** | +4.45 % (vs 2026-11-20) | 2.88 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 26,726.500 | 11-23 14:00 | **LIVE (~10 min old)** | +6.37 % (vs 2026-11-20) | 2.75 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,665.400 | 11-23 14:00 | **LIVE (~10 min old)** | +3.01 % (vs 2026-11-20) | 1.88 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,244.270 | 11-23 14:10 | **LIVE (~0 min old)** | +4.83 % (vs 2026-11-20) | 3.09 | **YES** | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 26,737.979 | 11-23 14:10 | **LIVE (~0 min old)** | +6.83 % (vs 2026-11-20) | 2.93 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,662.549 | 11-23 13:55 | **LIVE (~15 min old)** | +3.13 % (vs 2026-11-20) | 1.96 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 27.340 | 11-23 13:55 | **LIVE (~15 min old)** | -8.55 pts (vs 2026-11-20) | -2.47 | **YES** | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.8s) |
| WTI crude | 80.490 | 11-23 14:00 | **LIVE (~10 min old)** | -4.16 % (vs 2026-11-20) | -1.46 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 87.100 | 11-23 14:00 | **LIVE (~10 min old)** | -5.91 % (vs 2026-11-20) | -1.87 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,648.000 | 11-23 14:00 | **LIVE (~10 min old)** | +3.77 % (vs 2026-11-20) | 1.96 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.627 | 11-23 14:00 | **LIVE (~10 min old)** | +2.74 % (vs 2026-11-20) | 1.45 |  | yahoo:HG=F (unofficial feed) |

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
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open
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

**BTC**: price 61,460.93, 24h 1.36%, z 0.52
- kraken: funding (raw, units unverified) 1.0233451803, OI 2283.0941, OI change vs prior snapshot 7.74%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 37236.20258, OI change vs prior snapshot -5.75%

**ETH**: price 1,741.44, 24h 1.66%, z 0.46
- kraken: funding (raw, units unverified) 0.000871938522917246, OI 34082.839, OI change vs prior snapshot 17.19%
- hyperliquid: funding (raw, units unverified) 0.0000032188, OI 616574.6204000004, OI change vs prior snapshot -3.79%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.7s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.8s)
