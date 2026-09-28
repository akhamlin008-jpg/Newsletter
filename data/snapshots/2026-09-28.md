# Data snapshot 2026-09-28 11:02 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 3.34)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.947 | 09-28 11:02 | **LIVE (~0 min old)** | +8.30 bp | 1.33 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.268 | 09-28 11:02 | **LIVE (~0 min old)** | +8.70 bp | 1.50 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.321 | 09-28 11:02 | **LIVE (~0 min old)** | +0.40 bp | 0.12 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.850 | 09-24 close | official value for 2026-09-24 (not live) | +9.00 bp (vs 2026-09-23) | 1.71 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 09-25 close | official value for 2026-09-25 (not live) | +1.00 bp (vs 2026-09-24) | 0.47 |  | fred:T10YIE |
| SOFR | 3.900 | 09-25 close | official value for 2026-09-25 (not live) | +2.00 bp (vs 2026-09-24) | 0.41 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.3s) |
| US dollar index (DXY) | 101.269 | 09-28 10:52 | **LIVE (~11 min old)** | +0.30 % (vs 2026-09-25) | 0.97 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.544 | 09-28 11:02 | **LIVE (~1 min old)** | -0.80 % (vs 2026-09-25) | -1.35 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.137 | 09-28 11:02 | **LIVE (~1 min old)** | -0.07 % (vs 2026-09-25) | -0.27 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 119.513 | 09-18 close | official value for 2026-09-18 (not live) | +0.14 % (vs 2026-09-17) | 0.61 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,732.000 | 09-28 10:52 | **LIVE (~11 min old)** | -0.92 % (vs 2026-09-25) | -1.51 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,383.750 | 09-28 10:52 | **LIVE (~11 min old)** | -1.64 % (vs 2026-09-25) | -1.75 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,832.900 | 09-28 10:52 | **LIVE (~11 min old)** | -0.92 % (vs 2026-09-25) | -1.10 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,671.980 | 09-28 11:02 | **LIVE (~1 min old)** | -0.92 % (vs 2026-09-25) | -1.35 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,149.883 | 09-28 11:02 | **LIVE (~1 min old)** | -1.50 % (vs 2026-09-25) | -1.35 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,814.912 | 09-28 10:47 | **LIVE (~16 min old)** | -0.80 % (vs 2026-09-25) | -0.98 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 16.620 | 09-28 10:47 | **LIVE (~16 min old)** | +1.75 pts | 1.74 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.5s) |
| WTI crude | 95.030 | 09-28 10:53 | **LIVE (~10 min old)** | +2.84 % (vs 2026-09-25) | 0.97 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 99.710 | 09-28 10:53 | **LIVE (~10 min old)** | -4.42 % (vs 2026-09-25) | -1.52 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,148.400 | 09-28 10:53 | **LIVE (~10 min old)** | -4.00 % (vs 2026-09-25) | -3.34 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.606 | 09-28 10:53 | **LIVE (~10 min old)** | -1.34 % (vs 2026-09-25) | -0.92 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-21)
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-21)
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-18, 2026-09-21)
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 82,974.17, 24h -1.75%, z -0.75
- kraken: funding (raw, units unverified) 0.6843644924087223, OI 2232.6898, OI change vs prior snapshot 2.31%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 36776.69606, OI change vs prior snapshot -0.58%

**ETH**: price 2,669.18, 24h -0.75%, z -0.28
- kraken: funding (raw, units unverified) 0.009728108023917555, OI 26440.781, OI change vs prior snapshot 0.54%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1100617.638400001, OI change vs prior snapshot -0.45%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.3s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.5s)
