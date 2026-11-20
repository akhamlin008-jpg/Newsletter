# Data snapshot 2026-11-20 11:02 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.26), crypto (max |z| 2.26)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.647 | 11-20 11:02 | **LIVE (~0 min old)** | -13.20 bp | -1.95 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.942 | 11-20 11:02 | **LIVE (~0 min old)** | -11.00 bp | -1.92 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.295 | 11-20 11:02 | **LIVE (~0 min old)** | +2.20 bp | 0.63 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.880 | 11-18 close | official value for 2026-11-18 (not live) | -1.00 bp (vs 2026-11-17) | -0.20 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.160 | 11-19 close | official value for 2026-11-19 (not live) | -3.00 bp (vs 2026-11-18) | -1.26 |  | fred:T10YIE |
| SOFR | 3.910 | 11-19 close | official value for 2026-11-19 (not live) | +1.00 bp (vs 2026-11-18) | 0.45 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.8s) |
| US dollar index (DXY) | 103.664 | 11-20 10:52 | **LIVE (~10 min old)** | -0.23 % (vs 2026-11-19) | -0.67 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.703 | 11-20 11:02 | **LIVE (~0 min old)** | -0.43 % (vs 2026-11-19) | -1.20 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.098 | 11-20 11:01 | **LIVE (~1 min old)** | +0.11 % (vs 2026-11-19) | 0.32 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 122.650 | 11-13 close | official value for 2026-11-13 (not live) | +0.09 % (vs 2026-11-12) | 0.34 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,113.500 | 11-20 10:52 | **LIVE (~10 min old)** | -1.16 % (vs 2026-11-19) | -0.89 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 25,923.500 | 11-20 10:52 | **LIVE (~10 min old)** | -2.54 % (vs 2026-11-19) | -1.32 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,640.900 | 11-20 10:52 | **LIVE (~10 min old)** | -0.84 % (vs 2026-11-19) | -0.56 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,069.160 | 11-20 11:02 | **LIVE (~0 min old)** | -1.49 % (vs 2026-11-19) | -1.13 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 25,719.182 | 11-20 11:02 | **LIVE (~0 min old)** | -3.01 % (vs 2026-11-19) | -1.55 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,631.681 | 11-20 10:47 | **LIVE (~15 min old)** | -0.88 % (vs 2026-11-19) | -0.59 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 30.590 | 11-20 10:47 | **LIVE (~15 min old)** | +2.15 pts (vs 2026-11-19) | 0.71 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.2s) |
| WTI crude | 81.980 | 11-20 10:52 | **LIVE (~10 min old)** | -1.48 % (vs 2026-11-19) | -0.50 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 88.610 | 11-20 10:52 | **LIVE (~10 min old)** | -3.66 % (vs 2026-11-19) | -1.13 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,551.500 | 11-20 10:52 | **LIVE (~10 min old)** | -3.64 % (vs 2026-11-19) | -2.26 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 5.510 | 11-20 10:52 | **LIVE (~10 min old)** | -2.04 % (vs 2026-11-19) | -1.12 |  | yahoo:HG=F (unofficial feed) |

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
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate); fell back after: cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.2s)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 59,214.96, 24h -5.56%, z -2.26 **FLAG**
- kraken: funding (raw, units unverified) 0.22537380595293646, OI 2182.0759, OI change vs prior snapshot -2.59%
- hyperliquid: funding (raw, units unverified) -0.0000120263, OI 39716.5249599999, OI change vs prior snapshot 5.09%

**ETH**: price 1,646.57, 24h -6.79%, z -2.13 **FLAG**
- kraken: funding (raw, units unverified) -0.014232805164, OI 30417.155, OI change vs prior snapshot 2.27%
- hyperliquid: funding (raw, units unverified) -0.0000432738, OI 626603.6604000008, OI change vs prior snapshot 2.78%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.8s)
- cboe:VIX -> HTTPError: HTTP Error 403: Forbidden (0.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.2s)
