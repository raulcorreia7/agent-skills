---
name: code
description: Implements or explains application behavior. Use when application code or its explanation is the primary deliverable. Not for diagnosis, refactoring, tests, scripts, docs, comments, or review; use that specialist skill.
---

# Code

## Job

Implement or explain the requested application behavior with the smallest
coherent change.

## Steps

1. Identify the requested behavior, non-goals, affected contracts,
   compatibility needs, and significant risks. Inspect the behavior owner,
   direct callers, dependencies, types, focused tests, configuration, and
   repository rules. Complete when the owner, each direct caller, and each affected
   contract are named.
2. For an explanation, trace the relevant types, callers, state, contracts, and
   side effects without editing. For non-trivial work, define observable
   criteria for the result, preserved behavior, significant failures, and
   operational constraints. Complete when the explanation answers the question
   with source locations, or every criterion has an observable pass condition.
3. Implement each criterion. Load only the references whose condition the
   change meets:
   - [input and errors](references/boundaries/input-and-errors.md): external
     input, validation, error translation, logging, retry, or resource cleanup.
   - [effects and concurrency](references/boundaries/effects-and-concurrency.md):
     multiple side effects, retryable mutation, concurrent work, non-trivial
     cancellation ownership, batches, streams, or shared state.
   - The [structured-data router](references/boundaries/structured-data/index.md):
     persistence, queries, HTTP, serialization, schemas, providers, paths,
     time, numeric representation, or large data. It routes to the common
     contract and only the applicable format or integration leaves.
   - The [security router](references/boundaries/security/index.md): a trust
     boundary, authorization, identity, credentials, cryptography, sensitive
     data, outbound destinations, untrusted files, or native object
     deserialization. It routes to the common contract and only the applicable
     security leaves.
   - [external contracts](references/boundaries/external-contracts.md):
     protocol compatibility, generated code, or feature flags.
   - The [quality router](references/quality/index.md): module ownership,
     abstraction, duplication, pattern use, functional design, performance,
     dependencies, observability, a code-owned user interface, a quality
     measure, or a bounded high-assurance component. Load each matching leaf.
   - [languages/index.md](references/languages/index.md): only when behavior
     depends on language-specific rules or the repository has no clear
     convention; then each matching contracts or verification leaf. For a language
     without a guide, use repository evidence.
   - [code structure](references/readability/structure.md): substantial
     control-flow, expression, naming, indentation, or semantic-block work.
   - [formatting](references/readability/formatting.md): only when wrapping or
     layout affects readability and repository rules are insufficient.
   - `references/readability/sources.yml`: only to audit or re-verify the
     external readability evidence.

   Complete when every criterion is implemented or names its specific blocking
   evidence.
4. Update directly coupled types, schemas, configuration, comments, and
   documentation. Run the smallest existing checks that support the affected
   behavior; read [verification.md](references/verification.md) only when you
   must select or interpret a check. Complete when every requested criterion and
   affected contract has evidence, directly coupled artifacts agree, and each
   check passes or has a stated blocker.

## Flow

```text
input ← request, behavior owner, callers, contracts
scope → criteria | explanation
explanation? yes → trace without editing → stop
loop: implement criterion → load matching reference → until every criterion is met or blocked
update coupled artifacts → smallest checks
stop: criteria and contracts have evidence, checks pass or blocker stated
```

## Contract

- Informal contracts include defaults, error shapes, ordering, structured log
  fields, configuration keys, and exit codes; preserve them like public ones.
- Use syntax and APIs that the repository versions support.
- Use typed representations for domain rules, valid absence, closed states,
  units, and values that are easy to confuse. Parse untrusted data at its
  authoritative boundary.
- Leave formatting, naming, and quality gates to the formatter, linter, or CI.
  Keep small cohesive behavior together.
- Keep the main path, failure behavior, and side effects visible. Make time,
  randomness, generated identifiers, and environment state controllable when
  they affect behavior.
- Isolate required compatibility behavior at one boundary and define its
  removal condition.

## Composition

Keep routine implementation, small rationale comments, and local restructuring
that the behavior change needs in this skill. Use a specialist skill when its
artifact or concern is primary:

- `debug` for an unknown failure cause; return here for an authorized fix.
- `create-tests` for tests, fixtures, snapshots, or coverage.
- `comments` for comments, docstrings, API documentation, markers, or
  directives.
- `docs` for standalone documentation and `scripts` for automation.
- `refactor` for requested behavior-preserving restructuring and `review` for
  independent assessment.

## Output

- The implemented application behavior or code explanation
- Updated directly coupled artifacts
- Public, data-shape, and compatibility changes that are part of the result
- Checks run, their results, and significant residual risk
