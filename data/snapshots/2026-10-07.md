# Data snapshot 2026-10-07 10:43 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** crypto (max |z| 2.84)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.787 | 10-07 10:43 | **LIVE (~0 min old)** | -0.40 bp | -0.06 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.316 | 10-07 10:43 | **LIVE (~0 min old)** | +4.50 bp | 0.86 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.529 | 10-07 10:43 | **LIVE (~0 min old)** | +4.90 bp | 1.42 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.950 | 10-05 close | official value for 2026-10-05 (not live) | +3.00 bp (vs 2026-10-02) | 0.58 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 10-06 close | official value for 2026-10-06 (not live) | +0.00 bp (vs 2026-10-05) | 0.00 |  | fred:T10YIE |
| SOFR | 3.900 | 10-06 close | official value for 2026-10-06 (not live) | +1.00 bp (vs 2026-10-05) | 0.24 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (16.4s) |
| US dollar index (DXY) | 102.324 | 10-07 10:33 | **LIVE (~11 min old)** | +0.49 % (vs 2026-10-06) | 1.57 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.154 | 10-07 10:43 | **LIVE (~1 min old)** | +0.12 % (vs 2026-10-06) | 0.24 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.119 | 10-07 10:43 | **LIVE (~1 min old)** | -0.22 % (vs 2026-10-06) | -0.76 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.385 | 10-02 close | official value for 2026-10-02 (not live) | -0.33 % (vs 2026-10-01) | -1.17 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,825.500 | 10-07 10:33 | **LIVE (~11 min old)** | -0.62 % (vs 2026-10-06) | -1.06 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 31,244.500 | 10-07 10:33 | **LIVE (~11 min old)** | -0.76 % (vs 2026-10-06) | -0.89 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,813.100 | 10-07 10:33 | **LIVE (~11 min old)** | -1.23 % (vs 2026-10-06) | -1.61 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,769.080 | 10-07 10:43 | **LIVE (~1 min old)** | -0.64 % (vs 2026-10-06) | -1.00 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 31,016.316 | 10-07 10:43 | **LIVE (~1 min old)** | -0.67 % (vs 2026-10-06) | -0.68 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,795.400 | 10-07 10:28 | **LIVE (~16 min old)** | -1.23 % (vs 2026-10-06) | -1.66 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.700 | 10-07 10:28 | **LIVE (~15 min old)** | +0.69 pts | 0.77 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (13.5s) |
| WTI crude | 89.630 | 10-07 10:33 | **LIVE (~11 min old)** | +0.21 % (vs 2026-10-06) | 0.08 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 101.600 | 10-07 10:34 | **LIVE (~10 min old)** | +1.01 % (vs 2026-10-06) | 0.41 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,131.000 | 10-07 10:34 | **LIVE (~10 min old)** | -1.34 % (vs 2026-10-06) | -1.08 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.646 | 10-07 10:33 | **LIVE (~11 min old)** | +0.77 % (vs 2026-10-06) | 0.59 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 82,955.57, 24h -4.21%, z -2.23 **FLAG**
- kraken: funding (raw, units unverified) 0.19360569036505562, OI 2254.1483, OI change vs prior snapshot 0.06%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 39798.90386, OI change vs prior snapshot -0.45%

**ETH**: price 2,558.01, 24h -6.02%, z -2.84 **FLAG**
- kraken: funding (raw, units unverified) 0.012670799078749144, OI 30164.091, OI change vs prior snapshot 0.34%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1176630.5298000001, OI change vs prior snapshot -0.08%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (16.4s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (13.5s)
