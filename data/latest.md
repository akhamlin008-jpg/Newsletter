# Data snapshot 2026-10-02 10:42 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.789 | 10-02 10:41 | **LIVE (~0 min old)** | +0.20 bp | 0.03 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.214 | 10-02 10:41 | **LIVE (~0 min old)** | -2.00 bp | -0.37 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.425 | 10-02 10:41 | **LIVE (~0 min old)** | -2.20 bp | -0.59 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.930 | 09-30 close | official value for 2026-09-30 (not live) | +2.00 bp (vs 2026-09-29) | 0.37 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 10-01 close | official value for 2026-10-01 (not live) | +0.00 bp (vs 2026-09-30) | 0.00 |  | fred:T10YIE |
| SOFR | 3.870 | 10-01 close | official value for 2026-10-01 (not live) | -3.00 bp (vs 2026-09-30) | -0.67 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.2s) |
| US dollar index (DXY) | 101.690 | 10-02 10:32 | **LIVE (~10 min old)** | -0.40 % (vs 2026-10-01) | -1.26 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.439 | 10-02 10:42 | **LIVE (~0 min old)** | -0.08 % (vs 2026-10-01) | -0.14 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.129 | 10-02 10:42 | **LIVE (~0 min old)** | -0.37 % (vs 2026-10-01) | -1.44 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,800.250 | 10-02 10:32 | **LIVE (~10 min old)** | +0.99 % (vs 2026-10-01) | 1.74 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 31,239.250 | 10-02 10:32 | **LIVE (~10 min old)** | +1.56 % (vs 2026-10-01) | 1.80 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,864.100 | 10-02 10:32 | **LIVE (~10 min old)** | +1.32 % (vs 2026-10-01) | 1.70 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,753.530 | 10-02 10:42 | **LIVE (~0 min old)** | +1.14 % (vs 2026-10-01) | 1.79 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,999.658 | 10-02 10:42 | **LIVE (~0 min old)** | +1.63 % (vs 2026-10-01) | 1.61 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,847.589 | 10-02 10:27 | **LIVE (~15 min old)** | +1.46 % (vs 2026-10-01) | 1.94 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.560 | 10-02 10:26 | **LIVE (~16 min old)** | -0.83 pts | -0.89 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.5s) |
| WTI crude | 88.720 | 10-02 10:32 | **LIVE (~10 min old)** | -4.47 % (vs 2026-10-01) | -1.60 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 99.020 | 10-02 10:32 | **LIVE (~10 min old)** | -3.22 % (vs 2026-10-01) | -1.20 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,202.000 | 10-02 10:32 | **LIVE (~10 min old)** | -0.01 % (vs 2026-10-01) | -0.01 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.582 | 10-02 10:32 | **LIVE (~10 min old)** | +1.55 % (vs 2026-10-01) | 1.12 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 85,930.00, 24h 2.27%, z 1.07
- kraken: funding (raw, units unverified) -0.21228134272480448, OI 2331.897, OI change vs prior snapshot -1.09%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 38045.9451599999, OI change vs prior snapshot 0.26%

**ETH**: price 2,725.63, 24h 1.36%, z 0.57
- kraken: funding (raw, units unverified) 0.025913655456250916, OI 28721.168, OI change vs prior snapshot -0.21%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1217564.8088000009, OI change vs prior snapshot 0.25%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.5s)
