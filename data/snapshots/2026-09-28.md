# Data snapshot 2026-09-28 12:43 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.94)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.924 | 09-28 12:43 | **LIVE (~0 min old)** | +6.00 bp | 0.96 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.247 | 09-28 12:43 | **LIVE (~0 min old)** | +6.60 bp | 1.14 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.323 | 09-28 12:43 | **LIVE (~0 min old)** | +0.60 bp | 0.17 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.850 | 09-24 close | official value for 2026-09-24 (not live) | +9.00 bp (vs 2026-09-23) | 1.71 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 09-25 close | official value for 2026-09-25 (not live) | +1.00 bp (vs 2026-09-24) | 0.47 |  | fred:T10YIE |
| SOFR | 3.900 | 09-25 close | official value for 2026-09-25 (not live) | +2.00 bp (vs 2026-09-24) | 0.41 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.0s) |
| US dollar index (DXY) | 101.115 | 09-28 12:33 | **LIVE (~10 min old)** | +0.14 % (vs 2026-09-25) | 0.47 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.239 | 09-28 12:43 | **LIVE (~0 min old)** | -0.99 % (vs 2026-09-25) | -1.68 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.138 | 09-28 12:42 | **LIVE (~1 min old)** | +0.04 % (vs 2026-09-25) | 0.14 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 119.513 | 09-18 close | official value for 2026-09-18 (not live) | +0.14 % (vs 2026-09-17) | 0.61 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,768.750 | 09-28 12:33 | **LIVE (~10 min old)** | -0.45 % (vs 2026-09-25) | -0.74 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,648.250 | 09-28 12:33 | **LIVE (~10 min old)** | -0.78 % (vs 2026-09-25) | -0.83 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,845.400 | 09-28 12:33 | **LIVE (~10 min old)** | -0.49 % (vs 2026-09-25) | -0.58 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,698.470 | 09-28 12:43 | **LIVE (~0 min old)** | -0.58 % (vs 2026-09-25) | -0.85 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,319.668 | 09-28 12:43 | **LIVE (~0 min old)** | -0.94 % (vs 2026-09-25) | -0.85 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,829.713 | 09-28 12:28 | **LIVE (~15 min old)** | -0.28 % (vs 2026-09-25) | -0.34 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.680 | 09-28 12:27 | **LIVE (~16 min old)** | +0.81 pts | 0.80 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.3s) |
| WTI crude | 92.730 | 09-28 12:33 | **LIVE (~10 min old)** | +0.35 % (vs 2026-09-25) | 0.12 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 97.760 | 09-28 12:33 | **LIVE (~10 min old)** | -6.29 % (vs 2026-09-25) | -2.16 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,169.400 | 09-28 12:33 | **LIVE (~10 min old)** | -3.51 % (vs 2026-09-25) | -2.94 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.638 | 09-28 12:33 | **LIVE (~10 min old)** | -0.87 % (vs 2026-09-25) | -0.60 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 83,697.98, 24h -0.84%, z -0.36
- kraken: funding (raw, units unverified) 1.1176728520841805, OI 2219.3559, OI change vs prior snapshot -0.72%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 37346.18704, OI change vs prior snapshot 1.72%

**ETH**: price 2,681.69, 24h -0.14%, z -0.05
- kraken: funding (raw, units unverified) 0.02523161249383244, OI 26526.925, OI change vs prior snapshot 0.42%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1107804.7363999989, OI change vs prior snapshot 0.34%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.3s)
