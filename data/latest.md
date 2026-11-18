# Data snapshot 2026-11-18 12:11 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 4.03)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.781 | 11-18 12:09 | **LIVE (~2 min old)** | -0.80 bp | -0.11 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.062 | 11-18 12:11 | **LIVE (~0 min old)** | -4.10 bp | -0.68 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.281 | 11-18 12:09 | **LIVE (~2 min old)** | -3.30 bp | -0.91 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.920 | 11-16 close | official value for 2026-11-16 (not live) | +1.00 bp (vs 2026-11-13) | 0.19 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.210 | 11-17 close | official value for 2026-11-17 (not live) | +1.00 bp (vs 2026-11-16) | 0.41 |  | fred:T10YIE |
| SOFR | 3.920 | 11-17 close | official value for 2026-11-17 (not live) | -1.00 bp (vs 2026-11-16) | -0.44 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.2s) |
| US dollar index (DXY) | 103.819 | 11-18 12:01 | **LIVE (~10 min old)** | +0.32 % (vs 2026-11-17) | 0.92 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.280 | 11-18 12:11 | **LIVE (~0 min old)** | -0.15 % (vs 2026-11-17) | -0.41 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.097 | 11-18 12:10 | **LIVE (~1 min old)** | -0.24 % (vs 2026-11-17) | -0.66 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 122.650 | 11-13 close | official value for 2026-11-13 (not live) | +0.09 % (vs 2026-11-12) | 0.34 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,337.500 | 11-18 12:01 | **LIVE (~10 min old)** | -0.29 % (vs 2026-11-17) | -0.23 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 27,076.750 | 11-18 12:01 | **LIVE (~10 min old)** | +0.00 % (vs 2026-11-17) | 0.00 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,728.800 | 11-18 12:01 | **LIVE (~10 min old)** | +0.65 % (vs 2026-11-17) | 0.44 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,321.350 | 11-18 12:11 | **LIVE (~0 min old)** | -0.26 % (vs 2026-11-17) | -0.20 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 27,014.217 | 11-18 12:11 | **LIVE (~0 min old)** | +0.05 % (vs 2026-11-17) | 0.02 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,711.539 | 11-18 11:56 | **LIVE (~15 min old)** | +0.36 % (vs 2026-11-17) | 0.24 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 25.640 | 11-18 11:55 | **LIVE (~16 min old)** | +0.18 pts | 0.06 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.5s) |
| WTI crude | 81.300 | 11-18 12:01 | **LIVE (~10 min old)** | -5.48 % (vs 2026-11-17) | -1.82 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 87.730 | 11-18 12:01 | **LIVE (~10 min old)** | -5.81 % (vs 2026-11-17) | -1.69 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,750.300 | 11-18 12:01 | **LIVE (~10 min old)** | -2.95 % (vs 2026-11-17) | -2.02 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 5.639 | 11-18 12:01 | **LIVE (~10 min old)** | -5.63 % (vs 2026-11-17) | -4.03 | **YES** | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 62,636.60, 24h -1.76%, z -0.71
- kraken: funding (raw, units unverified) 0.6224905505000209, OI 2303.1154, OI change vs prior snapshot 0.49%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40198.75014, OI change vs prior snapshot -1.02%

**ETH**: price 1,749.33, 24h -2.05%, z -0.62
- kraken: funding (raw, units unverified) -0.007326797978666084, OI 30019.855, OI change vs prior snapshot 0.35%
- hyperliquid: funding (raw, units unverified) 0.0000016475, OI 618736.1947999997, OI change vs prior snapshot 0.15%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.5s)
