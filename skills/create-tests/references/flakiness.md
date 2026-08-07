# Flakiness

Treat a rerun as diagnostic evidence, not as a pass.

1. Preserve the first failure, logs, seed, order, shard, worker count,
   platform, versions, time zone, and schedule clues.
2. Rerun controlled variants to classify isolation, state pollution, time,
   randomness, resources, external dependencies, or a product race.
3. Fix the classified cause.
4. Confirm deterministic outcomes under the relevant variants.

Do not weaken assertions, add sleeps, increase timeouts, or normalize retries
without evidence that the change controls the cause.

If quarantine is necessary, record the owner, reason, issue, and removal
condition. Preserve the original failure and report the lost gate signal.

## Example

```text
Failure: an expiry test fails only after the daylight-saving boundary case.
Evidence: preserve the first log and run with a fixed clock in two time zones.
Cause: the fixture mixes local and UTC timestamps.
Fix check: both controlled variants pass repeatedly without retries.
```

## Evidence Base

- [Luo et al., empirical analysis of flaky tests](https://doi.org/10.1145/2635868.2635920)
