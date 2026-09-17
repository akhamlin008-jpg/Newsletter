# Morning Letter: Phase 0 Charter

**Status:** Draft v0.2, September 15, 2026. Nothing here is in force until approved.
**Operating basis:** free project. No paid data, no options data, no paid tools. All roles may be held by one person.

**Notation used throughout:**
- **[YOU]** means a decision only you can make.
- **[VERIFY]** means a fact I believe is correct but have not confirmed against a primary source.
- **[TUNE]** means a starting value to be adjusted during the pilot and then frozen before live use.

---

## 0. Read this first

### What changed in v0.2 (free project)

- **No options data, permanently.** Trade ideas use only instruments whose value moves one-for-one with price: futures, ETFs, spot, and perpetual futures. Event-linked ideas are measured against how much prices *historically* moved on past event days, not against options prices (Section 4.2).
- **No paid data.** The dashboard is built from free sources by a free scheduled job (Section 9). Rates data will show the prior day's close, not overnight moves. Crypto is the only dependable overnight information; equity futures are included only if a free source holds up.
- **No named people required.** The charter defines jobs, not people. One person can do all of them (Section 3.2).
- **No fund strategy required.** The strategy-neutral dashboard is the permanent design, and the trend diagnostic is defined now (Section 6.2).
- **No consensus history.** Surprise thresholds use a free substitute until the project has collected its own consensus record (Section 4.4).

### Changes from the agreed plan (carried from v0.1)

Writing the rules out in full exposed four problems in what the PM and I agreed. Each needs the PM's sign-off.

**1. Probability buckets must go below 50%.**
- **What we agreed:** buckets of 55 / 65 / 75 / 85%.
- **The problem:** any trade whose target is farther away than its stop has a market-implied chance of success below 50% (see Section 4.2). A 2-to-1 trade starts at about 33%. With buckets that begin at 55%, we could only record "better than a coin flip" and could never express "35% on a 3-to-1 payoff," which is often the best kind of idea.
- **Proposed fix:** buckets of 15 / 25 / 35 / 45 / 55 / 65 / 75 / 85%.

**2. Event-map forecasts get a different reference.**
- **What we agreed:** score event-map forecasts against consensus and market-implied odds.
- **The problem:** most event-map lines are conditional ("if CPI beats by X, the 10-year yield rises"). No market prices that conditional probability. Consensus only defines what counts as a surprise; it is not a probability.
- **Proposed fix:** the reference is the historical frequency of that reaction, computed before launch and frozen (Section 4.4).

**3. The overconfidence stop rule uses an exact test.**
- **What we agreed:** the closing argument used a "three margins of error" rule.
- **The problem:** at 30 ideas and an 85% bucket, the normal approximation behind that rule is poor.
- **Proposed fix:** an exact binomial test at the equivalent threshold (Section 6.3).

**4. The premium-adjusted baseline is replaced.** It required options prices, which this project won't have. The replacement reference is built from realized (actual past) moves, so it contains no options premium to correct for (Section 4.2).

### A disclosure to keep in writing

The "analyst" is an AI system (Claude, made by Anthropic).
- **Starting sessions:** it does not start sessions on its own.
- **Knowledge limits:** its knowledge has a cutoff (roughly May 2026).
- **Data access:** it cannot pull live market data.
- **Review:** every output requires human review before distribution.
- **For counsel:** whether and how to disclose AI involvement to desk readers and to any external audience (Section 10).

---

## 1. Purpose and scope

**Product.** A written briefing for the trading desk, delivered by 7:00 AM ET each US trading day, readable in about two minutes. It carries at most one new trade idea per day, or states "no trade." It replaces the long morning meeting with a 10-minute huddle.

**In scope now:** the internal desk letter, post-event flashes, the Monday preview, and the Friday scorecard.

**Gated, not in scope until approved:**
- A public (external) version of the letter.
- A sleeve that trades the public ideas.
- Both require outside counsel's sign-off. You schedule a yes/no decision on the public version six months after internal launch **[YOU: date]**.

**Out of scope:**
- **Position sizing,** which stays with the PM and risk.
- **Access to the firm's positions.** The analyst never sees them.
- **Any use of non-public information.**

---

## 2. Product specification

### 2.1 Daily letter

- **Send time:** 7:00 AM ET, fixed. The send time does not move for events.
- **Length cap:** 500 words, excluding the dashboard table **[TUNE]**.

| # | Section | Rules |
|---|---|---|
| 1 | Open ideas | One line each: instrument, direction, current result in R (Section 4.1), days remaining to time stop. Maximum 4 open. |
| 2 | Today's idea or "no trade" | Uses the idea template (2.2). Published only if it passes the qualification rule (4.3) and fewer than 4 ideas are open. Otherwise it is logged as a shadow idea (4.5). |
| 3 | Risk to common exposures | What today could do to broad exposure types: duration, dollar, equity beta, volatility, commodities. A crowding line appears only with a named, measurable source. |
| 4 | Event map | Today's scheduled events: consensus, surprise threshold, expected reactions with probability buckets. Flow calendar items. At most one sentence on an overnight cause. |
| 5 | Dashboard | Machine-generated only. Commentary for at most two factor groups (Section 5). |

Two output labels are always kept distinct:
- **"No trade"** means nothing cleared the bar.
- **"No new idea (at cap)"** means an idea qualified, but 4 were already open.

### 2.2 Idea template (internal)

- **Thesis:** 2 to 3 sentences.
- **Instrument and why this instrument.** Linear instruments only: futures, ETFs, spot, perpetual futures. No options.
- **Entry, stop, target.**
- **Time stop:** a calendar date, at most 30 calendar days out **[TUNE]**.
- **Reward-to-risk:** target distance ÷ stop distance.
- **Our probability bucket vs. reference probability,** with the source of the reference.
- **Premium-side classification,** applied by rule (Section 4.6).
- **Conviction tier:** equal to the gap between our bucket and the reference, measured in bucket steps. The PM maps tiers to size.

The external version, if approved, is produced by deleting fields from the same draft; counsel decides which. It is never rewritten.

### 2.3 Flashes

- **Trigger list (closed):** FOMC decision, ECB decision, BoE decision, US CPI, US Employment Situation (payrolls), US PCE (Personal Income and Outlays). The trigger applies only when the event occurs after 7:00 AM ET.
- **BoJ:** decisions normally land during Tokyo hours, which is overnight in New York, so they go in the main letter **[VERIFY each meeting]**.
- **Merging:** listed events within 45 minutes of each other get one combined flash.
- **Additions:** at most 2 per day, each with a reason logged the prior evening.
- **Length cap:** 120 words.
- **Content:**
  - actual vs. consensus;
  - surprise size vs. threshold;
  - reaction vs. the typical historical move for that event (Section 4.2);
  - which event-map forecasts resolved and how;
  - one line on open ideas.

### 2.4 Weekly pieces

- **Monday:** week-ahead calendar, CFTC positioning (released Fridays for Tuesday positions **[VERIFY]**), fund flows, divergence flags that persisted.
- **Friday:** the scorecard (Section 6).

### 2.5 Degraded mode

If drafting or review fails by 6:55 AM, the machine-generated dashboard and calendar go out, headed "PRODUCTION FAILURE: no idea today." The prior evening's event map is still scored (Section 4.4).

Failure days are:
- excluded from the trade-idea skill score;
- counted in the reliability metric;
- reported separately for event days and quiet days.

---

## 3. Production schedule and roles

### 3.1 Daily timeline (ET)

| Time | Step | Owner |
|---|---|---|
| 6:00 to 8:00 PM prior evening (optional) | Evening session: next-day calendar, draft event map (frozen and timestamped at session end), flash additions with reasons. If skipped, the event map is frozen during the morning session, still before any 8:30 release. | Session operator starts it; analyst drafts |
| About 6:00 AM | Free data job runs and publishes the snapshot (Section 9) | Automated |
| 5:30 AM | Morning session: overnight events (including BoJ, UK data), idea decision, event-map updates (logged as amendments; the frozen version is what gets scored) | Session operator starts it; analyst drafts |
| 6:30 to 6:50 AM | Review: facts, premium classification, qualification check, word caps | Reviewer |
| 7:00 AM | Send internal letter (and external, if approved and cleared; otherwise the external version skips the day, with a logged reason) | Reviewer |
| After listed events | Flash | Session operator, analyst, reviewer |

### 3.2 Roles

These are jobs, not headcount. In a one-person project, you hold every role except the analyst's.

| Role | Responsibility | Why it can't be skipped |
|---|---|---|
| Analyst (AI) | Drafting, computations on supplied data, ledger entries | n/a |
| Session operator | Opens each session with the analyst | The analyst cannot start on its own |
| Reviewer | Reads the draft against the review checklist before it's used | Catches wrong numbers and rule breaks; AI output requires a human check |
| Decision-maker | Sizing (if anything is traded), go/no-go decisions | The analyst doesn't size positions |
| Data job owner | Keeps the free data job (Section 9) running | A broken job means a degraded-mode day |

**Backup:** if the only person is unavailable, the day is a production failure (Section 2.5). That is acceptable for a free project, as long as it's logged.

**Review checklist (self-review works):** every dashboard number came from the data file; the idea passes Section 4.3; the premium classification follows Section 4.6; word caps met; all [VERIFY] items for the day checked.

### 3.3 Huddle (10 minutes)

1. A named trader makes the case against today's idea (2 minutes).
2. Discussion of the idea.
3. The desk maps Section 3 to actual positions (not recorded in anything the analyst sees).

### 3.4 Calendar hazards (ops checklist)

**US–Europe clock-change mismatch weeks.** During these weeks, a BoE noon decision lands at about 8:00 AM ET and the ECB 14:15 CET decision at about 9:15 AM ET.
- **Autumn 2026: October 26 to 30.** Europe changes October 25; the US changes November 1.
  - Two secondary sources list an ECB decision on October 29 **[VERIFY on ecb.europa.eu]**.
  - The BoE schedule, per the PM's check, has no decision that week.
- **Spring 2027: March 15 to 26** (my calculation). The US changes March 14; Europe changes March 28.

**Release schedules.** US data release dates can be moved or delayed, as happens during government shutdowns. The data owner confirms the week's calendar every Friday.

**Holidays.** US market holidays and early closes are loaded into the calendar before each month.

**Fed blackout.** My understanding is that it begins the second Saturday before an FOMC meeting and ends the day after **[VERIFY against the Fed's policy]**.

---

## 4. Forecasts, references, and qualification

### 4.1 Units

- **R:** one unit of risk, equal to the distance from entry to stop. A trade that hits a target twice as far as the stop earns +2R; a trade that hits its stop earns −1R. R is how ideas of different sizes and instruments are compared.
- **Probability buckets:** 15, 25, 35, 45, 55, 65, 75, 85%. One bucket step is 10 percentage points.

### 4.2 What "success" means, and the reference probability

**Success** means the target is hit before the stop and before the time stop. Anything else is scored as failure for the probability score and at its actual R for the P&L track.

**Reference probability** is the market's rough fair chance of success. It is computed by the data owner's software, never estimated by hand:

- **Non-event ideas.**
  - **Method:** simulate the instrument's price with zero drift, using exponentially weighted realized volatility (decay 0.94) as the volatility input and the time stop as the horizon.
  - **Reference value:** the share of simulated paths that reach the target first.
  - **Sanity check:** with no time limit and zero drift, this equals stop distance ÷ (stop distance + target distance). A 2-to-1 trade gives 1 ÷ 3, about 33%. The time stop makes the simulated figure lower.
  - **Known limitations:** it ignores carry, drift, and fat tails. These are accepted for the headline score and revisited at the quarterly review.
- **Event-linked ideas** (the idea's outcome is driven by a scheduled event):
  - **Method:** the same simulation, but the size of the event-day move is drawn from that instrument's actual moves on past days with the same event type (for example, the last 5 years of CPI days), taken from free daily price history.
  - **Why this works without options:** the reference is built from what prices actually did, so it contains no options premium. The v0.1 concern (scoring premium collection as skill) mostly disappears.
  - **What we lose:** we can't see whether the market expected an unusually large move *this time*. The letter must say so when it matters (for example, "VIX is elevated going into CPI").
  - **Caveat:** about 12 events a year per type means a small sample; with 5 years, about 60 event days. The distribution is fixed before launch and updated once a year.
- **Inputs are recorded.** Every reference computation stores its inputs (price, volatility, source, timestamp, horizon, event-move sample if used, simulation seed) so it can be reproduced.

### 4.3 Qualification rule

An idea may be published only if both conditions hold:

1. **Gap:** our bucket is at least one step (10 points) away from the reference probability **[TUNE: step size]**.
2. **Positive expectation:** at our probability, expected R is positive: p × (target R) − (1 − p) × 1 > 0.

If our bucket is *below* the reference, the idea is expressed in the opposite direction, with its own levels and a new reference.

### 4.4 Event-map forecasts

- **Format:** "If [release] prints at least [threshold] above/below consensus, [instrument] moves [direction] by at least [size] within [window]," plus a probability bucket. Unconditional lines are also allowed ("[instrument] moves more than its typical move on this event").
- **Surprise threshold:** ideally, one standard deviation of past surprises (actual minus consensus). Free historical consensus data isn't reliably available, so:
  - **From day one,** each morning session records the consensus shown on a free calendar at freeze time, with source and timestamp. This builds our own consensus history.
  - **Until 24 releases are recorded,** the threshold is a substitute: 0.5 × the standard deviation of the release's month-to-month change, from free government data **[TUNE]**. Lines scored under the substitute are tagged so they can be analyzed separately.
- **Reference:** the historical frequency of the stated reaction given that size of surprise. It is computed before launch from at least 5 years of data where available, frozen, and updated on a fixed quarterly schedule.
- **Scoring:** conditional lines whose condition didn't occur are logged as "condition not met" and not scored. The version frozen at the end of the evening session is the one scored; morning amendments are scored separately as their own entries.

### 4.5 Shadow ideas

A qualifying idea that can't be published because 4 ideas are open is logged in full and scored, but not published and not traded. Shadow ideas are reported as a separate line on the Friday scorecard, with the same margins of error as published ideas. The open-ideas cap is only reconsidered at a scheduled quarterly review, not in response to a short run.

### 4.6 Premium-side classification rule

An idea is **premium-side** if any of these is true:

1. The idea is on the fixed carry list: long a higher-yielding currency funded in a lower-yielding one; short volatility ETFs or futures; long credit spread exposure (for example, high-yield bond ETFs against Treasuries); collecting positive perpetual funding.
2. The idea profits when an event's move is smaller than its historical typical move.

With no options, this list is short, and most ideas will be non-premium. The classification is still recorded because carry-style ideas tend to win small and often, then lose large, and the scorecard should show that separately.

Everything else is non-premium. The analyst applies the rule and the reviewer confirms it. Disputes are resolved by the PM and logged. Changes to the list happen only at a quarterly review.

---

## 5. Dashboard rules

**Rows (permanent, strategy-neutral).** Each row's free source and freshness are in Section 9. Rows are dropped if the Phase 1 test finds no dependable free source.
- **Rates (prior-day close):** US 2-year, US 10-year, 2s10s spread, 10-year real yield, 10-year breakeven inflation, SOFR.
- **Dollar:** broad trade-weighted dollar index (a free substitute for DXY), USDJPY, EURUSD.
- **Equity:** S&P 500, Nasdaq 100, Russell 2000 (futures if a free source holds up; otherwise ETF prior close).
- **Volatility:** VIX.
- **Commodities:** WTI, Brent, gold, copper.
- **Crypto (two rows, real time):**
  - BTC: price, 24-hour change, perpetual funding rate, open interest change.
  - ETH: the same fields.

Removed from v0.1: MOVE (no free source I know of), USDCNH (free sources I know of carry onshore CNY instead), VIX term-structure slope (pending a free source).

**Unusual-move score (z) for each row:**
- **Formula:** z = today's change ÷ σ.
- **σ (the volatility estimate):** the larger of two figures:
  - exponentially weighted realized volatility, with decay 0.94;
  - a floor equal to 0.5 × one-year realized volatility **[TUNE]**.

**Flags:**
- **Threshold:** a row flags at |z| ≥ 2.0 **[TUNE]**.
- **Chance flags:** under a normal distribution this happens about 4.6% of the time per row, so across about 25 rows expect roughly one chance flag a day. Real markets have fatter tails, which means more.
- **Grouping:** flags are grouped by factor (rates, dollar, equity, volatility, commodities, crypto), and only the two groups with the largest |z| get text. A flag gets text only if it connects to a thesis or to Section 3; otherwise it shows in the table alone.

**Event days:** each listed event's actual reaction is compared with the median historical move for that event type. The ratio is reported in the flash.

**Divergence flags:**
- **Pair list (fixed):**
  - 10-year real yield vs. gold;
  - 10-year breakeven inflation vs. WTI;
  - USDJPY vs. the US–Japan 2-year yield gap.
- **Method:** each pair is a regression of daily changes over the prior 120 trading days, excluding the last 5.
- **Flag:** when the 5-day cumulative residual has |z| ≥ 2.5. As a rough guide, that is about 1.2% per pair per day by chance, or roughly one chance flag a month across three pairs, ignoring the overlap between days.
- **Level-based pairs:** added only after passing a cointegration test (a check for a stable long-run relationship), re-tested quarterly.
- **Frequency:** divergence flags go in the Monday piece unless a divergence is itself the trade idea.

**Machine output only.** No number in the dashboard is typed by a person or by the analyst. Every row shows its source and timestamp.

---

## 6. Scoring

### 6.1 Headline skill score (trade ideas, published only)

- **Per idea:** d = (reference probability − outcome)² − (our probability − outcome)². Outcome is 1 for success and 0 otherwise.
- **Headline:** the average of d. Positive means we forecast better than the reference.
- **Uncertainty:** the Newey-West standard error, which adjusts for overlapping ideas, with lag = 21 trading days (the longest allowed time stop). Results are reported as the estimate with its 95% range.
- **Split:** event-linked ideas (against the historical event-move reference) and non-event ideas (against the zero-drift reference) are reported separately and combined.

### 6.2 Other tracks (Friday scorecard)

- **P&L in R (internal only):**
  - mean R, hit rate, average win, and average loss;
  - a 95% range using the same error method;
  - split by premium-side and non-premium ideas.
- **Event-map skill:** the same d formula against the historical-frequency reference, with standard errors clustered by event day.
- **Calibration table:** for each bucket, the number of forecasts, the share that came true, and the exact binomial p-value.
- **Diagnostics (not headline):**
  - shadow ideas;
  - the trend-rule baseline: for each idea, what a rule that simply follows the instrument's last 60 trading days of direction would have scored over the same horizon;
  - "no change from consensus" for event-map lines;
  - reliability, meaning the on-time rate and failure days split by event and quiet days.
- **Every result carries its sample size.** No result is shown without it.

### 6.3 Overconfidence stop rule

- **Trigger:** a bucket with at least 30 resolved forecasts whose hit rate differs from the bucket value with an exact binomial p-value below 0.0027. That is the same strictness as three standard deviations under a normal distribution.
- **Effect:** forecasting in that bucket's range pauses, and the method is reviewed within 5 trading days.
- **Caveat:** because 8 buckets are checked every week, false alarms will happen occasionally, plausibly around once a year. A trigger starts a review; it does not end the product.

### 6.4 Record integrity

- **Timestamps:** every entry is timestamped by the system before its outcome is knowable.
- **Append-only:** the ledger only grows. Corrections are new entries that reference the original and are never overwrites.
- **Storage:** a Git repository (Section 9). Each entry is committed when made. Note that commit dates can be edited by whoever commits, so the stronger timestamp is GitHub's own record of when a push arrived **[VERIFY how to export it]**. If the repository is public, the ledger becomes a public record; decide that deliberately **[YOU]**.

### 6.5 Ledger fields

- entry ID, created timestamp, type (trade, event-map, shadow), status (live, closed, shadow, no-trade, at-cap, production-failure, condition-not-met, reference-unavailable)
- thesis, instrument, rationale, direction
- entry, stop, target, time stop, reward-to-risk
- our bucket, reference probability, reference method and inputs, *k* if used
- qualification check result, premium classification, reviewer confirmation
- event ID and frozen event-map version, if applicable
- outcome, exit timestamp, exit price, R result, score d
- amendment links

---

## 7. Review criteria (decided now, applied later)

### 7.1 Pilot exit (about six weeks)

Proceed to internal live use if all of the following hold:
- **On time:** at least 95% of letters sent by 7:00 **[TUNE]**.
- **Failures:** at most 2 production-failure days, with none unexplained.
- **Accuracy:** zero dashboard numbers found typed by hand or wrong-sourced.
- **Flashes:** every listed event after 7:00 received one.
- **Data:** the free data job completed on at least 90% of days, and every dashboard row that failed more than twice has been fixed or dropped **[TUNE]**.

The pilot does **not** assess forecasting skill; the sample will be far too small.

### 7.2 Six months after internal launch (process)

- **Reliability:** on-time rate and failure rate against the pilot thresholds.
- **Use:** in a one-person project, a weekly one-line note: did the letter change a decision this week?
- **Decisions:** did it change decisions (short trader survey, documented examples)?
- **Stop rule:** has the overconfidence rule been triggered, and what did the review find?
- **Public version:** you decide yes or no.

### 7.3 Twelve months (judgment)

**Continue if:**
- the process criteria still hold;
- a review of every losing idea finds that the reasoning was sound, with losses from reasonable risks rather than errors;
- the desk reports continued use.

Statistical proof of skill is **not** required. The 95% range of the headline score is reported and is expected to include zero.

**Stop or rework if either holds:**
- the headline score is below zero with its entire 95% range below zero;
- the overconfidence rule triggered twice in the same bucket range.

### 7.4 Why no review can prove skill quickly

To confirm a true 55% success rate against 50% (5% one-sided significance, 80% power) takes roughly 620 independent ideas; with a two-sided test, roughly 780. At one idea per day, minus no-trade days and overlap, that is several years. Early reviews can catch overconfidence and operational failure; they cannot confirm a small edge.

---

## 8. Timeline (approximate; depends on approvals)

| Phase | Dates | Exit condition |
|---|---|---|
| 0. Charter | Sept 15 to Sept 29, 2026 | Charter approved; counsel engaged; roles named |
| 1. Build | Sept 29 to Oct 13 | Dashboard generator, ledger, reference simulator, templates tested; pre-launch parameters computed (Section 9.3) |
| 2. Silent pilot | Oct 13 to Nov 24 | Section 7.1. Includes the Oct 26 to 30 mismatch week and a likely ECB decision on Oct 29 **[VERIFY]**. Ends before the US Thanksgiving holiday (Nov 26). |
| 3. Internal live | After pilot review | Six-month review scheduled |
| 4. External and sleeve | After counsel sign-off and your decision | Counsel-approved procedures in place |

---

## 9. Data plan (free)

### 9.1 How data reaches the analyst

I tested my own environment on September 15, 2026: it can read files from GitHub, and it cannot reach FRED or the crypto exchange I tried. So the design is:

1. **A free GitHub repository** holds a small Python script and its output.
2. **GitHub Actions** (GitHub's built-in job scheduler) runs the script around 6:00 AM ET each weekday. It pulls the free sources below and commits one snapshot file.
3. **At the start of each session,** the analyst reads the snapshot directly from GitHub. No upload is needed.

**Things to know about this setup** (my understanding; **[VERIFY]** in Phase 1):
- Standard GitHub Actions runners are free for public repositories.
- Scheduled runs use UTC time and can start late when GitHub is busy, so the job is scheduled with margin.
- GitHub may disable scheduled jobs in public repositories after a long stretch without activity. The job's own daily commits should count as activity, but this should be confirmed.
- A **public** repository means anyone can see the snapshot. That's fine for public market data. Keep anything private (notes, anything you trade) out of it.
- The analyst still cannot start sessions. You open each one; the data is waiting.

### 9.2 Sources

All free. "Confidence" is my confidence that the source works as described, before Phase 1 testing.

| Rows | Free source | Freshness at 7:00 AM | Confidence |
|---|---|---|---|
| 2y, 10y, 2s10s, 10y real yield, 10y breakeven | FRED (St. Louis Fed) | Prior business day at best | High on availability; **[VERIFY]** exact update times |
| SOFR | NY Fed or FRED | Prior business day | High |
| Broad dollar index, USDJPY, EURUSD | FRED | Can lag by several days; I believe the Fed's daily FX rates are published weekly | Medium; may need another free FX source |
| WTI, Brent | FRED | Lags a few days | Medium |
| VIX | FRED or Cboe's free historical file | Prior close | Medium-high |
| Equity index, gold, copper | Free delayed quote services or ETF prices | Prior close, or delayed | **Low.** Many free quote services restrict automated collection in their terms, and unofficial tools break. This is the weakest link. |
| BTC, ETH price, perp funding, open interest | Public crypto exchange APIs | Real time | Medium. Some exchanges block US connections, and GitHub's servers may count as US. Test several venues. |
| CFTC positioning | CFTC | Weekly | High |
| Economic calendar and consensus | Free calendar sites, recorded daily by the analyst via web search | Current | Medium; methods vary by site and aren't always stated |

**Plain consequence:** at 7:00 AM, the free dashboard shows yesterday for rates, dollar, and commodities, and overnight information only for crypto (and equity futures, if a source holds up). The letter will say which rows are stale on each day.

### 9.3 Pre-launch computations (Phase 1, all from free daily history)

- **Event-day move distributions:** for each listed event type and each dashboard instrument, the actual moves on past event days, going back 5 years where the source allows.
- **Surprise substitutes:** the standard deviation of month-to-month change for each listed release.
- **Volatility floors and z thresholds:** for each row, with a chance-flag count on the prior year.
- **Divergence pairs:** the regression setup and chance-flag check for the three pairs.

### 9.4 What I still need from you, once

- **Create the GitHub repository and tell me its name.** I'll write the script and the scheduled job; you paste them in, since I can't write to your GitHub.
- **Run the first job and confirm it succeeded.** After that, it runs on its own.

## 10. Compliance (applies if the letter is shared, marketed, or tied to a fund)

### 10.1 Draft information policy (for counsel)

1. The analyst uses only public information and data supplied by the firm's data owner.
2. Nothing obtained from any other client or engagement enters the letter.
3. The analyst does not receive the firm's positions, orders, or pipeline.
4. All drafts, amendments, ledger entries, and communications are retained on firm systems under the firm's retention schedule.
5. The firm's compliance team controls handling of material non-public information; any suspected exposure halts production until cleared.
6. Internal distribution lists are approved by compliance.

### 10.2 Questions for outside counsel

These reflect my understanding from secondary sources and are framed as questions, not conclusions.

1. **Paper P&L.** Does "as if traded" idea P&L count as hypothetical performance under the SEC Marketing Rule if it ever appears externally? What procedures would be required?
2. **Past recommendations.** How must a record of past recommendations be presented to be fair and balanced (for example, the full ledger including losers)?
3. **The sleeve's record.** If the sleeve trades the ideas:
   - is its record actual performance;
   - do the extracted-performance and net-of-fees presentation requirements apply;
   - does publish-then-execute at a fixed time adequately address the concerns associated with *SEC v. Capital Gains Research Bureau* (1963)?
4. **Fundraising.** If the fund raises capital under Rule 506(b), could an external letter constitute general solicitation? Is 506(c) relevant?
5. **External letter status.** Does the external letter fall within the publisher's exclusion from the definition of investment adviser (as I recall, addressed in *Lowe v. SEC*, 1985 **[VERIFY]**)? Do specific entry, stop, and target levels affect that?
6. **Record keeping.** What books-and-records requirements apply to the ledger and drafts?
7. **AI disclosure.** Must or should AI involvement in drafting be disclosed to internal or external readers, and how should it be described accurately?
8. **Skipped days.** Does skipping and logging external issues that aren't cleared in time raise any presentation issue?
9. **Crypto data.** Are there restrictions on using data from crypto exchanges that restrict US persons?

---

## 11. Open decisions

1. **Approve the Section 0 changes and the Section 7 criteria.**
2. **Create the GitHub repository** (Section 9.4) and decide whether the ledger lives in it publicly.
3. **Decide on the evening session:** use it, or freeze the event map each morning.
4. **Counsel:** only needed if the letter will be shared beyond you, used to market anything, or tied to a fund. For a private, free, personal project, Section 10 is guidance for later, not a launch requirement.

Items removed in v0.2: named staff, fund strategy, data budget.
