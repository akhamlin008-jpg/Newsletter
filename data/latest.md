# Data snapshot 2026-11-02 12:24 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 5.07)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.577 | 11-02 12:24 | **LIVE (~0 min old)** | -0.40 bp | -0.07 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.880 | 11-02 12:24 | **LIVE (~0 min old)** | -4.90 bp | -0.84 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.303 | 11-02 12:24 | **LIVE (~0 min old)** | -4.50 bp | -1.27 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.630 | 10-29 close | official value for 2026-10-29 (not live) | -4.00 bp (vs 2026-10-28) | -0.83 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 10-30 close | official value for 2026-10-30 (not live) | -1.00 bp (vs 2026-10-29) | -0.47 |  | fred:T10YIE |
| SOFR | 3.950 | 10-30 close | official value for 2026-10-30 (not live) | +1.00 bp (vs 2026-10-29) | 0.38 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.4s) |
| US dollar index (DXY) | 101.665 | 11-02 12:14 | **LIVE (~10 min old)** | -0.21 % (vs 2026-10-30) | -0.78 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.832 | 11-02 12:24 | **LIVE (~0 min old)** | +0.02 % (vs 2026-10-30) | 0.04 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.121 | 11-02 12:24 | **LIVE (~0 min old)** | +0.26 % (vs 2026-10-30) | 0.99 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,652.250 | 11-02 12:14 | **LIVE (~10 min old)** | +0.50 % (vs 2026-10-30) | 0.68 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,648.250 | 11-02 12:14 | **LIVE (~10 min old)** | +0.40 % (vs 2026-10-30) | 0.28 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,847.800 | 11-02 12:14 | **LIVE (~10 min old)** | +0.94 % (vs 2026-10-30) | 1.00 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,617.090 | 11-02 12:24 | **LIVE (~0 min old)** | +0.49 % (vs 2026-10-30) | 0.65 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,480.652 | 11-02 12:24 | **LIVE (~0 min old)** | +0.34 % (vs 2026-10-30) | 0.23 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,838.324 | 11-02 12:09 | **LIVE (~15 min old)** | +0.94 % (vs 2026-10-30) | 0.99 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 19.100 | 11-02 12:08 | **LIVE (~16 min old)** | -0.32 pts | -0.26 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.1s) |
| WTI crude | 96.510 | 11-02 12:14 | **LIVE (~10 min old)** | -7.31 % (vs 2026-10-30) | -2.89 | **YES** | yahoo:CL=F (unofficial feed) |
| Brent crude | 104.750 | 11-02 12:14 | **LIVE (~10 min old)** | -10.96 % (vs 2026-10-30) | -5.07 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 3,978.000 | 11-02 12:14 | **LIVE (~10 min old)** | +2.03 % (vs 2026-10-30) | 1.52 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.580 | 11-02 12:14 | **LIVE (~10 min old)** | +1.88 % (vs 2026-10-30) | 1.45 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open
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

**BTC**: price 77,191.55, 24h -0.85%, z -0.52
- kraken: funding (raw, units unverified) 0.18085262596330753, OI 2644.8605, OI change vs prior snapshot 0.03%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41175.1233399999, OI change vs prior snapshot -0.26%

**ETH**: price 2,258.10, 24h -0.16%, z -0.08
- kraken: funding (raw, units unverified) 0.02559832808091591, OI 33242.635, OI change vs prior snapshot -3.54%
- hyperliquid: funding (raw, units unverified) 0.000011937, OI 995240.4034000003, OI change vs prior snapshot 1.40%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.4s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.1s)
