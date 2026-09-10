---
name: triage
description: Manual invocation only. Triages bugs, issues, tickets, pull requests, alerts, and reports into classified, ordered, owned next actions. Use when the queue must be sorted, not inspected or fixed.
---

# Triage

## Job

Sort a set of work items when demand exceeds what the team can act on at once.
Decide each item's kind, urgency, impact, outcome, and owner, and return an
order, not a fix. Triage is a boundary: a neutral pass over the queue that keeps
work moving without consuming the specialists who do it.

## Steps

1. Fix the boundary and the capacity. List the items and the intake window, and
   name who can act and how much they can take. Complete when the queue and the
   acting capacity are both explicit.
2. Normalize each item into one record: source locator, kind, reported
   severity, evidence state, age, and current state (new, in flight, blocked,
   stale). Skip closed and already-triaged items.
3. Classify the kind and check for duplicates or superseded work: incident,
   defect or regression, security, request or feature, question or support,
   change under review, or noise. Correct a wrong kind when the evidence shows
   it.
4. Judge urgency and impact separately, for this project and its users. Urgency
   follows ongoing harm, active exposure, and reversibility. Impact follows
   users, contracts, data, security and privacy, cost, and delivery. A general
   severity score is an input to that judgement, not the decision.
5. Choose the outcome from the ladder below. State the evidence and criterion
   that produced it, so the decision can be re-run when the evidence changes.
6. Name the owner, the first concrete action, and, for a deferred or
   evidence-blocked item, the condition that brings it back.
7. Order the actionable set. Act-now items first; then reversible mitigations,
   which precede root-cause work; then dependency gates; then the rest by
   impact. Keep the order inside the stated capacity, and leave same-outcome
   items in any stable order.
8. Finish when every item has a kind, an evidence state, an urgency and impact
   statement, an outcome, and either an owner with a next action or a reason;
   the actionable set starts with one executable step; and every item left in
   flight has a follow-up point.

## Outcomes

| Outcome | Meaning |
|---|---|
| `Act now` | Ongoing harm, active exposure, or a broken trust boundary. Stop other work and mitigate. |
| `Out-of-cycle` | Pull it forward with extra resource at the next opportunity, without pausing everything else. |
| `Scheduled` | Normal queue: a named owner, an entry point, and normal resource. |
| `Needs evidence` | Not judgeable yet. Name the missing evidence and who can supply it, and keep the item in the queue. |
| `Defer` | Real but not now. Record the revisit condition and the default outcome if it recurs. |
| `Decline` | Duplicate, superseded, noise, or out of scope. Close with a reason, never silently. |

## Guardrails

- Keep triage read-only. It changes order, never severity, evidence, or scope.
- Treat an incident as an incident: escalate it ahead of the backlog and
  declare it early rather than waiting for certainty.
- Prefer one extra look at a possible incident over a missed one, and label the
  uncertainty honestly. Overtriage costs attention; undertriage costs trust.
- Do not close an item without a stated reason and a route back: what evidence,
  event, or owner decision would reopen it.
- Label unverified items as unverified. Repetition does not promote a claim.
- Keep one item per record. Do not hide distinct items inside a summary.
- Read `references/sources.yml` only to audit or re-verify this skill's
  external practice sources.

## Composition

- Use `audit` or `code-scanner` first when an item has no evidence.
- Use `review` when a pull request, change, or design needs assessment against
  its intent.
- Use `plan-remediation` when verified findings need horizons and a portfolio
  order.
- Use `to-issues` when the triaged set becomes tracker work.
- Use `debug` when one failure's cause is still unknown, and `optimize` when a
  single measurable target owns the work.

## Output

- Boundary: item list, intake window, acting capacity, evidence limits
- Per item: kind, evidence state, urgency, impact, outcome, owner, next action,
  and the revisit condition or decline reason
- The ordered actionable set with one executable first step
- Escalations, unverified items, follow-ups, and residual decision risk
