# Data snapshot 2026-10-01 10:44 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.12)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.843 | 10-01 10:44 | **LIVE (~0 min old)** | -4.40 bp | -0.68 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.298 | 10-01 10:44 | **LIVE (~0 min old)** | +0.50 bp | 0.09 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.455 | 10-01 10:44 | **LIVE (~0 min old)** | +4.90 bp | 1.35 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.910 | 09-29 close | official value for 2026-09-29 (not live) | +1.00 bp (vs 2026-09-28) | 0.18 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 09-30 close | official value for 2026-09-30 (not live) | +1.00 bp (vs 2026-09-29) | 0.51 |  | fred:T10YIE |
| SOFR | 3.900 | 09-30 close | official value for 2026-09-30 (not live) | +2.00 bp (vs 2026-09-29) | 0.44 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.8s) |
| US dollar index (DXY) | 101.763 | 10-01 10:34 | **LIVE (~11 min old)** | +0.31 % (vs 2026-09-30) | 1.08 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.595 | 10-01 10:45 | **LIVE (~0 min old)** | +0.12 % (vs 2026-09-30) | 0.21 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.128 | 10-01 10:44 | **LIVE (~1 min old)** | -0.56 % (vs 2026-09-30) | -2.12 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,700.750 | 10-01 10:35 | **LIVE (~10 min old)** | -0.19 % (vs 2026-09-30) | -0.33 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,680.000 | 10-01 10:35 | **LIVE (~10 min old)** | -0.06 % (vs 2026-09-30) | -0.07 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,802.100 | 10-01 10:35 | **LIVE (~10 min old)** | -0.55 % (vs 2026-09-30) | -0.69 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,643.040 | 10-01 10:45 | **LIVE (~0 min old)** | -0.11 % (vs 2026-09-30) | -0.17 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,414.387 | 10-01 10:44 | **LIVE (~1 min old)** | +0.02 % (vs 2026-09-30) | 0.02 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,781.045 | 10-01 10:30 | **LIVE (~15 min old)** | -0.57 % (vs 2026-09-30) | -0.73 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.260 | 10-01 10:29 | **LIVE (~16 min old)** | +0.92 pts | 0.96 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.6s) |
| WTI crude | 91.800 | 10-01 10:35 | **LIVE (~10 min old)** | +1.53 % (vs 2026-09-30) | 0.54 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 100.670 | 10-01 10:35 | **LIVE (~10 min old)** | -2.76 % (vs 2026-09-30) | -1.01 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,195.700 | 10-01 10:35 | **LIVE (~10 min old)** | +0.21 % (vs 2026-09-30) | 0.16 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.584 | 10-01 10:35 | **LIVE (~10 min old)** | +0.38 % (vs 2026-09-30) | 0.27 |  | yahoo:HG=F (unofficial feed) |

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
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 84,022.81, 24h 0.32%, z 0.15
- kraken: funding (raw, units unverified) 0.7941137522130137, OI 2371.2971, OI change vs prior snapshot -0.71%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 34008.99182, OI change vs prior snapshot -0.68%

**ETH**: price 2,691.95, 24h 0.56%, z 0.23
- kraken: funding (raw, units unverified) 0.025185023792499102, OI 26358.506, OI change vs prior snapshot 1.39%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1197333.5998, OI change vs prior snapshot -0.08%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.8s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.6s)
