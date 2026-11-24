# Data snapshot 2026-11-24 14:03 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.35)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.683 | 11-24 14:01 | **LIVE (~2 min old)** | +1.70 bp | 0.24 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.904 | 11-24 14:03 | **LIVE (~0 min old)** | -1.60 bp | -0.26 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.221 | 11-24 14:01 | **LIVE (~2 min old)** | -3.30 bp | -1.00 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.770 | 11-20 close | official value for 2026-11-20 (not live) | -11.00 bp (vs 2026-11-19) | -2.35 | **YES** | fred:DFII10 |
| 10-year breakeven inflation | 2.130 | 11-23 close | official value for 2026-11-23 (not live) | -2.00 bp (vs 2026-11-20) | -0.85 |  | fred:T10YIE |
| SOFR | 3.920 | 11-23 close | official value for 2026-11-23 (not live) | +0.00 bp (vs 2026-11-20) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.7s) |
| US dollar index (DXY) | 103.807 | 11-24 13:53 | **LIVE (~11 min old)** | -0.49 % (vs 2026-11-23) | -1.45 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.267 | 11-24 14:03 | **LIVE (~1 min old)** | +0.21 % (vs 2026-11-23) | 0.59 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.097 | 11-24 14:02 | **LIVE (~2 min old)** | -0.02 % (vs 2026-11-23) | -0.05 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 123.598 | 11-20 close | official value for 2026-11-20 (not live) | +0.06 % (vs 2026-11-19) | 0.23 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,210.000 | 11-24 13:53 | **LIVE (~11 min old)** | -0.61 % (vs 2026-11-23) | -0.33 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 26,283.500 | 11-24 13:53 | **LIVE (~11 min old)** | -1.96 % (vs 2026-11-23) | -0.70 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,694.300 | 11-24 13:53 | **LIVE (~11 min old)** | +0.76 % (vs 2026-11-23) | 0.43 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,190.570 | 11-24 14:03 | **LIVE (~1 min old)** | -0.64 % (vs 2026-11-23) | -0.34 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 26,192.375 | 11-24 14:03 | **LIVE (~1 min old)** | -2.07 % (vs 2026-11-23) | -0.74 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,692.098 | 11-24 13:48 | **LIVE (~16 min old)** | +0.84 % (vs 2026-11-23) | 0.48 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 26.450 | 11-24 13:48 | **LIVE (~16 min old)** | -0.17 pts (vs 2026-11-23) | -0.04 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s) |
| WTI crude | 81.840 | 11-24 13:53 | **LIVE (~11 min old)** | +2.08 % (vs 2026-11-23) | 0.70 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 88.420 | 11-24 13:53 | **LIVE (~11 min old)** | -1.06 % (vs 2026-11-23) | -0.33 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,557.300 | 11-24 13:53 | **LIVE (~11 min old)** | -2.58 % (vs 2026-11-23) | -1.23 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.463 | 11-24 13:53 | **LIVE (~11 min old)** | -2.92 % (vs 2026-11-23) | -1.50 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 59,792.33, 24h -2.29%, z -0.90
- kraken: funding (raw, units unverified) 0.4645929873360616, OI 2054.608, OI change vs prior snapshot 0.18%
- hyperliquid: funding (raw, units unverified) -0.0000146699, OI 36351.65692, OI change vs prior snapshot 0.17%

**ETH**: price 1,675.84, 24h -3.12%, z -0.90
- kraken: funding (raw, units unverified) -0.005648808770332774, OI 30577.991, OI change vs prior snapshot 0.17%
- hyperliquid: funding (raw, units unverified) 0.0000047925, OI 612566.8341999995, OI change vs prior snapshot 0.19%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.7s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s)
