# Data snapshot 2026-11-24 13:48 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.35)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.683 | 11-24 13:48 | **LIVE (~0 min old)** | +1.70 bp | 0.24 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.906 | 11-24 13:48 | **LIVE (~0 min old)** | -1.40 bp | -0.23 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.223 | 11-24 13:48 | **LIVE (~0 min old)** | -3.10 bp | -0.94 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.770 | 11-20 close | official value for 2026-11-20 (not live) | -11.00 bp (vs 2026-11-19) | -2.35 | **YES** | fred:DFII10 |
| 10-year breakeven inflation | 2.130 | 11-23 close | official value for 2026-11-23 (not live) | -2.00 bp (vs 2026-11-20) | -0.85 |  | fred:T10YIE |
| SOFR | 3.920 | 11-23 close | official value for 2026-11-23 (not live) | +0.00 bp (vs 2026-11-20) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (12.3s) |
| US dollar index (DXY) | 103.796 | 11-24 13:38 | **LIVE (~11 min old)** | -0.50 % (vs 2026-11-23) | -1.48 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.283 | 11-24 13:48 | **LIVE (~1 min old)** | +0.22 % (vs 2026-11-23) | 0.62 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.097 | 11-24 13:48 | **LIVE (~1 min old)** | +0.01 % (vs 2026-11-23) | 0.02 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 123.598 | 11-20 close | official value for 2026-11-20 (not live) | +0.06 % (vs 2026-11-19) | 0.23 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,216.000 | 11-24 13:38 | **LIVE (~11 min old)** | -0.53 % (vs 2026-11-23) | -0.28 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 26,310.000 | 11-24 13:38 | **LIVE (~11 min old)** | -1.86 % (vs 2026-11-23) | -0.67 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,697.400 | 11-24 13:38 | **LIVE (~11 min old)** | +0.87 % (vs 2026-11-23) | 0.50 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,200.240 | 11-24 13:48 | **LIVE (~1 min old)** | -0.51 % (vs 2026-11-23) | -0.27 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 26,244.045 | 11-24 13:48 | **LIVE (~1 min old)** | -1.88 % (vs 2026-11-23) | -0.67 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,693.546 | 11-24 13:33 | **LIVE (~16 min old)** | +0.89 % (vs 2026-11-23) | 0.51 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 26.240 | 11-24 13:33 | **LIVE (~16 min old)** | -0.38 pts (vs 2026-11-23) | -0.09 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.2s) |
| WTI crude | 81.870 | 11-24 13:38 | **LIVE (~11 min old)** | +2.12 % (vs 2026-11-23) | 0.71 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 88.390 | 11-24 13:38 | **LIVE (~11 min old)** | -1.10 % (vs 2026-11-23) | -0.35 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,559.200 | 11-24 13:38 | **LIVE (~11 min old)** | -2.53 % (vs 2026-11-23) | -1.21 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.457 | 11-24 13:38 | **LIVE (~11 min old)** | -3.03 % (vs 2026-11-23) | -1.56 |  | yahoo:HG=F (unofficial feed) |

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
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate); fell back after: cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.2s)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 60,023.97, 24h -2.10%, z -0.83
- kraken: funding (raw, units unverified) 0.41485050186064665, OI 2050.9411, OI change vs prior snapshot -8.73%
- hyperliquid: funding (raw, units unverified) -0.0000034536, OI 36290.18688, OI change vs prior snapshot -2.32%

**ETH**: price 1,681.08, 24h -3.30%, z -0.95
- kraken: funding (raw, units unverified) -0.015932772608333895, OI 30526.623, OI change vs prior snapshot -8.63%
- hyperliquid: funding (raw, units unverified) 0.000004871, OI 611403.9841999997, OI change vs prior snapshot 0.61%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (12.3s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.2s)
