# Data snapshot 2026-11-04 10:43 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** crypto (max |z| 3.08), vol (max |z| 2.71)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.627 | 11-04 10:43 | **LIVE (~0 min old)** | +1.30 bp | 0.24 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.941 | 11-04 10:43 | **LIVE (~0 min old)** | -0.90 bp | -0.16 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.314 | 11-04 10:43 | **LIVE (~0 min old)** | -2.20 bp | -0.60 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.620 | 11-02 close | official value for 2026-11-02 (not live) | +2.00 bp (vs 2026-10-30) | 0.43 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.300 | 11-03 close | official value for 2026-11-03 (not live) | +1.00 bp (vs 2026-11-02) | 0.43 |  | fred:T10YIE |
| SOFR | 3.970 | 11-03 close | official value for 2026-11-03 (not live) | +2.00 bp (vs 2026-11-02) | 0.79 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.7s) |
| US dollar index (DXY) | 101.516 | 11-04 10:33 | **LIVE (~10 min old)** | -0.35 % (vs 2026-11-03) | -1.36 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.590 | 11-04 10:43 | **LIVE (~0 min old)** | +0.43 % (vs 2026-11-03) | 1.11 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.124 | 11-04 10:43 | **LIVE (~0 min old)** | +0.41 % (vs 2026-11-03) | 1.56 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,717.000 | 11-04 10:33 | **LIVE (~10 min old)** | +1.58 % (vs 2026-11-03) | 2.23 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,774.000 | 11-04 10:33 | **LIVE (~10 min old)** | +1.65 % (vs 2026-11-03) | 1.19 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,851.300 | 11-04 10:33 | **LIVE (~10 min old)** | +0.93 % (vs 2026-11-03) | 1.05 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,692.220 | 11-04 10:43 | **LIVE (~0 min old)** | +1.63 % (vs 2026-11-03) | 2.25 | **YES** | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,614.627 | 11-04 10:43 | **LIVE (~0 min old)** | +1.54 % (vs 2026-11-03) | 1.09 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,834.611 | 11-04 10:28 | **LIVE (~15 min old)** | +0.79 % (vs 2026-11-03) | 0.88 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.460 | 11-04 10:27 | **LIVE (~16 min old)** | -3.37 pts | -2.71 | **YES** | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s) |
| WTI crude | 93.850 | 11-04 10:33 | **LIVE (~10 min old)** | -2.33 % (vs 2026-11-03) | -0.79 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 101.280 | 11-04 10:33 | **LIVE (~10 min old)** | -2.24 % (vs 2026-11-03) | -0.68 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,046.200 | 11-04 10:33 | **LIVE (~10 min old)** | +2.69 % (vs 2026-11-03) | 2.01 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.396 | 11-04 10:33 | **LIVE (~10 min old)** | +0.27 % (vs 2026-11-03) | 0.20 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 80,359.80, 24h 3.58%, z 2.21 **FLAG**
- kraken: funding (raw, units unverified) 0.9295914922910264, OI 2363.6501, OI change vs prior snapshot -0.09%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41350.60964, OI change vs prior snapshot 1.83%

**ETH**: price 2,427.54, 24h 5.71%, z 3.08 **FLAG**
- kraken: funding (raw, units unverified) 0.0656663111387508, OI 28872.955, OI change vs prior snapshot -2.80%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1033166.0899999996, OI change vs prior snapshot -0.15%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.7s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s)
