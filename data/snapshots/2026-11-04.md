# Data snapshot 2026-11-04 10:20 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** crypto (max |z| 3.32), vol (max |z| 3.07)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.633 | 11-04 10:20 | **LIVE (~0 min old)** | +1.90 bp | 0.34 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.958 | 11-04 10:20 | **LIVE (~0 min old)** | +0.80 bp | 0.14 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.325 | 11-04 10:20 | **LIVE (~0 min old)** | -1.10 bp | -0.30 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.620 | 11-02 close | official value for 2026-11-02 (not live) | +2.00 bp (vs 2026-10-30) | 0.43 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.300 | 11-03 close | official value for 2026-11-03 (not live) | +1.00 bp (vs 2026-11-02) | 0.43 |  | fred:T10YIE |
| SOFR | 3.970 | 11-03 close | official value for 2026-11-03 (not live) | +2.00 bp (vs 2026-11-02) | 0.79 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.6s) |
| US dollar index (DXY) | 101.476 | 11-04 10:10 | **LIVE (~10 min old)** | -0.39 % (vs 2026-11-03) | -1.51 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.588 | 11-04 10:20 | **LIVE (~0 min old)** | +0.43 % (vs 2026-11-03) | 1.11 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.124 | 11-04 10:20 | **LIVE (~0 min old)** | +0.43 % (vs 2026-11-03) | 1.60 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,729.000 | 11-04 10:10 | **LIVE (~10 min old)** | +1.74 % (vs 2026-11-03) | 2.45 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,878.250 | 11-04 10:10 | **LIVE (~10 min old)** | +2.02 % (vs 2026-11-03) | 1.45 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,858.300 | 11-04 10:10 | **LIVE (~10 min old)** | +1.18 % (vs 2026-11-03) | 1.33 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,701.360 | 11-04 10:20 | **LIVE (~0 min old)** | +1.75 % (vs 2026-11-03) | 2.42 | **YES** | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,765.715 | 11-04 10:20 | **LIVE (~0 min old)** | +2.08 % (vs 2026-11-03) | 1.46 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,850.224 | 11-04 10:05 | **LIVE (~15 min old)** | +1.34 % (vs 2026-11-03) | 1.50 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.020 | 11-04 10:04 | **LIVE (~16 min old)** | -3.81 pts | -3.07 | **YES** | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.4s) |
| WTI crude | 93.990 | 11-04 10:10 | **LIVE (~10 min old)** | -2.19 % (vs 2026-11-03) | -0.74 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 101.290 | 11-04 10:10 | **LIVE (~10 min old)** | -2.23 % (vs 2026-11-03) | -0.67 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,045.000 | 11-04 10:10 | **LIVE (~10 min old)** | +2.65 % (vs 2026-11-03) | 1.99 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.404 | 11-04 10:10 | **LIVE (~10 min old)** | +0.41 % (vs 2026-11-03) | 0.29 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
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

**BTC**: price 80,622.81, 24h 3.92%, z 2.42 **FLAG**
- kraken: funding (raw, units unverified) 0.9295914922910264, OI 2365.843, OI change vs prior snapshot -7.98%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40607.42496, OI change vs prior snapshot -0.23%

**ETH**: price 2,437.47, 24h 6.15%, z 3.32 **FLAG**
- kraken: funding (raw, units unverified) 0.0656663111387508, OI 29703.18, OI change vs prior snapshot -9.00%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1034721.1015999999, OI change vs prior snapshot 3.29%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.6s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.4s)
