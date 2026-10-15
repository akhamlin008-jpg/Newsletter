# Data snapshot 2026-10-15 08:36 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** equity (max |z| 2.69), rates (max |z| 2.32)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.766 | 10-15 08:36 | **LIVE (~0 min old)** | -3.60 bp | -0.64 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.077 | 10-15 08:36 | **LIVE (~0 min old)** | -11.30 bp | -2.32 | **YES** | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.311 | 10-15 08:36 | **LIVE (~0 min old)** | -7.70 bp | -2.21 | **YES** | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.880 | 10-13 close | official value for 2026-10-13 (not live) | -3.00 bp (vs 2026-10-09) | -0.62 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-14 close | official value for 2026-10-14 (not live) | +2.00 bp (vs 2026-10-13) | 1.25 |  | fred:T10YIE |
| SOFR | 3.880 | 10-14 close | official value for 2026-10-14 (not live) | -1.00 bp (vs 2026-10-13) | -0.28 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.8s) |
| US dollar index (DXY) | 102.135 | 10-15 08:27 | **LIVE (~10 min old)** | -0.40 % (vs 2026-10-14) | -1.30 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.992 | 10-15 08:37 | **LIVE (~0 min old)** | -0.21 % (vs 2026-10-14) | -0.48 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.120 | 10-15 08:36 | **LIVE (~1 min old)** | -0.02 % (vs 2026-10-14) | -0.07 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.602 | 10-09 close | official value for 2026-10-09 (not live) | +0.13 % (vs 2026-10-08) | 0.46 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,751.250 | 10-15 08:27 | **LIVE (~10 min old)** | -0.24 % (vs 2026-10-14) | -0.42 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,840.500 | 10-15 08:27 | **LIVE (~10 min old)** | -1.13 % (vs 2026-10-14) | -1.22 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,753.200 | 10-15 08:27 | **LIVE (~10 min old)** | +0.30 % (vs 2026-10-14) | 0.35 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,718.940 | 10-14 16:36 | not trading now; last trade 10-14 16:36 ET | -1.11 % (vs 2026-10-13) | -1.93 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,950.816 | 10-14 17:16 | not trading now; last trade 10-14 17:16 ET | -2.02 % (vs 2026-10-13) | -2.19 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,729.531 | 10-14 16:30 | not trading now; last trade 10-14 16:30 ET | -1.93 % (vs 2026-10-13) | -2.69 | **YES** | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.510 | 10-15 08:22 | **LIVE (~15 min old)** | +0.64 pts (vs 2026-10-14) | 0.74 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.2s) |
| WTI crude | 93.780 | 10-15 08:27 | **LIVE (~10 min old)** | -1.38 % (vs 2026-10-14) | -0.58 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 104.350 | 10-15 08:27 | **LIVE (~10 min old)** | -1.61 % (vs 2026-10-14) | -0.70 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,170.600 | 10-15 08:27 | **LIVE (~10 min old)** | +1.53 % (vs 2026-10-14) | 1.28 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.568 | 10-15 08:27 | **LIVE (~10 min old)** | -0.66 % (vs 2026-10-14) | -0.53 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 80,727.04, 24h -2.33%, z -1.28
- kraken: funding (raw, units unverified) 0.9346968817809853, OI 2411.4067, OI change vs prior snapshot 7.92%
- hyperliquid: funding (raw, units unverified) 0.0000082066, OI 39033.55194, OI change vs prior snapshot 0.88%

**ETH**: price 2,351.85, 24h -4.94%, z -2.05 **FLAG**
- kraken: funding (raw, units unverified) 0.013068411402999212, OI 30512.637, OI change vs prior snapshot -2.63%
- hyperliquid: funding (raw, units unverified) 0.0000081408, OI 1065423.3241999997, OI change vs prior snapshot -0.86%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.8s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.2s)
