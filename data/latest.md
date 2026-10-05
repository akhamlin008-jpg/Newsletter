# Data snapshot 2026-10-05 12:44 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.848 | 10-05 12:43 | **LIVE (~1 min old)** | +2.30 bp | 0.35 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.334 | 10-05 12:43 | **LIVE (~1 min old)** | +5.70 bp | 1.05 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.486 | 10-05 12:43 | **LIVE (~1 min old)** | +3.40 bp | 0.94 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.880 | 10-01 close | official value for 2026-10-01 (not live) | -5.00 bp (vs 2026-09-30) | -0.96 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 10-02 close | official value for 2026-10-02 (not live) | +0.00 bp (vs 2026-10-01) | 0.00 |  | fred:T10YIE |
| SOFR | 3.880 | 10-02 close | official value for 2026-10-02 (not live) | +1.00 bp (vs 2026-10-01) | 0.23 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.8s) |
| US dollar index (DXY) | 102.248 | 10-05 12:34 | **LIVE (~10 min old)** | +0.31 % (vs 2026-10-02) | 1.00 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.039 | 10-05 12:44 | **LIVE (~0 min old)** | +0.07 % (vs 2026-10-02) | 0.13 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.121 | 10-05 12:43 | **LIVE (~1 min old)** | -0.37 % (vs 2026-10-02) | -1.24 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,818.000 | 10-05 12:34 | **LIVE (~10 min old)** | +0.52 % (vs 2026-10-02) | 0.91 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 31,243.000 | 10-05 12:34 | **LIVE (~10 min old)** | +0.58 % (vs 2026-10-02) | 0.67 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,867.400 | 10-05 12:34 | **LIVE (~10 min old)** | +0.58 % (vs 2026-10-02) | 0.74 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,772.590 | 10-05 12:44 | **LIVE (~0 min old)** | +0.65 % (vs 2026-10-02) | 1.01 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 31,015.514 | 10-05 12:44 | **LIVE (~0 min old)** | +0.67 % (vs 2026-10-02) | 0.66 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,849.980 | 10-05 12:29 | **LIVE (~15 min old)** | +0.60 % (vs 2026-10-02) | 0.79 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.510 | 10-05 12:28 | **LIVE (~16 min old)** | +0.20 pts | 0.21 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.6s) |
| WTI crude | 90.120 | 10-05 12:34 | **LIVE (~10 min old)** | -1.09 % (vs 2026-10-02) | -0.40 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 100.770 | 10-05 12:34 | **LIVE (~10 min old)** | -1.45 % (vs 2026-10-02) | -0.56 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,157.100 | 10-05 12:34 | **LIVE (~10 min old)** | -0.12 % (vs 2026-10-02) | -0.10 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.642 | 10-05 12:34 | **LIVE (~10 min old)** | +2.31 % (vs 2026-10-02) | 1.72 |  | yahoo:HG=F (unofficial feed) |

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
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-21)
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

**BTC**: price 85,171.29, 24h -0.22%, z -0.11
- kraken: funding (raw, units unverified) -0.37418197447257007, OI 2097.4889, OI change vs prior snapshot -0.86%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 38073.09568, OI change vs prior snapshot -0.07%

**ETH**: price 2,688.51, 24h -0.54%, z -0.24
- kraken: funding (raw, units unverified) -0.0163068421428759, OI 28738.723, OI change vs prior snapshot -0.82%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1192807.7783999988, OI change vs prior snapshot 0.19%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.8s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.6s)
