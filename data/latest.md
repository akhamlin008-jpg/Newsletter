# Data snapshot 2026-11-27 13:07 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.37)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.704 | 11-27 13:06 | **LIVE (~0 min old)** | +6.90 bp | 1.02 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.932 | 11-27 13:06 | **LIVE (~0 min old)** | +8.40 bp | 1.45 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.228 | 11-27 13:06 | **LIVE (~0 min old)** | +1.50 bp | 0.46 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.790 | 11-24 close | official value for 2026-11-24 (not live) | +0.00 bp (vs 2026-11-23) | 0.00 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.120 | 11-25 close | official value for 2026-11-25 (not live) | +0.00 bp (vs 2026-11-24) | 0.00 |  | fred:T10YIE |
| SOFR | 3.950 | 11-25 close | official value for 2026-11-25 (not live) | +1.00 bp (vs 2026-11-24) | 0.49 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.4s) |
| US dollar index (DXY) | 104.016 | 11-27 12:56 | **LIVE (~11 min old)** | +0.33 % (vs 2026-11-25) | 0.98 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.506 | 11-27 13:07 | **LIVE (~0 min old)** | +0.18 % (vs 2026-11-26) | 0.56 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.094 | 11-27 13:06 | **LIVE (~1 min old)** | -0.29 % (vs 2026-11-26) | -0.84 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 123.598 | 11-20 close | official value for 2026-11-20 (not live) | +0.06 % (vs 2026-11-19) | 0.23 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,302.250 | 11-27 13:00 | **LIVE (~7 min old)** | +1.48 % (vs 2026-11-25) | 0.84 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 26,779.000 | 11-27 13:00 | **LIVE (~7 min old)** | +2.60 % (vs 2026-11-25) | 0.98 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,748.200 | 11-27 13:00 | **LIVE (~7 min old)** | +1.56 % (vs 2026-11-25) | 0.93 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,298.180 | 11-27 13:00 | **LIVE (~7 min old)** | +1.61 % (vs 2026-11-25) | 0.89 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 26,726.389 | 11-27 13:00 | **LIVE (~7 min old)** | +2.61 % (vs 2026-11-25) | 0.97 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,737.753 | 11-27 12:51 | **LIVE (~16 min old)** | +1.25 % (vs 2026-11-25) | 0.75 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 24.700 | 11-27 12:52 | **LIVE (~15 min old)** | -2.10 pts (vs 2026-11-26) | -0.56 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s) |
| WTI crude | 82.850 | 11-27 13:00 | **LIVE (~7 min old)** | -0.99 % (vs 2026-11-25) | -0.34 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 90.150 | 11-27 13:00 | **LIVE (~7 min old)** | -4.71 % (vs 2026-11-25) | -1.49 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,673.100 | 11-27 13:00 | **LIVE (~7 min old)** | +3.88 % (vs 2026-11-25) | 1.89 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.604 | 11-27 13:00 | **LIVE (~7 min old)** | +5.08 % (vs 2026-11-25) | 2.37 | **YES** | yahoo:HG=F (unofficial feed) |

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
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate); fell back after: cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.2s)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 59,806.93, 24h -0.98%, z -0.41
- kraken: funding (raw, units unverified) 0.12758873987475, OI 2061.2747, OI change vs prior snapshot -0.14%
- hyperliquid: funding (raw, units unverified) 0.0000058258, OI 35653.80088, OI change vs prior snapshot -1.91%

**ETH**: price 1,669.08, 24h -1.69%, z -0.53
- kraken: funding (raw, units unverified) -0.004767535340749443, OI 33976.469, OI change vs prior snapshot -0.29%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 601391.115, OI change vs prior snapshot 0.43%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.4s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s)
