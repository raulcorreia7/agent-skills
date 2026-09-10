---
name: create-tests
description: Creates or improves tests for observable behavior. Use when tests are the primary deliverable.
---

# Create Tests

## Job

Add the smallest stable test set that proves the requested behavior through an
observable boundary.

## Steps

1. State each behavior claim and risk. Name an independent oracle such as a
   requirement, public contract, reproduced bug, invariant, reference
   implementation, consumer expectation, or reviewed domain example. Do not
   derive the expected result from the code under test; treat a missing oracle
   as a requirement gap.
2. Select the smallest level that observes the real risk: unit for an isolated
   deterministic rule, integration for a real boundary, contract for
   consumer-provider compatibility, or system for a deployed journey. A test
   double cannot prove the boundary it replaces. Give every case an observable
   pass condition.
3. Read [the branch index](references/index.md) only when the task needs an
   extended evidence example, case shape or row count guidance, or involves
   broad input spaces, fault-based testing, flakiness, concurrency, migrations,
   security, agent-generated tests, or test metrics; then load only the
   matching leaf.
4. Inspect the test style, fixtures, helpers, commands, and continuous
   integration contract. Reuse a suitable local pattern.
5. Select rows that distinguish separate paths. Each row must protect a
   contract, regression, boundary, or failure mode that cheaper evidence does
   not prove.
6. Control applicable instability in time, randomness, paths, networks,
   dependencies, shared state, and cleanup.
7. Add only the selected cases and necessary support code. Prefer stable public
   boundaries to private mechanics.
8. Run the narrowest command that proves the cases. For a regression, safely
   confirm that the test detects the known broken behavior.
9. Run each broader repository gate that the changed boundary requires. Record
   material evidence limits.
10. Finish when each row protects a distinct risk and no assertion depends on
    an incidental implementation detail.

## Cases

Express one behavior as a table of named rows and one test body.

- Rows are data: a friendly name, the inputs, the expected result, and the risk
  the row protects.
- Name rows for what the behavior does, prefixed by path: `happy: applies
  percentage discount`, `edit: accepts the exact minimum`, `unhappy: rejects an
  expired coupon`. The row names are the case map.
- One body arranges, acts, and asserts once. A row that needs its own branch is
  a different behavior; give it its own table.
- Cover the happy path first, then boundaries, then each failure mode you can
  name. Usually 3 to 8 rows; split a table before it grows past about ten.
- Take expected results from the oracle, never from recomputing with the code
  under test.

## Guardrails

- Keep runtime behavior unchanged. Return to the behavior owner when the test
  requires a production change.
- Use live services or production data only with an existing explicit test gate.
- Use snapshots or interaction assertions only when that representation is the
  reviewed contract.
- Do not use a fixed test ratio, coverage target, or rerun count as proof of
  adequacy. Coverage numbers and lint live in CI; this skill owns oracle
  selection.

## Output

- Tests and required support code that prove each selected behavior through an
  observable boundary.
- A risk-and-case map that states the contract or failure mode each test covers.
- Commands, results, and relevant environment facts, or the reason no safe
  check ran.
- Material boundaries, platforms, schedules, and data states that the checks
  did not exercise.
