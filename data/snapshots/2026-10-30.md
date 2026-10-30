# Data snapshot 2026-10-30 10:00 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.34), equity (max |z| 2.32)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.621 | 10-30 10:00 | **LIVE (~0 min old)** | -3.50 bp | -0.62 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.945 | 10-30 10:00 | **LIVE (~0 min old)** | -4.40 bp | -0.76 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.324 | 10-30 10:00 | **LIVE (~0 min old)** | -0.90 bp | -0.25 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.670 | 10-28 close | official value for 2026-10-28 (not live) | +3.00 bp (vs 2026-10-27) | 0.61 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-29 close | official value for 2026-10-29 (not live) | -3.00 bp (vs 2026-10-28) | -1.46 |  | fred:T10YIE |
| SOFR | 3.940 | 10-29 close | official value for 2026-10-29 (not live) | +0.00 bp (vs 2026-10-28) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.6s) |
| US dollar index (DXY) | 101.982 | 10-30 09:50 | **LIVE (~10 min old)** | -0.06 % (vs 2026-10-29) | -0.21 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.328 | 10-30 10:00 | **LIVE (~0 min old)** | -0.32 % (vs 2026-10-29) | -0.76 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.115 | 10-30 09:59 | **LIVE (~1 min old)** | -0.02 % (vs 2026-10-29) | -0.08 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,657.000 | 10-30 09:50 | **LIVE (~10 min old)** | -1.25 % (vs 2026-10-29) | -2.05 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,752.000 | 10-30 09:50 | **LIVE (~10 min old)** | -2.74 % (vs 2026-10-29) | -2.32 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,839.700 | 10-30 09:50 | **LIVE (~10 min old)** | -0.96 % (vs 2026-10-29) | -1.09 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,635.730 | 10-30 10:00 | **LIVE (~0 min old)** | -1.10 % (vs 2026-10-29) | -1.75 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,710.365 | 10-30 10:00 | **LIVE (~0 min old)** | -2.35 % (vs 2026-10-29) | -1.92 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,836.422 | 10-30 09:45 | **LIVE (~15 min old)** | -0.80 % (vs 2026-10-29) | -0.90 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 19.010 | 10-30 09:44 | **LIVE (~16 min old)** | +1.81 pts | 1.57 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.6s) |
| WTI crude | 103.990 | 10-30 09:50 | **LIVE (~10 min old)** | +1.95 % (vs 2026-10-29) | 0.76 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 113.360 | 10-30 09:50 | **LIVE (~10 min old)** | -1.32 % (vs 2026-10-29) | -0.62 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,928.300 | 10-30 09:50 | **LIVE (~10 min old)** | -2.56 % (vs 2026-10-29) | -2.34 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.514 | 10-30 09:50 | **LIVE (~10 min old)** | -1.01 % (vs 2026-10-29) | -0.80 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
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

**BTC**: price 76,961.78, 24h -4.02%, z -2.28 **FLAG**
- kraken: funding (raw, units unverified) 0.995827778828266, OI 2697.6162, OI change vs prior snapshot 10.12%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40173.43754, OI change vs prior snapshot -7.06%

**ETH**: price 2,222.67, 24h -4.37%, z -2.07 **FLAG**
- kraken: funding (raw, units unverified) 0.01023891929, OI 30121.925, OI change vs prior snapshot -8.38%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1033411.9051999997, OI change vs prior snapshot -7.14%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.6s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.6s)
