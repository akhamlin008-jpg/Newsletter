# Data snapshot 2026-11-05 10:22 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** equity (max |z| 3.27), vol (max |z| 3.0)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.558 | 11-05 10:22 | **LIVE (~0 min old)** | -2.30 bp | -0.43 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.872 | 11-05 10:22 | **LIVE (~0 min old)** | -2.00 bp | -0.36 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.314 | 11-05 10:22 | **LIVE (~0 min old)** | +0.30 bp | 0.08 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.650 | 11-03 close | official value for 2026-11-03 (not live) | +3.00 bp (vs 2026-11-02) | 0.66 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.260 | 11-04 close | official value for 2026-11-04 (not live) | -4.00 bp (vs 2026-11-03) | -1.75 |  | fred:T10YIE |
| SOFR | 3.940 | 11-04 close | official value for 2026-11-04 (not live) | -3.00 bp (vs 2026-11-03) | -1.18 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.4s) |
| US dollar index (DXY) | 101.595 | 11-05 10:12 | **LIVE (~10 min old)** | +0.08 % (vs 2026-11-04) | 0.32 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.979 | 11-05 10:21 | **LIVE (~1 min old)** | -0.31 % (vs 2026-11-04) | -0.81 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.122 | 11-05 10:21 | **LIVE (~1 min old)** | +0.14 % (vs 2026-11-04) | 0.55 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,555.500 | 11-05 10:11 | **LIVE (~11 min old)** | -2.14 % (vs 2026-11-04) | -2.69 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,327.750 | 11-05 10:11 | **LIVE (~11 min old)** | -4.34 % (vs 2026-11-04) | -3.17 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,818.900 | 11-05 10:11 | **LIVE (~11 min old)** | -1.64 % (vs 2026-11-04) | -1.76 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,505.350 | 11-05 10:22 | **LIVE (~0 min old)** | -2.38 % (vs 2026-11-04) | -2.97 | **YES** | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,139.568 | 11-05 10:22 | **LIVE (~0 min old)** | -4.56 % (vs 2026-11-04) | -3.27 | **YES** | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,815.221 | 11-05 10:06 | **LIVE (~16 min old)** | -1.46 % (vs 2026-11-04) | -1.54 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 21.380 | 11-05 10:06 | **LIVE (~16 min old)** | +4.77 pts | 3.00 | **YES** | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.0s) |
| WTI crude | 89.650 | 11-05 10:11 | **LIVE (~11 min old)** | +1.74 % (vs 2026-11-04) | 0.49 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 96.560 | 11-05 10:11 | **LIVE (~11 min old)** | +2.05 % (vs 2026-11-04) | 0.53 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,128.300 | 11-05 10:11 | **LIVE (~11 min old)** | +1.36 % (vs 2026-11-04) | 0.88 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.337 | 11-05 10:11 | **LIVE (~11 min old)** | -1.03 % (vs 2026-11-04) | -0.75 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 77,059.94, 24h -3.93%, z -2.12 **FLAG**
- kraken: funding (raw, units unverified) 1.4017957564768595, OI 2772.7674, OI change vs prior snapshot 17.07%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 38642.13992, OI change vs prior snapshot -5.22%

**ETH**: price 2,291.62, 24h -5.46%, z -2.25 **FLAG**
- kraken: funding (raw, units unverified) 0.05575118946600078, OI 35940.013, OI change vs prior snapshot 30.08%
- hyperliquid: funding (raw, units unverified) -0.0000094785, OI 985800.2917999998, OI change vs prior snapshot -4.92%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.4s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.0s)
