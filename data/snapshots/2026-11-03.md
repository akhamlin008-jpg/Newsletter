# Data snapshot 2026-11-03 10:27 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 2.42)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.631 | 11-03 10:27 | **LIVE (~0 min old)** | +4.80 bp | 0.85 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.958 | 11-03 10:27 | **LIVE (~0 min old)** | +6.40 bp | 1.11 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.327 | 11-03 10:27 | **LIVE (~0 min old)** | +1.60 bp | 0.43 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.600 | 10-30 close | official value for 2026-10-30 (not live) | -3.00 bp (vs 2026-10-29) | -0.63 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.290 | 11-02 close | official value for 2026-11-02 (not live) | -5.00 bp (vs 2026-10-30) | -2.42 | **YES** | fred:T10YIE |
| SOFR | 3.950 | 11-02 close | official value for 2026-11-02 (not live) | +0.00 bp (vs 2026-10-30) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.3s) |
| US dollar index (DXY) | 101.899 | 11-03 10:17 | **LIVE (~10 min old)** | +0.15 % (vs 2026-11-02) | 0.56 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.575 | 11-03 10:27 | **LIVE (~0 min old)** | +0.57 % (vs 2026-11-02) | 1.44 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.118 | 11-03 10:26 | **LIVE (~1 min old)** | +0.20 % (vs 2026-11-02) | 0.77 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,599.000 | 11-03 10:17 | **LIVE (~10 min old)** | +0.32 % (vs 2026-11-02) | 0.44 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,346.000 | 11-03 10:17 | **LIVE (~10 min old)** | +0.78 % (vs 2026-11-02) | 0.54 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,837.900 | 11-03 10:17 | **LIVE (~10 min old)** | +0.71 % (vs 2026-11-02) | 0.78 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,566.790 | 11-03 10:27 | **LIVE (~0 min old)** | +0.34 % (vs 2026-11-02) | 0.45 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,187.527 | 11-03 10:27 | **LIVE (~0 min old)** | +0.71 % (vs 2026-11-02) | 0.49 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,821.270 | 11-03 10:12 | **LIVE (~15 min old)** | +0.55 % (vs 2026-11-02) | 0.59 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 20.770 | 11-03 10:11 | **LIVE (~16 min old)** | -0.38 pts | -0.30 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.3s) |
| WTI crude | 96.440 | 11-03 10:17 | **LIVE (~10 min old)** | -0.02 % (vs 2026-11-02) | -0.01 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 104.200 | 11-03 10:17 | **LIVE (~10 min old)** | -0.54 % (vs 2026-11-02) | -0.16 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,944.000 | 11-03 10:17 | **LIVE (~10 min old)** | -0.64 % (vs 2026-11-02) | -0.47 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.420 | 11-03 10:17 | **LIVE (~10 min old)** | -1.89 % (vs 2026-11-02) | -1.45 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 77,195.94, 24h -0.26%, z -0.16
- kraken: funding (raw, units unverified) 1.377933726082125, OI 2595.8109, OI change vs prior snapshot -0.35%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40576.14096, OI change vs prior snapshot 0.07%

**ETH**: price 2,281.64, 24h 0.51%, z 0.27
- kraken: funding (raw, units unverified) 0.051584209631665906, OI 33178.371, OI change vs prior snapshot -1.26%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 994705.0691999999, OI change vs prior snapshot -0.24%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.3s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.3s)
