# Data snapshot 2026-10-01 11:24 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.76)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.814 | 10-01 11:23 | **LIVE (~0 min old)** | -7.30 bp | -1.13 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.272 | 10-01 11:24 | **LIVE (~0 min old)** | -2.10 bp | -0.38 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.458 | 10-01 11:23 | **LIVE (~0 min old)** | +5.20 bp | 1.43 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.910 | 09-29 close | official value for 2026-09-29 (not live) | +1.00 bp (vs 2026-09-28) | 0.18 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 09-30 close | official value for 2026-09-30 (not live) | +1.00 bp (vs 2026-09-29) | 0.51 |  | fred:T10YIE |
| SOFR | 3.900 | 09-30 close | official value for 2026-09-30 (not live) | +2.00 bp (vs 2026-09-29) | 0.44 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.3s) |
| US dollar index (DXY) | 101.923 | 10-01 11:14 | **LIVE (~10 min old)** | +0.47 % (vs 2026-09-30) | 1.63 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.536 | 10-01 11:24 | **LIVE (~0 min old)** | +0.08 % (vs 2026-09-30) | 0.15 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.126 | 10-01 11:23 | **LIVE (~1 min old)** | -0.72 % (vs 2026-09-30) | -2.76 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,686.000 | 10-01 11:14 | **LIVE (~10 min old)** | -0.38 % (vs 2026-09-30) | -0.66 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,599.250 | 10-01 11:14 | **LIVE (~10 min old)** | -0.32 % (vs 2026-09-30) | -0.36 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,801.400 | 10-01 11:14 | **LIVE (~10 min old)** | -0.57 % (vs 2026-09-30) | -0.72 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,636.500 | 10-01 11:24 | **LIVE (~0 min old)** | -0.20 % (vs 2026-09-30) | -0.30 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,377.514 | 10-01 11:24 | **LIVE (~0 min old)** | -0.10 % (vs 2026-09-30) | -0.10 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,780.291 | 10-01 11:09 | **LIVE (~15 min old)** | -0.59 % (vs 2026-09-30) | -0.77 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.560 | 10-01 11:08 | **LIVE (~16 min old)** | +1.22 pts | 1.27 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.5s) |
| WTI crude | 92.590 | 10-01 11:14 | **LIVE (~10 min old)** | +2.40 % (vs 2026-09-30) | 0.86 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 101.650 | 10-01 11:14 | **LIVE (~10 min old)** | -1.82 % (vs 2026-09-30) | -0.66 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,185.100 | 10-01 11:14 | **LIVE (~10 min old)** | -0.04 % (vs 2026-09-30) | -0.03 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.553 | 10-01 11:14 | **LIVE (~10 min old)** | -0.09 % (vs 2026-09-30) | -0.07 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 84,138.92, 24h 0.06%, z 0.03
- kraken: funding (raw, units unverified) 1.072037077869347, OI 2376.3189, OI change vs prior snapshot 0.21%
- hyperliquid: funding (raw, units unverified) 0.0000104553, OI 33815.4382, OI change vs prior snapshot -0.57%

**ETH**: price 2,692.15, 24h 0.38%, z 0.16
- kraken: funding (raw, units unverified) 0.040817639212375, OI 26553.512, OI change vs prior snapshot 0.74%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1201629.3273999987, OI change vs prior snapshot 0.36%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.3s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.5s)
