---
name: to-prd
description: Manual invocation only. Turns a problem, opportunity, or feature idea into decision-ready, source-backed requirements before implementation planning.
---

# To PRD

## Job

Produce a decision-ready requirements document defining the problem, desired
outcomes, boundaries, requirements, evidence, and unresolved decisions. Do not
invent implementation details.

## Steps

1. Identify the reader, decision, problem or opportunity, evidence boundary,
   users, business context, constraints, and requested document location.
2. Inspect repository, documentation, research, issues, or approved external
   evidence when it can change requirements.
3. Separate observed facts, user direction, assumptions, and open questions.
   Resolve only questions that materially change scope or outcome.
4. Define goals, measurable outcomes, non-goals, users, use cases, functional
   requirements, quality attributes, constraints, dependencies, and risks.
5. State acceptance measures. Omit architecture or task order unless decided.
6. Check consistency, traceability, feasibility, terminology, and missing
   evidence. Apply the document-shape evidence and acceptance rules; keep
   unresolved decisions visible.

## Document shape

Use applicable items from step 4 as sections.

- State observable behavior, not a preferred implementation.
- Keep a compact evidence register:

  | ID | Source locator | Status | Claim or requirement |
  | --- | --- | --- | --- |
  | E1 | source and location | evidence, policy, user direction, or assumption | concise statement |

  Every material requirement cites an ID. Without evidence, label an assumption,
  policy, or user direction; never imply validation.
- Keep current facts separate from target decisions; make acceptance measures
  inspectable; do not invent arbitrary targets.
- A PRD is not decision-ready while material contract, data, security,
  ownership, migration, rollout, or acceptance decisions remain hidden.

## Composition

- Recommend `discuss-architecture` when unresolved boundaries or major
  trade-offs block requirements.
- Recommend `to-plan` after approved requirements make sequencing primary.
- Recommend `to-issues` when an approved PRD or plan is ready to decompose.

## Guardrails

- Label stakeholder direction separately from verified facts.
- Keep non-goals, constraints, privacy, security, accessibility, operations,
  migration, and rollout requirements visible.
- Keep external work-item systems unchanged.

## Output

- A decision-ready PRD with traceable requirements, inspectable acceptance
  measures, explicit assumptions, and visible open decisions.
