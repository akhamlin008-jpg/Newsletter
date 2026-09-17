# Data snapshot 2026-09-17 05:07 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** equity (max |z| 2.71), rates (max |z| 2.34)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.709 | 09-17 05:05 | **LIVE (~2 min old)** | -1.80 bp | -0.34 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.986 | 09-17 05:07 | **LIVE (~0 min old)** | -1.80 bp | -0.41 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.277 | 09-17 05:05 | **LIVE (~2 min old)** | +0.00 bp | 0.00 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.620 | 09-15 close | official value for 2026-09-15 (not live) | +2.00 bp (vs 2026-09-14) | 0.53 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 09-16 close | official value for 2026-09-16 (not live) | -5.00 bp (vs 2026-09-15) | -2.34 | **YES** | fred:T10YIE |
| SOFR | 3.640 | 09-15 close | official value for 2026-09-15 (not live) | +2.00 bp (vs 2026-09-14) | 0.89 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.3s) |
| US dollar index (DXY) | 100.199 | 09-17 04:58 | **LIVE (~10 min old)** | -0.11 % (vs 2026-09-16) | -0.34 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 155.751 | 09-17 05:08 | **LIVE (~0 min old)** | +0.31 % (vs 2026-09-16) | 0.46 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.148 | 09-17 05:07 | **LIVE (~1 min old)** | -0.50 % (vs 2026-09-16) | -1.98 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 118.213 | 09-11 close | official value for 2026-09-11 (not live) | +0.11 % (vs 2026-09-10) | 0.54 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,684.250 | 09-17 04:58 | **LIVE (~10 min old)** | +1.69 % (vs 2026-09-16) | 2.71 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,559.000 | 09-17 04:58 | **LIVE (~10 min old)** | +2.06 % (vs 2026-09-16) | 2.10 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,905.500 | 09-17 04:57 | **LIVE (~11 min old)** | +1.53 % (vs 2026-09-16) | 1.86 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,551.810 | 09-16 16:31 | not trading now; last trade 09-16 16:31 ET | -0.45 % (vs 2026-09-15) | -0.69 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,945.060 | 09-16 17:16 | not trading now; last trade 09-16 17:16 ET | +0.03 % (vs 2026-09-15) | 0.02 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,858.811 | 09-16 16:30 | not trading now; last trade 09-16 16:30 ET | -0.40 % (vs 2026-09-15) | -0.47 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 16.130 | 09-17 04:53 | **LIVE (~15 min old)** | -1.58 pts (vs 2026-09-16) | -1.56 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.4s) |
| WTI crude | 101.280 | 09-17 04:58 | **LIVE (~10 min old)** | -1.12 % (vs 2026-09-16) | -0.36 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 104.220 | 09-17 04:57 | **LIVE (~11 min old)** | -1.52 % (vs 2026-09-16) | -0.50 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,351.800 | 09-17 04:58 | **LIVE (~10 min old)** | -0.81 % (vs 2026-09-16) | -0.58 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.559 | 09-17 04:57 | **LIVE (~11 min old)** | +1.97 % (vs 2026-09-16) | 1.24 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); quarterly roll window: roll date 2026-09-10, expiry 2026-09-18; a jump may be the contract switch; roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); quarterly roll window: roll date 2026-09-10, expiry 2026-09-18; a jump may be the contract switch; roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); quarterly roll window: roll date 2026-09-10, expiry 2026-09-18; a jump may be the contract switch; roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: POSSIBLE ROLL on latest change; flag suppressed; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 76,598.42, 24h 0.89%, z 0.43
- kraken: funding (raw, units unverified) 1.4644414864434745, OI 2213.7813, OI change vs prior snapshot 0.54%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 37631.4476199999, OI change vs prior snapshot -2.13%

**ETH**: price 2,444.37, 24h 1.69%, z 0.58
- kraken: funding (raw, units unverified) 0.026860481765249185, OI 34400.936, OI change vs prior snapshot -2.61%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 968565.1187999989, OI change vs prior snapshot -1.65%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.3s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.4s)
