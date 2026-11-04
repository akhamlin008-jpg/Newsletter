# Data snapshot 2026-11-04 11:12 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** crypto (max |z| 3.51), vol (max |z| 2.55)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.600 | 11-04 11:12 | **LIVE (~0 min old)** | -1.40 bp | -0.25 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.917 | 11-04 11:12 | **LIVE (~0 min old)** | -3.30 bp | -0.59 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.317 | 11-04 11:12 | **LIVE (~0 min old)** | -1.90 bp | -0.52 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.620 | 11-02 close | official value for 2026-11-02 (not live) | +2.00 bp (vs 2026-10-30) | 0.43 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.300 | 11-03 close | official value for 2026-11-03 (not live) | +1.00 bp (vs 2026-11-02) | 0.43 |  | fred:T10YIE |
| SOFR | 3.970 | 11-03 close | official value for 2026-11-03 (not live) | +2.00 bp (vs 2026-11-02) | 0.79 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.1s) |
| US dollar index (DXY) | 101.492 | 11-04 11:02 | **LIVE (~11 min old)** | -0.37 % (vs 2026-11-03) | -1.45 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.501 | 11-04 11:12 | **LIVE (~1 min old)** | +0.37 % (vs 2026-11-03) | 0.96 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.123 | 11-04 11:12 | **LIVE (~1 min old)** | +0.35 % (vs 2026-11-03) | 1.31 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.666 | 10-30 close | official value for 2026-10-30 (not live) | -0.06 % (vs 2026-10-29) | -0.25 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,718.250 | 11-04 11:02 | **LIVE (~11 min old)** | +1.60 % (vs 2026-11-03) | 2.25 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,647.000 | 11-04 11:02 | **LIVE (~11 min old)** | +1.21 % (vs 2026-11-03) | 0.86 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,853.900 | 11-04 11:02 | **LIVE (~11 min old)** | +1.02 % (vs 2026-11-03) | 1.15 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,683.810 | 11-04 11:12 | **LIVE (~1 min old)** | +1.52 % (vs 2026-11-03) | 2.10 | **YES** | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,502.314 | 11-04 11:12 | **LIVE (~1 min old)** | +1.14 % (vs 2026-11-03) | 0.80 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,838.818 | 11-04 10:57 | **LIVE (~16 min old)** | +0.94 % (vs 2026-11-03) | 1.05 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.660 | 11-04 10:56 | **LIVE (~16 min old)** | -3.17 pts | -2.55 | **YES** | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.0s) |
| WTI crude | 91.840 | 11-04 11:02 | **LIVE (~11 min old)** | -4.42 % (vs 2026-11-03) | -1.50 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 98.900 | 11-04 11:02 | **LIVE (~11 min old)** | -4.54 % (vs 2026-11-03) | -1.37 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,058.900 | 11-04 11:02 | **LIVE (~11 min old)** | +3.01 % (vs 2026-11-03) | 2.25 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.403 | 11-04 11:02 | **LIVE (~11 min old)** | +0.38 % (vs 2026-11-03) | 0.27 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 80,564.45, 24h 3.79%, z 2.33 **FLAG**
- kraken: funding (raw, units unverified) 1.27431886974236, OI 2368.3892, OI change vs prior snapshot 0.20%
- hyperliquid: funding (raw, units unverified) 0.0000047299, OI 40770.61858, OI change vs prior snapshot -1.40%

**ETH**: price 2,444.18, 24h 6.52%, z 3.51 **FLAG**
- kraken: funding (raw, units unverified) 0.037388125874, OI 27628.556, OI change vs prior snapshot -4.31%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1036787.3634, OI change vs prior snapshot 0.35%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (9.0s)
