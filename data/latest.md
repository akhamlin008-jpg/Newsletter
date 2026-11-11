# Data snapshot 2026-11-11 11:04 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 4.69), dollar (max |z| 3.22)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.748 | 11-10 17:05 | not trading now; last trade 11-10 17:05 ET | +20.10 bp | 3.47 | **YES** | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.998 | 11-11 10:49 | **LIVE (~16 min old)** | +1.50 bp (vs 2026-11-10) | 0.25 |  | yahoo:^TNX (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.250 | 11-10 17:05 | not trading now; last trade 11-10 17:05 ET | -18.60 bp | -4.69 | **YES** | calc: yahoo:^TNX minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.660 | 11-09 close | official value for 2026-11-09 (not live) | +3.00 bp (vs 2026-11-06) | 0.70 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.200 | 11-10 close | official value for 2026-11-10 (not live) | -2.00 bp (vs 2026-11-09) | -0.87 |  | fred:T10YIE |
| SOFR | 3.880 | 11-09 close | official value for 2026-11-09 (not live) | -1.00 bp (vs 2026-11-06) | -0.40 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.0s) |
| US dollar index (DXY) | 102.894 | 11-11 10:54 | **LIVE (~11 min old)** | +0.65 % (vs 2026-11-10) | 1.83 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.773 | 11-11 11:04 | **LIVE (~1 min old)** | +1.13 % (vs 2026-11-10) | 2.96 | **YES** | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.110 | 11-11 11:04 | **LIVE (~1 min old)** | -1.08 % (vs 2026-11-10) | -3.22 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,625.000 | 11-11 10:54 | **LIVE (~11 min old)** | +1.07 % (vs 2026-11-10) | 0.81 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,516.000 | 11-11 10:54 | **LIVE (~11 min old)** | +2.45 % (vs 2026-11-10) | 1.19 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,847.300 | 11-11 10:54 | **LIVE (~11 min old)** | +0.65 % (vs 2026-11-10) | 0.42 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,607.480 | 11-11 11:04 | **LIVE (~1 min old)** | +1.15 % (vs 2026-11-10) | 0.86 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,418.418 | 11-11 11:04 | **LIVE (~1 min old)** | +2.44 % (vs 2026-11-10) | 1.18 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,837.871 | 11-11 10:49 | **LIVE (~16 min old)** | +0.58 % (vs 2026-11-10) | 0.38 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.730 | 11-11 10:49 | **LIVE (~15 min old)** | -1.73 pts | -0.53 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (4.2s) |
| WTI crude | 88.420 | 11-11 10:54 | **LIVE (~11 min old)** | +2.77 % (vs 2026-11-10) | 0.83 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 94.350 | 11-11 10:54 | **LIVE (~11 min old)** | +3.13 % (vs 2026-11-10) | 0.83 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,009.300 | 11-11 10:54 | **LIVE (~11 min old)** | -0.52 % (vs 2026-11-10) | -0.35 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.285 | 11-11 10:54 | **LIVE (~11 min old)** | +1.05 % (vs 2026-11-10) | 0.72 |  | yahoo:HG=F (unofficial feed) |

## Row notes

- **US 10-year yield**: live move vs prior close, scored against full-day volatility (approximate); fell back after: yahoo:10Y=F -> no prior close before the current session (11.8s)
- **2s10s spread (10Y minus 2Y)**: legs come from different sources; spread is approximate
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

**BTC**: price 73,960.25, 24h 1.60%, z 0.79
- kraken: funding (raw, units unverified) 1.286021852060483, OI 2614.1616, OI change vs prior snapshot 0.16%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40495.15178, OI change vs prior snapshot -0.28%

**ETH**: price 2,072.64, 24h 2.78%, z 0.93
- kraken: funding (raw, units unverified) 0.04020030484983402, OI 29933.585, OI change vs prior snapshot 0.87%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 778495.8608000011, OI change vs prior snapshot -0.45%


## Source errors

- yahoo:10Y=F -> no prior close before the current session (11.8s)
- yahoo:SR3=F -> no prior close before the current session (9.0s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (4.2s)
