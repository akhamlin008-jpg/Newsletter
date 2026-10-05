# Data snapshot 2026-10-05 11:53 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.841 | 10-05 11:52 | **LIVE (~1 min old)** | +1.60 bp | 0.24 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.328 | 10-05 11:53 | **LIVE (~0 min old)** | +5.10 bp | 0.94 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.487 | 10-05 11:52 | **LIVE (~1 min old)** | +3.50 bp | 0.97 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.880 | 10-01 close | official value for 2026-10-01 (not live) | -5.00 bp (vs 2026-09-30) | -0.96 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 10-02 close | official value for 2026-10-02 (not live) | +0.00 bp (vs 2026-10-01) | 0.00 |  | fred:T10YIE |
| SOFR | 3.880 | 10-02 close | official value for 2026-10-02 (not live) | +1.00 bp (vs 2026-10-01) | 0.23 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.1s) |
| US dollar index (DXY) | 102.172 | 10-05 11:43 | **LIVE (~11 min old)** | +0.24 % (vs 2026-10-02) | 0.76 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.018 | 10-05 11:53 | **LIVE (~1 min old)** | +0.06 % (vs 2026-10-02) | 0.11 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.121 | 10-05 11:53 | **LIVE (~1 min old)** | -0.33 % (vs 2026-10-02) | -1.09 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,815.250 | 10-05 11:43 | **LIVE (~11 min old)** | +0.49 % (vs 2026-10-02) | 0.85 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 31,242.500 | 10-05 11:43 | **LIVE (~11 min old)** | +0.58 % (vs 2026-10-02) | 0.67 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,861.200 | 10-05 11:43 | **LIVE (~11 min old)** | +0.36 % (vs 2026-10-02) | 0.46 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,762.220 | 10-05 11:53 | **LIVE (~1 min old)** | +0.51 % (vs 2026-10-02) | 0.80 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,992.623 | 10-05 11:53 | **LIVE (~1 min old)** | +0.60 % (vs 2026-10-02) | 0.59 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,842.399 | 10-05 11:38 | **LIVE (~16 min old)** | +0.34 % (vs 2026-10-02) | 0.44 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.580 | 10-05 11:37 | **LIVE (~16 min old)** | +0.27 pts | 0.29 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.2s) |
| WTI crude | 90.670 | 10-05 11:43 | **LIVE (~11 min old)** | -0.48 % (vs 2026-10-02) | -0.18 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 101.750 | 10-05 11:43 | **LIVE (~11 min old)** | -0.49 % (vs 2026-10-02) | -0.19 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,166.000 | 10-05 11:43 | **LIVE (~11 min old)** | +0.09 % (vs 2026-10-02) | 0.07 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.649 | 10-05 11:43 | **LIVE (~11 min old)** | +2.42 % (vs 2026-10-02) | 1.80 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 85,250.94, 24h 0.02%, z 0.01
- kraken: funding (raw, units unverified) 0.86914373814525, OI 2101.946, OI change vs prior snapshot -1.86%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 38009.1233, OI change vs prior snapshot 0.24%

**ETH**: price 2,696.49, 24h -0.07%, z -0.03
- kraken: funding (raw, units unverified) 0.026361620775, OI 28395.717, OI change vs prior snapshot 2.15%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1189742.1627999991, OI change vs prior snapshot -0.11%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.2s)
