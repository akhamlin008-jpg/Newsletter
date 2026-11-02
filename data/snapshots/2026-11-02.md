# Data snapshot 2026-11-02 11:58 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 4.98)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.569 | 11-02 11:58 | **LIVE (~0 min old)** | -1.20 bp | -0.21 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.875 | 11-02 11:58 | **LIVE (~0 min old)** | -5.40 bp | -0.92 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.306 | 11-02 11:58 | **LIVE (~0 min old)** | -4.20 bp | -1.18 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.630 | 10-29 close | official value for 2026-10-29 (not live) | -4.00 bp (vs 2026-10-28) | -0.83 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 10-30 close | official value for 2026-10-30 (not live) | -1.00 bp (vs 2026-10-29) | -0.47 |  | fred:T10YIE |
| SOFR | 3.950 | 10-30 close | official value for 2026-10-30 (not live) | +1.00 bp (vs 2026-10-29) | 0.38 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.6s) |
| US dollar index (DXY) | 101.704 | 11-02 11:49 | **LIVE (~10 min old)** | -0.17 % (vs 2026-10-30) | -0.64 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.816 | 11-02 11:59 | **LIVE (~0 min old)** | +0.01 % (vs 2026-10-30) | 0.02 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.121 | 11-02 11:58 | **LIVE (~1 min old)** | +0.21 % (vs 2026-10-30) | 0.78 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.320 | 10-23 close | official value for 2026-10-23 (not live) | -0.03 % (vs 2026-10-22) | -0.11 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,655.000 | 11-02 11:49 | **LIVE (~10 min old)** | +0.54 % (vs 2026-10-30) | 0.73 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,647.000 | 11-02 11:49 | **LIVE (~10 min old)** | +0.40 % (vs 2026-10-30) | 0.28 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,851.000 | 11-02 11:49 | **LIVE (~10 min old)** | +1.05 % (vs 2026-10-30) | 1.12 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,623.220 | 11-02 11:59 | **LIVE (~0 min old)** | +0.57 % (vs 2026-10-30) | 0.76 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,511.365 | 11-02 11:59 | **LIVE (~0 min old)** | +0.45 % (vs 2026-10-30) | 0.31 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,842.306 | 11-02 11:44 | **LIVE (~15 min old)** | +1.08 % (vs 2026-10-30) | 1.14 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 18.830 | 11-02 11:43 | **LIVE (~16 min old)** | -0.59 pts | -0.47 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s) |
| WTI crude | 96.850 | 11-02 11:49 | **LIVE (~10 min old)** | -6.98 % (vs 2026-10-30) | -2.76 | **YES** | yahoo:CL=F (unofficial feed) |
| Brent crude | 104.980 | 11-02 11:49 | **LIVE (~10 min old)** | -10.76 % (vs 2026-10-30) | -4.98 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 3,979.500 | 11-02 11:49 | **LIVE (~10 min old)** | +2.07 % (vs 2026-10-30) | 1.55 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.572 | 11-02 11:49 | **LIVE (~10 min old)** | +1.76 % (vs 2026-10-30) | 1.35 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 77,348.77, 24h -0.86%, z -0.53
- kraken: funding (raw, units unverified) 1.63629297485775, OI 2644.0059, OI change vs prior snapshot -3.94%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 41281.57692, OI change vs prior snapshot 0.39%

**ETH**: price 2,265.67, 24h -0.05%, z -0.03
- kraken: funding (raw, units unverified) 0.08764712662416742, OI 34461.99, OI change vs prior snapshot 12.47%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 981507.9430000002, OI change vs prior snapshot -4.64%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.6s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s)
