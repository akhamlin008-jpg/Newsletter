# Data snapshot 2026-11-03 09:59 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.42)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.606 | 11-03 09:59 | **LIVE (~0 min old)** | +2.30 bp | 0.41 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.939 | 11-03 09:59 | **LIVE (~0 min old)** | +4.50 bp | 0.78 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.333 | 11-03 09:59 | **LIVE (~0 min old)** | +2.20 bp | 0.59 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.600 | 10-30 close | official value for 2026-10-30 (not live) | -3.00 bp (vs 2026-10-29) | -0.63 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.290 | 11-02 close | official value for 2026-11-02 (not live) | -5.00 bp (vs 2026-10-30) | -2.42 | **YES** | fred:T10YIE |
| SOFR | 3.950 | 11-02 close | official value for 2026-11-02 (not live) | +0.00 bp (vs 2026-10-30) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.0s) |
| US dollar index (DXY) | 101.789 | 11-03 09:49 | **LIVE (~10 min old)** | +0.04 % (vs 2026-11-02) | 0.15 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.288 | 11-03 09:59 | **LIVE (~0 min old)** | +0.39 % (vs 2026-11-02) | 0.98 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.120 | 11-03 09:59 | **LIVE (~0 min old)** | +0.39 % (vs 2026-11-02) | 1.50 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,591.250 | 11-03 09:49 | **LIVE (~10 min old)** | +0.22 % (vs 2026-11-02) | 0.30 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,345.500 | 11-03 09:49 | **LIVE (~10 min old)** | +0.78 % (vs 2026-11-02) | 0.54 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,824.600 | 11-03 09:49 | **LIVE (~10 min old)** | +0.24 % (vs 2026-11-02) | 0.26 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,561.280 | 11-03 09:59 | **LIVE (~0 min old)** | +0.26 % (vs 2026-11-02) | 0.36 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,153.484 | 11-03 09:59 | **LIVE (~0 min old)** | +0.58 % (vs 2026-11-02) | 0.40 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,820.360 | 11-03 09:44 | **LIVE (~15 min old)** | +0.52 % (vs 2026-11-02) | 0.56 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 20.890 | 11-03 09:43 | **LIVE (~16 min old)** | -0.26 pts | -0.20 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.7s) |
| WTI crude | 95.920 | 11-03 09:49 | **LIVE (~10 min old)** | -0.56 % (vs 2026-11-02) | -0.18 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 103.490 | 11-03 09:49 | **LIVE (~10 min old)** | -1.22 % (vs 2026-11-02) | -0.36 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,957.000 | 11-03 09:49 | **LIVE (~10 min old)** | -0.32 % (vs 2026-11-02) | -0.23 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.429 | 11-03 09:49 | **LIVE (~10 min old)** | -1.74 % (vs 2026-11-02) | -1.34 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 77,258.98, 24h -0.63%, z -0.38
- kraken: funding (raw, units unverified) 0.86332357668, OI 2604.9909, OI change vs prior snapshot -2.02%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40547.58818, OI change vs prior snapshot -1.08%

**ETH**: price 2,283.01, 24h -0.21%, z -0.11
- kraken: funding (raw, units unverified) 0.04526719872812576, OI 33602.853, OI change vs prior snapshot 1.47%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 997048.1836000001, OI change vs prior snapshot 1.27%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.7s)
