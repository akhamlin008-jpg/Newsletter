# Data snapshot 2026-11-13 11:12 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.86)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.852 | 11-13 11:12 | **LIVE (~0 min old)** | -1.20 bp | -0.17 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.135 | 11-13 11:11 | **LIVE (~1 min old)** | +3.20 bp | 0.57 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.283 | 11-13 11:11 | **LIVE (~1 min old)** | +4.40 bp | 1.14 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.780 | 11-10 close | official value for 2026-11-10 (not live) | +12.00 bp (vs 2026-11-09) | 2.86 | **YES** | fred:DFII10 |
| 10-year breakeven inflation | 2.240 | 11-12 close | official value for 2026-11-12 (not live) | +4.00 bp (vs 2026-11-10) | 1.76 |  | fred:T10YIE |
| SOFR | 3.900 | 11-12 close | official value for 2026-11-12 (not live) | +1.00 bp (vs 2026-11-10) | 0.42 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.5s) |
| US dollar index (DXY) | 103.358 | 11-13 11:02 | **LIVE (~10 min old)** | +0.18 % (vs 2026-11-12) | 0.49 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.901 | 11-13 11:12 | **LIVE (~0 min old)** | +0.10 % (vs 2026-11-12) | 0.26 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.104 | 11-13 11:11 | **LIVE (~1 min old)** | -0.52 % (vs 2026-11-12) | -1.40 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,539.000 | 11-13 11:02 | **LIVE (~10 min old)** | -1.00 % (vs 2026-11-12) | -0.78 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,782.000 | 11-13 11:02 | **LIVE (~10 min old)** | -2.12 % (vs 2026-11-12) | -1.05 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,775.700 | 11-13 11:02 | **LIVE (~10 min old)** | -1.13 % (vs 2026-11-12) | -0.74 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,525.070 | 11-13 11:12 | **LIVE (~0 min old)** | -0.89 % (vs 2026-11-12) | -0.69 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,713.051 | 11-13 11:12 | **LIVE (~0 min old)** | -2.04 % (vs 2026-11-12) | -1.01 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,772.730 | 11-13 10:57 | **LIVE (~15 min old)** | -0.94 % (vs 2026-11-12) | -0.63 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 20.280 | 11-13 10:56 | **LIVE (~16 min old)** | +1.58 pts | 0.50 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.5s) |
| WTI crude | 88.920 | 11-13 11:02 | **LIVE (~10 min old)** | +0.20 % (vs 2026-11-12) | 0.06 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 96.250 | 11-13 11:02 | **LIVE (~10 min old)** | +0.45 % (vs 2026-11-12) | 0.12 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,875.000 | 11-13 11:02 | **LIVE (~10 min old)** | -0.27 % (vs 2026-11-12) | -0.17 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.109 | 11-13 11:02 | **LIVE (~10 min old)** | -1.19 % (vs 2026-11-12) | -0.83 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 68,695.08, 24h -4.17%, z -2.00
- kraken: funding (raw, units unverified) 1.350606349922523, OI 2522.1926, OI change vs prior snapshot -0.34%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 39387.4155, OI change vs prior snapshot -1.13%

**ETH**: price 1,933.28, 24h -3.60%, z -1.27
- kraken: funding (raw, units unverified) -0.008327457462, OI 28943.07, OI change vs prior snapshot -0.08%
- hyperliquid: funding (raw, units unverified) 0.0000069587, OI 726482.0554000002, OI change vs prior snapshot -0.28%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.5s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.5s)
