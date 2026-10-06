# Data snapshot 2026-10-06 11:03 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

Status: LIVE = a trade within the last 60 min (free feeds are typically ~10-15 min delayed). Anything else is labeled with the date it refers to.

| Row | Value | Data time (ET) | Status | Change vs prior close | z | Flag | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | 4.779 | 10-06 11:03 | **LIVE (~0 min old)** | -5.40 bp | -0.84 |  | cnbc:US2Y (unofficial feed) |
| US 10-year yield | 5.260 | 10-06 11:03 | **LIVE (~0 min old)** | -5.10 bp | -0.95 |  | cnbc:US10Y (unofficial feed) |
| 2s10s spread (10Y minus 2Y) | 0.481 | 10-06 11:03 | **LIVE (~0 min old)** | +0.30 bp | 0.08 |  | calc: cnbc:US10Y minus cnbc:US2Y (unofficial feed) |
| 10-year real yield (TIPS) | 2.920 | 10-02 close | official value for 2026-10-02 (not live) | +4.00 bp (vs 2026-10-01) | 0.77 |  | fred:DFII10 |
| 10-year breakeven inflation | 2.360 | 10-05 close | official value for 2026-10-05 (not live) | +0.00 bp (vs 2026-10-02) | 0.00 |  | fred:T10YIE |
| SOFR | 3.890 | 10-05 close | official value for 2026-10-05 (not live) | +1.00 bp (vs 2026-10-02) | 0.24 |  | nyfed:SOFR |
| 3M SOFR futures implied rate (front) | FAILED | | | | | | yahoo:SR3=F -> no prior close before the current session (10.7s) |
| US dollar index (DXY) | 101.857 | 10-06 10:53 | **LIVE (~11 min old)** | -0.31 % (vs 2026-10-05) | -1.00 |  | yahoo:DX-Y.NYB (unofficial feed) |
| USD/JPY | 158.064 | 10-06 11:03 | **LIVE (~1 min old)** | +0.21 % (vs 2026-10-05) | 0.40 |  | yahoo:JPY=X (unofficial feed) |
| EUR/USD | 1.126 | 10-06 11:03 | **LIVE (~1 min old)** | +0.06 % (vs 2026-10-05) | 0.21 |  | yahoo:EURUSD=X (unofficial feed) |
| Broad trade-weighted dollar | 121.385 | 10-02 close | official value for 2026-10-02 (not live) | -0.33 % (vs 2026-10-01) | -1.17 |  | fred:DTWEXBGS |
| S&P 500 futures (ES) | 7,884.000 | 10-06 10:53 | **LIVE (~11 min old)** | +0.74 % (vs 2026-10-05) | 1.28 |  | yahoo:ES=F (unofficial feed) |
| Nasdaq 100 futures (NQ) | 31,580.750 | 10-06 10:53 | **LIVE (~11 min old)** | +0.84 % (vs 2026-10-05) | 0.97 |  | yahoo:NQ=F (unofficial feed) |
| Russell 2000 futures (RTY) | 2,860.200 | 10-06 10:53 | **LIVE (~11 min old)** | -0.27 % (vs 2026-10-05) | -0.34 |  | yahoo:RTY=F (unofficial feed) |
| S&P 500 index (cash) | 7,834.660 | 10-06 11:03 | **LIVE (~1 min old)** | +0.78 % (vs 2026-10-05) | 1.22 |  | yahoo:^GSPC (unofficial feed) |
| Nasdaq 100 index (cash) | 31,336.598 | 10-06 11:03 | **LIVE (~1 min old)** | +0.84 % (vs 2026-10-05) | 0.83 |  | yahoo:^NDX (unofficial feed) |
| Russell 2000 index (cash) | 2,836.203 | 10-06 10:48 | **LIVE (~16 min old)** | -0.38 % (vs 2026-10-05) | -0.51 |  | yahoo:^RUT (unofficial feed) |
| VIX (spot) | 15.410 | 10-06 10:48 | **LIVE (~15 min old)** | -0.11 pts | -0.12 |  | cboe:VIX (unofficial feed) |
| VIX futures (front month) | FAILED | | | | | | yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s) |
| WTI crude | 87.860 | 10-06 10:53 | **LIVE (~11 min old)** | -1.76 % (vs 2026-10-05) | -0.65 |  | yahoo:CL=F (unofficial feed) |
| Brent crude | 98.250 | 10-06 10:53 | **LIVE (~11 min old)** | -2.06 % (vs 2026-10-05) | -0.81 |  | yahoo:BZ=F (unofficial feed) |
| Gold | 4,185.300 | 10-06 10:53 | **LIVE (~11 min old)** | +0.69 % (vs 2026-10-05) | 0.54 |  | yahoo:GC=F (unofficial feed) |
| Copper | 6.628 | 10-06 10:53 | **LIVE (~11 min old)** | +0.65 % (vs 2026-10-05) | 0.48 |  | yahoo:HG=F (unofficial feed) |

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

**BTC**: price 86,642.01, 24h 1.63%, z 0.84
- kraken: funding (raw, units unverified) 1.61818683315575, OI 2257.471, OI change vs prior snapshot 0.98%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 40276.8673000001, OI change vs prior snapshot 0.59%

**ETH**: price 2,720.41, 24h 0.87%, z 0.40
- kraken: funding (raw, units unverified) 0.02496460554525, OI 28400.533, OI change vs prior snapshot -0.57%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 1182394.8392, OI change vs prior snapshot 0.39%


## Source errors

- yahoo:SR3=F -> no prior close before the current session (10.7s)
- yahoo:VX=F -> YFTzMissingError: $VX=F: possibly delisted; no timezone found (8.5s)
