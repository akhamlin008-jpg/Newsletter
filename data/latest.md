# Data snapshot 2026-09-24 09:30 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.88)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.850 | 09-24 09:30 | **LIVE (~0 min old)** | -4.50 bp | -0.81 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.096 | 09-24 09:30 | **LIVE (~0 min old)** | -1.80 bp | -0.40 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.246 | 09-24 09:30 | **LIVE (~0 min old)** | +2.70 bp | 0.84 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.630 | 09-22 close | official value for 2026-09-22 (not live) | +1.00 bp (vs 2026-09-21) | 0.22 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 09-23 close | official value for 2026-09-23 (not live) | +2.00 bp (vs 2026-09-22) | 0.93 |  | fred:T10YIE |
| SOFR | 3.870 | 09-23 close | official value for 2026-09-23 (not live) | +0.00 bp (vs 2026-09-22) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.6s) |
| US dollar index (DXY) | 101.266 | 09-24 09:20 | **LIVE (~11 min old)** | +0.16 % (vs 2026-09-23) | 0.49 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.825 | 09-24 09:31 | **LIVE (~0 min old)** | +0.86 % (vs 2026-09-23) | 1.42 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.136 | 09-24 09:30 | **LIVE (~1 min old)** | -0.74 % (vs 2026-09-23) | -2.88 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 119.513 | 09-18 close | official value for 2026-09-18 (not live) | +0.14 % (vs 2026-09-17) | 0.61 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,740.250 | 09-24 09:20 | **LIVE (~11 min old)** | -0.41 % (vs 2026-09-23) | -0.65 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,513.000 | 09-24 09:21 | **LIVE (~10 min old)** | -0.82 % (vs 2026-09-23) | -0.83 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,853.100 | 09-24 09:21 | **LIVE (~10 min old)** | -0.25 % (vs 2026-09-23) | -0.28 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,666.330 | 09-24 09:31 | **LIVE (~0 min old)** | -0.52 % (vs 2026-09-23) | -0.70 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,219.709 | 09-24 09:31 | **LIVE (~0 min old)** | -0.82 % (vs 2026-09-23) | -0.70 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,838.660 | 09-23 16:30 | not trading now; last trade 09-23 16:30 ET | -1.28 % (vs 2026-09-21) | -1.61 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.920 | 09-24 09:16 | **LIVE (~15 min old)** | +0.74 pts (vs 2026-09-23) | 0.71 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.0s) |
| WTI crude | 93.630 | 09-24 09:21 | **LIVE (~10 min old)** | +1.59 % (vs 2026-09-23) | 0.54 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 99.660 | 09-24 09:21 | **LIVE (~10 min old)** | -3.32 % (vs 2026-09-23) | -1.14 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,312.300 | 09-24 09:21 | **LIVE (~10 min old)** | -0.14 % (vs 2026-09-23) | -0.11 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.756 | 09-24 09:21 | **LIVE (~10 min old)** | +1.17 % (vs 2026-09-23) | 0.76 |  | yahoo:HG=F (unofficial feed) |

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
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-18, 2026-09-21)
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 83,796.34, 24h -2.32%, z -0.88
- kraken: funding (raw, units unverified) 0.6426581221913612, OI 2229.2865, OI change vs prior snapshot 1.65%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 38459.64738, OI change vs prior snapshot 1.57%

**ETH**: price 2,660.71, 24h -2.01%, z -0.66
- kraken: funding (raw, units unverified) 0.018562547398500884, OI 27308.586, OI change vs prior snapshot -0.27%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1066868.0189999996, OI change vs prior snapshot -0.10%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.6s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.0s)
