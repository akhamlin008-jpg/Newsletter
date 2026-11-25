# Data snapshot 2026-11-25 12:55 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.13)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.623 | 11-25 12:54 | **LIVE (~1 min old)** | -4.80 bp | -0.69 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.838 | 11-25 12:54 | **LIVE (~0 min old)** | -6.40 bp | -1.07 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.215 | 11-25 12:54 | **LIVE (~1 min old)** | -1.60 bp | -0.50 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.790 | 11-23 close | official value for 2026-11-23 (not live) | +2.00 bp (vs 2026-11-20) | 0.38 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.120 | 11-24 close | official value for 2026-11-24 (not live) | -1.00 bp (vs 2026-11-23) | -0.43 |  | fred:T10YIE |
| SOFR | 3.940 | 11-24 close | official value for 2026-11-24 (not live) | +2.00 bp (vs 2026-11-23) | 0.96 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.1s) |
| US dollar index (DXY) | 103.639 | 11-25 12:45 | **LIVE (~10 min old)** | -0.16 % (vs 2026-11-24) | -0.47 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.933 | 11-25 12:55 | **LIVE (~0 min old)** | -0.05 % (vs 2026-11-24) | -0.14 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.099 | 11-25 12:54 | **LIVE (~1 min old)** | +0.73 % (vs 2026-11-24) | 2.13 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 123.598 | 11-20 close | official value for 2026-11-20 (not live) | +0.06 % (vs 2026-11-19) | 0.23 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,130.000 | 11-25 12:45 | **LIVE (~10 min old)** | -1.21 % (vs 2026-11-24) | -0.66 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 25,674.250 | 11-25 12:45 | **LIVE (~10 min old)** | -2.29 % (vs 2026-11-24) | -0.84 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,683.400 | 11-25 12:45 | **LIVE (~10 min old)** | -0.22 % (vs 2026-11-24) | -0.13 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,131.460 | 11-25 12:55 | **LIVE (~0 min old)** | -0.97 % (vs 2026-11-24) | -0.52 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 25,686.881 | 11-25 12:55 | **LIVE (~0 min old)** | -2.01 % (vs 2026-11-24) | -0.73 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,677.955 | 11-25 12:40 | **LIVE (~15 min old)** | -0.26 % (vs 2026-11-24) | -0.15 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 30.430 | 11-25 12:40 | **LIVE (~15 min old)** | +4.07 pts (vs 2026-11-24) | 1.04 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.6s) |
| WTI crude | 83.460 | 11-25 12:45 | **LIVE (~10 min old)** | +1.72 % (vs 2026-11-24) | 0.58 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 90.130 | 11-25 12:45 | **LIVE (~10 min old)** | -1.39 % (vs 2026-11-24) | -0.44 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,529.600 | 11-25 12:45 | **LIVE (~10 min old)** | -0.91 % (vs 2026-11-24) | -0.43 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.401 | 11-25 12:45 | **LIVE (~10 min old)** | +0.72 % (vs 2026-11-24) | 0.32 |  | yahoo:HG=F (unofficial feed) |

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
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
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

**BTC**: price 59,525.58, 24h -0.84%, z -0.33
- kraken: funding (raw, units unverified) 0.20127765438081383, OI 2002.5791, OI change vs prior snapshot -2.31%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 35582.64072, OI change vs prior snapshot -1.70%

**ETH**: price 1,675.50, 24h -0.47%, z -0.14
- kraken: funding (raw, units unverified) -0.040897459112, OI 35733.013, OI change vs prior snapshot 16.54%
- hyperliquid: funding (raw, units unverified) 0.0000055397, OI 644825.1517999999, OI change vs prior snapshot 4.93%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.1s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.6s)
