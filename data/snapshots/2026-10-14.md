# Data snapshot 2026-10-14 09:03 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.6)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.944 | 10-14 09:03 | **LIVE (~0 min old)** | +15.10 bp | 2.60 | **YES** | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.319 | 10-14 09:03 | **LIVE (~0 min old)** | +10.20 bp | 2.06 | **YES** | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.375 | 10-14 09:03 | **LIVE (~0 min old)** | -4.90 bp | -1.46 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.910 | 10-09 close | official value for 2026-10-09 (not live) | +4.00 bp (vs 2026-10-08) | 0.82 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 10-13 close | official value for 2026-10-13 (not live) | +0.00 bp (vs 2026-10-09) | 0.00 |  | fred:T10YIE |
| SOFR | 3.890 | 10-13 close | official value for 2026-10-13 (not live) | +2.00 bp (vs 2026-10-09) | 0.54 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.8s) |
| US dollar index (DXY) | 102.672 | 10-14 08:53 | **LIVE (~11 min old)** | +0.48 % (vs 2026-10-13) | 1.56 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.860 | 10-14 09:03 | **LIVE (~1 min old)** | +0.21 % (vs 2026-10-13) | 0.48 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.112 | 10-14 09:03 | **LIVE (~1 min old)** | -0.34 % (vs 2026-10-13) | -1.14 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.602 | 10-09 close | official value for 2026-10-09 (not live) | +0.13 % (vs 2026-10-08) | 0.46 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,831.250 | 10-14 08:53 | **LIVE (~11 min old)** | -0.31 % (vs 2026-10-13) | -0.59 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,600.750 | 10-14 08:53 | **LIVE (~11 min old)** | -0.62 % (vs 2026-10-13) | -0.75 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,768.100 | 10-14 08:53 | **LIVE (~11 min old)** | -1.14 % (vs 2026-10-13) | -1.57 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,805.450 | 10-13 16:33 | not trading now; last trade 10-13 16:33 ET | -0.02 % (vs 2026-10-12) | -0.04 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,569.480 | 10-13 17:16 | not trading now; last trade 10-13 17:16 ET | -0.31 % (vs 2026-10-12) | -0.33 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,783.369 | 10-13 16:30 | not trading now; last trade 10-13 16:30 ET | -0.40 % (vs 2026-10-12) | -0.54 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.760 | 10-14 08:48 | **LIVE (~16 min old)** | +0.49 pts (vs 2026-10-13) | 0.62 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s) |
| WTI crude | 95.670 | 10-14 08:53 | **LIVE (~11 min old)** | +1.63 % (vs 2026-10-13) | 0.66 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 105.830 | 10-14 08:53 | **LIVE (~11 min old)** | +0.13 % (vs 2026-10-13) | 0.06 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,124.600 | 10-14 08:53 | **LIVE (~11 min old)** | -1.26 % (vs 2026-10-13) | -1.09 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.734 | 10-14 08:53 | **LIVE (~11 min old)** | +0.84 % (vs 2026-10-13) | 0.67 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 82,711.82, 24h -0.54%, z -0.30
- kraken: funding (raw, units unverified) 1.4573627884945557, OI 2181.3152, OI change vs prior snapshot -1.07%
- hyperliquid: funding (raw, units unverified) 0.0000115452, OI 38477.2855400001, OI change vs prior snapshot 0.13%

**ETH**: price 2,475.27, 24h -0.98%, z -0.41
- kraken: funding (raw, units unverified) 0.01854342299991749, OI 31774.545, OI change vs prior snapshot -0.42%
- hyperliquid: funding (raw, units unverified) -0.0000039586, OI 1078847.2214000009, OI change vs prior snapshot 0.01%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.8s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s)
