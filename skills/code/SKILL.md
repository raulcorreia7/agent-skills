---
name: code
description: Implements or explains application behavior when code is the primary artifact. Use specialist skills for diagnosis, behavior-preserving refactoring, tests, scripts, documentation, comments, or review.
---

# Code

## Job

Implement or explain the requested application behavior with the smallest
coherent change.

## Steps

1. Identify the requested behavior, non-goals, affected contracts,
   compatibility needs, and material risks. Resolve only choices that change
   behavior, data, security, cost, rollout, or the deliverable.
2. Inspect the behavior owner, direct callers, dependencies, types, focused
   tests, configuration, and repository rules. Load only applicable references.
   Determine whether the behavior is missing, partial, or already satisfied; if
   satisfied, return supporting evidence without a code change.
3. For non-trivial work, define observable criteria for the result, preserved
   behavior, material failures, and operational constraints. For an explanation,
   trace the relevant types, callers, state, contracts, and side effects without
   editing. Otherwise, implement each criterion or name the specific blocking
   evidence.
4. Update directly coupled types, schemas, configuration, comments, and
   documentation. Maintain generated artifacts through their schema, template,
   configuration, or generator. Inspect each changed block and the final diff;
   remove experiments, speculative paths, duplicates, unwanted features, and
   unrelated churn. Run the smallest existing checks that support the affected
   behavior.
Stop when every requested criterion and affected contract has evidence, directly
coupled artifacts agree, and the smallest relevant checks pass or have a stated
blocker.

## Contract

- Preserve public and informal contracts unless the request changes them.
  Informal contracts include defaults, error shapes, ordering, structured log
  fields, configuration keys, and exit codes.
- Reuse repository architecture, types, conventions, and maintained
  dependencies. Use syntax and APIs that the repository versions support.
- Use typed representations for domain rules, valid absence, closed states,
  units, and values that are easy to confuse. Parse untrusted data at its
  authoritative boundary.
- Put each rule with the owner that can enforce it. Formatting, naming, and
  quality gates belong in the formatter, linter, or CI. This skill owns
  judgment and seams. Add a seam only for current variation, ownership,
  testability, or compatibility. Keep small cohesive behavior together.
- Keep the main path, failure behavior, and side effects visible. Make time,
  randomness, generated identifiers, and environment state controllable when
  they affect behavior.
- Add compatibility behavior only for a current consumer, stored data, staged
  rollout, or external contract. Isolate it at one boundary and define its
  removal condition.

## References

- Read [input and errors](references/boundaries/input-and-errors.md) when the
  change touches external input, validation, error translation, logging, retry,
  or resource cleanup.
- Read [effects and concurrency](references/boundaries/effects-and-concurrency.md)
  when the change has multiple side effects, retryable mutation, concurrent
  work, non-trivial cancellation ownership, batches, streams, or shared state.
- Read the [structured-data router](references/boundaries/structured-data/index.md)
  when the change touches persistence, queries, HTTP, serialization, schemas,
  providers, paths, time, numeric representation, or large data. It routes to
  the common contract and only the applicable format or integration leaves.
- Read the [security router](references/boundaries/security/index.md) when the
  change touches a trust boundary, authorization, identity, credentials,
  cryptography, sensitive data, outbound destinations, untrusted files, or
  native object deserialization. It routes to the common contract and only the
  applicable security leaves.
- Read [external contracts](references/boundaries/external-contracts.md) when
  the change touches protocol compatibility, generated code, or feature flags.
- Read the [quality router](references/quality/index.md) when the change alters
  module ownership, abstraction, duplication, pattern use, functional design,
  performance, dependencies, observability, a code-owned user interface, a
  quality measure, or a bounded high-assurance component. Load only the
  matching leaf.
- Read [languages/index.md](references/languages/index.md) only when behavior
  depends on language-specific rules or the repository has no clear convention.
  Then read only the matching language and concern leaf.
- Read [code structure](references/readability/structure.md) for substantial
  control-flow, expression, naming, or semantic-block work.
- Read [formatting](references/readability/formatting.md) only when wrapping or
  layout materially affects readability and repository rules are insufficient.
- Read `references/readability/sources.yml` only to audit or re-verify the
  external readability evidence.
- Read [verification.md](references/verification.md) only when you must select
  or interpret a check.

For another language, use repository evidence. Add a language guide only after
repeated demand.

## Scope

Keep routine implementation and small rationale comments in this skill. Use a
maintained specialist skill when its artifact or concern is primary:

- `debug` for an unknown failure cause; return here for an authorized fix.
- `create-tests` for tests, fixtures, snapshots, or coverage.
- `comments` for comments, docstrings, API documentation, markers, or
  directives.
- `docs` for standalone documentation and `scripts` for automation.
- `refactor` for requested behavior-preserving restructuring and `review` for
  independent assessment.

Local restructuring that is necessary for the behavior change remains here.

## Output

- The implemented application behavior or code explanation
- Updated directly coupled artifacts
- Public, data-shape, and compatibility changes that are part of the result
- Checks run, their results, and material residual risk
- An evidence-backed no-change result when the current behavior already meets
  the requested contract
