# Data snapshot 2026-10-16 08:17 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** crypto (max |z| 2.09)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.751 | 10-16 08:17 | **LIVE (~0 min old)** | +0.00 bp | 0.00 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.115 | 10-16 08:17 | **LIVE (~0 min old)** | +2.80 bp | 0.59 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.364 | 10-16 08:17 | **LIVE (~0 min old)** | +2.80 bp | 0.80 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.840 | 10-14 close | official value for 2026-10-14 (not live) | -4.00 bp (vs 2026-10-13) | -0.85 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.320 | 10-15 close | official value for 2026-10-15 (not live) | -3.00 bp (vs 2026-10-14) | -1.85 |  | fred:T10YIE |
| SOFR | 3.890 | 10-15 close | official value for 2026-10-15 (not live) | +1.00 bp (vs 2026-10-14) | 0.29 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.7s) |
| US dollar index (DXY) | 101.690 | 10-16 08:07 | **LIVE (~10 min old)** | -0.30 % (vs 2026-10-15) | -0.92 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.992 | 10-16 08:17 | **LIVE (~0 min old)** | +0.02 % (vs 2026-10-15) | 0.05 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.125 | 10-16 08:17 | **LIVE (~0 min old)** | +0.51 % (vs 2026-10-15) | 1.73 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.602 | 10-09 close | official value for 2026-10-09 (not live) | +0.13 % (vs 2026-10-08) | 0.46 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,802.000 | 10-16 08:07 | **LIVE (~10 min old)** | +0.14 % (vs 2026-10-15) | 0.25 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,115.250 | 10-16 08:07 | **LIVE (~10 min old)** | -0.09 % (vs 2026-10-15) | -0.10 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,786.400 | 10-16 08:07 | **LIVE (~10 min old)** | +0.17 % (vs 2026-10-15) | 0.19 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,744.060 | 10-15 16:33 | not trading now; last trade 10-15 16:33 ET | +0.33 % (vs 2026-10-14) | 0.52 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,935.594 | 10-15 17:16 | not trading now; last trade 10-15 17:16 ET | -0.05 % (vs 2026-10-14) | -0.05 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,767.269 | 10-15 16:30 | not trading now; last trade 10-15 16:30 ET | +1.38 % (vs 2026-10-14) | 1.64 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 16.050 | 10-16 08:02 | **LIVE (~15 min old)** | -0.41 pts (vs 2026-10-15) | -0.49 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.8s) |
| WTI crude | 96.400 | 10-16 08:07 | **LIVE (~10 min old)** | -1.60 % (vs 2026-10-15) | -0.66 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 106.170 | 10-16 08:07 | **LIVE (~10 min old)** | +0.24 % (vs 2026-10-15) | 0.11 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,196.400 | 10-16 08:07 | **LIVE (~10 min old)** | +0.63 % (vs 2026-10-15) | 0.52 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.646 | 10-16 08:07 | **LIVE (~10 min old)** | +2.07 % (vs 2026-10-15) | 1.64 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 82,115.23, 24h 2.08%, z 1.17
- kraken: funding (raw, units unverified) 2.0285177186093892, OI 2261.3146, OI change vs prior snapshot -5.64%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41874.17594, OI change vs prior snapshot 6.99%

**ETH**: price 2,461.96, 24h 4.90%, z 2.09 **FLAG**
- kraken: funding (raw, units unverified) 0.02783860745604249, OI 27548.807, OI change vs prior snapshot -6.77%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1089910.0450000002, OI change vs prior snapshot 2.55%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.7s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.8s)
