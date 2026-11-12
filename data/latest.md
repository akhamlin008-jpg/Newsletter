# Data snapshot 2026-11-12 11:11 EST

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** dollar (max |z| 2.74), commodities (max |z| 2.18)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.837 | 11-12 11:11 | **LIVE (~0 min old)** | +11.00 bp | 1.90 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.068 | 11-12 11:11 | **LIVE (~0 min old)** | +7.90 bp | 1.50 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.231 | 11-12 11:11 | **LIVE (~0 min old)** | -3.10 bp | -0.78 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.660 | 11-09 close | official value for 2026-11-09 (not live) | +3.00 bp (vs 2026-11-06) | 0.70 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.200 | 11-10 close | official value for 2026-11-10 (not live) | -2.00 bp (vs 2026-11-09) | -0.87 |  | fred:T10YIE |
| SOFR | 3.890 | 11-10 close | official value for 2026-11-10 (not live) | +1.00 bp (vs 2026-11-09) | 0.41 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.2s) |
| US dollar index (DXY) | 103.118 | 11-12 11:01 | **LIVE (~10 min old)** | +0.20 % (vs 2026-11-11) | 0.53 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 159.949 | 11-12 11:11 | **LIVE (~0 min old)** | +0.78 % (vs 2026-11-11) | 2.02 | **YES** | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.106 | 11-12 11:10 | **LIVE (~1 min old)** | -0.95 % (vs 2026-11-11) | -2.74 | **YES** | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.880 | 11-06 close | official value for 2026-11-06 (not live) | +0.31 % (vs 2026-11-05) | 1.32 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,647.250 | 11-12 11:01 | **LIVE (~10 min old)** | +0.09 % (vs 2026-11-11) | 0.07 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 28,498.500 | 11-12 11:01 | **LIVE (~10 min old)** | +0.09 % (vs 2026-11-11) | 0.04 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,830.100 | 11-12 11:01 | **LIVE (~10 min old)** | -0.83 % (vs 2026-11-11) | -0.55 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,647.720 | 11-12 11:11 | **LIVE (~0 min old)** | +0.37 % (vs 2026-11-11) | 0.28 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 28,509.197 | 11-12 11:11 | **LIVE (~0 min old)** | +0.48 % (vs 2026-11-11) | 0.23 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,821.108 | 11-12 10:56 | **LIVE (~15 min old)** | -0.88 % (vs 2026-11-11) | -0.59 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 17.770 | 11-12 10:55 | **LIVE (~16 min old)** | +0.28 pts | 0.09 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.3s) |
| WTI crude | 86.620 | 11-12 11:01 | **LIVE (~10 min old)** | +0.10 % (vs 2026-11-11) | 0.03 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 93.460 | 11-12 11:01 | **LIVE (~10 min old)** | +0.75 % (vs 2026-11-11) | 0.20 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 3,872.800 | 11-12 11:01 | **LIVE (~10 min old)** | -3.19 % (vs 2026-11-11) | -2.18 | **YES** | yahoo:GC=F (unofficial feed) |
| Copper | 6.184 | 11-12 11:01 | **LIVE (~10 min old)** | -1.45 % (vs 2026-11-11) | -1.02 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 72,066.32, 24h -2.85%, z -1.45
- kraken: funding (raw, units unverified) 1.3483444539506428, OI 2573.2522, OI change vs prior snapshot -1.69%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 39703.0884399999, OI change vs prior snapshot 2.08%

**ETH**: price 2,023.87, 24h -2.48%, z -0.86
- kraken: funding (raw, units unverified) 0.03514575993487567, OI 29436.562, OI change vs prior snapshot -0.56%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 763601.3115999997, OI change vs prior snapshot 1.72%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.2s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.3s)
