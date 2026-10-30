# Data snapshot 2026-10-30 10:29 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** crypto (max |z| 3.09), commodities (max |z| 2.64)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.606 | 10-30 10:29 | **LIVE (~0 min old)** | -5.00 bp | -0.88 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.933 | 10-30 10:29 | **LIVE (~0 min old)** | -5.60 bp | -0.97 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.327 | 10-30 10:29 | **LIVE (~0 min old)** | -0.60 bp | -0.16 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.670 | 10-28 close | official value for 2026-10-28 (not live) | +3.00 bp (vs 2026-10-27) | 0.61 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-29 close | official value for 2026-10-29 (not live) | -3.00 bp (vs 2026-10-28) | -1.46 |  | fred:T10YIE |
| SOFR | 3.940 | 10-29 close | official value for 2026-10-29 (not live) | +0.00 bp (vs 2026-10-28) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.6s) |
| US dollar index (DXY) | 102.050 | 10-30 10:19 | **LIVE (~11 min old)** | +0.01 % (vs 2026-10-29) | 0.04 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.262 | 10-30 10:29 | **LIVE (~1 min old)** | -0.36 % (vs 2026-10-29) | -0.86 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.115 | 10-30 10:29 | **LIVE (~1 min old)** | -0.07 % (vs 2026-10-29) | -0.25 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,639.000 | 10-30 10:19 | **LIVE (~11 min old)** | -1.49 % (vs 2026-10-29) | -2.43 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,689.000 | 10-30 10:19 | **LIVE (~11 min old)** | -2.95 % (vs 2026-10-29) | -2.50 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,828.300 | 10-30 10:19 | **LIVE (~11 min old)** | -1.36 % (vs 2026-10-29) | -1.54 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,604.840 | 10-30 10:29 | **LIVE (~1 min old)** | -1.50 % (vs 2026-10-29) | -2.39 | **YES** | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,530.871 | 10-30 10:29 | **LIVE (~1 min old)** | -2.96 % (vs 2026-10-29) | -2.42 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,819.248 | 10-30 10:14 | **LIVE (~16 min old)** | -1.40 % (vs 2026-10-29) | -1.58 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 19.330 | 10-30 10:14 | **LIVE (~15 min old)** | +2.13 pts | 1.84 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s) |
| WTI crude | 104.590 | 10-30 10:19 | **LIVE (~11 min old)** | +2.54 % (vs 2026-10-29) | 0.99 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 113.700 | 10-30 10:19 | **LIVE (~11 min old)** | -1.03 % (vs 2026-10-29) | -0.48 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,915.100 | 10-30 10:19 | **LIVE (~11 min old)** | -2.88 % (vs 2026-10-29) | -2.64 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.499 | 10-30 10:19 | **LIVE (~11 min old)** | -1.25 % (vs 2026-10-29) | -0.99 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 76,679.31, 24h -5.44%, z -3.09 **FLAG**
- kraken: funding (raw, units unverified) 0.995827778828266, OI 2746.1552, OI change vs prior snapshot 1.80%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40671.5397399999, OI change vs prior snapshot 1.24%

**ETH**: price 2,217.68, 24h -5.31%, z -2.52 **FLAG**
- kraken: funding (raw, units unverified) 0.01023891929, OI 30823.91, OI change vs prior snapshot 2.33%
- hyperliquid: funding (raw, units unverified) 0.0000038259, OI 1033975.9982000007, OI change vs prior snapshot 0.05%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.6s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s)
