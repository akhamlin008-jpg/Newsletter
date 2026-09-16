# Data snapshot 2026-09-16 10:21 EDT

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
| Russell 2000 index | FAILED | | | | | | stooq:^rut -> unexpected Stooq response (no Close column) (0.8s) |
| S&P 500 futures | FAILED | | | | | | stooq:es.f -> unexpected Stooq response (no Close column) (0.6s) |
| Nasdaq 100 futures | FAILED | | | | | | stooq:nq.f -> unexpected Stooq response (no Close column) (0.5s) |
| VIX | 17.200 | 2026-09-15 | +0.10 pts | 0.09 |  |  | cboe_vix:VIX |
| WTI crude | FAILED | | | | | | fred:DCOILWTICO -> TimeoutError: The read operation timed out (17.1s); stooq:cl.f -> unexpected Stooq response (no Close |
| Brent crude | FAILED | | | | | | fred:DCOILBRENTEU -> TimeoutError: The read operation timed out (17.1s); stooq:cb.f -> unexpected Stooq response (no Clo |
| Gold | FAILED | | | | | | stooq:xauusd -> unexpected Stooq response (no Close column) (0.5s); stooq:gc.f -> unexpected Stooq response (no Close co |
| Copper | FAILED | | | | | | stooq:hg.f -> unexpected Stooq response (no Close column) (0.5s) |

## Crypto

**BTC**: price 75,547.68, 24h -0.42%, z -0.20
- kraken: funding (raw, units unverified) 1.0315933397329748, OI 2087.2689, OI change vs prior snapshot 0.21%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 37186.03468, OI change vs prior snapshot 3.17%

**ETH**: price 2,389.31, 24h -0.71%, z -0.24
- kraken: funding (raw, units unverified) 0.022614760209584132, OI 31566.588, OI change vs prior snapshot -0.66%
- hyperliquid: funding (raw, units unverified) 0.0000125, OI 982280.6186000002, OI change vs prior snapshot 2.84%


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
- stooq:^spx -> unexpected Stooq response (no Close column) (0.5s)
- fred:NASDAQ100 -> TimeoutError: The read operation timed out (17.4s)
- stooq:^ndx -> unexpected Stooq response (no Close column) (0.5s)
- stooq:^rut -> unexpected Stooq response (no Close column) (0.8s)
- stooq:es.f -> unexpected Stooq response (no Close column) (0.6s)
- stooq:nq.f -> unexpected Stooq response (no Close column) (0.5s)
- fred:VIXCLS -> TimeoutError: The read operation timed out (17.0s)
- fred:DCOILWTICO -> TimeoutError: The read operation timed out (17.1s)
- stooq:cl.f -> unexpected Stooq response (no Close column) (0.5s)
- fred:DCOILBRENTEU -> TimeoutError: The read operation timed out (17.1s)
- stooq:cb.f -> unexpected Stooq response (no Close column) (0.5s)
- stooq:xauusd -> unexpected Stooq response (no Close column) (0.5s)
- stooq:gc.f -> unexpected Stooq response (no Close column) (0.5s)
- stooq:hg.f -> unexpected Stooq response (no Close column) (0.5s)

Stale = more than one weekday old (market holidays not yet accounted for).
