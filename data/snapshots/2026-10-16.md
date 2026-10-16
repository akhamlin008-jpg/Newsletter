# Data snapshot 2026-10-16 09:12 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** crypto (max |z| 2.23)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.763 | 10-16 09:12 | **LIVE (~0 min old)** | +1.20 bp | 0.22 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.117 | 10-16 09:11 | **LIVE (~0 min old)** | +3.00 bp | 0.63 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.354 | 10-16 09:11 | **LIVE (~0 min old)** | +1.80 bp | 0.51 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.840 | 10-14 close | official value for 2026-10-14 (not live) | -4.00 bp (vs 2026-10-13) | -0.85 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.320 | 10-15 close | official value for 2026-10-15 (not live) | -3.00 bp (vs 2026-10-14) | -1.85 |  | fred:T10YIE |
| SOFR | 3.890 | 10-15 close | official value for 2026-10-15 (not live) | +1.00 bp (vs 2026-10-14) | 0.29 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (9.9s) |
| US dollar index (DXY) | 101.779 | 10-16 09:02 | **LIVE (~10 min old)** | -0.22 % (vs 2026-10-15) | -0.66 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.055 | 10-16 09:12 | **LIVE (~0 min old)** | +0.06 % (vs 2026-10-15) | 0.15 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.125 | 10-16 09:11 | **LIVE (~1 min old)** | +0.47 % (vs 2026-10-15) | 1.57 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.602 | 10-09 close | official value for 2026-10-09 (not live) | +0.13 % (vs 2026-10-08) | 0.46 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,803.250 | 10-16 09:02 | **LIVE (~10 min old)** | +0.16 % (vs 2026-10-15) | 0.28 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 30,062.500 | 10-16 09:02 | **LIVE (~10 min old)** | -0.27 % (vs 2026-10-15) | -0.30 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,785.700 | 10-16 09:02 | **LIVE (~10 min old)** | +0.14 % (vs 2026-10-15) | 0.16 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,744.060 | 10-15 16:33 | not trading now; last trade 10-15 16:33 ET | +0.33 % (vs 2026-10-14) | 0.52 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 29,935.594 | 10-15 17:16 | not trading now; last trade 10-15 17:16 ET | -0.05 % (vs 2026-10-14) | -0.05 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,767.269 | 10-15 16:30 | not trading now; last trade 10-15 16:30 ET | +1.38 % (vs 2026-10-14) | 1.64 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.970 | 10-16 08:57 | **LIVE (~15 min old)** | -0.49 pts (vs 2026-10-15) | -0.58 |  | yahoo:^VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s) |
| WTI crude | 95.860 | 10-16 09:02 | **LIVE (~10 min old)** | -2.15 % (vs 2026-10-15) | -0.88 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 105.960 | 10-16 09:02 | **LIVE (~10 min old)** | +0.04 % (vs 2026-10-15) | 0.02 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,190.200 | 10-16 09:02 | **LIVE (~10 min old)** | +0.48 % (vs 2026-10-15) | 0.40 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.631 | 10-16 09:02 | **LIVE (~10 min old)** | +1.84 % (vs 2026-10-15) | 1.47 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 81,904.15, 24h 2.26%, z 1.27
- kraken: funding (raw, units unverified) 2.0280701861541393, OI 2265.895, OI change vs prior snapshot -0.50%
- hyperliquid: funding (raw, units unverified) 0.000012393, OI 42031.32078, OI change vs prior snapshot -0.06%

**ETH**: price 2,459.26, 24h 5.21%, z 2.23 **FLAG**
- kraken: funding (raw, units unverified) 0.0252401500575, OI 27708.053, OI change vs prior snapshot 0.13%
- hyperliquid: funding (raw, units unverified) 0.0000094883, OI 1090102.6224000002, OI change vs prior snapshot 0.21%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (9.9s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.9s)
