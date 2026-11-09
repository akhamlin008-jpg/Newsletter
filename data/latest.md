# Data snapshot 2026-11-09 12:23 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.566 | 11-09 12:22 | **LIVE (~0 min old)** | +4.40 bp | 0.75 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.878 | 11-09 12:23 | **LIVE (~0 min old)** | +1.90 bp | 0.34 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.312 | 11-09 12:22 | **LIVE (~0 min old)** | -2.50 bp | -0.67 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.600 | 11-05 close | official value for 2026-11-05 (not live) | -4.00 bp (vs 2026-11-04) | -0.92 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.230 | 11-06 close | official value for 2026-11-06 (not live) | -1.00 bp (vs 2026-11-05) | -0.42 |  | fred:T10YIE |
| SOFR | 3.890 | 11-06 close | official value for 2026-11-06 (not live) | -3.00 bp (vs 2026-11-05) | -1.17 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.8s) |
| US dollar index (DXY) | 101.832 | 11-09 12:13 | **LIVE (~10 min old)** | -0.46 % (vs 2026-11-06) | -1.49 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.962 | 11-09 12:23 | **LIVE (~0 min old)** | +0.29 % (vs 2026-11-06) | 0.77 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.121 | 11-09 12:22 | **LIVE (~1 min old)** | -0.16 % (vs 2026-11-06) | -0.62 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,567.500 | 11-09 12:13 | **LIVE (~10 min old)** | +2.24 % (vs 2026-11-06) | 1.75 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,962.500 | 11-09 12:13 | **LIVE (~10 min old)** | +3.24 % (vs 2026-11-06) | 1.61 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,838.000 | 11-09 12:13 | **LIVE (~10 min old)** | +2.81 % (vs 2026-11-06) | 1.99 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,547.850 | 11-09 12:23 | **LIVE (~0 min old)** | +2.32 % (vs 2026-11-06) | 1.81 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,875.039 | 11-09 12:23 | **LIVE (~0 min old)** | +3.28 % (vs 2026-11-06) | 1.62 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,828.842 | 11-09 12:08 | **LIVE (~15 min old)** | +2.71 % (vs 2026-11-06) | 1.94 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 20.480 | 11-09 12:07 | **LIVE (~16 min old)** | -5.16 pts | -1.62 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s) |
| WTI crude | 87.790 | 11-09 12:13 | **LIVE (~10 min old)** | -3.35 % (vs 2026-11-06) | -1.00 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 93.920 | 11-09 12:13 | **LIVE (~10 min old)** | -4.48 % (vs 2026-11-06) | -1.20 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,114.800 | 11-09 12:13 | **LIVE (~10 min old)** | +0.98 % (vs 2026-11-06) | 0.66 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.349 | 11-09 12:13 | **LIVE (~10 min old)** | +2.11 % (vs 2026-11-06) | 1.49 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 74,697.28, 24h -1.26%, z -0.61
- kraken: funding (raw, units unverified) 0.03957253767425, OI 2557.8373, OI change vs prior snapshot -6.96%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42904.6781999999, OI change vs prior snapshot 0.54%

**ETH**: price 2,122.42, 24h -4.74%, z -1.57
- kraken: funding (raw, units unverified) -0.01116277961949929, OI 29558.832, OI change vs prior snapshot -8.90%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 810695.3692, OI change vs prior snapshot -18.57%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.8s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.9s)
