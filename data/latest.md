# Data snapshot 2026-10-21 09:42 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.768 | 10-21 09:42 | **LIVE (~0 min old)** | -1.90 bp | -0.36 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.090 | 10-21 09:42 | **LIVE (~0 min old)** | -2.70 bp | -0.54 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.322 | 10-21 09:42 | **LIVE (~0 min old)** | -0.80 bp | -0.23 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.800 | 10-19 close | official value for 2026-10-19 (not live) | +6.00 bp (vs 2026-10-16) | 1.27 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-20 close | official value for 2026-10-20 (not live) | +0.00 bp (vs 2026-10-19) | 0.00 |  | fred:T10YIE |
| SOFR | 3.880 | 10-20 close | official value for 2026-10-20 (not live) | +1.00 bp (vs 2026-10-19) | 0.31 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (12.0s) |
| US dollar index (DXY) | 101.698 | 10-21 09:32 | **LIVE (~11 min old)** | -0.03 % (vs 2026-10-20) | -0.10 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.979 | 10-21 09:42 | **LIVE (~1 min old)** | -0.34 % (vs 2026-10-20) | -0.85 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.124 | 10-21 09:42 | **LIVE (~1 min old)** | +0.18 % (vs 2026-10-20) | 0.65 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.405 | 10-16 close | official value for 2026-10-16 (not live) | -0.14 % (vs 2026-10-15) | -0.48 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,766.750 | 10-21 09:32 | **LIVE (~11 min old)** | +0.15 % (vs 2026-10-20) | 0.25 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,842.750 | 10-21 09:32 | **LIVE (~11 min old)** | +0.56 % (vs 2026-10-20) | 0.54 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,800.800 | 10-21 09:32 | **LIVE (~11 min old)** | +0.50 % (vs 2026-10-20) | 0.51 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,730.240 | 10-21 09:42 | **LIVE (~1 min old)** | +0.23 % (vs 2026-10-20) | 0.37 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,651.713 | 10-21 09:42 | **LIVE (~1 min old)** | +0.55 % (vs 2026-10-20) | 0.49 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,773.420 | 10-20 16:30 | not trading now; last trade 10-20 16:30 ET | +1.65 % (vs 2026-10-19) | 1.79 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 16.940 | 10-21 09:25 | **LIVE (~18 min old)** | -0.37 pts (vs 2026-10-20) | -0.31 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.2s) |
| WTI crude | 97.390 | 10-21 09:33 | **LIVE (~10 min old)** | -4.32 % (vs 2026-10-20) | -1.76 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 108.300 | 10-21 09:32 | **LIVE (~11 min old)** | -0.45 % (vs 2026-10-20) | -0.20 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,152.900 | 10-21 09:33 | **LIVE (~10 min old)** | +0.25 % (vs 2026-10-20) | 0.22 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.549 | 10-21 09:33 | **LIVE (~10 min old)** | -0.27 % (vs 2026-10-20) | -0.23 |  | yahoo:HG=F (unofficial feed) |

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
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 83,493.64, 24h 1.77%, z 1.12
- kraken: funding (raw, units unverified) 1.3308503308795, OI 2507.4815, OI change vs prior snapshot 0.10%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41424.25136, OI change vs prior snapshot 0.48%

**ETH**: price 2,464.04, 24h 2.31%, z 1.12
- kraken: funding (raw, units unverified) 0.04816395900266749, OI 27777.902, OI change vs prior snapshot 0.14%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1100879.8795999982, OI change vs prior snapshot -0.03%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (12.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.2s)
