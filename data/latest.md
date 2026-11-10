# Data snapshot 2026-11-10 10:31 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 3.16)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.731 | 11-10 10:30 | **LIVE (~1 min old)** | +18.40 bp | 3.16 | **YES** | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.988 | 11-10 10:31 | **LIVE (~0 min old)** | +12.60 bp | 2.33 | **YES** | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.257 | 11-10 10:30 | **LIVE (~1 min old)** | -5.80 bp | -1.57 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.630 | 11-06 close | official value for 2026-11-06 (not live) | +3.00 bp (vs 2026-11-05) | 0.69 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.220 | 11-09 close | official value for 2026-11-09 (not live) | -1.00 bp (vs 2026-11-06) | -0.43 |  | fred:T10YIE |
| SOFR | 3.880 | 11-09 close | official value for 2026-11-09 (not live) | -1.00 bp (vs 2026-11-06) | -0.40 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.7s) |
| US dollar index (DXY) | 102.081 | 11-10 10:21 | **LIVE (~11 min old)** | +0.42 % (vs 2026-11-09) | 1.26 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.584 | 11-10 10:31 | **LIVE (~1 min old)** | +0.18 % (vs 2026-11-09) | 0.47 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.118 | 11-10 10:31 | **LIVE (~1 min old)** | +0.28 % (vs 2026-11-09) | 0.92 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,550.750 | 11-10 10:21 | **LIVE (~11 min old)** | -0.31 % (vs 2026-11-09) | -0.23 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,995.750 | 11-10 10:21 | **LIVE (~11 min old)** | -0.07 % (vs 2026-11-09) | -0.03 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,827.800 | 11-10 10:21 | **LIVE (~11 min old)** | -0.73 % (vs 2026-11-09) | -0.47 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,518.420 | 11-10 10:31 | **LIVE (~1 min old)** | -0.42 % (vs 2026-11-09) | -0.30 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,825.748 | 11-10 10:31 | **LIVE (~1 min old)** | -0.29 % (vs 2026-11-09) | -0.14 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,821.188 | 11-10 10:16 | **LIVE (~16 min old)** | -0.69 % (vs 2026-11-09) | -0.44 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 20.170 | 11-10 10:16 | **LIVE (~15 min old)** | +0.25 pts | 0.07 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.8s) |
| WTI crude | 85.460 | 11-10 10:21 | **LIVE (~11 min old)** | -1.60 % (vs 2026-11-09) | -0.47 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 90.680 | 11-10 10:21 | **LIVE (~11 min old)** | -2.04 % (vs 2026-11-09) | -0.52 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,059.400 | 11-10 10:21 | **LIVE (~11 min old)** | -1.34 % (vs 2026-11-09) | -0.92 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.286 | 11-10 10:21 | **LIVE (~11 min old)** | -0.67 % (vs 2026-11-09) | -0.47 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 73,964.92, 24h -1.94%, z -0.96
- kraken: funding (raw, units unverified) 0.694230678087358, OI 2515.6547, OI change vs prior snapshot -1.97%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42332.95244, OI change vs prior snapshot 0.39%

**ETH**: price 2,058.03, 24h -4.05%, z -1.39
- kraken: funding (raw, units unverified) -0.01581160784875, OI 29964.874, OI change vs prior snapshot 1.14%
- hyperliquid: funding (raw, units unverified) 0.0000071587, OI 796847.0660000005, OI change vs prior snapshot -1.11%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.7s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.8s)
