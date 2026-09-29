# Data snapshot 2026-09-29 10:34 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.99)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.920 | 09-29 10:34 | **LIVE (~0 min old)** | -0.40 bp | -0.06 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.245 | 09-29 10:34 | **LIVE (~0 min old)** | +0.30 bp | 0.05 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.325 | 09-29 10:34 | **LIVE (~0 min old)** | +0.70 bp | 0.20 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.830 | 09-25 close | official value for 2026-09-25 (not live) | -2.00 bp (vs 2026-09-24) | -0.36 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 09-28 close | official value for 2026-09-28 (not live) | +0.00 bp (vs 2026-09-25) | 0.00 |  | fred:T10YIE |
| SOFR | 3.900 | 09-28 close | official value for 2026-09-28 (not live) | +0.00 bp (vs 2026-09-25) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.1s) |
| US dollar index (DXY) | 101.389 | 09-29 10:24 | **LIVE (~11 min old)** | +0.19 % (vs 2026-09-28) | 0.62 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.321 | 09-29 10:35 | **LIVE (~0 min old)** | -0.09 % (vs 2026-09-28) | -0.15 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.135 | 09-29 10:34 | **LIVE (~1 min old)** | -0.26 % (vs 2026-09-28) | -0.97 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,739.000 | 09-29 10:25 | **LIVE (~10 min old)** | -0.10 % (vs 2026-09-28) | -0.16 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,662.750 | 09-29 10:25 | **LIVE (~10 min old)** | +0.32 % (vs 2026-09-28) | 0.33 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,832.300 | 09-29 10:25 | **LIVE (~10 min old)** | -0.27 % (vs 2026-09-28) | -0.33 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,683.980 | 09-29 10:35 | **LIVE (~0 min old)** | +0.00 % (vs 2026-09-28) | 0.01 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,415.830 | 09-29 10:35 | **LIVE (~0 min old)** | +0.46 % (vs 2026-09-28) | 0.41 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,817.020 | 09-29 10:20 | **LIVE (~15 min old)** | -0.03 % (vs 2026-09-28) | -0.04 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.830 | 09-29 10:19 | **LIVE (~16 min old)** | -0.24 pts | -0.24 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (5.9s) |
| WTI crude | 91.120 | 09-29 10:25 | **LIVE (~10 min old)** | -1.60 % (vs 2026-09-28) | -0.56 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 96.370 | 09-29 10:25 | **LIVE (~10 min old)** | -8.46 % (vs 2026-09-28) | -2.99 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,206.500 | 09-29 10:25 | **LIVE (~10 min old)** | +0.91 % (vs 2026-09-28) | 0.63 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.640 | 09-29 10:25 | **LIVE (~10 min old)** | +1.13 % (vs 2026-09-28) | 0.76 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 83,931.10, 24h 1.12%, z 0.49
- kraken: funding (raw, units unverified) 0.706451560540875, OI 2340.9754, OI change vs prior snapshot 0.56%
- hyperliquid: funding (raw, units unverified) 0.0000108012, OI 34598.128, OI change vs prior snapshot -0.25%

**ETH**: price 2,716.96, 24h 1.89%, z 0.72
- kraken: funding (raw, units unverified) 0.016293114031582425, OI 26213.13, OI change vs prior snapshot -0.11%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1203938.487, OI change vs prior snapshot -0.11%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (5.9s)
