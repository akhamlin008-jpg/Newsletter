# Data snapshot 2026-11-02 13:13 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 5.29)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.575 | 11-02 13:13 | **LIVE (~0 min old)** | -0.60 bp | -0.11 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.875 | 11-02 13:13 | **LIVE (~0 min old)** | -5.40 bp | -0.92 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.300 | 11-02 13:13 | **LIVE (~0 min old)** | -4.80 bp | -1.35 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.630 | 10-29 close | official value for 2026-10-29 (not live) | -4.00 bp (vs 2026-10-28) | -0.83 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 10-30 close | official value for 2026-10-30 (not live) | -1.00 bp (vs 2026-10-29) | -0.47 |  | fred:T10YIE |
| SOFR | 3.950 | 10-30 close | official value for 2026-10-30 (not live) | +1.00 bp (vs 2026-10-29) | 0.38 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (12.0s) |
| US dollar index (DXY) | 101.671 | 11-02 13:03 | **LIVE (~10 min old)** | -0.21 % (vs 2026-10-30) | -0.76 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.804 | 11-02 13:13 | **LIVE (~0 min old)** | +0.00 % (vs 2026-10-30) | 0.00 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.121 | 11-02 13:13 | **LIVE (~0 min old)** | +0.22 % (vs 2026-10-30) | 0.82 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,636.250 | 11-02 13:03 | **LIVE (~10 min old)** | +0.29 % (vs 2026-10-30) | 0.39 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,552.250 | 11-02 13:03 | **LIVE (~10 min old)** | +0.06 % (vs 2026-10-30) | 0.04 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,837.000 | 11-02 13:03 | **LIVE (~10 min old)** | +0.56 % (vs 2026-10-30) | 0.59 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,611.970 | 11-02 13:13 | **LIVE (~0 min old)** | +0.42 % (vs 2026-10-30) | 0.56 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,427.922 | 11-02 13:13 | **LIVE (~0 min old)** | +0.15 % (vs 2026-10-30) | 0.10 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,827.020 | 11-02 12:58 | **LIVE (~15 min old)** | +0.54 % (vs 2026-10-30) | 0.57 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 19.800 | 11-02 12:57 | **LIVE (~16 min old)** | +0.38 pts | 0.31 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.0s) |
| WTI crude | 95.910 | 11-02 13:03 | **LIVE (~10 min old)** | -7.89 % (vs 2026-10-30) | -3.12 | **YES** | yahoo:CL=F (unofficial feed) |
| Brent crude | 104.200 | 11-02 13:03 | **LIVE (~10 min old)** | -11.42 % (vs 2026-10-30) | -5.29 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 3,972.600 | 11-02 13:03 | **LIVE (~10 min old)** | +1.89 % (vs 2026-10-30) | 1.42 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.572 | 11-02 13:03 | **LIVE (~10 min old)** | +1.76 % (vs 2026-10-30) | 1.35 |  | yahoo:HG=F (unofficial feed) |

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
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 77,138.42, 24h -0.80%, z -0.49
- kraken: funding (raw, units unverified) 0.42940685658035904, OI 2658.6917, OI change vs prior snapshot 0.52%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40989.9175599999, OI change vs prior snapshot -0.45%

**ETH**: price 2,260.40, 24h -0.01%, z -0.00
- kraken: funding (raw, units unverified) 0.010364859599, OI 33116.842, OI change vs prior snapshot -0.38%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 984517.064, OI change vs prior snapshot -1.08%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (12.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.0s)
