---
name: discuss-architecture
description: Manual invocation only. Architecture decisions that require system-boundary and trade-off alignment.
---

# Discuss Architecture

## Job

Help the user reach an architecture decision. Keep implementation and detailed
plans in their owning workflows.

## Steps

1. Frame the decision, desired outcome, constraints, stakeholders, and material
   unknowns.
2. Inspect repository evidence when current boundaries, contracts, data,
   deployment, or ownership can change the answer.
3. Ask one material alignment question at a time when the answer changes
   direction, public contracts, risk, cost, or ownership. Use progressive discovery.
4. Compare viable options by consequences: coupling, data ownership,
   operability, security and privacy, migration, cost, and testability.
5. Recommend a default and explain the decisive trade-offs. Keep the decision
   human-owned and distinguish evidence from assumptions.
6. Return a concise decision snapshot when alignment emerges: distinguish the
   recommendation, decision owner, and `proposed` or explicitly confirmed
   `accepted` state. Finish when the snapshot records the chosen direction,
   decisive trade-offs, evidence, assumptions, owner, and acceptance state.

## Composition

- Use `diagrams` when a small dependency, sequence, or data-flow visual would
  materially clarify the decision.
- Use `docs` when the user wants a durable ADR or architecture document.
- Recommend explicit `to-plan` only after the architecture decision is stable
  enough to sequence implementation.

## Guardrails

- Record `accepted` only after the decision owner explicitly confirms it.
- Label unknown architecture, ownership, API, deployment, and data facts.

## Output

- A decision comparison with the material options, consequential trade-offs,
  evidence, assumptions, and open questions.
- When alignment exists, a decision snapshot with its owner and acceptance
  state.
