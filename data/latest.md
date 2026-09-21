# Data snapshot 2026-09-21 07:56 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** rates (max |z| 3.92), crypto (max |z| 2.39)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.705 | 09-21 07:56 | **LIVE (~1 min old)** | -3.80 bp | -0.69 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.947 | 09-21 07:56 | **LIVE (~0 min old)** | -4.90 bp | -1.10 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.242 | 09-21 07:56 | **LIVE (~1 min old)** | -1.10 bp | -0.37 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.610 | 09-17 close | official value for 2026-09-17 (not live) | -7.00 bp (vs 2026-09-16) | -1.81 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 09-18 close | official value for 2026-09-18 (not live) | +0.00 bp (vs 2026-09-17) | 0.00 |  | fred:T10YIE |
| SOFR | 3.850 | 09-17 close | official value for 2026-09-17 (not live) | +23.00 bp (vs 2026-09-16) | 3.92 | **YES** | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.1s) |
| US dollar index (DXY) | 100.238 | 09-21 07:46 | **LIVE (~11 min old)** | +0.02 % (vs 2026-09-18) | 0.06 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.204 | 09-21 07:56 | **LIVE (~1 min old)** | +0.69 % (vs 2026-09-18) | 1.07 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.149 | 09-21 07:56 | **LIVE (~1 min old)** | +0.16 % (vs 2026-09-18) | 0.57 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 118.213 | 09-11 close | official value for 2026-09-11 (not live) | +0.11 % (vs 2026-09-10) | 0.54 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,768.000 | 09-21 07:46 | **LIVE (~11 min old)** | +1.45 % (vs 2026-09-18) | 2.24 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,241.500 | 09-21 07:46 | **LIVE (~11 min old)** | +2.12 % (vs 2026-09-18) | 2.10 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,905.000 | 09-21 07:46 | **LIVE (~11 min old)** | +1.11 % (vs 2026-09-18) | 1.37 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,650.500 | 09-18 17:29 | not trading now; last trade 09-18 17:29 ET | +0.17 % (vs 2026-09-17) | 0.25 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,644.168 | 09-18 17:16 | not trading now; last trade 09-18 17:16 ET | +0.67 % (vs 2026-09-17) | 0.64 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,860.396 | 09-21 04:51 | not trading now; last trade 09-21 04:51 ET | -0.00 % (vs 2026-09-18) | -0.00 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 14.840 | 09-21 07:41 | **LIVE (~16 min old)** | +0.03 pts (vs 2026-09-18) | 0.03 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.6s) |
| WTI crude | 93.350 | 09-21 07:46 | **LIVE (~11 min old)** | -6.93 % (vs 2026-09-18) | -2.34 | **YES** | yahoo:CL=F (unofficial feed) |
| Brent crude | 96.930 | 09-21 07:45 | **LIVE (~12 min old)** | -6.68 % (vs 2026-09-18) | -2.31 | **YES** | yahoo:BZ=F (unofficial feed) |
| Gold | 4,405.000 | 09-21 07:46 | **LIVE (~11 min old)** | -0.45 % (vs 2026-09-18) | -0.34 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.811 | 09-21 07:46 | **LIVE (~11 min old)** | +2.97 % (vs 2026-09-18) | 1.85 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 futures (ES)**: live move vs prior close, scored against full-day volatility (approximate); quarterly roll window: roll date 2026-09-10, expiry 2026-09-18; a jump may be the contract switch; roll check: last completed session: latest change not checkable (reference has no close for that date yet); the live move vs prior close can't be checked before the cash open
- **Nasdaq 100 futures (NQ)**: live move vs prior close, scored against full-day volatility (approximate); quarterly roll window: roll date 2026-09-10, expiry 2026-09-18; a jump may be the contract switch; roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); quarterly roll window: roll date 2026-09-10, expiry 2026-09-18; a jump may be the contract switch; roll check: last completed session: POSSIBLE ROLL on latest change; flag suppressed; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-18)
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-16)
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 84,800.00, 24h 5.42%, z 2.39 **FLAG**
- kraken: funding (raw, units unverified) 1.368703944203972, OI 2215.5824, OI change vs prior snapshot 0.28%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42555.18196, OI change vs prior snapshot -0.00%

**ETH**: price 2,723.56, 24h 5.66%, z 1.87
- kraken: funding (raw, units unverified) 0.032825216744915765, OI 31004.476, OI change vs prior snapshot -0.20%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1150706.9742000001, OI change vs prior snapshot 0.12%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.1s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.6s)
