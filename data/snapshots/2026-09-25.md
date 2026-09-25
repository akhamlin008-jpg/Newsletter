# Data snapshot 2026-09-25 09:40 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 3.0), commodities (max |z| 2.51)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.889 | 09-25 09:40 | **LIVE (~0 min old)** | -0.60 bp | -0.09 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.183 | 09-25 09:39 | **LIVE (~1 min old)** | +2.10 bp | 0.37 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.294 | 09-25 09:39 | **LIVE (~1 min old)** | +2.70 bp | 0.81 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.760 | 09-23 close | official value for 2026-09-23 (not live) | +13.00 bp (vs 2026-09-22) | 3.00 | **YES** | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 09-24 close | official value for 2026-09-24 (not live) | -2.00 bp (vs 2026-09-23) | -0.93 |  | fred:T10YIE |
| SOFR | 3.880 | 09-24 close | official value for 2026-09-24 (not live) | +1.00 bp (vs 2026-09-23) | 0.20 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.2s) |
| US dollar index (DXY) | 100.974 | 09-25 09:30 | **LIVE (~10 min old)** | -0.31 % (vs 2026-09-24) | -1.03 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.027 | 09-25 09:40 | **LIVE (~0 min old)** | -0.78 % (vs 2026-09-24) | -1.30 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.141 | 09-25 09:40 | **LIVE (~0 min old)** | +0.22 % (vs 2026-09-24) | 0.75 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 119.513 | 09-18 close | official value for 2026-09-18 (not live) | +0.14 % (vs 2026-09-17) | 0.61 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,770.250 | 09-25 09:30 | **LIVE (~10 min old)** | +0.04 % (vs 2026-09-24) | 0.07 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,795.000 | 09-25 09:30 | **LIVE (~10 min old)** | +0.09 % (vs 2026-09-24) | 0.10 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,860.400 | 09-25 09:30 | **LIVE (~10 min old)** | +0.13 % (vs 2026-09-24) | 0.15 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,725.590 | 09-25 09:40 | **LIVE (~0 min old)** | +0.28 % (vs 2026-09-24) | 0.40 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,599.062 | 09-25 09:40 | **LIVE (~0 min old)** | +0.39 % (vs 2026-09-24) | 0.35 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,835.574 | 09-24 16:30 | not trading now; last trade 09-24 16:30 ET | -0.11 % (vs 2026-09-23) | -0.13 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.250 | 09-25 09:25 | **LIVE (~15 min old)** | -0.42 pts (vs 2026-09-24) | -0.41 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s) |
| WTI crude | 93.130 | 09-25 09:30 | **LIVE (~10 min old)** | -1.56 % (vs 2026-09-24) | -0.53 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 98.700 | 09-25 09:30 | **LIVE (~10 min old)** | -7.41 % (vs 2026-09-24) | -2.51 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,312.400 | 09-25 09:30 | **LIVE (~10 min old)** | +0.34 % (vs 2026-09-24) | 0.27 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.760 | 09-25 09:30 | **LIVE (~10 min old)** | +0.61 % (vs 2026-09-24) | 0.41 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-21)
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-21)
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-18, 2026-09-21)
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 84,078.71, 24h -0.19%, z -0.07
- kraken: funding (raw, units unverified) 0.4293494951955552, OI 2209.439, OI change vs prior snapshot -1.24%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40379.1146, OI change vs prior snapshot 0.23%

**ETH**: price 2,698.42, 24h 1.09%, z 0.37
- kraken: funding (raw, units unverified) 0.02661198874508243, OI 26337.291, OI change vs prior snapshot 0.06%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1099061.3797999998, OI change vs prior snapshot -0.34%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s)
