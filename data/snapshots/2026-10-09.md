# Data snapshot 2026-10-09 10:37 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** commodities (max |z| 2.17)

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.806 | 10-09 10:37 | **LIVE (~1 min old)** | +5.00 bp | 0.83 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.274 | 10-09 10:37 | **LIVE (~1 min old)** | +4.10 bp | 0.82 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.468 | 10-09 10:37 | **LIVE (~1 min old)** | -0.90 bp | -0.26 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.920 | 10-07 close | official value for 2026-10-07 (not live) | +1.00 bp (vs 2026-10-06) | 0.20 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.350 | 10-08 close | official value for 2026-10-08 (not live) | -1.00 bp (vs 2026-10-07) | -0.61 |  | fred:T10YIE |
| SOFR | 3.870 | 10-08 close | official value for 2026-10-08 (not live) | -1.00 bp (vs 2026-10-07) | -0.26 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (16.6s) |
| US dollar index (DXY) | 102.283 | 10-09 10:27 | **LIVE (~11 min old)** | +0.14 % (vs 2026-10-08) | 0.46 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.342 | 10-09 10:37 | **LIVE (~1 min old)** | +0.18 % (vs 2026-10-08) | 0.37 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.120 | 10-09 10:37 | **LIVE (~1 min old)** | -0.01 % (vs 2026-10-08) | -0.02 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.385 | 10-02 close | official value for 2026-10-02 (not live) | -0.33 % (vs 2026-10-01) | -1.17 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,841.500 | 10-09 10:28 | **LIVE (~10 min old)** | +0.32 % (vs 2026-10-08) | 0.58 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 31,054.750 | 10-09 10:28 | **LIVE (~10 min old)** | +0.28 % (vs 2026-10-08) | 0.32 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,818.500 | 10-09 10:28 | **LIVE (~10 min old)** | +0.32 % (vs 2026-10-08) | 0.41 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,791.470 | 10-09 10:38 | **LIVE (~0 min old)** | +0.34 % (vs 2026-10-08) | 0.55 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 30,830.836 | 10-09 10:38 | **LIVE (~0 min old)** | +0.34 % (vs 2026-10-08) | 0.35 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,803.733 | 10-09 10:22 | **LIVE (~16 min old)** | +0.34 % (vs 2026-10-08) | 0.45 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.090 | 10-09 10:22 | **LIVE (~16 min old)** | -0.32 pts | -0.38 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.7s) |
| WTI crude | 91.370 | 10-09 10:28 | **LIVE (~10 min old)** | -0.13 % (vs 2026-10-08) | -0.05 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 104.080 | 10-09 10:27 | **LIVE (~11 min old)** | -0.19 % (vs 2026-10-08) | -0.08 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,208.100 | 10-09 10:28 | **LIVE (~10 min old)** | +1.23 % (vs 2026-10-08) | 1.03 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.699 | 10-09 10:28 | **LIVE (~10 min old)** | +2.75 % (vs 2026-10-08) | 2.17 | **YES** | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 83,080.50, 24h 0.53%, z 0.28
- kraken: funding (raw, units unverified) 0.790161069346, OI 2372.0169, OI change vs prior snapshot 0.71%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 39061.13422, OI change vs prior snapshot -0.08%

**ETH**: price 2,493.12, 24h -1.44%, z -0.59
- kraken: funding (raw, units unverified) 0.003441437169749173, OI 28657.963, OI change vs prior snapshot -0.57%
- hyperliquid: funding (raw, units unverified) 0.000011323, OI 1121805.9098000003, OI change vs prior snapshot 0.56%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (16.6s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (7.7s)
