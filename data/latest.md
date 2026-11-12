# Data snapshot 2026-11-12 11:45 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.83), commodities (max |z| 2.2)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.845 | 11-12 11:45 | **LIVE (~1 min old)** | +11.80 bp | 2.04 | **YES** | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.085 | 11-12 11:45 | **LIVE (~0 min old)** | +9.60 bp | 1.83 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.240 | 11-12 11:45 | **LIVE (~1 min old)** | -2.20 bp | -0.55 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.660 | 11-09 close | official value for 2026-11-09 (not live) | +3.00 bp (vs 2026-11-06) | 0.70 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.200 | 11-10 close | official value for 2026-11-10 (not live) | -2.00 bp (vs 2026-11-09) | -0.87 |  | fred:T10YIE |
| SOFR | 3.890 | 11-10 close | official value for 2026-11-10 (not live) | +1.00 bp (vs 2026-11-09) | 0.41 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.6s) |
| US dollar index (DXY) | 103.178 | 11-12 11:35 | **LIVE (~11 min old)** | +0.26 % (vs 2026-11-11) | 0.69 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.633 | 11-12 11:45 | **LIVE (~1 min old)** | +0.58 % (vs 2026-11-11) | 1.51 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.106 | 11-12 11:45 | **LIVE (~1 min old)** | -0.98 % (vs 2026-11-11) | -2.83 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,654.500 | 11-12 11:35 | **LIVE (~11 min old)** | +0.18 % (vs 2026-11-11) | 0.14 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,539.750 | 11-12 11:35 | **LIVE (~11 min old)** | +0.23 % (vs 2026-11-11) | 0.11 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,833.200 | 11-12 11:35 | **LIVE (~11 min old)** | -0.72 % (vs 2026-11-11) | -0.48 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,622.530 | 11-12 11:45 | **LIVE (~1 min old)** | +0.04 % (vs 2026-11-11) | 0.03 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,362.748 | 11-12 11:45 | **LIVE (~1 min old)** | -0.04 % (vs 2026-11-11) | -0.02 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,828.464 | 11-12 11:30 | **LIVE (~16 min old)** | -0.63 % (vs 2026-11-11) | -0.42 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.500 | 11-12 11:29 | **LIVE (~16 min old)** | +0.01 pts | 0.00 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.0s) |
| WTI crude | 86.980 | 11-12 11:35 | **LIVE (~11 min old)** | +0.52 % (vs 2026-11-11) | 0.16 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 93.850 | 11-12 11:35 | **LIVE (~11 min old)** | +1.18 % (vs 2026-11-11) | 0.32 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,871.800 | 11-12 11:35 | **LIVE (~11 min old)** | -3.22 % (vs 2026-11-11) | -2.20 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.178 | 11-12 11:35 | **LIVE (~11 min old)** | -1.54 % (vs 2026-11-11) | -1.08 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 71,450.46, 24h -3.68%, z -1.87
- kraken: funding (raw, units unverified) 1.3483444539506428, OI 2570.6007, OI change vs prior snapshot -0.10%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 39075.40112, OI change vs prior snapshot -1.58%

**ETH**: price 1,998.72, 24h -3.69%, z -1.28
- kraken: funding (raw, units unverified) 0.03514575993487567, OI 29483.947, OI change vs prior snapshot 0.16%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 750468.6740000001, OI change vs prior snapshot -1.72%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.6s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.0s)
