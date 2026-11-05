---
name: to-prd
description: Manual invocation only. Turns a problem, opportunity, or feature idea into decision-ready, source-backed requirements before implementation planning.
---

# To PRD

## Job

Produce a decision-ready requirements document defining the problem, desired
outcomes, boundaries, requirements, evidence, and unresolved decisions.
Include architecture, task order, or other implementation detail only when it
is already decided.

## Steps

1. Identify the reader, decision, problem or opportunity, evidence boundary,
   users, business context, constraints, and requested document location.
   Complete when each is stated or marked unknown.
2. Inspect repository, documentation, research, issues, or approved external
   evidence when it can change requirements. Record each claim in the evidence
   register with one status: `fact` (observed in a source), `policy` (a
   standing rule), `direction` (stakeholder or user direction), `assumption`,
   or `open` (an unanswered question). Complete when every key claim has a
   register entry with a status.
3. Define goals, measurable outcomes, non-goals, users, use cases, functional
   requirements, quality attributes, constraints, dependencies, risks, and
   acceptance measures. Complete when every significant requirement cites a
   register ID and has an inspectable acceptance measure.
4. Check consistency, traceability, feasibility, terminology, and missing
   evidence against the document shape. Complete when no significant contract,
   data, security, ownership, migration, rollout, or acceptance decision is
   hidden: each is decided or listed as open.

## Flow

```text
input ← problem, opportunity, or idea + reader and evidence boundary
inspect evidence → register(fact | policy | direction | assumption | open)
requirements ← goals, outcomes, non-goals, acceptance; each cites an ID
check → hidden significant decision? yes → mark it open | no → continue
stop: decision-ready, every open decision visible
```

## Document shape

Use applicable items from step 3 as sections.

- State observable behavior, not a preferred implementation.
- Keep a compact evidence register:

  | ID | Source locator | Status | Claim or requirement |
  | --- | --- | --- | --- |
  | E1 | source and location | fact, policy, direction, assumption, or open | concise statement |

  Every significant requirement cites an ID. Without a `fact`, use `policy`,
  `direction`, `assumption`, or `open`; never imply validation.
- Keep current facts separate from target decisions. Set a numeric target only
  from evidence or user direction; otherwise mark it open.
- A PRD is not decision-ready while significant contract, data, security,
  ownership, migration, rollout, or acceptance decisions remain hidden.

## Guardrails

- Label `direction` separately from `fact`.
- Keep non-goals, constraints, privacy, security, accessibility, operations,
  migration, and rollout requirements visible.
- Keep external work-item systems unchanged.

## Composition

- Recommend `discuss-architecture` when unresolved boundaries or major
  trade-offs block requirements.
- Recommend `to-plan` after approved requirements make sequencing primary.
- Recommend `to-issues` when an approved PRD or plan is ready to decompose.

## Output

- A decision-ready PRD with traceable requirements, inspectable acceptance
  measures, explicit assumptions, and visible open decisions.
