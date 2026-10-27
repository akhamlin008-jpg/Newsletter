# Data snapshot 2026-10-27 10:22 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.42)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.741 | 10-27 10:22 | **LIVE (~0 min old)** | +3.00 bp | 0.49 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.003 | 10-27 10:22 | **LIVE (~0 min old)** | +1.70 bp | 0.28 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.262 | 10-27 10:22 | **LIVE (~0 min old)** | -1.30 bp | -0.41 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.660 | 10-23 close | official value for 2026-10-23 (not live) | +2.00 bp (vs 2026-10-22) | 0.38 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 10-26 close | official value for 2026-10-26 (not live) | +0.00 bp (vs 2026-10-23) | 0.00 |  | fred:T10YIE |
| SOFR | 3.930 | 10-26 close | official value for 2026-10-26 (not live) | +1.00 bp (vs 2026-10-23) | 0.34 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.2s) |
| US dollar index (DXY) | 102.177 | 10-27 10:12 | **LIVE (~10 min old)** | +0.21 % (vs 2026-10-26) | 0.75 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.896 | 10-27 10:22 | **LIVE (~0 min old)** | +0.68 % (vs 2026-10-26) | 1.55 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.115 | 10-27 10:21 | **LIVE (~1 min old)** | -0.60 % (vs 2026-10-26) | -2.42 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,720.250 | 10-27 10:12 | **LIVE (~10 min old)** | +0.07 % (vs 2026-10-26) | 0.12 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,527.250 | 10-27 10:12 | **LIVE (~10 min old)** | +0.31 % (vs 2026-10-26) | 0.26 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,804.600 | 10-27 10:12 | **LIVE (~10 min old)** | +0.25 % (vs 2026-10-26) | 0.29 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,682.150 | 10-27 10:22 | **LIVE (~0 min old)** | +0.07 % (vs 2026-10-26) | 0.11 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,370.479 | 10-27 10:22 | **LIVE (~0 min old)** | +0.33 % (vs 2026-10-26) | 0.27 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,792.179 | 10-27 10:07 | **LIVE (~15 min old)** | +0.21 % (vs 2026-10-26) | 0.24 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 18.010 | 10-27 10:06 | **LIVE (~16 min old)** | -0.38 pts | -0.31 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.5s) |
| WTI crude | 101.510 | 10-27 10:12 | **LIVE (~10 min old)** | -0.25 % (vs 2026-10-26) | -0.09 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 110.630 | 10-27 10:12 | **LIVE (~10 min old)** | -4.47 % (vs 2026-10-26) | -1.95 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,053.200 | 10-27 10:12 | **LIVE (~10 min old)** | +0.37 % (vs 2026-10-26) | 0.32 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.614 | 10-27 10:12 | **LIVE (~10 min old)** | +1.64 % (vs 2026-10-26) | 1.28 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 79,880.02, 24h -0.49%, z -0.32
- kraken: funding (raw, units unverified) 0.64900169411664, OI 2684.9629, OI change vs prior snapshot 0.34%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42993.38336, OI change vs prior snapshot -1.10%

**ETH**: price 2,317.04, 24h -0.26%, z -0.14
- kraken: funding (raw, units unverified) 0.021122372865125773, OI 32829.87, OI change vs prior snapshot -1.64%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1129088.0784000005, OI change vs prior snapshot 0.91%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.5s)
