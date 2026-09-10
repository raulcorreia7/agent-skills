---
name: to-issues
description: Manual invocation only. Decomposes an approved PRD or plan into dependency-aware issue drafts; publish only with explicit approval.
---

# To Issues

## Job

Turn an approved requirements document or plan into issue drafts with explicit
readiness and dependencies.

## Steps

1. Confirm the source, delivery boundary, tracker, issue granularity, hierarchy,
   and publication intent. Draft when resolved or explicitly deferred; resolve
   target tracker and publication intent before publication.
2. Verify that decision owners resolved material scope, contracts, data,
   ownership, rollout, and validation. Resolve each decision before calling
   affected implementation work actionable. If a delivery-graph decision remains,
   create a preceding decision issue with an owner, criterion, and output; keep
   affected implementation drafts blocked on it.
3. Slice coherent outcomes by stable ownership. Put shared contracts before
   consumers; order migrations and rollout.
4. Use the issue contract. Keep source terminology; do not invent requirements.
5. Check independent completion, hidden context, duplicate work, collisions,
   cycles, and the critical path. Finish drafting when each issue has an
   outcome, acceptance criteria, validation, declared dependencies, and explicit
   readiness, and no implementation issue can start before its material decision
   issues finish.
6. When publication is requested, finish only when read-back matches the
   approved write set or the failure report accounts for every attempted
   mutation.

## Issue Contract

Every issue includes:

- issue kind, outcome title, and parent or objective.
- build outcome, scope, and exclusions.
- behavior-focused acceptance and validation.
- readiness state, dependencies, delivery notes, and source locator.

A decision issue uses `decision` as its kind and replaces the build outcome with
its decision criterion and required output. `A -> B` means A must finish before
B; use that direction in drafts and tracker links.

## Guardrails

- Return drafts unless the user explicitly approves publication.
- Obtain tracker values from evidence or the user.
- Keep unresolved requirements visible. Coordination issues must not hide them.
- Do not mark implementation issues as actionable while a material decision
  that can change them is unresolved.
- Treat edits, closure, assignment, priority changes, and deletion as separate
  external mutations that require explicit approval.

## Composition

- Return to requirements or planning when the source is missing or not
  implementation-ready; do not decompose an unapproved source.
- Use `git` for branch, PR, release, and work-item linking conventions after
  issues exist.

## Output

- Source and material decomposition assumptions
- Ordered issue drafts and hierarchy
- Dependency, collision, and critical-path map
- Decision issues and the implementation drafts that they block
- For publication: approved preview, created IDs, and read-back result
- Unresolved decisions and residual delivery risk
