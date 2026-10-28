# Data snapshot 2026-10-28 11:03 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.776 | 10-28 11:03 | **LIVE (~0 min old)** | +3.90 bp | 0.66 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.032 | 10-28 11:03 | **LIVE (~0 min old)** | +3.90 bp | 0.66 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.256 | 10-28 11:03 | **LIVE (~0 min old)** | +0.00 bp | 0.00 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.660 | 10-26 close | official value for 2026-10-26 (not live) | +0.00 bp (vs 2026-10-23) | 0.00 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-27 close | official value for 2026-10-27 (not live) | +1.00 bp (vs 2026-10-26) | 0.50 |  | fred:T10YIE |
| SOFR | 3.950 | 10-27 close | official value for 2026-10-27 (not live) | +2.00 bp (vs 2026-10-26) | 0.70 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (12.4s) |
| US dollar index (DXY) | 102.360 | 10-28 10:53 | **LIVE (~11 min old)** | +0.04 % (vs 2026-10-27) | 0.14 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.214 | 10-28 11:03 | **LIVE (~1 min old)** | +0.44 % (vs 2026-10-27) | 0.99 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.114 | 10-28 11:03 | **LIVE (~1 min old)** | -0.32 % (vs 2026-10-27) | -1.23 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,763.250 | 10-28 10:53 | **LIVE (~11 min old)** | +0.06 % (vs 2026-10-27) | 0.10 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,814.000 | 10-28 10:53 | **LIVE (~11 min old)** | +0.01 % (vs 2026-10-27) | 0.01 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,825.600 | 10-28 10:53 | **LIVE (~11 min old)** | -0.10 % (vs 2026-10-27) | -0.11 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,732.260 | 10-28 11:03 | **LIVE (~1 min old)** | +0.13 % (vs 2026-10-27) | 0.19 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,683.008 | 10-28 11:03 | **LIVE (~1 min old)** | +0.11 % (vs 2026-10-27) | 0.09 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,819.944 | 10-28 10:48 | **LIVE (~16 min old)** | +0.04 % (vs 2026-10-27) | 0.04 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.350 | 10-28 10:48 | **LIVE (~15 min old)** | -0.17 pts | -0.14 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.1s) |
| WTI crude | 102.620 | 10-28 10:53 | **LIVE (~11 min old)** | +2.72 % (vs 2026-10-27) | 1.04 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 111.880 | 10-28 10:54 | **LIVE (~10 min old)** | -1.76 % (vs 2026-10-27) | -0.78 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,054.400 | 10-28 10:54 | **LIVE (~10 min old)** | -0.50 % (vs 2026-10-27) | -0.43 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.652 | 10-28 10:54 | **LIVE (~10 min old)** | +0.45 % (vs 2026-10-27) | 0.34 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 80,565.52, 24h 0.16%, z 0.11
- kraken: funding (raw, units unverified) 1.28775154528664, OI 2503.7615, OI change vs prior snapshot -0.03%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 43166.59572, OI change vs prior snapshot 0.73%

**ETH**: price 2,333.25, 24h -0.42%, z -0.22
- kraken: funding (raw, units unverified) 0.023519541767875, OI 31913.748, OI change vs prior snapshot 0.57%
- hyperliquid: funding (raw, units unverified) 0.0000078825, OI 1137476.1612000002, OI change vs prior snapshot 0.96%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (12.4s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (10.1s)
