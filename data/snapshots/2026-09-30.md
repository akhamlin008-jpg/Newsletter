# Data snapshot 2026-09-30 10:13 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.847 | 09-30 10:12 | **LIVE (~0 min old)** | -4.20 bp | -0.64 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.249 | 09-30 10:12 | **LIVE (~0 min old)** | -0.60 bp | -0.10 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.402 | 09-30 10:12 | **LIVE (~0 min old)** | +3.60 bp | 1.00 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.900 | 09-28 close | official value for 2026-09-28 (not live) | +7.00 bp (vs 2026-09-25) | 1.29 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 09-29 close | official value for 2026-09-29 (not live) | +1.00 bp (vs 2026-09-28) | 0.50 |  | fred:T10YIE |
| SOFR | 3.880 | 09-29 close | official value for 2026-09-29 (not live) | -2.00 bp (vs 2026-09-28) | -0.43 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.3s) |
| US dollar index (DXY) | 101.208 | 09-30 10:03 | **LIVE (~10 min old)** | -0.16 % (vs 2026-09-29) | -0.54 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 156.859 | 09-30 10:13 | **LIVE (~0 min old)** | -0.32 % (vs 2026-09-29) | -0.54 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.136 | 09-30 10:12 | **LIVE (~1 min old)** | -0.09 % (vs 2026-09-29) | -0.35 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,771.250 | 09-30 10:03 | **LIVE (~10 min old)** | +0.51 % (vs 2026-09-29) | 0.85 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,860.250 | 09-30 10:03 | **LIVE (~10 min old)** | +0.81 % (vs 2026-09-29) | 0.88 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,833.100 | 09-30 10:03 | **LIVE (~10 min old)** | +0.14 % (vs 2026-09-29) | 0.17 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,712.970 | 09-30 10:13 | **LIVE (~0 min old)** | +0.55 % (vs 2026-09-29) | 0.82 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,558.980 | 09-30 10:13 | **LIVE (~0 min old)** | +0.72 % (vs 2026-09-29) | 0.67 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,813.575 | 09-30 09:58 | **LIVE (~15 min old)** | +0.20 % (vs 2026-09-29) | 0.25 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.710 | 09-30 09:57 | **LIVE (~16 min old)** | -0.33 pts | -0.33 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.1s) |
| WTI crude | 90.640 | 09-30 10:03 | **LIVE (~10 min old)** | +1.41 % (vs 2026-09-29) | 0.49 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 98.230 | 09-30 10:03 | **LIVE (~10 min old)** | -4.25 % (vs 2026-09-29) | -1.51 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,207.900 | 09-30 10:03 | **LIVE (~10 min old)** | +0.67 % (vs 2026-09-29) | 0.48 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.641 | 09-30 10:03 | **LIVE (~10 min old)** | +1.49 % (vs 2026-09-29) | 1.03 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 84,248.71, 24h 0.64%, z 0.29
- kraken: funding (raw, units unverified) 1.5516526845099718, OI 2421.7085, OI change vs prior snapshot 3.36%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 34145.37638, OI change vs prior snapshot 1.21%

**ETH**: price 2,701.02, 24h -0.34%, z -0.13
- kraken: funding (raw, units unverified) 0.0519915562543741, OI 28261.801, OI change vs prior snapshot 2.32%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1150026.7359999986, OI change vs prior snapshot -0.21%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.3s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.1s)
