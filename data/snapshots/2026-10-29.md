# Data snapshot 2026-10-29 11:11 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.24)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.644 | 10-29 11:10 | **LIVE (~0 min old)** | -9.10 bp | -1.58 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.976 | 10-29 11:10 | **LIVE (~0 min old)** | -6.90 bp | -1.20 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.332 | 10-29 11:10 | **LIVE (~0 min old)** | +2.20 bp | 0.59 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.640 | 10-27 close | official value for 2026-10-27 (not live) | -2.00 bp (vs 2026-10-26) | -0.40 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.380 | 10-28 close | official value for 2026-10-28 (not live) | +3.00 bp (vs 2026-10-27) | 1.52 |  | fred:T10YIE |
| SOFR | 3.940 | 10-28 close | official value for 2026-10-28 (not live) | -1.00 bp (vs 2026-10-27) | -0.36 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.7s) |
| US dollar index (DXY) | 102.038 | 10-29 11:01 | **LIVE (~10 min old)** | -0.15 % (vs 2026-10-28) | -0.53 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.824 | 10-29 11:11 | **LIVE (~0 min old)** | -0.11 % (vs 2026-10-28) | -0.25 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.117 | 10-29 11:10 | **LIVE (~1 min old)** | +0.36 % (vs 2026-10-28) | 1.34 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,753.500 | 10-29 11:01 | **LIVE (~10 min old)** | -0.38 % (vs 2026-10-28) | -0.61 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 29,576.250 | 10-29 11:01 | **LIVE (~10 min old)** | -1.35 % (vs 2026-10-28) | -1.15 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,869.800 | 10-29 11:01 | **LIVE (~10 min old)** | +1.07 % (vs 2026-10-28) | 1.22 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,723.570 | 10-29 11:11 | **LIVE (~0 min old)** | -0.26 % (vs 2026-10-28) | -0.41 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,460.623 | 10-29 11:11 | **LIVE (~0 min old)** | -1.18 % (vs 2026-10-28) | -0.97 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,857.818 | 10-29 10:56 | **LIVE (~15 min old)** | +0.96 % (vs 2026-10-28) | 1.10 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 16.710 | 10-29 10:55 | **LIVE (~16 min old)** | -0.20 pts | -0.17 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.2s) |
| WTI crude | 100.350 | 10-29 11:01 | **LIVE (~10 min old)** | -2.36 % (vs 2026-10-28) | -0.90 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 109.620 | 10-29 11:01 | **LIVE (~10 min old)** | -4.94 % (vs 2026-10-28) | -2.24 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,038.500 | 10-29 11:01 | **LIVE (~10 min old)** | -0.32 % (vs 2026-10-28) | -0.29 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.585 | 10-29 11:01 | **LIVE (~10 min old)** | -0.84 % (vs 2026-10-28) | -0.66 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 81,387.20, 24h 1.18%, z 0.81
- kraken: funding (raw, units unverified) 0.98722135705, OI 2449.7614, OI change vs prior snapshot 0.67%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 43225.74658, OI change vs prior snapshot 0.55%

**ETH**: price 2,359.35, 24h 1.19%, z 0.65
- kraken: funding (raw, units unverified) -0.01159773916399922, OI 32878.25, OI change vs prior snapshot 1.56%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1112875.5092000004, OI change vs prior snapshot -1.70%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.7s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.2s)
