# Data snapshot 2026-09-28 11:18 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 3.25)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.939 | 09-28 11:18 | **LIVE (~0 min old)** | +7.50 bp | 1.20 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.257 | 09-28 11:18 | **LIVE (~1 min old)** | +7.60 bp | 1.31 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.318 | 09-28 11:18 | **LIVE (~0 min old)** | +0.10 bp | 0.03 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.850 | 09-24 close | official value for 2026-09-24 (not live) | +9.00 bp (vs 2026-09-23) | 1.71 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.340 | 09-25 close | official value for 2026-09-25 (not live) | +1.00 bp (vs 2026-09-24) | 0.47 |  | fred:T10YIE |
| SOFR | 3.900 | 09-25 close | official value for 2026-09-25 (not live) | +2.00 bp (vs 2026-09-24) | 0.41 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.5s) |
| US dollar index (DXY) | 101.230 | 09-28 11:08 | **LIVE (~11 min old)** | +0.26 % (vs 2026-09-25) | 0.84 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.453 | 09-28 11:19 | **LIVE (~0 min old)** | -0.86 % (vs 2026-09-25) | -1.45 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.137 | 09-28 11:18 | **LIVE (~1 min old)** | -0.04 % (vs 2026-09-25) | -0.15 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 119.513 | 09-18 close | official value for 2026-09-18 (not live) | +0.14 % (vs 2026-09-17) | 0.61 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,741.750 | 09-28 11:09 | **LIVE (~10 min old)** | -0.79 % (vs 2026-09-25) | -1.31 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,476.500 | 09-28 11:09 | **LIVE (~10 min old)** | -1.34 % (vs 2026-09-25) | -1.43 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,830.300 | 09-28 11:09 | **LIVE (~10 min old)** | -1.01 % (vs 2026-09-25) | -1.21 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,678.150 | 09-28 11:19 | **LIVE (~0 min old)** | -0.84 % (vs 2026-09-25) | -1.23 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,177.645 | 09-28 11:19 | **LIVE (~0 min old)** | -1.41 % (vs 2026-09-25) | -1.27 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,811.229 | 09-28 11:04 | **LIVE (~15 min old)** | -0.93 % (vs 2026-09-25) | -1.13 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 16.460 | 09-28 11:03 | **LIVE (~16 min old)** | +1.59 pts | 1.58 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.9s) |
| WTI crude | 95.520 | 09-28 11:09 | **LIVE (~10 min old)** | +3.37 % (vs 2026-09-25) | 1.15 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 100.140 | 09-28 11:09 | **LIVE (~10 min old)** | -4.01 % (vs 2026-09-25) | -1.38 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,153.300 | 09-28 11:09 | **LIVE (~10 min old)** | -3.89 % (vs 2026-09-25) | -3.25 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.622 | 09-28 11:09 | **LIVE (~10 min old)** | -1.10 % (vs 2026-09-25) | -0.76 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-21)
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-21)
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-18, 2026-09-21)
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures); live move vs prior close, scored against full-day volatility (approximate)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 82,824.44, 24h -1.92%, z -0.83
- kraken: funding (raw, units unverified) 0.6843644924087223, OI 2241.5026, OI change vs prior snapshot 0.39%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 36683.25352, OI change vs prior snapshot -0.25%

**ETH**: price 2,659.41, 24h -1.12%, z -0.41
- kraken: funding (raw, units unverified) 0.009728108023917555, OI 26494.797, OI change vs prior snapshot 0.20%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1103517.2778000019, OI change vs prior snapshot 0.26%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.5s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (6.9s)
