# Data snapshot 2026-10-15 08:50 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** equity (max |z| 2.69), rates (max |z| 2.59)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.757 | 10-15 08:50 | **LIVE (~0 min old)** | -4.50 bp | -0.80 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.064 | 10-15 08:50 | **LIVE (~0 min old)** | -12.60 bp | -2.59 | **YES** | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.307 | 10-15 08:50 | **LIVE (~0 min old)** | -8.10 bp | -2.33 | **YES** | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.880 | 10-13 close | official value for 2026-10-13 (not live) | -3.00 bp (vs 2026-10-09) | -0.62 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-14 close | official value for 2026-10-14 (not live) | +2.00 bp (vs 2026-10-13) | 1.25 |  | fred:T10YIE |
| SOFR | 3.880 | 10-14 close | official value for 2026-10-14 (not live) | -1.00 bp (vs 2026-10-13) | -0.28 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.0s) |
| US dollar index (DXY) | 102.074 | 10-15 08:40 | **LIVE (~10 min old)** | -0.46 % (vs 2026-10-14) | -1.49 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.924 | 10-15 08:50 | **LIVE (~0 min old)** | -0.25 % (vs 2026-10-14) | -0.58 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.121 | 10-15 08:49 | **LIVE (~1 min old)** | +0.01 % (vs 2026-10-14) | 0.04 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.602 | 10-09 close | official value for 2026-10-09 (not live) | +0.13 % (vs 2026-10-08) | 0.46 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,752.000 | 10-15 08:40 | **LIVE (~10 min old)** | -0.23 % (vs 2026-10-14) | -0.41 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,834.750 | 10-15 08:40 | **LIVE (~10 min old)** | -1.15 % (vs 2026-10-14) | -1.24 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,750.300 | 10-15 08:40 | **LIVE (~10 min old)** | +0.19 % (vs 2026-10-14) | 0.23 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,718.940 | 10-14 16:36 | not trading now; last trade 10-14 16:36 ET | -1.11 % (vs 2026-10-13) | -1.93 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,950.816 | 10-14 17:16 | not trading now; last trade 10-14 17:16 ET | -2.02 % (vs 2026-10-13) | -2.19 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,729.531 | 10-14 16:30 | not trading now; last trade 10-14 16:30 ET | -1.93 % (vs 2026-10-13) | -2.69 | **YES** | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.500 | 10-15 08:35 | **LIVE (~15 min old)** | +0.63 pts (vs 2026-10-14) | 0.73 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.7s) |
| WTI crude | 93.830 | 10-15 08:40 | **LIVE (~10 min old)** | -1.33 % (vs 2026-10-14) | -0.55 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 104.260 | 10-15 08:40 | **LIVE (~10 min old)** | -1.70 % (vs 2026-10-14) | -0.74 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,176.400 | 10-15 08:40 | **LIVE (~10 min old)** | +1.67 % (vs 2026-10-14) | 1.40 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.564 | 10-15 08:40 | **LIVE (~10 min old)** | -0.73 % (vs 2026-10-14) | -0.59 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 80,703.64, 24h -2.36%, z -1.29
- kraken: funding (raw, units unverified) 0.9346968817809853, OI 2410.4986, OI change vs prior snapshot -0.04%
- hyperliquid: funding (raw, units unverified) 0.0000088527, OI 39275.08938, OI change vs prior snapshot 0.62%

**ETH**: price 2,352.34, 24h -4.92%, z -2.04 **FLAG**
- kraken: funding (raw, units unverified) 0.013068411402999212, OI 30375.597, OI change vs prior snapshot -0.45%
- hyperliquid: funding (raw, units unverified) 0.0000065293, OI 1066421.2011999998, OI change vs prior snapshot 0.09%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.7s)
