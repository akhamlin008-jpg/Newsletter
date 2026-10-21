# Data snapshot 2026-10-21 08:52 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.774 | 10-21 08:52 | **LIVE (~0 min old)** | -1.30 bp | -0.25 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.096 | 10-21 08:51 | **LIVE (~1 min old)** | -2.10 bp | -0.42 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.322 | 10-21 08:51 | **LIVE (~1 min old)** | -0.80 bp | -0.23 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.800 | 10-19 close | official value for 2026-10-19 (not live) | +6.00 bp (vs 2026-10-16) | 1.27 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-20 close | official value for 2026-10-20 (not live) | +0.00 bp (vs 2026-10-19) | 0.00 |  | fred:T10YIE |
| SOFR | 3.880 | 10-20 close | official value for 2026-10-20 (not live) | +1.00 bp (vs 2026-10-19) | 0.31 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.9s) |
| US dollar index (DXY) | 101.695 | 10-21 08:42 | **LIVE (~10 min old)** | -0.03 % (vs 2026-10-20) | -0.11 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.936 | 10-21 08:52 | **LIVE (~0 min old)** | -0.37 % (vs 2026-10-20) | -0.91 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.123 | 10-21 08:52 | **LIVE (~0 min old)** | +0.17 % (vs 2026-10-20) | 0.61 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.405 | 10-16 close | official value for 2026-10-16 (not live) | -0.14 % (vs 2026-10-15) | -0.48 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,777.500 | 10-21 08:42 | **LIVE (~10 min old)** | +0.29 % (vs 2026-10-20) | 0.49 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,852.750 | 10-21 08:42 | **LIVE (~10 min old)** | +0.60 % (vs 2026-10-20) | 0.57 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,796.400 | 10-21 08:42 | **LIVE (~10 min old)** | +0.34 % (vs 2026-10-20) | 0.35 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,712.570 | 10-20 16:45 | not trading now; last trade 10-20 16:45 ET | +0.28 % (vs 2026-10-19) | 0.45 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,490.283 | 10-20 17:16 | not trading now; last trade 10-20 17:16 ET | -0.13 % (vs 2026-10-19) | -0.12 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,773.420 | 10-20 16:30 | not trading now; last trade 10-20 16:30 ET | +1.65 % (vs 2026-10-19) | 1.79 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.190 | 10-21 08:37 | **LIVE (~15 min old)** | -0.12 pts (vs 2026-10-20) | -0.10 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.3s) |
| WTI crude | 97.750 | 10-21 08:42 | **LIVE (~10 min old)** | -3.97 % (vs 2026-10-20) | -1.61 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 108.520 | 10-21 08:42 | **LIVE (~10 min old)** | -0.25 % (vs 2026-10-20) | -0.11 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,146.300 | 10-21 08:42 | **LIVE (~10 min old)** | +0.09 % (vs 2026-10-20) | 0.08 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.546 | 10-21 08:42 | **LIVE (~10 min old)** | -0.30 % (vs 2026-10-20) | -0.26 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 83,397.52, 24h 2.33%, z 1.48
- kraken: funding (raw, units unverified) 1.571236792706, OI 2506.0034, OI change vs prior snapshot 5.18%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41364.40834, OI change vs prior snapshot 0.53%

**ETH**: price 2,466.18, 24h 3.05%, z 1.48
- kraken: funding (raw, units unverified) 0.06885542844583416, OI 27643.072, OI change vs prior snapshot -4.65%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1100324.0445999992, OI change vs prior snapshot 3.43%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.9s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.3s)
