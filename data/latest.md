# Data snapshot 2026-09-18 05:04 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.05)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.705 | 09-18 05:04 | **LIVE (~0 min old)** | +1.50 bp | 0.28 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.951 | 09-18 05:04 | **LIVE (~0 min old)** | +0.40 bp | 0.09 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.246 | 09-18 05:04 | **LIVE (~0 min old)** | -1.10 bp | -0.36 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.680 | 09-16 close | official value for 2026-09-16 (not live) | +6.00 bp (vs 2026-09-15) | 1.63 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 09-17 close | official value for 2026-09-17 (not live) | +0.00 bp (vs 2026-09-16) | 0.00 |  | fred:T10YIE |
| SOFR | 3.620 | 09-16 close | official value for 2026-09-16 (not live) | -2.00 bp (vs 2026-09-15) | -0.89 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.0s) |
| US dollar index (DXY) | 100.363 | 09-18 04:54 | **LIVE (~11 min old)** | +0.14 % (vs 2026-09-17) | 0.45 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.762 | 09-18 05:04 | **LIVE (~1 min old)** | +1.12 % (vs 2026-09-17) | 1.68 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.149 | 09-18 05:03 | **LIVE (~2 min old)** | +0.14 % (vs 2026-09-17) | 0.51 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 118.213 | 09-11 close | official value for 2026-09-11 (not live) | +0.11 % (vs 2026-09-10) | 0.54 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,727.750 | 09-18 04:54 | **LIVE (~11 min old)** | +1.15 % (vs 2026-09-17) | 1.73 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,896.750 | 09-18 04:54 | **LIVE (~11 min old)** | +1.53 % (vs 2026-09-17) | 1.48 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,898.800 | 09-18 04:54 | **LIVE (~11 min old)** | +0.80 % (vs 2026-09-17) | 0.99 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,637.760 | 09-17 16:34 | not trading now; last trade 09-17 16:34 ET | +1.14 % (vs 2026-09-16) | 1.79 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,446.980 | 09-17 17:16 | not trading now; last trade 09-17 17:16 ET | +1.73 % (vs 2026-09-16) | 1.76 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,874.630 | 09-17 16:30 | not trading now; last trade 09-17 16:30 ET | +0.55 % (vs 2026-09-16) | 0.66 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.230 | 09-18 04:49 | **LIVE (~16 min old)** | -0.21 pts (vs 2026-09-17) | -0.19 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.4s) |
| WTI crude | 95.600 | 09-18 04:55 | **LIVE (~10 min old)** | -6.19 % (vs 2026-09-17) | -2.05 | **YES** | yahoo:CL=F (unofficial feed) |
| Brent crude | 98.450 | 09-18 04:53 | **LIVE (~12 min old)** | -6.08 % (vs 2026-09-17) | -2.04 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,432.000 | 09-18 04:55 | **LIVE (~10 min old)** | +0.73 % (vs 2026-09-17) | 0.55 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.665 | 09-18 04:55 | **LIVE (~10 min old)** | +1.19 % (vs 2026-09-17) | 0.72 |  | yahoo:HG=F (unofficial feed) |

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
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 78,236.06, 24h 2.41%, z 1.22
- kraken: funding (raw, units unverified) 0.978650622305, OI 2256.2836, OI change vs prior snapshot 1.42%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 35718.13968, OI change vs prior snapshot -2.18%

**ETH**: price 2,504.39, 24h 2.78%, z 0.98
- kraken: funding (raw, units unverified) 0.05073376041599917, OI 35312.141, OI change vs prior snapshot 1.56%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1022532.8503999999, OI change vs prior snapshot 3.84%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.4s)
