# Data snapshot 2026-11-12 10:55 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.68), commodities (max |z| 2.14)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.839 | 11-12 10:55 | **LIVE (~0 min old)** | +11.20 bp | 1.94 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.068 | 11-12 10:55 | **LIVE (~0 min old)** | +7.90 bp | 1.50 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.229 | 11-12 10:55 | **LIVE (~0 min old)** | -3.30 bp | -0.83 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.660 | 11-09 close | official value for 2026-11-09 (not live) | +3.00 bp (vs 2026-11-06) | 0.70 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.200 | 11-10 close | official value for 2026-11-10 (not live) | -2.00 bp (vs 2026-11-09) | -0.87 |  | fred:T10YIE |
| SOFR | 3.890 | 11-10 close | official value for 2026-11-10 (not live) | +1.00 bp (vs 2026-11-09) | 0.41 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.3s) |
| US dollar index (DXY) | 103.170 | 11-12 10:45 | **LIVE (~11 min old)** | +0.25 % (vs 2026-11-11) | 0.66 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.894 | 11-12 10:55 | **LIVE (~1 min old)** | +0.75 % (vs 2026-11-11) | 1.93 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.107 | 11-12 10:55 | **LIVE (~1 min old)** | -0.93 % (vs 2026-11-11) | -2.68 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,628.750 | 11-12 10:45 | **LIVE (~11 min old)** | -0.15 % (vs 2026-11-11) | -0.12 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,358.250 | 11-12 10:45 | **LIVE (~11 min old)** | -0.40 % (vs 2026-11-11) | -0.19 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,827.900 | 11-12 10:45 | **LIVE (~11 min old)** | -0.90 % (vs 2026-11-11) | -0.60 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,615.740 | 11-12 10:55 | **LIVE (~1 min old)** | -0.05 % (vs 2026-11-11) | -0.04 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,336.891 | 11-12 10:55 | **LIVE (~1 min old)** | -0.13 % (vs 2026-11-11) | -0.06 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,813.131 | 11-12 10:40 | **LIVE (~16 min old)** | -1.16 % (vs 2026-11-11) | -0.78 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 18.120 | 11-12 10:39 | **LIVE (~16 min old)** | +0.63 pts | 0.20 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.1s) |
| WTI crude | 86.460 | 11-12 10:45 | **LIVE (~11 min old)** | -0.08 % (vs 2026-11-11) | -0.02 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 93.380 | 11-12 10:45 | **LIVE (~11 min old)** | +0.67 % (vs 2026-11-11) | 0.18 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,875.300 | 11-12 10:45 | **LIVE (~11 min old)** | -3.13 % (vs 2026-11-11) | -2.14 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.170 | 11-12 10:45 | **LIVE (~11 min old)** | -1.67 % (vs 2026-11-11) | -1.17 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 71,451.92, 24h -3.33%, z -1.69
- kraken: funding (raw, units unverified) 0.6324435119306905, OI 2617.5083, OI change vs prior snapshot 0.13%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 38895.28832, OI change vs prior snapshot -3.95%

**ETH**: price 2,003.17, 24h -3.36%, z -1.16
- kraken: funding (raw, units unverified) -0.01203117477975, OI 29602.594, OI change vs prior snapshot -1.11%
- hyperliquid: funding (raw, units unverified) 0.0000099209, OI 750706.3054000001, OI change vs prior snapshot -3.57%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.3s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.1s)
