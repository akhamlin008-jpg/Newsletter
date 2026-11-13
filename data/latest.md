# Data snapshot 2026-11-13 10:39 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.86), crypto (max |z| 2.32)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.838 | 11-13 10:39 | **LIVE (~0 min old)** | -2.60 bp | -0.37 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.129 | 11-13 10:39 | **LIVE (~0 min old)** | +2.60 bp | 0.46 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.291 | 11-13 10:39 | **LIVE (~0 min old)** | +5.20 bp | 1.35 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.780 | 11-10 close | official value for 2026-11-10 (not live) | +12.00 bp (vs 2026-11-09) | 2.86 | **YES** | fred:DFII10 |
| 10-year breakeven inflation | 2.240 | 11-12 close | official value for 2026-11-12 (not live) | +4.00 bp (vs 2026-11-10) | 1.76 |  | fred:T10YIE |
| SOFR | 3.900 | 11-12 close | official value for 2026-11-12 (not live) | +1.00 bp (vs 2026-11-10) | 0.42 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.3s) |
| US dollar index (DXY) | 103.315 | 11-13 10:29 | **LIVE (~11 min old)** | +0.14 % (vs 2026-11-12) | 0.38 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.831 | 11-13 10:39 | **LIVE (~1 min old)** | +0.06 % (vs 2026-11-12) | 0.15 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.104 | 11-13 10:39 | **LIVE (~1 min old)** | -0.50 % (vs 2026-11-12) | -1.34 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,541.250 | 11-13 10:30 | **LIVE (~10 min old)** | -0.97 % (vs 2026-11-12) | -0.75 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,836.250 | 11-13 10:30 | **LIVE (~10 min old)** | -1.93 % (vs 2026-11-12) | -0.96 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,777.600 | 11-13 10:30 | **LIVE (~10 min old)** | -1.06 % (vs 2026-11-12) | -0.70 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,519.570 | 11-13 10:40 | **LIVE (~0 min old)** | -0.96 % (vs 2026-11-12) | -0.74 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,685.955 | 11-13 10:39 | **LIVE (~1 min old)** | -2.13 % (vs 2026-11-12) | -1.05 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,767.024 | 11-13 10:24 | **LIVE (~16 min old)** | -1.14 % (vs 2026-11-12) | -0.76 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 20.700 | 11-13 10:24 | **LIVE (~16 min old)** | +2.00 pts | 0.64 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.3s) |
| WTI crude | 89.280 | 11-13 10:30 | **LIVE (~10 min old)** | +0.61 % (vs 2026-11-12) | 0.19 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 96.630 | 11-13 10:30 | **LIVE (~10 min old)** | +0.85 % (vs 2026-11-12) | 0.23 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,880.600 | 11-13 10:30 | **LIVE (~10 min old)** | -0.12 % (vs 2026-11-12) | -0.08 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.114 | 11-13 10:30 | **LIVE (~10 min old)** | -1.11 % (vs 2026-11-12) | -0.78 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 68,151.20, 24h -4.84%, z -2.32 **FLAG**
- kraken: funding (raw, units unverified) 1.0997032697670603, OI 2530.6932, OI change vs prior snapshot -0.13%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 39837.01572, OI change vs prior snapshot -0.86%

**ETH**: price 1,915.02, 24h -4.54%, z -1.60
- kraken: funding (raw, units unverified) 0.02739826132125, OI 28965.279, OI change vs prior snapshot -1.40%
- hyperliquid: funding (raw, units unverified) 0.0000023127, OI 728531.3003999999, OI change vs prior snapshot -0.14%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.3s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.3s)
