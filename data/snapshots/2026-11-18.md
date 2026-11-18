# Data snapshot 2026-11-18 11:41 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 4.6)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.785 | 11-18 11:41 | **LIVE (~0 min old)** | -0.40 bp | -0.06 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.072 | 11-18 11:41 | **LIVE (~0 min old)** | -3.10 bp | -0.52 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.287 | 11-18 11:41 | **LIVE (~0 min old)** | -2.70 bp | -0.75 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.920 | 11-16 close | official value for 2026-11-16 (not live) | +1.00 bp (vs 2026-11-13) | 0.19 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.210 | 11-17 close | official value for 2026-11-17 (not live) | +1.00 bp (vs 2026-11-16) | 0.41 |  | fred:T10YIE |
| SOFR | 3.920 | 11-17 close | official value for 2026-11-17 (not live) | -1.00 bp (vs 2026-11-16) | -0.44 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.0s) |
| US dollar index (DXY) | 103.876 | 11-18 11:31 | **LIVE (~11 min old)** | +0.37 % (vs 2026-11-17) | 1.08 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.304 | 11-18 11:42 | **LIVE (~0 min old)** | -0.14 % (vs 2026-11-17) | -0.37 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.096 | 11-18 11:41 | **LIVE (~1 min old)** | -0.31 % (vs 2026-11-17) | -0.87 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 122.650 | 11-13 close | official value for 2026-11-13 (not live) | +0.09 % (vs 2026-11-12) | 0.34 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,323.000 | 11-18 11:32 | **LIVE (~10 min old)** | -0.49 % (vs 2026-11-17) | -0.38 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,013.000 | 11-18 11:32 | **LIVE (~10 min old)** | -0.23 % (vs 2026-11-17) | -0.12 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,719.800 | 11-18 11:32 | **LIVE (~10 min old)** | +0.32 % (vs 2026-11-17) | 0.21 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,299.750 | 11-18 11:42 | **LIVE (~0 min old)** | -0.56 % (vs 2026-11-17) | -0.43 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 26,907.863 | 11-18 11:42 | **LIVE (~0 min old)** | -0.35 % (vs 2026-11-17) | -0.18 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,710.779 | 11-18 11:26 | **LIVE (~16 min old)** | +0.33 % (vs 2026-11-17) | 0.22 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 25.140 | 11-18 11:26 | **LIVE (~16 min old)** | -0.32 pts | -0.10 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.2s) |
| WTI crude | 82.460 | 11-18 11:32 | **LIVE (~10 min old)** | -4.13 % (vs 2026-11-17) | -1.37 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 88.480 | 11-18 11:32 | **LIVE (~10 min old)** | -5.00 % (vs 2026-11-17) | -1.45 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,741.000 | 11-18 11:32 | **LIVE (~10 min old)** | -3.19 % (vs 2026-11-17) | -2.18 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 5.592 | 11-18 11:32 | **LIVE (~10 min old)** | -6.43 % (vs 2026-11-17) | -4.60 | **YES** | yahoo:HG=F (unofficial feed) |

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
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 62,299.52, 24h -2.15%, z -0.87
- kraken: funding (raw, units unverified) 0.874856222543479, OI 2291.7763, OI change vs prior snapshot -0.53%
- hyperliquid: funding (raw, units unverified) 0.0000101416, OI 40611.1157600001, OI change vs prior snapshot 0.20%

**ETH**: price 1,736.92, 24h -2.21%, z -0.66
- kraken: funding (raw, units unverified) 0.00254138672175, OI 29916.023, OI change vs prior snapshot 0.40%
- hyperliquid: funding (raw, units unverified) 0.0000012041, OI 617814.4827999995, OI change vs prior snapshot 0.40%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.2s)
