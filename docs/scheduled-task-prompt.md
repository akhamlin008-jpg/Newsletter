# Morning session: scheduled task instructions

Schedule: every weekday at 6:45 AM Eastern.

You are drafting the morning letter defined in the charter. Nobody can answer
questions during this run, so follow these steps exactly and state any problem
in the output instead of asking.

## 1. Load the inputs

Fetch these three files:
- https://raw.githubusercontent.com/akhamlin008-jpg/Newsletter/main/docs/charter.md
- https://raw.githubusercontent.com/akhamlin008-jpg/Newsletter/main/data/latest.json
- https://raw.githubusercontent.com/akhamlin008-jpg/Newsletter/main/data/latest.md

## 2. Check the snapshot

The snapshot is usable only if `generated_et` is today's date and the time is
after 6:00 AM Eastern.
- If it is not usable, or cannot be fetched, write a DEGRADED MODE output
  (charter Section 2.5): the headline "PRODUCTION FAILURE: no idea today," the
  reason, and today's calendar from step 3. Do not use numbers from memory or
  from web search as dashboard values. Stop after that.

## 3. Calendar and overnight news

Search the web for:
- today's scheduled US, eurozone, UK, and Japan economic releases and central
  bank decisions, with times in Eastern time and consensus figures where shown
  (record the source of each consensus figure);
- overnight news that explains any flagged row in the snapshot;
- anything from yesterday afternoon or evening that the snapshot's prices
  reflect but the prior letter could not have covered.

Verify the date on every result. Discard anything not clearly about today or
the last 24 hours.

## 4. Draft the letter (charter Section 2.1)

Maximum 500 words, excluding the dashboard table. Sections, in order:
1. Open ideas: "none yet (pilot not started)" until the ledger exists.
2. Today's idea or "no trade": until the reference data exists (charter
   Section 9.3), write any idea in full using the charter's template, but
   label it "PRACTICE: not scored."
3. Risk to common exposures.
4. Event map: event, time (ET), consensus, surprise threshold, expected
   reaction with a probability bucket (15/25/35/45/55/65/75/85%). Mark any
   listed event after 7:00 AM ET as "flash due."
5. Dashboard: copy the table from latest.md. Write commentary only for the
   groups in `flag_groups_ranked`. Label stale or lagged rows.

Every number in the letter must come from the snapshot or from a named,
dated search result. Mark anything not confirmed with [VERIFY].

## 5. Review checklist

End the output with this checklist, each item marked pass or fail with a
one-line reason:
- Every dashboard number came from the snapshot.
- The idea (if any) passes charter Section 4.3, or is labeled practice.
- The premium classification follows charter Section 4.6.
- Word cap met.
- Every [VERIFY] item is listed.
- Every listed event after 7:00 AM ET is marked "flash due."

## 6. Deliver

Title the output "Morning Letter DRAFT [date]". It is a draft until a person
reviews it.
