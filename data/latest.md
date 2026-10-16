# Data snapshot 2026-10-16 08:42 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** crypto (max |z| 2.26)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.751 | 10-16 08:41 | **LIVE (~1 min old)** | +0.00 bp | 0.00 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.100 | 10-16 08:41 | **LIVE (~1 min old)** | +1.30 bp | 0.27 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.349 | 10-16 08:41 | **LIVE (~1 min old)** | +1.30 bp | 0.37 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.840 | 10-14 close | official value for 2026-10-14 (not live) | -4.00 bp (vs 2026-10-13) | -0.85 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.320 | 10-15 close | official value for 2026-10-15 (not live) | -3.00 bp (vs 2026-10-14) | -1.85 |  | fred:T10YIE |
| SOFR | 3.890 | 10-15 close | official value for 2026-10-15 (not live) | +1.00 bp (vs 2026-10-14) | 0.29 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.4s) |
| US dollar index (DXY) | 101.730 | 10-16 08:32 | **LIVE (~10 min old)** | -0.26 % (vs 2026-10-15) | -0.80 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 157.968 | 10-16 08:42 | **LIVE (~0 min old)** | +0.01 % (vs 2026-10-15) | 0.02 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.125 | 10-16 08:41 | **LIVE (~1 min old)** | +0.49 % (vs 2026-10-15) | 1.65 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.602 | 10-09 close | official value for 2026-10-09 (not live) | +0.13 % (vs 2026-10-08) | 0.46 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,803.000 | 10-16 08:32 | **LIVE (~10 min old)** | +0.15 % (vs 2026-10-15) | 0.27 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,117.750 | 10-16 08:32 | **LIVE (~10 min old)** | -0.09 % (vs 2026-10-15) | -0.10 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,785.500 | 10-16 08:32 | **LIVE (~10 min old)** | +0.13 % (vs 2026-10-15) | 0.15 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,744.060 | 10-15 16:33 | not trading now; last trade 10-15 16:33 ET | +0.33 % (vs 2026-10-14) | 0.52 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,935.594 | 10-15 17:16 | not trading now; last trade 10-15 17:16 ET | -0.05 % (vs 2026-10-14) | -0.05 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,767.269 | 10-15 16:30 | not trading now; last trade 10-15 16:30 ET | +1.38 % (vs 2026-10-14) | 1.64 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 16.020 | 10-16 08:27 | **LIVE (~15 min old)** | -0.44 pts (vs 2026-10-15) | -0.52 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.0s) |
| WTI crude | 95.740 | 10-16 08:32 | **LIVE (~10 min old)** | -2.28 % (vs 2026-10-15) | -0.93 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 105.860 | 10-16 08:32 | **LIVE (~10 min old)** | -0.06 % (vs 2026-10-15) | -0.03 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,198.100 | 10-16 08:32 | **LIVE (~10 min old)** | +0.67 % (vs 2026-10-15) | 0.55 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.633 | 10-16 08:32 | **LIVE (~10 min old)** | +1.86 % (vs 2026-10-15) | 1.48 |  | yahoo:HG=F (unofficial feed) |

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
- **S&P 500 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Nasdaq 100 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **Russell 2000 index (cash)**: cash index is only calculated 9:30-16:00 ET; before the open this is the prior close (use futures)
- **VIX (spot)**: Cboe publishes spot VIX overnight (~3:15-9:25 AM ET); some feeds show only the prior close; live move vs prior close, scored against full-day volatility (approximate)
- **VIX futures (front month)**: futures price, not the same number as spot VIX
- **WTI crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Brent crude**: live move vs prior close, scored against full-day volatility (approximate)
- **Gold**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open
- **Copper**: live move vs prior close, scored against full-day volatility (approximate); roll check: last completed session: ok; the live move vs prior close can't be checked before the cash open

## Crypto

**BTC**: price 82,220.15, 24h 2.21%, z 1.24
- kraken: funding (raw, units unverified) 2.0285177186093892, OI 2277.2404, OI change vs prior snapshot 0.70%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 42056.63284, OI change vs prior snapshot 0.44%

**ETH**: price 2,471.29, 24h 5.30%, z 2.26 **FLAG**
- kraken: funding (raw, units unverified) 0.02783860745604249, OI 27672.604, OI change vs prior snapshot 0.45%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1087794.2644000005, OI change vs prior snapshot -0.19%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.4s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.0s)
