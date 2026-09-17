# Data snapshot 2026-09-17 10:41 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** equity (max |z| 2.99), rates (max |z| 2.34)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.683 | 09-17 10:41 | **LIVE (~0 min old)** | -4.40 bp | -0.83 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.951 | 09-17 10:41 | **LIVE (~0 min old)** | -5.30 bp | -1.21 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.268 | 09-17 10:41 | **LIVE (~0 min old)** | -0.90 bp | -0.29 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.620 | 09-15 close | official value for 2026-09-15 (not live) | +2.00 bp (vs 2026-09-14) | 0.53 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 09-16 close | official value for 2026-09-16 (not live) | -5.00 bp (vs 2026-09-15) | -2.34 | **YES** | fred:T10YIE |
| SOFR | 3.620 | 09-16 close | official value for 2026-09-16 (not live) | -2.00 bp (vs 2026-09-15) | -0.89 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.0s) |
| US dollar index (DXY) | 100.089 | 09-17 10:31 | **LIVE (~11 min old)** | -0.22 % (vs 2026-09-16) | -0.68 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 155.700 | 09-17 10:41 | **LIVE (~1 min old)** | +0.28 % (vs 2026-09-16) | 0.41 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.149 | 09-17 10:40 | **LIVE (~2 min old)** | -0.39 % (vs 2026-09-16) | -1.53 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 118.213 | 09-11 close | official value for 2026-09-11 (not live) | +0.11 % (vs 2026-09-10) | 0.54 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,697.750 | 09-17 10:31 | **LIVE (~11 min old)** | +1.87 % (vs 2026-09-16) | 2.99 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,716.250 | 09-17 10:31 | **LIVE (~11 min old)** | +2.60 % (vs 2026-09-16) | 2.66 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,914.300 | 09-17 10:31 | **LIVE (~11 min old)** | +1.84 % (vs 2026-09-16) | 2.23 | **YES** | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,631.650 | 09-17 10:41 | **LIVE (~1 min old)** | +1.06 % (vs 2026-09-16) | 1.67 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,439.344 | 09-17 10:41 | **LIVE (~1 min old)** | +1.71 % (vs 2026-09-16) | 1.73 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,891.841 | 09-17 10:26 | **LIVE (~16 min old)** | +1.16 % (vs 2026-09-16) | 1.38 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.630 | 09-17 10:25 | **LIVE (~16 min old)** | -2.08 pts | -2.06 | **YES** | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.9s) |
| WTI crude | 100.520 | 09-17 10:31 | **LIVE (~11 min old)** | -1.86 % (vs 2026-09-16) | -0.60 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 103.130 | 09-17 10:31 | **LIVE (~11 min old)** | -2.55 % (vs 2026-09-16) | -0.83 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,406.700 | 09-17 10:31 | **LIVE (~11 min old)** | +0.44 % (vs 2026-09-16) | 0.31 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.656 | 09-17 10:31 | **LIVE (~11 min old)** | +3.49 % (vs 2026-09-16) | 2.19 | **YES** | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: POSSIBLE ROLL on latest change; flag suppressed; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 76,725.47, 24h 1.44%, z 0.70
- kraken: funding (raw, units unverified) 1.0783198687708078, OI 2224.7164, OI change vs prior snapshot 0.49%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 36515.29366, OI change vs prior snapshot -2.97%

**ETH**: price 2,468.06, 24h 3.33%, z 1.14
- kraken: funding (raw, units unverified) 0.021356046733, OI 34768.457, OI change vs prior snapshot 1.07%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 984736.7214, OI change vs prior snapshot 1.67%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.9s)
