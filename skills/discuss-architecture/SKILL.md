---
name: discuss-architecture
description: "Compares architecture options and helps the user reach a decision on system boundaries, data ownership, and trade-offs. Use when an architecture decision is the primary deliverable. Not for assessing an existing design; use `review`."
---

# Discuss Architecture

## Job

Help the user reach an architecture decision: frame it, compare the viable
options by their consequences, recommend a default, and record what was
decided. Implementation and detailed plans stay with the skills that own them.

The lightest path is one framed decision, the viable options compared, and a
recommendation, with no repository inspection unless a current fact could
change the answer. Escalate to repository evidence when current boundaries,
contracts, data, deployment, or ownership are in question.

## Steps

1. Frame the decision, the desired outcome, constraints, stakeholders, and key
   unknowns. Inspect repository evidence when current boundaries, contracts,
   data, deployment, or ownership can change the answer. Complete when the
   decision is stated and each significant unknown is labelled.
2. Align on the questions whose answers change direction, public contracts,
   risk, cost, or ownership. Complete when each such question is answered or
   recorded as open.
3. Compare the viable options by consequence: coupling, data ownership,
   operability, security and privacy, migration, cost, and testability.
   Recommend a default, explain the trade-offs that decide it, and keep
   evidence apart from assumptions. Complete when every viable option has its
   consequences stated and the recommendation names its deciding trade-offs.
4. When the user aligns on a direction, return a decision snapshot: the chosen
   direction, deciding trade-offs, evidence, assumptions, decision owner, and
   a `proposed` or `accepted` state. Complete when the snapshot records each
   of these.

## Flow

```text
input ← decision, constraints, repository evidence when it matters
frame → align on significant questions → compare options → recommend
aligned? yes → snapshot | no → return the comparison with open questions
stop: snapshot records direction, trade-offs, owner, and acceptance state
```

## Guardrails

- The decision belongs to the user. Record `accepted` only after the decision
  owner confirms it; otherwise the state is `proposed`.

## Composition

- Use `diagrams` when a small dependency, sequence, or data-flow visual would
  clarify the decision.
- Use `docs` when the user wants a durable ADR or architecture document.
- Use `to-plan` once the decision is stable enough to sequence implementation.

## Output

- A comparison of the viable options with their trade-offs, evidence,
  assumptions, and open questions.
- When the user has aligned, a decision snapshot with its owner and
  acceptance state.
