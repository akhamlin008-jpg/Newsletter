# Data snapshot 2026-10-27 09:07 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.28), commodities (max |z| 2.13)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.733 | 10-27 09:07 | **LIVE (~0 min old)** | +2.20 bp | 0.36 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.993 | 10-27 09:07 | **LIVE (~0 min old)** | +0.70 bp | 0.11 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.260 | 10-27 09:07 | **LIVE (~0 min old)** | -1.50 bp | -0.48 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.660 | 10-23 close | official value for 2026-10-23 (not live) | +2.00 bp (vs 2026-10-22) | 0.38 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 10-26 close | official value for 2026-10-26 (not live) | +0.00 bp (vs 2026-10-23) | 0.00 |  | fred:T10YIE |
| SOFR | 3.930 | 10-26 close | official value for 2026-10-26 (not live) | +1.00 bp (vs 2026-10-23) | 0.34 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.2s) |
| US dollar index (DXY) | 102.170 | 10-27 08:58 | **LIVE (~10 min old)** | +0.21 % (vs 2026-10-26) | 0.73 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.804 | 10-27 09:08 | **LIVE (~0 min old)** | +0.62 % (vs 2026-10-26) | 1.41 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.115 | 10-27 09:07 | **LIVE (~1 min old)** | -0.56 % (vs 2026-10-26) | -2.28 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,742.750 | 10-27 08:58 | **LIVE (~10 min old)** | +0.37 % (vs 2026-10-26) | 0.57 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,609.750 | 10-27 08:58 | **LIVE (~10 min old)** | +0.59 % (vs 2026-10-26) | 0.49 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,809.700 | 10-27 08:58 | **LIVE (~10 min old)** | +0.44 % (vs 2026-10-26) | 0.49 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,676.770 | 10-26 16:00 | not trading now; last trade 10-26 16:00 ET | +0.70 % (vs 2026-10-23) | 1.06 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,273.404 | 10-26 16:00 | not trading now; last trade 10-26 16:00 ET | +1.09 % (vs 2026-10-23) | 0.87 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,786.424 | 10-26 16:00 | not trading now; last trade 10-26 16:00 ET | +0.38 % (vs 2026-10-23) | 0.42 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.730 | 10-27 08:53 | **LIVE (~15 min old)** | -0.66 pts (vs 2026-10-26) | -0.53 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.7s) |
| WTI crude | 101.020 | 10-27 08:58 | **LIVE (~10 min old)** | -0.73 % (vs 2026-10-26) | -0.27 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 110.160 | 10-27 08:57 | **LIVE (~11 min old)** | -4.88 % (vs 2026-10-26) | -2.13 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,036.800 | 10-27 08:58 | **LIVE (~10 min old)** | -0.04 % (vs 2026-10-26) | -0.03 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.606 | 10-27 08:58 | **LIVE (~10 min old)** | +1.51 % (vs 2026-10-26) | 1.18 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open
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

**BTC**: price 80,077.57, 24h 0.64%, z 0.42
- kraken: funding (raw, units unverified) 1.630980409032, OI 2687.382, OI change vs prior snapshot -3.47%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 43270.4447600001, OI change vs prior snapshot 2.07%

**ETH**: price 2,325.68, 24h 1.17%, z 0.61
- kraken: funding (raw, units unverified) 0.054167604727999225, OI 33453.56, OI change vs prior snapshot 2.28%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1117813.9258000006, OI change vs prior snapshot 0.05%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.7s)
