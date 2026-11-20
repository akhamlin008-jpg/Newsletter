# Data snapshot 2026-11-20 11:20 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.27), crypto (max |z| 2.22)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.655 | 11-20 11:20 | **LIVE (~0 min old)** | -12.40 bp | -1.83 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.952 | 11-20 11:20 | **LIVE (~0 min old)** | -10.00 bp | -1.75 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.297 | 11-20 11:20 | **LIVE (~0 min old)** | +2.40 bp | 0.69 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.880 | 11-18 close | official value for 2026-11-18 (not live) | -1.00 bp (vs 2026-11-17) | -0.20 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.160 | 11-19 close | official value for 2026-11-19 (not live) | -3.00 bp (vs 2026-11-18) | -1.26 |  | fred:T10YIE |
| SOFR | 3.910 | 11-19 close | official value for 2026-11-19 (not live) | +1.00 bp (vs 2026-11-18) | 0.45 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.3s) |
| US dollar index (DXY) | 103.740 | 11-20 11:10 | **LIVE (~10 min old)** | -0.15 % (vs 2026-11-19) | -0.46 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.761 | 11-20 11:20 | **LIVE (~0 min old)** | -0.39 % (vs 2026-11-19) | -1.10 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.099 | 11-20 11:19 | **LIVE (~1 min old)** | +0.12 % (vs 2026-11-19) | 0.36 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 122.650 | 11-13 close | official value for 2026-11-13 (not live) | +0.09 % (vs 2026-11-12) | 0.34 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,096.750 | 11-20 11:10 | **LIVE (~10 min old)** | -1.40 % (vs 2026-11-19) | -1.07 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 25,856.750 | 11-20 11:10 | **LIVE (~10 min old)** | -2.80 % (vs 2026-11-19) | -1.45 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,638.300 | 11-20 11:10 | **LIVE (~10 min old)** | -0.94 % (vs 2026-11-19) | -0.63 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,081.140 | 11-20 11:20 | **LIVE (~0 min old)** | -1.32 % (vs 2026-11-19) | -1.01 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 25,779.570 | 11-20 11:20 | **LIVE (~0 min old)** | -2.78 % (vs 2026-11-19) | -1.43 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,626.353 | 11-20 11:05 | **LIVE (~15 min old)** | -1.08 % (vs 2026-11-19) | -0.73 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 30.900 | 11-20 11:05 | **LIVE (~15 min old)** | +2.46 pts (vs 2026-11-19) | 0.81 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s) |
| WTI crude | 82.020 | 11-20 11:10 | **LIVE (~10 min old)** | -1.43 % (vs 2026-11-19) | -0.49 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 88.760 | 11-20 11:10 | **LIVE (~10 min old)** | -3.50 % (vs 2026-11-19) | -1.08 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,551.100 | 11-20 11:10 | **LIVE (~10 min old)** | -3.65 % (vs 2026-11-19) | -2.27 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 5.498 | 11-20 11:10 | **LIVE (~10 min old)** | -2.26 % (vs 2026-11-19) | -1.24 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open
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

**BTC**: price 59,272.45, 24h -5.47%, z -2.22 **FLAG**
- kraken: funding (raw, units unverified) 0.22537380595293646, OI 2116.318, OI change vs prior snapshot -3.01%
- hyperliquid: funding (raw, units unverified) -0.0000068873, OI 39424.07666, OI change vs prior snapshot -0.74%

**ETH**: price 1,642.02, 24h -7.05%, z -2.21 **FLAG**
- kraken: funding (raw, units unverified) -0.014232805164, OI 29378.303, OI change vs prior snapshot -3.42%
- hyperliquid: funding (raw, units unverified) -0.0000255189, OI 624087.9114000003, OI change vs prior snapshot -0.40%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.3s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s)
