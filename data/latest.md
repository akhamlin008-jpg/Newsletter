# Data snapshot 2026-11-03 11:07 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.42)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.608 | 11-03 11:07 | **LIVE (~0 min old)** | +2.50 bp | 0.44 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.937 | 11-03 11:07 | **LIVE (~0 min old)** | +4.30 bp | 0.75 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.329 | 11-03 11:07 | **LIVE (~0 min old)** | +1.80 bp | 0.48 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.600 | 10-30 close | official value for 2026-10-30 (not live) | -3.00 bp (vs 2026-10-29) | -0.63 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.290 | 11-02 close | official value for 2026-11-02 (not live) | -5.00 bp (vs 2026-10-30) | -2.42 | **YES** | fred:T10YIE |
| SOFR | 3.950 | 11-02 close | official value for 2026-11-02 (not live) | +0.00 bp (vs 2026-10-30) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.2s) |
| US dollar index (DXY) | 101.802 | 11-03 10:57 | **LIVE (~11 min old)** | +0.05 % (vs 2026-11-02) | 0.19 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.427 | 11-03 11:07 | **LIVE (~1 min old)** | +0.48 % (vs 2026-11-02) | 1.20 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.120 | 11-03 11:07 | **LIVE (~1 min old)** | +0.37 % (vs 2026-11-02) | 1.41 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,611.250 | 11-03 10:57 | **LIVE (~11 min old)** | +0.49 % (vs 2026-11-02) | 0.67 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,396.750 | 11-03 10:57 | **LIVE (~11 min old)** | +0.96 % (vs 2026-11-02) | 0.67 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,843.300 | 11-03 10:57 | **LIVE (~11 min old)** | +0.91 % (vs 2026-11-02) | 0.99 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,586.390 | 11-03 11:07 | **LIVE (~1 min old)** | +0.60 % (vs 2026-11-02) | 0.81 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,291.963 | 11-03 11:07 | **LIVE (~1 min old)** | +1.08 % (vs 2026-11-02) | 0.74 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,834.735 | 11-03 10:52 | **LIVE (~16 min old)** | +1.03 % (vs 2026-11-02) | 1.12 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 20.460 | 11-03 10:51 | **LIVE (~16 min old)** | -0.69 pts | -0.54 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s) |
| WTI crude | 95.660 | 11-03 10:57 | **LIVE (~11 min old)** | -0.83 % (vs 2026-11-02) | -0.27 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 103.040 | 11-03 10:57 | **LIVE (~11 min old)** | -1.65 % (vs 2026-11-02) | -0.49 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,946.500 | 11-03 10:57 | **LIVE (~11 min old)** | -0.58 % (vs 2026-11-02) | -0.43 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.419 | 11-03 10:57 | **LIVE (~11 min old)** | -1.90 % (vs 2026-11-02) | -1.46 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 77,521.85, 24h 0.20%, z 0.12
- kraken: funding (raw, units unverified) 1.18570420214925, OI 2571.1086, OI change vs prior snapshot -0.95%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40703.04474, OI change vs prior snapshot 0.31%

**ETH**: price 2,293.84, 24h 1.23%, z 0.65
- kraken: funding (raw, units unverified) 0.03043863502354243, OI 32641.374, OI change vs prior snapshot -1.62%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1001745.9095999998, OI change vs prior snapshot 0.71%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s)
