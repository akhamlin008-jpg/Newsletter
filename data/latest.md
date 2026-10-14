# Data snapshot 2026-10-14 09:39 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.895 | 10-14 09:38 | **LIVE (~0 min old)** | +10.20 bp | 1.75 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.287 | 10-14 09:38 | **LIVE (~0 min old)** | +7.00 bp | 1.41 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.392 | 10-14 09:38 | **LIVE (~0 min old)** | -3.20 bp | -0.95 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.910 | 10-09 close | official value for 2026-10-09 (not live) | +4.00 bp (vs 2026-10-08) | 0.82 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 10-13 close | official value for 2026-10-13 (not live) | +0.00 bp (vs 2026-10-09) | 0.00 |  | fred:T10YIE |
| SOFR | 3.890 | 10-13 close | official value for 2026-10-13 (not live) | +2.00 bp (vs 2026-10-09) | 0.54 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.0s) |
| US dollar index (DXY) | 102.788 | 10-14 09:29 | **LIVE (~10 min old)** | +0.59 % (vs 2026-10-13) | 1.93 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.843 | 10-14 09:39 | **LIVE (~0 min old)** | +0.20 % (vs 2026-10-13) | 0.46 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.114 | 10-14 09:38 | **LIVE (~1 min old)** | -0.20 % (vs 2026-10-13) | -0.66 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.602 | 10-09 close | official value for 2026-10-09 (not live) | +0.13 % (vs 2026-10-08) | 0.46 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,826.250 | 10-14 09:29 | **LIVE (~10 min old)** | -0.38 % (vs 2026-10-13) | -0.71 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,547.500 | 10-14 09:29 | **LIVE (~10 min old)** | -0.79 % (vs 2026-10-13) | -0.96 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,766.200 | 10-14 09:29 | **LIVE (~10 min old)** | -1.21 % (vs 2026-10-13) | -1.66 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,780.950 | 10-14 09:39 | **LIVE (~0 min old)** | -0.31 % (vs 2026-10-13) | -0.55 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,348.246 | 10-14 09:39 | **LIVE (~0 min old)** | -0.72 % (vs 2026-10-13) | -0.78 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,783.369 | 10-13 16:30 | not trading now; last trade 10-13 16:30 ET | -0.40 % (vs 2026-10-12) | -0.54 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.860 | 10-14 09:24 | **LIVE (~15 min old)** | +0.59 pts (vs 2026-10-13) | 0.75 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.4s) |
| WTI crude | 95.360 | 10-14 09:29 | **LIVE (~10 min old)** | +1.30 % (vs 2026-10-13) | 0.53 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 105.700 | 10-14 09:29 | **LIVE (~10 min old)** | +0.01 % (vs 2026-10-13) | 0.00 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,111.600 | 10-14 09:29 | **LIVE (~10 min old)** | -1.57 % (vs 2026-10-13) | -1.36 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.695 | 10-14 09:29 | **LIVE (~10 min old)** | +0.25 % (vs 2026-10-13) | 0.20 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 82,895.48, 24h -0.32%, z -0.18
- kraken: funding (raw, units unverified) 1.4573627884945557, OI 2234.4407, OI change vs prior snapshot 2.44%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 38694.81988, OI change vs prior snapshot 0.57%

**ETH**: price 2,483.43, 24h -0.65%, z -0.28
- kraken: funding (raw, units unverified) 0.01854342299991749, OI 31335.316, OI change vs prior snapshot -1.38%
- hyperliquid: funding (raw, units unverified) -0.0000045616, OI 1074622.2184000006, OI change vs prior snapshot -0.39%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.4s)
