# Data snapshot 2026-09-29 10:18 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.9)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.926 | 09-29 10:18 | **LIVE (~0 min old)** | +0.20 bp | 0.03 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.251 | 09-29 10:18 | **LIVE (~0 min old)** | +0.90 bp | 0.16 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.325 | 09-29 10:18 | **LIVE (~0 min old)** | +0.70 bp | 0.20 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.830 | 09-25 close | official value for 2026-09-25 (not live) | -2.00 bp (vs 2026-09-24) | -0.36 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 09-28 close | official value for 2026-09-28 (not live) | +0.00 bp (vs 2026-09-25) | 0.00 |  | fred:T10YIE |
| SOFR | 3.900 | 09-28 close | official value for 2026-09-28 (not live) | +0.00 bp (vs 2026-09-25) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.0s) |
| US dollar index (DXY) | 101.378 | 09-29 10:09 | **LIVE (~10 min old)** | +0.18 % (vs 2026-09-28) | 0.58 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.427 | 09-29 10:18 | **LIVE (~1 min old)** | -0.02 % (vs 2026-09-28) | -0.04 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.134 | 09-29 10:18 | **LIVE (~1 min old)** | -0.31 % (vs 2026-09-28) | -1.14 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,738.250 | 09-29 10:09 | **LIVE (~10 min old)** | -0.11 % (vs 2026-09-28) | -0.18 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,609.000 | 09-29 10:09 | **LIVE (~10 min old)** | +0.14 % (vs 2026-09-28) | 0.15 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,832.400 | 09-29 10:09 | **LIVE (~10 min old)** | -0.27 % (vs 2026-09-28) | -0.33 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,684.340 | 09-29 10:19 | **LIVE (~0 min old)** | +0.01 % (vs 2026-09-28) | 0.01 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,384.219 | 09-29 10:18 | **LIVE (~1 min old)** | +0.35 % (vs 2026-09-28) | 0.32 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,817.212 | 09-29 10:03 | **LIVE (~16 min old)** | -0.02 % (vs 2026-09-28) | -0.03 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.910 | 09-29 10:03 | **LIVE (~16 min old)** | -0.16 pts | -0.16 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.2s) |
| WTI crude | 91.220 | 09-29 10:09 | **LIVE (~10 min old)** | -1.49 % (vs 2026-09-28) | -0.53 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 96.630 | 09-29 10:09 | **LIVE (~10 min old)** | -8.22 % (vs 2026-09-28) | -2.90 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,200.300 | 09-29 10:09 | **LIVE (~10 min old)** | +0.77 % (vs 2026-09-28) | 0.53 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.625 | 09-29 10:08 | **LIVE (~11 min old)** | +0.90 % (vs 2026-09-28) | 0.60 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 83,942.83, 24h 1.14%, z 0.50
- kraken: funding (raw, units unverified) 0.706451560540875, OI 2327.8488, OI change vs prior snapshot -0.34%
- hyperliquid: funding (raw, units unverified) 0.0000099751, OI 34684.17378, OI change vs prior snapshot 1.49%

**ETH**: price 2,715.82, 24h 1.84%, z 0.70
- kraken: funding (raw, units unverified) 0.016293114031582425, OI 26241.961, OI change vs prior snapshot 0.05%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1205229.8048000012, OI change vs prior snapshot 0.01%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.2s)
