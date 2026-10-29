# Data snapshot 2026-10-29 10:08 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.19)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.662 | 10-29 10:07 | **LIVE (~0 min old)** | -7.30 bp | -1.26 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.991 | 10-29 10:08 | **LIVE (~0 min old)** | -5.40 bp | -0.94 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.329 | 10-29 10:07 | **LIVE (~0 min old)** | +1.90 bp | 0.51 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.640 | 10-27 close | official value for 2026-10-27 (not live) | -2.00 bp (vs 2026-10-26) | -0.40 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.380 | 10-28 close | official value for 2026-10-28 (not live) | +3.00 bp (vs 2026-10-27) | 1.52 |  | fred:T10YIE |
| SOFR | 3.940 | 10-28 close | official value for 2026-10-28 (not live) | -1.00 bp (vs 2026-10-27) | -0.36 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.7s) |
| US dollar index (DXY) | 102.241 | 10-29 09:58 | **LIVE (~10 min old)** | +0.05 % (vs 2026-10-28) | 0.18 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.887 | 10-29 10:08 | **LIVE (~0 min old)** | -0.07 % (vs 2026-10-28) | -0.16 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.114 | 10-29 10:07 | **LIVE (~1 min old)** | +0.09 % (vs 2026-10-28) | 0.33 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,739.750 | 10-29 09:58 | **LIVE (~10 min old)** | -0.56 % (vs 2026-10-28) | -0.90 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,519.500 | 10-29 09:58 | **LIVE (~10 min old)** | -1.53 % (vs 2026-10-28) | -1.31 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,865.500 | 10-29 09:58 | **LIVE (~10 min old)** | +0.92 % (vs 2026-10-28) | 1.04 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,720.710 | 10-29 10:08 | **LIVE (~0 min old)** | -0.30 % (vs 2026-10-28) | -0.47 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,451.098 | 10-29 10:08 | **LIVE (~0 min old)** | -1.21 % (vs 2026-10-28) | -1.00 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,857.850 | 10-29 09:53 | **LIVE (~15 min old)** | +0.97 % (vs 2026-10-28) | 1.10 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.120 | 10-29 09:52 | **LIVE (~16 min old)** | +0.21 pts | 0.18 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.0s) |
| WTI crude | 100.460 | 10-29 09:58 | **LIVE (~10 min old)** | -2.26 % (vs 2026-10-28) | -0.86 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 109.740 | 10-29 09:58 | **LIVE (~10 min old)** | -4.84 % (vs 2026-10-28) | -2.19 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,033.300 | 10-29 09:58 | **LIVE (~10 min old)** | -0.45 % (vs 2026-10-28) | -0.40 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.554 | 10-29 09:58 | **LIVE (~10 min old)** | -1.32 % (vs 2026-10-28) | -1.03 |  | yahoo:HG=F (unofficial feed) |

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
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 80,226.03, 24h -0.32%, z -0.22
- kraken: funding (raw, units unverified) 0.52344273058564, OI 2477.6317, OI change vs prior snapshot -1.04%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 43531.2152, OI change vs prior snapshot 0.84%

**ETH**: price 2,324.22, 24h -0.25%, z -0.14
- kraken: funding (raw, units unverified) -0.01293087684579244, OI 32245.672, OI change vs prior snapshot 1.04%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1131918.2850000004, OI change vs prior snapshot -0.49%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.7s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.0s)
