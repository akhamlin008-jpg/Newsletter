# Data snapshot 2026-11-25 13:09 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.16)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.621 | 11-25 13:09 | **LIVE (~0 min old)** | -5.00 bp | -0.72 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.836 | 11-25 13:08 | **LIVE (~1 min old)** | -6.60 bp | -1.10 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.215 | 11-25 13:08 | **LIVE (~1 min old)** | -1.60 bp | -0.50 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.790 | 11-23 close | official value for 2026-11-23 (not live) | +2.00 bp (vs 2026-11-20) | 0.38 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.120 | 11-24 close | official value for 2026-11-24 (not live) | -1.00 bp (vs 2026-11-23) | -0.43 |  | fred:T10YIE |
| SOFR | 3.940 | 11-24 close | official value for 2026-11-24 (not live) | +2.00 bp (vs 2026-11-23) | 0.96 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.3s) |
| US dollar index (DXY) | 103.619 | 11-25 12:59 | **LIVE (~11 min old)** | -0.18 % (vs 2026-11-24) | -0.53 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.935 | 11-25 13:09 | **LIVE (~1 min old)** | -0.05 % (vs 2026-11-24) | -0.13 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.099 | 11-25 13:09 | **LIVE (~1 min old)** | +0.74 % (vs 2026-11-24) | 2.16 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 123.598 | 11-20 close | official value for 2026-11-20 (not live) | +0.06 % (vs 2026-11-19) | 0.23 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,138.250 | 11-25 12:59 | **LIVE (~11 min old)** | -1.10 % (vs 2026-11-24) | -0.60 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 25,700.000 | 11-25 12:59 | **LIVE (~11 min old)** | -2.19 % (vs 2026-11-24) | -0.80 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,685.500 | 11-25 12:59 | **LIVE (~11 min old)** | -0.14 % (vs 2026-11-24) | -0.08 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,128.900 | 11-25 13:09 | **LIVE (~1 min old)** | -1.00 % (vs 2026-11-24) | -0.54 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 25,677.822 | 11-25 13:09 | **LIVE (~1 min old)** | -2.05 % (vs 2026-11-24) | -0.74 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,682.547 | 11-25 12:54 | **LIVE (~16 min old)** | -0.09 % (vs 2026-11-24) | -0.05 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 29.550 | 11-25 12:54 | **LIVE (~16 min old)** | +3.19 pts (vs 2026-11-24) | 0.81 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.2s) |
| WTI crude | 83.560 | 11-25 13:00 | **LIVE (~10 min old)** | +1.84 % (vs 2026-11-24) | 0.62 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 90.250 | 11-25 13:00 | **LIVE (~10 min old)** | -1.26 % (vs 2026-11-24) | -0.40 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,541.800 | 11-25 13:00 | **LIVE (~10 min old)** | -0.56 % (vs 2026-11-24) | -0.27 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.423 | 11-25 13:00 | **LIVE (~10 min old)** | +1.13 % (vs 2026-11-24) | 0.51 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 59,677.04, 24h -0.21%, z -0.08
- kraken: funding (raw, units unverified) 1.0554802509078134, OI 2030.0098, OI change vs prior snapshot 1.37%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 35586.9914, OI change vs prior snapshot 0.01%

**ETH**: price 1,677.45, 24h 0.04%, z 0.01
- kraken: funding (raw, units unverified) -0.02399093522, OI 35744.894, OI change vs prior snapshot 0.03%
- hyperliquid: funding (raw, units unverified) 0.0000109167, OI 641640.3159999986, OI change vs prior snapshot -0.49%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.3s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.2s)
