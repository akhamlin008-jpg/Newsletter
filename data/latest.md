# Data snapshot 2026-09-16 00:49 EDT

Machine-generated. Numbers here are the only numbers the letter may use.

**Flagged groups (top two get commentary):** none

| Row | Value | As of | Change | z | Flag | Stale | Source |
|---|---|---|---|---|---|---|---|
| US 2-year yield | FAILED | | | | | | fred:DGS2 -> TimeoutError: The read operation timed out (17.4s) |
| US 10-year yield | FAILED | | | | | | fred:DGS10 -> TimeoutError: The read operation timed out (17.4s) |
| 2s10s spread | FAILED | | | | | | fred:T10Y2Y -> TimeoutError: The read operation timed out (17.4s) |
| 10-year real yield (TIPS) | FAILED | | | | | | fred:DFII10 -> TimeoutError: The read operation timed out (17.4s) |
| 10-year breakeven inflation | FAILED | | | | | | fred:T10YIE -> TimeoutError: The read operation timed out (17.4s) |
| SOFR | FAILED | | | | | | fred:SOFR -> TimeoutError: The read operation timed out (17.4s) |
| Broad trade-weighted dollar | FAILED | | | | | | fred:DTWEXBGS -> TimeoutError: The read operation timed out (17.4s) |
| USD/JPY | FAILED | | | | | | fred:DEXJPUS -> TimeoutError: The read operation timed out (17.4s) |
| EUR/USD | FAILED | | | | | | fred:DEXUSEU -> TimeoutError: The read operation timed out (17.4s) |
| S&P 500 index | FAILED | | | | | | fred:SP500 -> TimeoutError: The read operation timed out (17.4s); stooq:^spx -> unexpected Stooq response (no Close colu |
| Nasdaq 100 index | FAILED | | | | | | fred:NASDAQ100 -> TimeoutError: The read operation timed out (17.4s); stooq:^ndx -> unexpected Stooq response (no Close  |
| Russell 2000 index | FAILED | | | | | | stooq:^rut -> unexpected Stooq response (no Close column) (0.6s) |
| S&P 500 futures | FAILED | | | | | | stooq:es.f -> unexpected Stooq response (no Close column) (0.4s) |
| Nasdaq 100 futures | FAILED | | | | | | stooq:nq.f -> unexpected Stooq response (no Close column) (0.4s) |
| VIX | 17.200 | 2026-09-15 | +0.10 pts | 0.09 |  |  | cboe_vix:VIX |
| WTI crude | FAILED | | | | | | fred:DCOILWTICO -> TimeoutError: The read operation timed out (17.2s); stooq:cl.f -> unexpected Stooq response (no Close |
| Brent crude | FAILED | | | | | | fred:DCOILBRENTEU -> TimeoutError: The read operation timed out (17.2s); stooq:cb.f -> unexpected Stooq response (no Clo |
| Gold | FAILED | | | | | | stooq:xauusd -> unexpected Stooq response (no Close column) (0.4s); stooq:gc.f -> unexpected Stooq response (no Close co |
| Copper | FAILED | | | | | | stooq:hg.f -> unexpected Stooq response (no Close column) (0.4s) |

## Crypto

**BTC**: price 75,847.14, 24h -2.19%, z -1.04
- kraken: funding (raw, units unverified) 1.921204325624375, OI 2082.8221, OI change vs prior snapshot n/a%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 36042.98712, OI change vs prior snapshot n/a%

**ETH**: price 2,403.90, 24h -3.46%, z -1.16
- kraken: funding (raw, units unverified) 0.06732031537304087, OI 31774.828, OI change vs prior snapshot n/a%
- hyperliquid: funding (raw, units unverified) 0.0000092942, OI 955130.4976000004, OI change vs prior snapshot n/a%


## Source errors

- fred:DGS2 -> TimeoutError: The read operation timed out (17.4s)
- fred:DGS10 -> TimeoutError: The read operation timed out (17.4s)
- fred:T10Y2Y -> TimeoutError: The read operation timed out (17.4s)
- fred:DFII10 -> TimeoutError: The read operation timed out (17.4s)
- fred:T10YIE -> TimeoutError: The read operation timed out (17.4s)
- fred:SOFR -> TimeoutError: The read operation timed out (17.4s)
- fred:DTWEXBGS -> TimeoutError: The read operation timed out (17.4s)
- fred:DEXJPUS -> TimeoutError: The read operation timed out (17.4s)
- fred:DEXUSEU -> TimeoutError: The read operation timed out (17.4s)
- fred:SP500 -> TimeoutError: The read operation timed out (17.4s)
- stooq:^spx -> unexpected Stooq response (no Close column) (0.4s)
- fred:NASDAQ100 -> TimeoutError: The read operation timed out (17.4s)
- stooq:^ndx -> unexpected Stooq response (no Close column) (0.4s)
- stooq:^rut -> unexpected Stooq response (no Close column) (0.6s)
- stooq:es.f -> unexpected Stooq response (no Close column) (0.4s)
- stooq:nq.f -> unexpected Stooq response (no Close column) (0.4s)
- fred:VIXCLS -> TimeoutError: The read operation timed out (17.1s)
- fred:DCOILWTICO -> TimeoutError: The read operation timed out (17.2s)
- stooq:cl.f -> unexpected Stooq response (no Close column) (0.5s)
- fred:DCOILBRENTEU -> TimeoutError: The read operation timed out (17.2s)
- stooq:cb.f -> unexpected Stooq response (no Close column) (0.5s)
- stooq:xauusd -> unexpected Stooq response (no Close column) (0.4s)
- stooq:gc.f -> unexpected Stooq response (no Close column) (0.3s)
- stooq:hg.f -> unexpected Stooq response (no Close column) (0.4s)

Stale = more than one weekday old (market holidays not yet accounted for).
