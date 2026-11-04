---
name: discuss-architecture
description: Manual invocation only. Architecture decisions that require system-boundary and trade-off alignment.
---

# Discuss Architecture

## Job

Help the user reach an architecture decision. Keep implementation and detailed
plans in their owning workflows.

## Steps

1. Frame the decision, desired outcome, constraints, stakeholders, and key
   unknowns. Inspect repository evidence when current boundaries, contracts,
   data, deployment, or ownership can change the answer. Complete when the
   decision is stated and each significant unknown is labeled.
2. Align on the questions whose answers change direction, public contracts,
   risk, cost, or ownership. Complete when each such question is answered or
   recorded as open.
3. Compare viable options by consequences: coupling, data ownership,
   operability, security and privacy, migration, cost, and testability.
   Recommend a default, explain the decisive trade-offs, keep the decision
   human-owned, and distinguish evidence from assumptions. Complete when every
   viable option has its consequences stated and the recommendation names its
   decisive trade-offs.
4. When alignment emerges, return a decision snapshot: the chosen direction,
   decisive trade-offs, evidence, assumptions, decision owner, and `proposed`
   or `accepted` state. Complete when the snapshot records each of these.

## Flow

```text
input ← decision, constraints, repository evidence
frame → align on significant questions → compare options → recommend
aligned? yes → snapshot | no → return the comparison with open questions
stop: snapshot records direction, trade-offs, owner, acceptance state
```

## Guardrails

- Record `accepted` only after the decision owner explicitly confirms it;
  otherwise the state is `proposed`.
- Label unknown architecture, ownership, API, deployment, and data facts.

## Composition

- Use `diagrams` when a small dependency, sequence, or data-flow visual would
  clarify the decision.
- Use `docs` when the user wants a durable ADR or architecture document.
- Recommend explicit `to-plan` only after the architecture decision is stable
  enough to sequence implementation.

## Output

- A decision comparison with the significant options, consequential trade-offs,
  evidence, assumptions, and open questions.
- When alignment exists, a decision snapshot with its owner and acceptance
  state.
