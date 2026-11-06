# Data snapshot 2026-11-06 10:21 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.59)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.534 | 11-06 10:21 | **LIVE (~0 min old)** | +5.70 bp | 1.08 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.874 | 11-06 10:20 | **LIVE (~0 min old)** | +3.70 bp | 0.67 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.340 | 11-06 10:20 | **LIVE (~0 min old)** | -2.00 bp | -0.53 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.640 | 11-04 close | official value for 2026-11-04 (not live) | -1.00 bp (vs 2026-11-03) | -0.22 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.240 | 11-05 close | official value for 2026-11-05 (not live) | -2.00 bp (vs 2026-11-04) | -0.82 |  | fred:T10YIE |
| SOFR | 3.920 | 11-05 close | official value for 2026-11-05 (not live) | -2.00 bp (vs 2026-11-04) | -0.79 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.3s) |
| US dollar index (DXY) | 102.149 | 11-06 10:11 | **LIVE (~10 min old)** | +0.59 % (vs 2026-11-05) | 2.31 | **YES** | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.289 | 11-06 10:21 | **LIVE (~0 min old)** | -0.04 % (vs 2026-11-05) | -0.12 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.116 | 11-06 10:20 | **LIVE (~1 min old)** | -0.67 % (vs 2026-11-05) | -2.59 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,443.000 | 11-06 10:11 | **LIVE (~10 min old)** | +0.81 % (vs 2026-11-05) | 0.62 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,234.750 | 11-06 10:11 | **LIVE (~10 min old)** | +1.80 % (vs 2026-11-05) | 0.88 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,748.000 | 11-06 10:11 | **LIVE (~10 min old)** | +0.46 % (vs 2026-11-05) | 0.32 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,430.330 | 11-06 10:21 | **LIVE (~0 min old)** | +1.04 % (vs 2026-11-05) | 0.79 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,190.170 | 11-06 10:21 | **LIVE (~0 min old)** | +2.10 % (vs 2026-11-05) | 1.02 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,734.237 | 11-06 10:06 | **LIVE (~15 min old)** | +0.16 % (vs 2026-11-05) | 0.11 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 24.760 | 11-06 10:05 | **LIVE (~15 min old)** | -3.42 pts | -1.06 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s) |
| WTI crude | 90.680 | 11-06 10:11 | **LIVE (~10 min old)** | +0.18 % (vs 2026-11-05) | 0.05 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 97.850 | 11-06 10:11 | **LIVE (~10 min old)** | -0.45 % (vs 2026-11-05) | -0.12 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,062.800 | 11-06 10:11 | **LIVE (~10 min old)** | -1.23 % (vs 2026-11-05) | -0.82 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.268 | 11-06 10:11 | **LIVE (~10 min old)** | +0.30 % (vs 2026-11-05) | 0.20 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 75,567.59, 24h -0.47%, z -0.21
- kraken: funding (raw, units unverified) 0.3965228917705, OI 2741.8079, OI change vs prior snapshot 3.54%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42635.0, OI change vs prior snapshot 0.86%

**ETH**: price 2,222.88, 24h -1.19%, z -0.39
- kraken: funding (raw, units unverified) -0.026075731463375, OI 32566.214, OI change vs prior snapshot 0.08%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 975445.8855999999, OI change vs prior snapshot 0.57%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.3s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s)
