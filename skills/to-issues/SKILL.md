---
name: to-issues
description: Manual invocation only. Decomposes an approved PRD or plan into dependency-aware issue drafts; publish only with explicit approval. Not for unresolved requirements or plans; use `to-prd` or `to-plan`.
---

# To Issues

## Job

Turn an approved requirements document or plan into issue drafts with explicit
readiness and dependencies.

## Steps

1. Confirm the source is approved and implementation-ready, then confirm the
   delivery boundary, tracker, issue granularity, hierarchy, and publication
   intent. Draft when these are resolved or explicitly deferred; resolve the
   target tracker and publication intent before publication. Take tracker
   values from evidence or the user. Complete when each item is resolved or
   explicitly deferred.
2. Verify that decision owners resolved material scope, contracts, data,
   ownership, rollout, and validation. For each delivery-graph decision that
   remains, create a preceding decision issue with an owner, criterion, and
   output, and keep the implementation drafts it can change blocked on it.
   Complete when every material decision is resolved or has a decision issue
   that blocks its affected drafts.
3. Slice coherent outcomes by stable ownership. Put shared contracts before
   consumers; order migrations and rollout. Write each draft per the issue
   contract in source terminology, adding only requirements the source states.
   Complete when each issue has an outcome, acceptance criteria, validation,
   declared dependencies, and explicit readiness.
4. Check independent completion, hidden context, duplicate work, collisions,
   cycles, and the critical path. Complete when the dependency graph is acyclic
   and no implementation issue can start before its decision issues finish.
5. When publication is requested and approved, publish the previewed write
   set. Complete when read-back matches the approved write set or the failure
   report accounts for every attempted mutation.

## Flow

```text
input ← approved PRD or plan, tracker, publication intent
source approved? yes → continue | no → stop and name what is missing
decisions → resolved | decision issue blocks affected drafts
slice → draft per issue contract → check graph
publish? approved → write → read back | otherwise → return drafts
stop: drafts complete and graph acyclic; read-back matches when published
```

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

- Keep unresolved requirements visible; a coordination issue records them
  rather than hiding them.

## Composition

- Use `git` for branch, PR, release, and work-item linking conventions after
  issues exist.

## Output

- Source and material decomposition assumptions
- Ordered issue drafts and hierarchy
- Dependency, collision, and critical-path map
- Decision issues and the implementation drafts that they block
- For publication: approved preview, created IDs, and read-back result
- Unresolved decisions and residual delivery risk
