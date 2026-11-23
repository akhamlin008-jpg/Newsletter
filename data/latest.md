# Data snapshot 2026-11-23 14:27 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** equity (max |z| 3.17), vol (max |z| 2.65)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.679 | 11-23 14:27 | **LIVE (~0 min old)** | +6.60 bp | 1.00 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.932 | 11-23 14:27 | **LIVE (~0 min old)** | +2.00 bp | 0.36 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.253 | 11-23 14:27 | **LIVE (~0 min old)** | -4.60 bp | -1.36 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.880 | 11-19 close | official value for 2026-11-19 (not live) | +0.00 bp (vs 2026-11-18) | 0.00 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.150 | 11-20 close | official value for 2026-11-20 (not live) | -1.00 bp (vs 2026-11-19) | -0.41 |  | fred:T10YIE |
| SOFR | 3.920 | 11-20 close | official value for 2026-11-20 (not live) | +1.00 bp (vs 2026-11-19) | 0.46 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.0s) |
| US dollar index (DXY) | 104.384 | 11-23 14:17 | **LIVE (~10 min old)** | +0.55 % (vs 2026-11-20) | 1.69 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.002 | 11-23 14:27 | **LIVE (~0 min old)** | -0.44 % (vs 2026-11-20) | -1.28 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.090 | 11-23 14:26 | **LIVE (~1 min old)** | -0.60 % (vs 2026-11-20) | -1.81 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 122.650 | 11-13 close | official value for 2026-11-13 (not live) | +0.09 % (vs 2026-11-12) | 0.34 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,269.000 | 11-23 14:17 | **LIVE (~10 min old)** | +4.82 % (vs 2026-11-20) | 3.11 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 26,850.000 | 11-23 14:17 | **LIVE (~10 min old)** | +6.86 % (vs 2026-11-20) | 2.97 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,675.700 | 11-23 14:17 | **LIVE (~10 min old)** | +3.41 % (vs 2026-11-20) | 2.13 | **YES** | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,252.380 | 11-23 14:27 | **LIVE (~0 min old)** | +4.95 % (vs 2026-11-20) | 3.17 | **YES** | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 26,765.037 | 11-23 14:27 | **LIVE (~0 min old)** | +6.94 % (vs 2026-11-20) | 2.98 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,667.782 | 11-23 14:12 | **LIVE (~15 min old)** | +3.33 % (vs 2026-11-20) | 2.09 | **YES** | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 26.730 | 11-23 14:12 | **LIVE (~15 min old)** | -9.16 pts (vs 2026-11-20) | -2.65 | **YES** | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.0s) |
| WTI crude | 80.390 | 11-23 14:17 | **LIVE (~10 min old)** | -4.27 % (vs 2026-11-20) | -1.50 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 86.990 | 11-23 14:17 | **LIVE (~10 min old)** | -6.03 % (vs 2026-11-20) | -1.91 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,655.500 | 11-23 14:17 | **LIVE (~10 min old)** | +3.99 % (vs 2026-11-20) | 2.07 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 5.633 | 11-23 14:17 | **LIVE (~10 min old)** | +2.85 % (vs 2026-11-20) | 1.51 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 61,437.39, 24h 1.32%, z 0.51
- kraken: funding (raw, units unverified) 1.0233451803, OI 2300.9176, OI change vs prior snapshot 0.78%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 37225.15136, OI change vs prior snapshot -0.03%

**ETH**: price 1,736.60, 24h 1.38%, z 0.39
- kraken: funding (raw, units unverified) 0.000871938522917246, OI 34080.94, OI change vs prior snapshot -0.01%
- hyperliquid: funding (raw, units unverified) 0.0000056527, OI 617368.4539999998, OI change vs prior snapshot 0.13%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.0s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.0s)
