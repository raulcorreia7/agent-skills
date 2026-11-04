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
   implementation, consumer expectation, or reviewed domain example. Take
   expected results from the oracle, never from the code under test.
   Complete when every claim names its oracle or is reported as a requirement
   gap.
2. Select the smallest level that observes the real risk: unit for an isolated
   deterministic rule, integration for a real boundary, contract for
   consumer-provider compatibility, or system for a deployed journey. A test
   double cannot prove the boundary it replaces. Inspect the test style,
   fixtures, helpers, commands, and continuous integration contract, and reuse
   a suitable local pattern. Read [the branch index](references/index.md) when
   the task needs an extended evidence example or involves broad input spaces,
   fault-based testing, flakiness, concurrency, migrations, security,
   agent-generated tests, or test metrics; then load each matching leaf.
   Complete when each claim has a level and the local pattern to reuse is
   named.
3. Select rows that distinguish separate paths, using
   [case tables](references/cases.md) for case shape, row names, and row count.
   Each row protects a contract, regression, boundary, or failure mode that
   cheaper evidence does not prove. Complete when every row has an observable
   pass condition and protects a distinct risk.
4. Add only the selected cases and necessary support code. Control applicable
   instability in time, randomness, paths, networks, dependencies, shared
   state, and cleanup. Prefer stable public boundaries to private mechanics.
   Complete when every selected row is implemented and no assertion depends on
   an incidental implementation detail.
5. Run the narrowest command that proves the cases. For a regression, safely
   confirm that the test detects the known broken behavior. Then run each
   broader repository gate that the changed boundary requires. Complete when
   each command passes, each regression test fails on the broken behavior, and
   material evidence limits are recorded.

## Flow

```text
input ← behavior claims, oracles, local test conventions
claims → level → rows → implement → run
oracle missing? yes → report the requirement gap | no → continue
loop: run → fix the test → until each case passes and each regression test catches its bug
stop: every row protects a distinct risk through an observable boundary
```

## Guardrails

- Keep runtime behavior unchanged. Return to the behavior owner when the test
  requires a production change.
- Use live services or production data only with an existing explicit test gate.
- Use snapshots or interaction assertions only when that representation is the
  reviewed contract.
- Judge adequacy by the risk-and-case map; a fixed test ratio, coverage target,
  or rerun count is not proof of adequacy.

## Output

- Tests and required support code that prove each selected behavior through an
  observable boundary.
- A risk-and-case map that states the contract or failure mode each test covers.
- Commands, results, and relevant environment facts, or the reason no safe
  check ran.
- Material boundaries, platforms, schedules, and data states that the checks
  did not exercise.
