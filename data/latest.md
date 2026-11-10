# Data snapshot 2026-11-10 11:23 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 3.52), dollar (max |z| 2.02)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.752 | 11-10 11:22 | **LIVE (~1 min old)** | +20.50 bp | 3.52 | **YES** | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.998 | 11-10 11:21 | **LIVE (~2 min old)** | +13.60 bp | 2.52 | **YES** | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.246 | 11-10 11:21 | **LIVE (~2 min old)** | -6.90 bp | -1.87 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.630 | 11-06 close | official value for 2026-11-06 (not live) | +3.00 bp (vs 2026-11-05) | 0.69 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.220 | 11-09 close | official value for 2026-11-09 (not live) | -1.00 bp (vs 2026-11-06) | -0.43 |  | fred:T10YIE |
| SOFR | 3.880 | 11-09 close | official value for 2026-11-09 (not live) | -1.00 bp (vs 2026-11-06) | -0.40 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.1s) |
| US dollar index (DXY) | 102.338 | 11-10 11:13 | **LIVE (~10 min old)** | +0.68 % (vs 2026-11-09) | 2.02 | **YES** | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.787 | 11-10 11:23 | **LIVE (~0 min old)** | +0.31 % (vs 2026-11-09) | 0.80 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.116 | 11-10 11:22 | **LIVE (~1 min old)** | +0.08 % (vs 2026-11-09) | 0.25 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,521.000 | 11-10 11:13 | **LIVE (~10 min old)** | -0.70 % (vs 2026-11-09) | -0.51 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,804.500 | 11-10 11:13 | **LIVE (~10 min old)** | -0.75 % (vs 2026-11-09) | -0.35 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,811.000 | 11-10 11:13 | **LIVE (~10 min old)** | -1.32 % (vs 2026-11-09) | -0.84 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,493.270 | 11-10 11:23 | **LIVE (~0 min old)** | -0.75 % (vs 2026-11-09) | -0.55 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,674.084 | 11-10 11:23 | **LIVE (~0 min old)** | -0.84 % (vs 2026-11-09) | -0.39 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,803.927 | 11-10 11:08 | **LIVE (~15 min old)** | -1.30 % (vs 2026-11-09) | -0.83 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 20.710 | 11-10 11:07 | **LIVE (~16 min old)** | +0.79 pts | 0.23 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.4s) |
| WTI crude | 85.870 | 11-10 11:13 | **LIVE (~10 min old)** | -1.13 % (vs 2026-11-09) | -0.33 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 90.840 | 11-10 11:13 | **LIVE (~10 min old)** | -1.87 % (vs 2026-11-09) | -0.48 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,046.300 | 11-10 11:13 | **LIVE (~10 min old)** | -1.66 % (vs 2026-11-09) | -1.14 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.256 | 11-10 11:13 | **LIVE (~10 min old)** | -1.14 % (vs 2026-11-09) | -0.79 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 73,348.11, 24h -2.17%, z -1.07
- kraken: funding (raw, units unverified) 0.5437908930535, OI 2576.3455, OI change vs prior snapshot 4.42%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42320.65356, OI change vs prior snapshot 1.21%

**ETH**: price 2,028.29, 24h -4.82%, z -1.65
- kraken: funding (raw, units unverified) -0.04359112196475, OI 30929.506, OI change vs prior snapshot 2.73%
- hyperliquid: funding (raw, units unverified) 0.000003702, OI 793953.5691999986, OI change vs prior snapshot -0.22%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.4s)
