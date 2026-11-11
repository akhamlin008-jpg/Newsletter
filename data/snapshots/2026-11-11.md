# Data snapshot 2026-11-11 10:34 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 4.69), dollar (max |z| 3.32)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.748 | 11-10 17:05 | not trading now; last trade 11-10 17:05 ET | +20.10 bp | 3.47 | **YES** | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.998 | 11-11 10:20 | **LIVE (~15 min old)** | +1.50 bp (vs 2026-11-10) | 0.25 |  | yahoo:^TNX (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.250 | 11-10 17:05 | not trading now; last trade 11-10 17:05 ET | -18.60 bp | -4.69 | **YES** | calc: yahoo:^TNX minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.660 | 11-09 close | official value for 2026-11-09 (not live) | +3.00 bp (vs 2026-11-06) | 0.70 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.200 | 11-10 close | official value for 2026-11-10 (not live) | -2.00 bp (vs 2026-11-09) | -0.87 |  | fred:T10YIE |
| SOFR | 3.880 | 11-09 close | official value for 2026-11-09 (not live) | -1.00 bp (vs 2026-11-06) | -0.40 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.4s) |
| US dollar index (DXY) | 102.867 | 11-11 10:25 | **LIVE (~10 min old)** | +0.62 % (vs 2026-11-10) | 1.76 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.773 | 11-11 10:34 | **LIVE (~1 min old)** | +1.13 % (vs 2026-11-10) | 2.96 | **YES** | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.110 | 11-11 10:34 | **LIVE (~1 min old)** | -1.11 % (vs 2026-11-10) | -3.32 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,604.500 | 11-11 10:25 | **LIVE (~10 min old)** | +0.80 % (vs 2026-11-10) | 0.60 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,300.750 | 11-11 10:25 | **LIVE (~10 min old)** | +1.67 % (vs 2026-11-10) | 0.81 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,841.200 | 11-11 10:25 | **LIVE (~10 min old)** | +0.43 % (vs 2026-11-10) | 0.28 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,587.740 | 11-11 10:35 | **LIVE (~0 min old)** | +0.89 % (vs 2026-11-10) | 0.67 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,269.885 | 11-11 10:35 | **LIVE (~0 min old)** | +1.91 % (vs 2026-11-10) | 0.92 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,836.088 | 11-11 10:20 | **LIVE (~15 min old)** | +0.52 % (vs 2026-11-10) | 0.34 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 18.140 | 11-11 10:19 | **LIVE (~16 min old)** | -1.32 pts | -0.40 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (4.7s) |
| WTI crude | 88.650 | 11-11 10:25 | **LIVE (~10 min old)** | +3.03 % (vs 2026-11-10) | 0.91 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 94.650 | 11-11 10:25 | **LIVE (~10 min old)** | +3.45 % (vs 2026-11-10) | 0.91 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,016.300 | 11-11 10:25 | **LIVE (~10 min old)** | -0.34 % (vs 2026-11-10) | -0.23 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.271 | 11-11 10:25 | **LIVE (~10 min old)** | +0.83 % (vs 2026-11-10) | 0.57 |  | yahoo:HG=F (unofficial feed) |

## Row notes

- **US 10-year yield**: live move vs prior close, scored against full-day volatility (approximate); fell back after: yahoo:10Y=F -> no prior close before the current session (13.0s)
- **2s10s spread (10Y minus 2Y)**: legs come from different sources; spread is approximate
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

**BTC**: price 73,842.12, 24h 0.97%, z 0.48
- kraken: funding (raw, units unverified) 0.836021733615375, OI 2610.0889, OI change vs prior snapshot -0.03%
- hyperliquid: funding (raw, units unverified) 0.000011041, OI 40610.10876, OI change vs prior snapshot -1.18%

**ETH**: price 2,066.12, 24h 2.20%, z 0.74
- kraken: funding (raw, units unverified) 0.03312942389258402, OI 29675.279, OI change vs prior snapshot -1.03%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 782037.6094, OI change vs prior snapshot 0.14%


## Source errors

- yahoo:10Y=F -> no prior close before the current session (13.0s)
- yahoo:SR3=F -> no prior close before the current session (9.4s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (4.7s)
