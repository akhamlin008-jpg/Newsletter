# Data snapshot 2026-10-08 10:53 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.05)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.816 | 10-08 10:52 | **LIVE (~1 min old)** | +5.20 bp | 0.84 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.301 | 10-08 10:52 | **LIVE (~0 min old)** | +2.40 bp | 0.46 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.485 | 10-08 10:52 | **LIVE (~1 min old)** | -2.80 bp | -0.82 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.910 | 10-06 close | official value for 2026-10-06 (not live) | -4.00 bp (vs 2026-10-05) | -0.79 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 10-07 close | official value for 2026-10-07 (not live) | +0.00 bp (vs 2026-10-06) | 0.00 |  | fred:T10YIE |
| SOFR | 3.880 | 10-07 close | official value for 2026-10-07 (not live) | -2.00 bp (vs 2026-10-06) | -0.50 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.8s) |
| US dollar index (DXY) | 102.115 | 10-08 10:43 | **LIVE (~10 min old)** | -0.12 % (vs 2026-10-07) | -0.39 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.185 | 10-08 10:53 | **LIVE (~0 min old)** | -0.07 % (vs 2026-10-07) | -0.14 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.122 | 10-08 10:52 | **LIVE (~1 min old)** | -0.34 % (vs 2026-10-07) | -1.14 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.385 | 10-02 close | official value for 2026-10-02 (not live) | -0.33 % (vs 2026-10-01) | -1.17 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,837.750 | 10-08 10:43 | **LIVE (~10 min old)** | -0.19 % (vs 2026-10-07) | -0.34 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 31,294.500 | 10-08 10:43 | **LIVE (~10 min old)** | -0.34 % (vs 2026-10-07) | -0.41 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,792.700 | 10-08 10:43 | **LIVE (~10 min old)** | -0.69 % (vs 2026-10-07) | -0.86 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,779.740 | 10-08 10:53 | **LIVE (~0 min old)** | -0.28 % (vs 2026-10-07) | -0.46 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 31,026.232 | 10-08 10:53 | **LIVE (~0 min old)** | -0.43 % (vs 2026-10-07) | -0.45 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,777.416 | 10-08 10:38 | **LIVE (~15 min old)** | -0.57 % (vs 2026-10-07) | -0.72 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.280 | 10-08 10:37 | **LIVE (~16 min old)** | +0.20 pts | 0.23 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.8s) |
| WTI crude | 92.330 | 10-08 10:43 | **LIVE (~10 min old)** | +4.59 % (vs 2026-10-07) | 1.79 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 105.140 | 10-08 10:43 | **LIVE (~10 min old)** | +4.93 % (vs 2026-10-07) | 2.05 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,151.600 | 10-08 10:43 | **LIVE (~10 min old)** | +0.26 % (vs 2026-10-07) | 0.21 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.618 | 10-08 10:43 | **LIVE (~10 min old)** | +0.33 % (vs 2026-10-07) | 0.26 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 82,593.67, 24h -0.46%, z -0.23
- kraken: funding (raw, units unverified) 1.3911361257310142, OI 2502.8007, OI change vs prior snapshot -0.29%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41180.1816, OI change vs prior snapshot 0.70%

**ETH**: price 2,530.71, 24h -1.24%, z -0.53
- kraken: funding (raw, units unverified) 0.021172011103332493, OI 29975.945, OI change vs prior snapshot 0.50%
- hyperliquid: funding (raw, units unverified) 0.0000044347, OI 1150479.7856000008, OI change vs prior snapshot 0.06%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.8s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.8s)
