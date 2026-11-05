---
name: create-tests
description: "Creates or improves tests for observable behavior. Use when tests are the primary deliverable. Not for changing the code under test; use `code`."
---

# Create Tests

## Job

Add the smallest stable set of tests that proves the requested behavior
through an observable boundary, with expected results taken from an
independent oracle.

The lightest path is one behavior with a clear oracle and an existing test
pattern to copy: every step, a few rows, no reference beyond case tables.
Escalate to a matching reference in References when the input space is
broad, the oracle is weak, or the behavior involves timing, concurrency,
migrations, security, or an existing flaky test.

## Steps

1. State each behavior claim and its risk, and name an independent oracle:
   a requirement, public contract, reproduced bug, invariant, reference
   implementation, consumer expectation, or reviewed domain example.
   Complete when every claim names its oracle or is reported as a
   requirement gap.
2. Choose the smallest level that observes the real risk (see Test levels),
   and inspect the local test style, fixtures, helpers, commands, and CI
   contract to reuse. Complete when each claim has a level and the local
   pattern to reuse is named.
3. Select rows that each protect a distinct contract, regression, boundary,
   or failure mode that cheaper evidence doesn't prove, using
   `references/cases.md` for shape, names, and count. Complete when every row
   has an observable pass condition and protects a distinct risk.
4. Add only the selected cases and the support code they need. Control time,
   randomness, paths, networks, dependencies, shared state, and cleanup where
   they apply, and assert through public boundaries rather than private
   mechanics. Complete when every row is implemented and no assertion depends
   on an incidental implementation detail.
5. Run the narrowest command that proves the cases. For a regression, confirm
   safely that the test fails on the known broken behavior. Then run each
   broader repository gate the changed boundary requires. Complete when each
   command passes, each regression test fails on the broken behavior, and the
   evidence record is written.

## Flow

```text
input ← behavior claims, oracles, local test conventions
claims → oracle missing? yes → report the requirement gap | no → continue
level → rows → implement → run
loop: run → fix the test → until each case passes and each regression test catches its bug
      same failure twice or results oscillate? → stop and report
stop: every row protects a distinct risk through an observable boundary
```

## Test levels

- Unit: an isolated deterministic rule.
- Integration: a real database, filesystem, framework, serializer, queue, or
  network boundary.
- Contract: compatibility between a consumer and a provider.
- System: a deployed journey or a result that emerges across components.

A test double can isolate local decisions but can't prove the boundary it
replaces.

## Evidence record

Record the claim, oracle, cases, command, result, and relevant environment,
and name each boundary the command didn't exercise. Coverage shows what ran,
not that it's correct.

```text
claim ← request ID is preserved
oracle ← versioned public API contract
level ← transport integration test
case ← valid request → response header equals the request ID
check ← focused API integration command passes
not proved ← proxy behavior in the deployed environment
```

Sources: [Barr et al., oracle problem](https://doi.org/10.1109/TSE.2014.2372785),
[ISO/IEC/IEEE 29119](https://committee.iso.org/sites/jtc1sc7/home/projects/flagship-standards/isoiecieee-29119-series.html),
[Inozemtseva and Holmes, coverage and effectiveness](https://doi.org/10.1145/2568225.2568271).

## References

Load each file whose condition applies.

| Condition | Load |
| --- | --- |
| Choosing case shape, row names, or row count | `references/cases.md` |
| Broad input spaces, weak oracles, parsers, transformations, or weak assertions | `references/generative-and-fault-based.md` |
| A test fails nondeterministically, or a change adds retries, sleeps, quarantine, or longer timeouts | `references/flakiness.md` |
| Shared state, asynchronous work, ordering, cancellation, retries, or idempotency | `references/concurrency.md` |
| Schemas, stored data, or compatibility between deployed versions | `references/migrations.md` |
| A claim crosses a trust boundary or fixes a vulnerability | `references/security.md` |
| An agent generated the tests being added or reviewed | `references/agent-generated-tests.md` |
| The user or repository uses coverage, mutation, pass, flake, runtime, count, or agent metrics | `references/metrics.md` |

## Gotchas

- Expected values computed by calling the code under test prove nothing; take
  them from the oracle.
- A test that never failed hasn't shown it can. Confirm a regression test
  fails on the broken behavior before trusting its pass.

## Guardrails

- Keep runtime behavior unchanged. When a test needs a production change,
  report it and stop at the test.
- Approval-gated: live services, production data, and networked dependency
  installs, unless an existing test gate already authorizes them.
- Use snapshots or interaction assertions only when that representation is the
  reviewed contract.
- Judge adequacy by the risk-and-case map; a test ratio, coverage target, or
  rerun count is not proof.

## Composition

- Not for the production change a test reveals; use `code`.
- Not for diagnosing why an existing test fails; use `debug`.

## Output

- Tests and support code that prove each selected behavior through an
  observable boundary.
- A risk-and-case map naming the contract or failure mode each test covers.
- Commands, results, and environment facts, or why no safe check ran.
- Boundaries, platforms, schedules, and data states the checks didn't
  exercise.
