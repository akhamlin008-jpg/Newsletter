# Data snapshot 2026-11-20 11:54 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.37), crypto (max |z| 2.2)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.649 | 11-20 11:54 | **LIVE (~0 min old)** | -13.00 bp | -1.92 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.948 | 11-20 11:54 | **LIVE (~0 min old)** | -10.40 bp | -1.82 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.299 | 11-20 11:54 | **LIVE (~0 min old)** | +2.60 bp | 0.75 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.880 | 11-18 close | official value for 2026-11-18 (not live) | -1.00 bp (vs 2026-11-17) | -0.20 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.160 | 11-19 close | official value for 2026-11-19 (not live) | -3.00 bp (vs 2026-11-18) | -1.26 |  | fred:T10YIE |
| SOFR | 3.910 | 11-19 close | official value for 2026-11-19 (not live) | +1.00 bp (vs 2026-11-18) | 0.45 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (12.7s) |
| US dollar index (DXY) | 103.703 | 11-20 11:44 | **LIVE (~11 min old)** | -0.19 % (vs 2026-11-19) | -0.56 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.684 | 11-20 11:54 | **LIVE (~1 min old)** | -0.44 % (vs 2026-11-19) | -1.24 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.098 | 11-20 11:54 | **LIVE (~1 min old)** | +0.11 % (vs 2026-11-19) | 0.32 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 122.650 | 11-13 close | official value for 2026-11-13 (not live) | +0.09 % (vs 2026-11-12) | 0.34 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,059.000 | 11-20 11:44 | **LIVE (~11 min old)** | -1.92 % (vs 2026-11-19) | -1.47 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 25,658.500 | 11-20 11:44 | **LIVE (~11 min old)** | -3.54 % (vs 2026-11-19) | -1.83 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,621.600 | 11-20 11:45 | **LIVE (~10 min old)** | -1.57 % (vs 2026-11-19) | -1.05 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,039.650 | 11-20 11:55 | **LIVE (~0 min old)** | -1.90 % (vs 2026-11-19) | -1.45 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 25,575.629 | 11-20 11:54 | **LIVE (~1 min old)** | -3.55 % (vs 2026-11-19) | -1.83 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,620.904 | 11-20 11:39 | **LIVE (~16 min old)** | -1.29 % (vs 2026-11-19) | -0.86 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 30.910 | 11-20 11:39 | **LIVE (~16 min old)** | +2.47 pts (vs 2026-11-19) | 0.81 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.8s) |
| WTI crude | 82.070 | 11-20 11:45 | **LIVE (~10 min old)** | -1.37 % (vs 2026-11-19) | -0.47 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 88.830 | 11-20 11:45 | **LIVE (~10 min old)** | -3.42 % (vs 2026-11-19) | -1.05 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,544.900 | 11-20 11:45 | **LIVE (~10 min old)** | -3.81 % (vs 2026-11-19) | -2.37 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 5.498 | 11-20 11:45 | **LIVE (~10 min old)** | -2.26 % (vs 2026-11-19) | -1.24 |  | yahoo:HG=F (unofficial feed) |

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
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate); fell back after: cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.1s)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 59,446.53, 24h -5.19%, z -2.11 **FLAG**
- kraken: funding (raw, units unverified) 0.22537380595293646, OI 2119.1691, OI change vs prior snapshot 0.13%
- hyperliquid: funding (raw, units unverified) -0.0000042876, OI 39506.1964, OI change vs prior snapshot 0.21%

**ETH**: price 1,642.23, 24h -7.04%, z -2.20 **FLAG**
- kraken: funding (raw, units unverified) -0.014232805164, OI 29082.798, OI change vs prior snapshot -1.01%
- hyperliquid: funding (raw, units unverified) -0.0000175236, OI 640886.4073999999, OI change vs prior snapshot 2.69%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (12.7s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.8s)
