# Data snapshot 2026-10-22 08:55 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.24)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.729 | 10-22 08:54 | **LIVE (~1 min old)** | -9.40 bp | -1.83 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.036 | 10-22 08:55 | **LIVE (~0 min old)** | -11.00 bp | -2.24 | **YES** | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.307 | 10-22 08:54 | **LIVE (~1 min old)** | -1.60 bp | -0.47 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.770 | 10-20 close | official value for 2026-10-20 (not live) | -3.00 bp (vs 2026-10-19) | -0.62 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.370 | 10-21 close | official value for 2026-10-21 (not live) | +2.00 bp (vs 2026-10-20) | 1.16 |  | fred:T10YIE |
| SOFR | 3.880 | 10-21 close | official value for 2026-10-21 (not live) | +0.00 bp (vs 2026-10-20) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.8s) |
| US dollar index (DXY) | 101.793 | 10-22 08:45 | **LIVE (~10 min old)** | +0.01 % (vs 2026-10-21) | 0.04 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.096 | 10-22 08:55 | **LIVE (~0 min old)** | -0.74 % (vs 2026-10-21) | -1.88 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.121 | 10-22 08:54 | **LIVE (~1 min old)** | -0.18 % (vs 2026-10-21) | -0.66 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.405 | 10-16 close | official value for 2026-10-16 (not live) | -0.14 % (vs 2026-10-15) | -0.48 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,727.500 | 10-22 08:45 | **LIVE (~10 min old)** | -0.93 % (vs 2026-10-21) | -1.60 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,530.000 | 10-22 08:45 | **LIVE (~10 min old)** | -1.59 % (vs 2026-10-21) | -1.52 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,778.000 | 10-22 08:45 | **LIVE (~10 min old)** | -0.58 % (vs 2026-10-21) | -0.61 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,757.170 | 10-21 16:00 | not trading now; last trade 10-21 16:00 ET | +0.58 % (vs 2026-10-20) | 0.93 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,822.518 | 10-21 16:00 | not trading now; last trade 10-21 16:00 ET | +1.13 % (vs 2026-10-20) | 1.02 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,781.021 | 10-21 16:00 | not trading now; last trade 10-21 16:00 ET | +0.27 % (vs 2026-10-20) | 0.28 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.980 | 10-22 08:40 | **LIVE (~15 min old)** | +1.30 pts (vs 2026-10-21) | 1.10 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.1s) |
| WTI crude | 99.360 | 10-22 08:45 | **LIVE (~10 min old)** | +2.27 % (vs 2026-10-21) | 0.86 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 111.790 | 10-22 08:45 | **LIVE (~10 min old)** | +2.73 % (vs 2026-10-21) | 1.28 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,096.400 | 10-22 08:45 | **LIVE (~10 min old)** | -1.29 % (vs 2026-10-21) | -1.19 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.420 | 10-22 08:45 | **LIVE (~10 min old)** | -1.88 % (vs 2026-10-21) | -1.68 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 81,613.88, 24h -2.14%, z -1.37
- kraken: funding (raw, units unverified) -0.019248811573360555, OI 2428.2248, OI change vs prior snapshot -3.16%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41936.96418, OI change vs prior snapshot 1.24%

**ETH**: price 2,399.54, 24h -2.69%, z -1.33
- kraken: funding (raw, units unverified) -0.002164517896, OI 27233.297, OI change vs prior snapshot -1.96%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1100305.3701999998, OI change vs prior snapshot -0.05%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.8s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.1s)
