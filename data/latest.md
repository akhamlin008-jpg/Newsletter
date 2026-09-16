# Data snapshot 2026-09-16 16:47 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.69)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.736 | 09-16 16:47 | **LIVE (~0 min old)** | +7.30 bp | 1.37 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.020 | 09-16 16:47 | **LIVE (~0 min old)** | +2.40 bp | 0.55 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.284 | 09-16 16:47 | **LIVE (~0 min old)** | -4.90 bp | -1.71 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.620 | 09-15 close | official value for 2026-09-15 (not live) | +2.00 bp (vs 2026-09-14) | 0.53 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.380 | 09-15 close | official value for 2026-09-15 (not live) | +1.00 bp (vs 2026-09-14) | 0.46 |  | fred:T10YIE |
| SOFR | 3.640 | 09-15 close | official value for 2026-09-15 (not live) | +2.00 bp (vs 2026-09-14) | 0.89 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.1s) |
| US dollar index (DXY) | 100.314 | 09-16 16:37 | **LIVE (~10 min old)** | +0.67 % (vs 2026-09-15) | 2.30 | **YES** | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 156.264 | 09-16 16:47 | **LIVE (~0 min old)** | +1.22 % (vs 2026-09-15) | 1.78 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.147 | 09-16 16:46 | **LIVE (~1 min old)** | -0.70 % (vs 2026-09-15) | -2.69 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 118.213 | 09-11 close | official value for 2026-09-11 (not live) | +0.11 % (vs 2026-09-10) | 0.54 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,620.750 | 09-16 16:37 | **LIVE (~10 min old)** | +0.42 % (vs 2026-09-15) | 0.65 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,246.500 | 09-16 16:37 | **LIVE (~10 min old)** | +1.01 % (vs 2026-09-15) | 1.00 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,881.300 | 09-16 16:37 | **LIVE (~10 min old)** | +0.29 % (vs 2026-09-15) | 0.34 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,551.810 | 09-16 16:20 | **LIVE (~27 min old)** | -0.45 % (vs 2026-09-15) | -0.69 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,945.060 | 09-16 16:46 | **LIVE (~1 min old)** | +0.03 % (vs 2026-09-15) | 0.02 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,858.811 | 09-16 16:04 | **LIVE (~43 min old)** | -0.40 % (vs 2026-09-15) | -0.47 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.710 | 09-16 16:15 | **LIVE (~32 min old)** | +0.51 pts | 0.49 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.2s) |
| WTI crude | 102.140 | 09-16 16:37 | **LIVE (~10 min old)** | -3.49 % (vs 2026-09-15) | -1.12 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 105.420 | 09-16 16:37 | **LIVE (~10 min old)** | -3.06 % (vs 2026-09-15) | -0.99 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,301.500 | 09-16 16:37 | **LIVE (~10 min old)** | -0.72 % (vs 2026-09-15) | -0.52 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.439 | 09-16 16:37 | **LIVE (~10 min old)** | +1.10 % (vs 2026-09-15) | 0.68 |  | yahoo:HG=F (unofficial feed) |

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
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 76,034.59, 24h 0.21%, z 0.10
- kraken: funding (raw, units unverified) 1.728535844251692, OI 2201.88, OI change vs prior snapshot -0.19%
- hyperliquid: funding (raw, units unverified) 0.0000083654, OI 38448.5305, OI change vs prior snapshot -1.27%

**ETH**: price 2,405.95, 24h 0.00%, z 0.00
- kraken: funding (raw, units unverified) 0.10431779400762581, OI 35321.278, OI change vs prior snapshot 0.32%
- hyperliquid: funding (raw, units unverified) 0.0000109241, OI 984812.1434000003, OI change vs prior snapshot -0.17%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.2s)
