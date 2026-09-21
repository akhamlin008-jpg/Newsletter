# Data snapshot 2026-09-21 11:03 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** equity (max |z| 3.0), crypto (max |z| 2.78)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.735 | 09-21 11:01 | **LIVE (~3 min old)** | -0.80 bp | -0.14 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.967 | 09-21 11:03 | **LIVE (~0 min old)** | -2.90 bp | -0.65 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.232 | 09-21 11:01 | **LIVE (~3 min old)** | -2.10 bp | -0.70 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.610 | 09-17 close | official value for 2026-09-17 (not live) | -7.00 bp (vs 2026-09-16) | -1.81 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 09-18 close | official value for 2026-09-18 (not live) | +0.00 bp (vs 2026-09-17) | 0.00 |  | fred:T10YIE |
| SOFR | 3.850 | 09-18 close | official value for 2026-09-18 (not live) | +0.00 bp (vs 2026-09-17) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.1s) |
| US dollar index (DXY) | 100.362 | 09-21 10:54 | **LIVE (~10 min old)** | +0.14 % (vs 2026-09-18) | 0.46 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.494 | 09-21 11:04 | **LIVE (~0 min old)** | +0.87 % (vs 2026-09-18) | 1.35 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.148 | 09-21 11:03 | **LIVE (~1 min old)** | -0.00 % (vs 2026-09-18) | -0.01 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 118.213 | 09-11 close | official value for 2026-09-11 (not live) | +0.11 % (vs 2026-09-10) | 0.54 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,787.250 | 09-21 10:54 | **LIVE (~10 min old)** | +1.70 % (vs 2026-09-18) | 2.63 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,511.000 | 09-21 10:54 | **LIVE (~10 min old)** | +3.03 % (vs 2026-09-18) | 3.00 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,897.000 | 09-21 10:54 | **LIVE (~10 min old)** | +0.83 % (vs 2026-09-18) | 1.03 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,723.170 | 09-21 11:04 | **LIVE (~0 min old)** | +0.95 % (vs 2026-09-18) | 1.45 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,268.227 | 09-21 11:04 | **LIVE (~0 min old)** | +2.11 % (vs 2026-09-18) | 2.05 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,877.801 | 09-21 10:49 | **LIVE (~15 min old)** | +0.61 % (vs 2026-09-18) | 0.76 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 14.650 | 09-21 10:47 | **LIVE (~16 min old)** | -0.16 pts | -0.15 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.1s) |
| WTI crude | 92.180 | 09-21 10:54 | **LIVE (~10 min old)** | -8.10 % (vs 2026-09-18) | -2.74 | **YES** | yahoo:CL=F (unofficial feed) |
| Brent crude | 100.150 | 09-21 10:54 | **LIVE (~10 min old)** | -3.58 % (vs 2026-09-18) | -1.24 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,379.800 | 09-21 10:54 | **LIVE (~10 min old)** | -1.02 % (vs 2026-09-18) | -0.78 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.770 | 09-21 10:54 | **LIVE (~10 min old)** | +2.34 % (vs 2026-09-18) | 1.46 |  | yahoo:HG=F (unofficial feed) |

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
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); quarterly roll window: roll date 2026-09-10, expiry 2026-09-18; a jump may be the contract switch; roll check: last completed session: POSSIBLE ROLL on latest change; flag suppressed; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-18)
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

**BTC**: price 85,974.59, 24h 6.31%, z 2.78 **FLAG**
- kraken: funding (raw, units unverified) 0.7607081911788047, OI 2142.1373, OI change vs prior snapshot -2.01%
- hyperliquid: funding (raw, units unverified) 0.0000436362, OI 45439.63266, OI change vs prior snapshot 1.13%

**ETH**: price 2,740.59, 24h 4.89%, z 1.62
- kraken: funding (raw, units unverified) 0.11998089524691576, OI 30745.822, OI change vs prior snapshot -1.59%
- hyperliquid: funding (raw, units unverified) 0.0000211801, OI 1165119.1350000023, OI change vs prior snapshot 0.15%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.1s)
