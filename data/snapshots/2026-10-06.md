# Data snapshot 2026-10-06 10:26 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.806 | 10-06 10:26 | **LIVE (~0 min old)** | -2.70 bp | -0.42 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.292 | 10-06 10:26 | **LIVE (~0 min old)** | -1.90 bp | -0.35 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.486 | 10-06 10:26 | **LIVE (~0 min old)** | +0.80 bp | 0.23 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.920 | 10-02 close | official value for 2026-10-02 (not live) | +4.00 bp (vs 2026-10-01) | 0.77 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 10-05 close | official value for 2026-10-05 (not live) | +0.00 bp (vs 2026-10-02) | 0.00 |  | fred:T10YIE |
| SOFR | 3.890 | 10-05 close | official value for 2026-10-05 (not live) | +1.00 bp (vs 2026-10-02) | 0.24 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (11.5s) |
| US dollar index (DXY) | 101.900 | 10-06 10:16 | **LIVE (~10 min old)** | -0.26 % (vs 2026-10-05) | -0.86 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.115 | 10-06 10:26 | **LIVE (~0 min old)** | +0.24 % (vs 2026-10-05) | 0.46 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.125 | 10-06 10:25 | **LIVE (~1 min old)** | -0.02 % (vs 2026-10-05) | -0.07 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.385 | 10-02 close | official value for 2026-10-02 (not live) | -0.33 % (vs 2026-10-01) | -1.17 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,883.500 | 10-06 10:16 | **LIVE (~10 min old)** | +0.73 % (vs 2026-10-05) | 1.27 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 31,562.750 | 10-06 10:16 | **LIVE (~10 min old)** | +0.78 % (vs 2026-10-05) | 0.90 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,862.400 | 10-06 10:16 | **LIVE (~10 min old)** | -0.19 % (vs 2026-10-05) | -0.24 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,820.080 | 10-06 10:26 | **LIVE (~0 min old)** | +0.59 % (vs 2026-10-05) | 0.93 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 31,276.584 | 10-06 10:26 | **LIVE (~0 min old)** | +0.64 % (vs 2026-10-05) | 0.64 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,846.825 | 10-06 10:11 | **LIVE (~15 min old)** | -0.01 % (vs 2026-10-05) | -0.01 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.480 | 10-06 10:10 | **LIVE (~16 min old)** | -0.04 pts | -0.04 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.4s) |
| WTI crude | 88.040 | 10-06 10:16 | **LIVE (~10 min old)** | -1.55 % (vs 2026-10-05) | -0.57 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 98.520 | 10-06 10:16 | **LIVE (~10 min old)** | -1.79 % (vs 2026-10-05) | -0.70 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,179.400 | 10-06 10:16 | **LIVE (~10 min old)** | +0.54 % (vs 2026-10-05) | 0.43 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.624 | 10-06 10:16 | **LIVE (~10 min old)** | +0.58 % (vs 2026-10-05) | 0.43 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 85,980.12, 24h 0.42%, z 0.22
- kraken: funding (raw, units unverified) 0.5593297700865, OI 2235.5786, OI change vs prior snapshot -1.53%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40039.67106, OI change vs prior snapshot -0.33%

**ETH**: price 2,707.40, 24h 0.15%, z 0.07
- kraken: funding (raw, units unverified) 0.013623785670167572, OI 28562.923, OI change vs prior snapshot -0.29%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1177785.4251999997, OI change vs prior snapshot 0.11%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (11.5s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.4s)
