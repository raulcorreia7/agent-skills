---
name: to-plan
description: Manual invocation only. Produces implementation-ready plans after requirements are approved or material decisions are resolved; do not implement.
---

# To Plan

## Job

Turn an ambiguous or non-trivial change into the smallest implementation-ready
plan with resolved decisions, ordered work, validation, and risk controls.

## Modes

- `sequential` is the default: order by dependency and risk; do not invent
  parallel slices.
- `parallel` applies only when the user explicitly requests parallel,
  concurrent, multi-agent, delegated, or ownership-sliced execution.

## Steps

1. Define the goal, non-goals, constraints, deliverable, reader, and evidence
   boundary: prompt-only, repository-informed, or greenfield.
2. Inspect repository evidence when it can change ownership, contracts, data,
   rollout, tests, generated artifacts, or risk.
3. Resolve material decisions before approval. If a choice changes scope,
   behavior, contracts, security, data, cost, rollout, or architecture, ask or
   record it as a blocker. Assume only bounded, reversible detail.
4. Describe target shape and affected ownership boundaries; omit unnecessary
   implementation detail.
5. In sequential mode, order work by dependency and risk. Add safety nets first,
   define contracts before consumers, and complete migration or rollout before
   cleanup.
6. In explicitly requested parallel mode, read
   [delegation.md](references/delegation.md) before defining slices; apply its
   slice contract, collision rules, and parent synthesis checks.
7. Give every step or slice an outcome, likely location or owner, dependencies,
   and proportionate local validation.
8. Include integration checks and rollback or recovery for irreversible,
   stateful, public-contract, or production-affecting changes.
9. Finish when every plan item has an owner or location, dependencies, outcome,
   and validation.

## Guardrails

- Keep the deliverable as a plan unless the user separately requests
  implementation.
- Resolve material public contracts, storage, rollout, and ownership before
  implementation starts.

## Composition

- Use `diagrams` when dependencies, flow, ownership, or rollout are materially
  clearer visually.
- Use `docs` when documentation structure or reader workflow is itself a major
  plan artifact.

## Output

- Implementation-ready plan and selected mode, or a decision-ready draft naming
  material blockers and alignment questions
- Decisions, assumptions, non-goals, and open blockers
- Target shape, ownership boundaries, contracts, and data impact
- Ordered steps or parallel slices with dependencies and validation
- Applicable integration, rollout, recovery, and residual risks
