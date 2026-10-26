# Data snapshot 2026-10-26 10:07 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.62), commodities (max |z| 2.1)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.694 | 10-26 10:07 | **LIVE (~1 min old)** | +1.20 bp | 0.19 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.970 | 10-26 10:07 | **LIVE (~0 min old)** | -1.80 bp | -0.29 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.276 | 10-26 10:07 | **LIVE (~1 min old)** | -3.00 bp | -0.93 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.640 | 10-22 close | official value for 2026-10-22 (not live) | -12.00 bp (vs 2026-10-21) | -2.62 | **YES** | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 10-23 close | official value for 2026-10-23 (not live) | +2.00 bp (vs 2026-10-22) | 0.96 |  | fred:T10YIE |
| SOFR | 3.920 | 10-23 close | official value for 2026-10-23 (not live) | +2.00 bp (vs 2026-10-22) | 0.67 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.4s) |
| US dollar index (DXY) | 102.025 | 10-26 09:57 | **LIVE (~11 min old)** | +0.21 % (vs 2026-10-23) | 0.73 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.405 | 10-26 10:08 | **LIVE (~0 min old)** | +0.58 % (vs 2026-10-23) | 1.29 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.118 | 10-26 10:07 | **LIVE (~1 min old)** | -0.35 % (vs 2026-10-23) | -1.39 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.405 | 10-16 close | official value for 2026-10-16 (not live) | -0.14 % (vs 2026-10-15) | -0.48 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,691.250 | 10-26 09:58 | **LIVE (~10 min old)** | +0.41 % (vs 2026-10-23) | 0.64 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,216.000 | 10-26 09:58 | **LIVE (~10 min old)** | +0.34 % (vs 2026-10-23) | 0.28 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,796.200 | 10-26 09:58 | **LIVE (~10 min old)** | +0.42 % (vs 2026-10-23) | 0.46 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,655.100 | 10-26 10:08 | **LIVE (~0 min old)** | +0.41 % (vs 2026-10-23) | 0.63 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,036.805 | 10-26 10:08 | **LIVE (~0 min old)** | +0.27 % (vs 2026-10-23) | 0.22 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,786.136 | 10-26 09:53 | **LIVE (~15 min old)** | +0.37 % (vs 2026-10-23) | 0.41 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 18.540 | 10-26 09:52 | **LIVE (~16 min old)** | -0.91 pts | -0.73 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.3s) |
| WTI crude | 101.880 | 10-26 09:58 | **LIVE (~10 min old)** | -1.35 % (vs 2026-10-23) | -0.50 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 110.950 | 10-26 09:58 | **LIVE (~10 min old)** | -4.94 % (vs 2026-10-23) | -2.10 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,003.700 | 10-26 09:58 | **LIVE (~10 min old)** | -0.10 % (vs 2026-10-23) | -0.09 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.518 | 10-26 09:58 | **LIVE (~10 min old)** | +0.65 % (vs 2026-10-23) | 0.49 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 79,527.10, 24h -1.27%, z -0.80
- kraken: funding (raw, units unverified) 0.768708422235, OI 2760.4804, OI change vs prior snapshot 6.06%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42212.33858, OI change vs prior snapshot -6.46%

**ETH**: price 2,298.99, 24h -1.76%, z -0.89
- kraken: funding (raw, units unverified) 0.011580535580875, OI 32030.86, OI change vs prior snapshot 10.66%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1112396.7825999996, OI change vs prior snapshot 2.00%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.4s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.3s)
