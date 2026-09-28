# Data snapshot 2026-09-28 11:53 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 3.25)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.945 | 09-28 11:52 | **LIVE (~1 min old)** | +8.10 bp | 1.30 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.266 | 09-28 11:53 | **LIVE (~0 min old)** | +8.50 bp | 1.46 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.321 | 09-28 11:52 | **LIVE (~1 min old)** | +0.40 bp | 0.12 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.850 | 09-24 close | official value for 2026-09-24 (not live) | +9.00 bp (vs 2026-09-23) | 1.71 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 09-25 close | official value for 2026-09-25 (not live) | +1.00 bp (vs 2026-09-24) | 0.47 |  | fred:T10YIE |
| SOFR | 3.900 | 09-25 close | official value for 2026-09-25 (not live) | +2.00 bp (vs 2026-09-24) | 0.41 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.9s) |
| US dollar index (DXY) | 101.209 | 09-28 11:43 | **LIVE (~10 min old)** | +0.24 % (vs 2026-09-25) | 0.78 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.421 | 09-28 11:53 | **LIVE (~0 min old)** | -0.88 % (vs 2026-09-25) | -1.49 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.137 | 09-28 11:52 | **LIVE (~1 min old)** | -0.05 % (vs 2026-09-25) | -0.19 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 119.513 | 09-18 close | official value for 2026-09-18 (not live) | +0.14 % (vs 2026-09-17) | 0.61 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,738.250 | 09-28 11:43 | **LIVE (~10 min old)** | -0.84 % (vs 2026-09-25) | -1.38 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,469.500 | 09-28 11:43 | **LIVE (~10 min old)** | -1.36 % (vs 2026-09-25) | -1.45 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,829.400 | 09-28 11:43 | **LIVE (~10 min old)** | -1.05 % (vs 2026-09-25) | -1.24 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,677.780 | 09-28 11:53 | **LIVE (~0 min old)** | -0.85 % (vs 2026-09-25) | -1.24 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,204.012 | 09-28 11:53 | **LIVE (~0 min old)** | -1.32 % (vs 2026-09-25) | -1.19 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,810.216 | 09-28 11:38 | **LIVE (~15 min old)** | -0.96 % (vs 2026-09-25) | -1.18 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 16.210 | 09-28 11:37 | **LIVE (~16 min old)** | +1.34 pts | 1.33 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.0s) |
| WTI crude | 95.480 | 09-28 11:43 | **LIVE (~10 min old)** | +3.32 % (vs 2026-09-25) | 1.14 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 100.080 | 09-28 11:43 | **LIVE (~10 min old)** | -4.06 % (vs 2026-09-25) | -1.40 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,153.300 | 09-28 11:43 | **LIVE (~10 min old)** | -3.89 % (vs 2026-09-25) | -3.25 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.623 | 09-28 11:43 | **LIVE (~10 min old)** | -1.08 % (vs 2026-09-25) | -0.75 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 83,218.15, 24h -1.46%, z -0.63
- kraken: funding (raw, units unverified) 0.6843644924087223, OI 2235.513, OI change vs prior snapshot -0.27%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 36713.52556, OI change vs prior snapshot 0.08%

**ETH**: price 2,675.03, 24h -0.54%, z -0.20
- kraken: funding (raw, units unverified) 0.009728108023917555, OI 26414.995, OI change vs prior snapshot -0.30%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1103996.1459999999, OI change vs prior snapshot 0.04%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.9s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.0s)
