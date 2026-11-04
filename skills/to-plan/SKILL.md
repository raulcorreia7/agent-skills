---
name: to-plan
description: Manual invocation only. Produces implementation-ready plans for a change whose requirements are approved; surfaces any open material decision as a blocker. Not for remediation of verified findings; use `plan-remediation`.
---

# To Plan

## Job

Turn a non-trivial change with approved requirements into the smallest
implementation-ready plan with ordered work, validation, and risk controls.
The deliverable is a plan; implementation is a separate request.

## Modes

| Mode | Use when | Order work by |
| --- | --- | --- |
| `sequential` | Default | Dependency and risk: safety nets first, contracts before consumers, migration or rollout before cleanup. Add no parallel slices. |
| `parallel` | The user explicitly requests parallel, concurrent, multi-agent, delegated, or ownership-sliced execution | Read [delegation.md](references/delegation.md) before defining slices; apply its slice contract, collision rules, and parent synthesis checks. |

## Steps

1. Define the goal, non-goals, constraints, deliverable, reader, and evidence
   boundary: prompt-only, repository-informed, or greenfield. Inspect
   repository evidence when it can change ownership, contracts, data, rollout,
   tests, generated artifacts, or risk. Complete when each item is stated and
   the evidence boundary is named.
2. Resolve material decisions. If a choice changes scope, behavior, contracts,
   security, data, cost, rollout, or architecture, ask or record it as a
   blocker. Assume only bounded, reversible detail. Resolve material public
   contracts, storage, rollout, and ownership before implementation starts.
   Complete when every material decision is resolved or listed as a blocker.
3. Describe the target shape and affected ownership boundaries; leave out
   implementation detail the plan does not need. Complete when each affected
   boundary and contract is named.
4. Order the work per the selected mode. Give every step or slice an outcome,
   likely location or owner, dependencies, and proportionate local validation.
   Add integration checks and rollback or recovery for irreversible, stateful,
   public-contract, or production-affecting changes. Complete when every plan
   item has an owner or location, dependencies, outcome, and validation.

## Flow

```text
input ← approved requirements, mode (parallel on request only)
define goal, boundary → decisions resolved | blocker recorded
shape ← target, ownership boundaries
order ← dependency, risk | slices per the delegation contract
stop: every item has owner, deps, outcome, validation
```

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
