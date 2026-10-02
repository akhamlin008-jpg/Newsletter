# Data snapshot 2026-10-02 10:06 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.766 | 10-02 10:06 | **LIVE (~0 min old)** | -2.10 bp | -0.34 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.193 | 10-02 10:06 | **LIVE (~0 min old)** | -4.10 bp | -0.75 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.427 | 10-02 10:06 | **LIVE (~0 min old)** | -2.00 bp | -0.54 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.930 | 09-30 close | official value for 2026-09-30 (not live) | +2.00 bp (vs 2026-09-29) | 0.37 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 10-01 close | official value for 2026-10-01 (not live) | +0.00 bp (vs 2026-09-30) | 0.00 |  | fred:T10YIE |
| SOFR | 3.870 | 10-01 close | official value for 2026-10-01 (not live) | -3.00 bp (vs 2026-09-30) | -0.67 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.5s) |
| US dollar index (DXY) | 101.833 | 10-02 09:56 | **LIVE (~10 min old)** | -0.26 % (vs 2026-10-01) | -0.82 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.503 | 10-02 10:06 | **LIVE (~0 min old)** | -0.03 % (vs 2026-10-01) | -0.06 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.128 | 10-02 10:06 | **LIVE (~0 min old)** | -0.38 % (vs 2026-10-01) | -1.49 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,776.250 | 10-02 09:56 | **LIVE (~10 min old)** | +0.68 % (vs 2026-10-01) | 1.20 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 31,126.000 | 10-02 09:56 | **LIVE (~10 min old)** | +1.19 % (vs 2026-10-01) | 1.37 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,857.500 | 10-02 09:56 | **LIVE (~10 min old)** | +1.08 % (vs 2026-10-01) | 1.40 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,743.700 | 10-02 10:06 | **LIVE (~0 min old)** | +1.01 % (vs 2026-10-01) | 1.59 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,970.047 | 10-02 10:06 | **LIVE (~0 min old)** | +1.54 % (vs 2026-10-01) | 1.51 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,844.757 | 10-02 09:51 | **LIVE (~15 min old)** | +1.36 % (vs 2026-10-01) | 1.80 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.760 | 10-02 09:50 | **LIVE (~16 min old)** | -0.63 pts | -0.68 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s) |
| WTI crude | 90.270 | 10-02 09:56 | **LIVE (~10 min old)** | -2.80 % (vs 2026-10-01) | -1.00 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 100.430 | 10-02 09:56 | **LIVE (~10 min old)** | -1.84 % (vs 2026-10-01) | -0.69 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,209.700 | 10-02 09:56 | **LIVE (~10 min old)** | +0.18 % (vs 2026-10-01) | 0.13 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.609 | 10-02 09:56 | **LIVE (~10 min old)** | +1.95 % (vs 2026-10-01) | 1.41 |  | yahoo:HG=F (unofficial feed) |

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
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 86,812.71, 24h 3.32%, z 1.57
- kraken: funding (raw, units unverified) -0.21228134272480448, OI 2357.5931, OI change vs prior snapshot -0.61%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 37949.15796, OI change vs prior snapshot 0.73%

**ETH**: price 2,746.40, 24h 2.13%, z 0.89
- kraken: funding (raw, units unverified) 0.025913655456250916, OI 28781.055, OI change vs prior snapshot 0.19%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1214558.0041999992, OI change vs prior snapshot 0.36%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.5s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s)
