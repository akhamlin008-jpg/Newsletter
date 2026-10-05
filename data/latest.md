# Data snapshot 2026-10-05 13:05 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.852 | 10-05 13:04 | **LIVE (~1 min old)** | +2.70 bp | 0.41 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.343 | 10-05 13:05 | **LIVE (~0 min old)** | +6.60 bp | 1.21 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.491 | 10-05 13:04 | **LIVE (~1 min old)** | +3.90 bp | 1.08 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.880 | 10-01 close | official value for 2026-10-01 (not live) | -5.00 bp (vs 2026-09-30) | -0.96 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 10-02 close | official value for 2026-10-02 (not live) | +0.00 bp (vs 2026-10-01) | 0.00 |  | fred:T10YIE |
| SOFR | 3.880 | 10-02 close | official value for 2026-10-02 (not live) | +1.00 bp (vs 2026-10-01) | 0.23 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (14.7s) |
| US dollar index (DXY) | 102.238 | 10-05 12:55 | **LIVE (~11 min old)** | +0.30 % (vs 2026-10-02) | 0.97 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.118 | 10-05 13:05 | **LIVE (~1 min old)** | +0.12 % (vs 2026-10-02) | 0.22 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.120 | 10-05 13:05 | **LIVE (~1 min old)** | -0.41 % (vs 2026-10-02) | -1.39 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 120.330 | 09-25 close | official value for 2026-09-25 (not live) | -0.18 % (vs 2026-09-24) | -0.76 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,823.500 | 10-05 12:55 | **LIVE (~11 min old)** | +0.59 % (vs 2026-10-02) | 1.04 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 31,257.000 | 10-05 12:55 | **LIVE (~11 min old)** | +0.63 % (vs 2026-10-02) | 0.72 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,867.700 | 10-05 12:55 | **LIVE (~11 min old)** | +0.59 % (vs 2026-10-02) | 0.76 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,767.640 | 10-05 13:05 | **LIVE (~1 min old)** | +0.58 % (vs 2026-10-02) | 0.91 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,989.186 | 10-05 13:05 | **LIVE (~1 min old)** | +0.59 % (vs 2026-10-02) | 0.58 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,852.157 | 10-05 12:50 | **LIVE (~16 min old)** | +0.68 % (vs 2026-10-02) | 0.89 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.500 | 10-05 12:49 | **LIVE (~16 min old)** | +0.19 pts | 0.20 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (12.6s) |
| WTI crude | 90.060 | 10-05 12:55 | **LIVE (~11 min old)** | -1.15 % (vs 2026-10-02) | -0.42 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 100.820 | 10-05 12:55 | **LIVE (~11 min old)** | -1.40 % (vs 2026-10-02) | -0.54 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,159.300 | 10-05 12:55 | **LIVE (~11 min old)** | -0.07 % (vs 2026-10-02) | -0.06 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.638 | 10-05 12:55 | **LIVE (~11 min old)** | +2.26 % (vs 2026-10-02) | 1.68 |  | yahoo:HG=F (unofficial feed) |

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
- **Russell 2000 futures (RTY)**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open (possible rolls in recent history: 2026-09-21)
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

**BTC**: price 85,227.02, 24h -0.09%, z -0.04
- kraken: funding (raw, units unverified) -0.38251401537136176, OI 2095.3513, OI change vs prior snapshot -0.10%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 38161.977, OI change vs prior snapshot 0.23%

**ETH**: price 2,693.31, 24h -0.30%, z -0.13
- kraken: funding (raw, units unverified) -0.03159544701133423, OI 28942.698, OI change vs prior snapshot 0.71%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1194193.7448000002, OI change vs prior snapshot 0.12%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (14.7s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (12.6s)
