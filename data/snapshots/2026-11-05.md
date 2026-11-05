# Data snapshot 2026-11-05 10:46 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** vol (max |z| 4.52), equity (max |z| 3.93)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.529 | 11-05 10:46 | **LIVE (~0 min old)** | -5.20 bp | -0.97 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.853 | 11-05 10:46 | **LIVE (~0 min old)** | -3.90 bp | -0.70 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.324 | 11-05 10:46 | **LIVE (~0 min old)** | +1.30 bp | 0.36 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.650 | 11-03 close | official value for 2026-11-03 (not live) | +3.00 bp (vs 2026-11-02) | 0.66 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.260 | 11-04 close | official value for 2026-11-04 (not live) | -4.00 bp (vs 2026-11-03) | -1.75 |  | fred:T10YIE |
| SOFR | 3.940 | 11-04 close | official value for 2026-11-04 (not live) | -3.00 bp (vs 2026-11-03) | -1.18 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.7s) |
| US dollar index (DXY) | 101.560 | 11-05 10:36 | **LIVE (~11 min old)** | +0.05 % (vs 2026-11-04) | 0.19 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.850 | 11-05 10:46 | **LIVE (~1 min old)** | -0.39 % (vs 2026-11-04) | -1.02 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.123 | 11-05 10:46 | **LIVE (~1 min old)** | +0.19 % (vs 2026-11-04) | 0.73 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,521.500 | 11-05 10:36 | **LIVE (~11 min old)** | -2.58 % (vs 2026-11-04) | -3.24 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,258.500 | 11-05 10:36 | **LIVE (~11 min old)** | -4.58 % (vs 2026-11-04) | -3.34 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,806.500 | 11-05 10:36 | **LIVE (~11 min old)** | -2.07 % (vs 2026-11-04) | -2.22 | **YES** | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,446.820 | 11-05 10:46 | **LIVE (~1 min old)** | -3.14 % (vs 2026-11-04) | -3.92 | **YES** | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 26,880.467 | 11-05 10:46 | **LIVE (~1 min old)** | -5.47 % (vs 2026-11-04) | -3.93 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,797.465 | 11-05 10:31 | **LIVE (~16 min old)** | -2.08 % (vs 2026-11-04) | -2.19 | **YES** | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 23.790 | 11-05 10:30 | **LIVE (~16 min old)** | +7.18 pts | 4.52 | **YES** | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s) |
| WTI crude | 90.410 | 11-05 10:36 | **LIVE (~11 min old)** | +2.60 % (vs 2026-11-04) | 0.74 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 97.210 | 11-05 10:36 | **LIVE (~11 min old)** | +2.74 % (vs 2026-11-04) | 0.71 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,112.500 | 11-05 10:36 | **LIVE (~11 min old)** | +0.97 % (vs 2026-11-04) | 0.63 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.316 | 11-05 10:36 | **LIVE (~11 min old)** | -1.35 % (vs 2026-11-04) | -0.99 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open
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

**BTC**: price 76,067.86, 24h -5.16%, z -2.78 **FLAG**
- kraken: funding (raw, units unverified) 1.4017957564768595, OI 2883.5875, OI change vs prior snapshot 4.00%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 38817.25832, OI change vs prior snapshot 0.45%

**ETH**: price 2,271.41, 24h -6.29%, z -2.60 **FLAG**
- kraken: funding (raw, units unverified) 0.05575118946600078, OI 37420.27, OI change vs prior snapshot 4.12%
- hyperliquid: funding (raw, units unverified) -0.0000162016, OI 976740.0596000011, OI change vs prior snapshot -0.92%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.7s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s)
