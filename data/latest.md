# Data snapshot 2026-11-16 13:22 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.844 | 11-16 13:21 | **LIVE (~1 min old)** | -3.00 bp | -0.40 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.137 | 11-16 13:21 | **LIVE (~1 min old)** | -1.60 bp | -0.26 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.293 | 11-16 13:21 | **LIVE (~1 min old)** | +1.40 bp | 0.37 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.860 | 11-12 close | official value for 2026-11-12 (not live) | +8.00 bp (vs 2026-11-10) | 1.59 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.240 | 11-13 close | official value for 2026-11-13 (not live) | +0.00 bp (vs 2026-11-12) | 0.00 |  | fred:T10YIE |
| SOFR | 3.900 | 11-13 close | official value for 2026-11-13 (not live) | +0.00 bp (vs 2026-11-12) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (12.2s) |
| US dollar index (DXY) | 103.607 | 11-16 13:12 | **LIVE (~11 min old)** | +0.19 % (vs 2026-11-13) | 0.52 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.580 | 11-16 13:22 | **LIVE (~1 min old)** | -0.18 % (vs 2026-11-13) | -0.47 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.100 | 11-16 13:22 | **LIVE (~1 min old)** | -0.49 % (vs 2026-11-13) | -1.30 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,464.250 | 11-16 13:12 | **LIVE (~11 min old)** | -1.57 % (vs 2026-11-13) | -1.25 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,393.250 | 11-16 13:12 | **LIVE (~11 min old)** | -2.29 % (vs 2026-11-13) | -1.16 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,757.300 | 11-16 13:12 | **LIVE (~11 min old)** | -1.44 % (vs 2026-11-13) | -0.98 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,436.680 | 11-16 13:22 | **LIVE (~1 min old)** | -1.65 % (vs 2026-11-13) | -1.32 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,276.928 | 11-16 13:22 | **LIVE (~1 min old)** | -2.39 % (vs 2026-11-13) | -1.20 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,751.302 | 11-16 13:07 | **LIVE (~16 min old)** | -1.40 % (vs 2026-11-13) | -0.96 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 22.280 | 11-16 13:06 | **LIVE (~16 min old)** | +2.98 pts | 0.98 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.1s) |
| WTI crude | 85.970 | 11-16 13:12 | **LIVE (~11 min old)** | -2.92 % (vs 2026-11-13) | -0.94 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 92.990 | 11-16 13:12 | **LIVE (~11 min old)** | -2.97 % (vs 2026-11-13) | -0.84 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,846.400 | 11-16 13:12 | **LIVE (~11 min old)** | -1.03 % (vs 2026-11-13) | -0.67 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.004 | 11-16 13:12 | **LIVE (~11 min old)** | -1.24 % (vs 2026-11-13) | -0.86 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 64,841.85, 24h 0.23%, z 0.09
- kraken: funding (raw, units unverified) 0.8694462988481466, OI 2271.5156, OI change vs prior snapshot 0.51%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 36442.0214999999, OI change vs prior snapshot 1.48%

**ETH**: price 1,819.15, 24h 0.25%, z 0.07
- kraken: funding (raw, units unverified) -0.01857065230775, OI 27755.589, OI change vs prior snapshot 0.93%
- hyperliquid: funding (raw, units unverified) 0.000009578, OI 597784.9870000008, OI change vs prior snapshot 2.11%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (12.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.1s)
