# Data snapshot 2026-11-19 11:29 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.821 | 11-19 11:29 | **LIVE (~0 min old)** | +2.10 bp | 0.30 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.080 | 11-19 11:29 | **LIVE (~0 min old)** | +1.40 bp | 0.24 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.259 | 11-19 11:29 | **LIVE (~0 min old)** | -0.70 bp | -0.20 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.890 | 11-17 close | official value for 2026-11-17 (not live) | -3.00 bp (vs 2026-11-16) | -0.59 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.190 | 11-18 close | official value for 2026-11-18 (not live) | -2.00 bp (vs 2026-11-17) | -0.83 |  | fred:T10YIE |
| SOFR | 3.900 | 11-18 close | official value for 2026-11-18 (not live) | -2.00 bp (vs 2026-11-17) | -0.88 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.3s) |
| US dollar index (DXY) | 103.835 | 11-19 11:19 | **LIVE (~11 min old)** | -0.02 % (vs 2026-11-18) | -0.07 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.860 | 11-19 11:29 | **LIVE (~1 min old)** | +0.22 % (vs 2026-11-18) | 0.61 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.098 | 11-19 11:29 | **LIVE (~1 min old)** | -0.13 % (vs 2026-11-18) | -0.38 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 122.650 | 11-13 close | official value for 2026-11-13 (not live) | +0.09 % (vs 2026-11-12) | 0.34 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,325.750 | 11-19 11:19 | **LIVE (~11 min old)** | -0.20 % (vs 2026-11-18) | -0.16 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,252.750 | 11-19 11:19 | **LIVE (~11 min old)** | +0.24 % (vs 2026-11-18) | 0.13 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,699.800 | 11-19 11:19 | **LIVE (~11 min old)** | -0.82 % (vs 2026-11-18) | -0.57 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,311.110 | 11-19 11:29 | **LIVE (~1 min old)** | -0.17 % (vs 2026-11-18) | -0.14 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,227.926 | 11-19 11:29 | **LIVE (~1 min old)** | +0.41 % (vs 2026-11-18) | 0.21 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,693.788 | 11-19 11:14 | **LIVE (~16 min old)** | -0.76 % (vs 2026-11-18) | -0.53 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 25.390 | 11-19 11:14 | **LIVE (~15 min old)** | +0.83 pts | 0.28 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s) |
| WTI crude | 83.390 | 11-19 11:19 | **LIVE (~11 min old)** | +0.16 % (vs 2026-11-18) | 0.05 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 90.010 | 11-19 11:18 | **LIVE (~12 min old)** | -2.11 % (vs 2026-11-18) | -0.63 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,681.000 | 11-19 11:19 | **LIVE (~11 min old)** | -1.63 % (vs 2026-11-18) | -1.01 |  | yahoo:GC=F (unofficial feed) |
| Copper | 5.651 | 11-19 11:19 | **LIVE (~11 min old)** | -0.16 % (vs 2026-11-18) | -0.08 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 62,980.06, 24h 0.46%, z 0.18
- kraken: funding (raw, units unverified) 0.4041618641654377, OI 2232.3172, OI change vs prior snapshot -3.07%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 38075.12886, OI change vs prior snapshot -5.28%

**ETH**: price 1,774.97, 24h 1.59%, z 0.49
- kraken: funding (raw, units unverified) -0.013325594019, OI 30270.432, OI change vs prior snapshot 0.83%
- hyperliquid: funding (raw, units unverified) 0.0000044349, OI 613371.9964000001, OI change vs prior snapshot -0.87%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.3s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s)
