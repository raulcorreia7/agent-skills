---
name: debug
description: Diagnoses failures and isolates their causes. Use when a root cause or testable hypothesis is the primary deliverable.
---

# Debug

## Job

Identify the root cause or the strongest testable hypothesis. Preserve runtime
behavior.

## Steps

1. Record the exact symptom, expected behavior, environment, frequency, and
   relevant recent change. Inspect the applicable command, logs, stack trace,
   configuration, dependencies, tests, and nearby code, removing sensitive
   values from retained evidence. Complete when the failure boundary is
   explicit.
2. Reproduce the smallest safe failure when feasible. Otherwise, preserve the
   available artifacts and record why reproduction is unavailable.
   Complete when a reproduction exists, or its absence and the preserved
   artifacts are recorded.
3. Locate the first incorrect state across inputs, configuration, dependencies,
   permissions, persistence, concurrency, I/O, and external services.
   Complete when the first incorrect state is located or each unchecked layer
   is named.
4. Rank hypotheses by evidence. Run one probe that could falsify the
   highest-ranked hypothesis, then update the ranking from the result.
   Complete when evidence identifies one root cause or one strongest remaining
   hypothesis, and a stated observation would falsify the conclusion.

## Flow

```text
input ← symptom, environment, recent change
record → reproduce | preserve artifacts → locate first incorrect state
loop: rank hypotheses → falsify the strongest → re-rank
stop: one cause | one hypothesis + the observation that would falsify it
```

## Guardrails

- Keep diagnosis read-only. Implement a fix only when the user requests it.
- Use synthetic or non-production evidence unless the user authorizes live
  data access.

## Output

- A diagnosis that states the symptom, reproduction state, root cause or
  strongest hypothesis, supporting evidence, and the observation that would
  falsify it.
- The next probe that could falsify the leading hypothesis when the available
  evidence cannot distinguish the remaining causes.
