# Data snapshot 2026-10-22 09:43 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.19)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.729 | 10-22 09:43 | **LIVE (~0 min old)** | -9.40 bp | -1.83 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.038 | 10-22 09:43 | **LIVE (~0 min old)** | -10.80 bp | -2.19 | **YES** | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.309 | 10-22 09:43 | **LIVE (~0 min old)** | -1.40 bp | -0.41 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.770 | 10-20 close | official value for 2026-10-20 (not live) | -3.00 bp (vs 2026-10-19) | -0.62 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.370 | 10-21 close | official value for 2026-10-21 (not live) | +2.00 bp (vs 2026-10-20) | 1.16 |  | fred:T10YIE |
| SOFR | 3.880 | 10-21 close | official value for 2026-10-21 (not live) | +0.00 bp (vs 2026-10-20) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.1s) |
| US dollar index (DXY) | 101.830 | 10-22 09:33 | **LIVE (~11 min old)** | +0.05 % (vs 2026-10-21) | 0.16 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.272 | 10-22 09:43 | **LIVE (~1 min old)** | -0.63 % (vs 2026-10-21) | -1.60 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.120 | 10-22 09:43 | **LIVE (~1 min old)** | -0.21 % (vs 2026-10-21) | -0.78 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.405 | 10-16 close | official value for 2026-10-16 (not live) | -0.14 % (vs 2026-10-15) | -0.48 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,732.750 | 10-22 09:33 | **LIVE (~11 min old)** | -0.87 % (vs 2026-10-21) | -1.48 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,509.750 | 10-22 09:33 | **LIVE (~11 min old)** | -1.66 % (vs 2026-10-21) | -1.59 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,786.200 | 10-22 09:33 | **LIVE (~11 min old)** | -0.29 % (vs 2026-10-21) | -0.30 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,692.450 | 10-22 09:43 | **LIVE (~1 min old)** | -0.83 % (vs 2026-10-21) | -1.35 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,340.330 | 10-22 09:43 | **LIVE (~1 min old)** | -1.62 % (vs 2026-10-21) | -1.46 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,781.021 | 10-21 16:00 | not trading now; last trade 10-21 16:00 ET | +0.27 % (vs 2026-10-20) | 0.28 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 18.080 | 10-22 09:25 | **LIVE (~19 min old)** | +1.40 pts (vs 2026-10-21) | 1.19 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.6s) |
| WTI crude | 99.950 | 10-22 09:33 | **LIVE (~11 min old)** | +2.88 % (vs 2026-10-21) | 1.09 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 112.450 | 10-22 09:33 | **LIVE (~11 min old)** | +3.34 % (vs 2026-10-21) | 1.56 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,088.500 | 10-22 09:33 | **LIVE (~11 min old)** | -1.48 % (vs 2026-10-21) | -1.37 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.439 | 10-22 09:33 | **LIVE (~11 min old)** | -1.59 % (vs 2026-10-21) | -1.42 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 81,598.97, 24h -2.55%, z -1.63
- kraken: funding (raw, units unverified) 0.4241451009591939, OI 2427.8563, OI change vs prior snapshot 0.31%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 43042.33456, OI change vs prior snapshot 2.39%

**ETH**: price 2,403.64, 24h -2.70%, z -1.34
- kraken: funding (raw, units unverified) 0.004746154182, OI 27400.89, OI change vs prior snapshot 0.67%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1097168.0978000001, OI change vs prior snapshot -0.02%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.6s)
