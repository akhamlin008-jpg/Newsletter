# Data snapshot 2026-09-21 09:54 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** crypto (max |z| 2.68), commodities (max |z| 2.57)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.738 | 09-21 09:54 | **LIVE (~0 min old)** | -0.50 bp | -0.09 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 4.972 | 09-21 09:54 | **LIVE (~0 min old)** | -2.40 bp | -0.54 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.234 | 09-21 09:54 | **LIVE (~0 min old)** | -1.90 bp | -0.63 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.610 | 09-17 close | official value for 2026-09-17 (not live) | -7.00 bp (vs 2026-09-16) | -1.81 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.330 | 09-18 close | official value for 2026-09-18 (not live) | +0.00 bp (vs 2026-09-17) | 0.00 |  | fred:T10YIE |
| SOFR | 3.850 | 09-18 close | official value for 2026-09-18 (not live) | +0.00 bp (vs 2026-09-17) | 0.00 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (8.7s) |
| US dollar index (DXY) | 100.330 | 09-21 09:45 | **LIVE (~10 min old)** | +0.11 % (vs 2026-09-18) | 0.36 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.420 | 09-21 09:55 | **LIVE (~0 min old)** | +0.83 % (vs 2026-09-18) | 1.28 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.148 | 09-21 09:55 | **LIVE (~0 min old)** | -0.00 % (vs 2026-09-18) | -0.01 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 118.213 | 09-11 close | official value for 2026-09-11 (not live) | +0.11 % (vs 2026-09-10) | 0.54 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,768.250 | 09-21 09:45 | **LIVE (~10 min old)** | +1.45 % (vs 2026-09-18) | 2.24 | **YES** | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,359.500 | 09-21 09:45 | **LIVE (~10 min old)** | +2.52 % (vs 2026-09-18) | 2.49 | **YES** | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,893.300 | 09-21 09:45 | **LIVE (~10 min old)** | +0.70 % (vs 2026-09-18) | 0.87 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,705.120 | 09-21 09:55 | **LIVE (~0 min old)** | +0.71 % (vs 2026-09-18) | 1.09 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,110.584 | 09-21 09:55 | **LIVE (~0 min old)** | +1.57 % (vs 2026-09-18) | 1.53 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,874.104 | 09-21 09:40 | **LIVE (~15 min old)** | +0.48 % (vs 2026-09-18) | 0.60 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 14.880 | 09-21 09:39 | **LIVE (~15 min old)** | +0.07 pts | 0.06 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.1s) |
| WTI crude | 92.670 | 09-21 09:45 | **LIVE (~10 min old)** | -7.61 % (vs 2026-09-18) | -2.57 | **YES** | yahoo:CL=F (unofficial feed) |
| Brent crude | 100.640 | 09-21 09:45 | **LIVE (~10 min old)** | -3.11 % (vs 2026-09-18) | -1.08 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,388.700 | 09-21 09:45 | **LIVE (~10 min old)** | -0.82 % (vs 2026-09-18) | -0.62 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.808 | 09-21 09:45 | **LIVE (~10 min old)** | +2.92 % (vs 2026-09-18) | 1.82 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 85,409.29, 24h 6.07%, z 2.68 **FLAG**
- kraken: funding (raw, units unverified) 1.3144991331773048, OI 2181.719, OI change vs prior snapshot -1.53%
- hyperliquid: funding (raw, units unverified) 0.0000184043, OI 44961.39818, OI change vs prior snapshot 5.65%

**ETH**: price 2,730.00, 24h 5.82%, z 1.92
- kraken: funding (raw, units unverified) 0.01894699144800091, OI 30536.84, OI change vs prior snapshot -1.51%
- hyperliquid: funding (raw, units unverified) 0.0000312683, OI 1175417.9853999997, OI change vs prior snapshot 2.15%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (8.7s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.1s)
