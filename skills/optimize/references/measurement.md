# Optimization Measurement

## Define The Claim

Write the target as a measurable comparison with a boundary and constraint.
Prefer user- or system-visible measures over internal counters. Record workload,
environment, versions, sample size, warm-up, cache state, variance, and known
noise when they materially affect the result.

## Baselines And Proxies

- Measure the current path before you choose an intervention.
- Use representative workloads, existing traces, CI history, or controlled
  experiments.
- If direct measurement is unavailable, state what the selected proxy can and
  cannot prove.
- Compare equivalent inputs and environments. Label cold and warm results.

## Evidence Strength

Prefer evidence closest to the decision:

1. Measure a representative workload directly in the target environment.
2. Approved production telemetry, traces, cost/usage data, or provider metrics.
3. Controlled experiments and repeatable load or microbenchmarks.
4. Comparable CI history, profiles, inventories, plans, and configuration.
5. Current vendor specifications, limits, pricing, and architecture guidance.
6. Independent benchmarks or research with a comparable workload and setup.
7. Explicit estimates or engineering models with sensitivity ranges.

Treat this as a confidence ladder, not an automatic ranking. Record provenance,
collection time, scope, dimensions, aggregation, workload, environment,
versions, and known confounders. Keep correlation separate from causation.

## Rank And Verify

Rank candidates by expected impact, effort, risk, confidence, reversibility,
maintenance cost, and validation plan. Change one material variable at a time
when practical, re-measure, and keep correctness and safety checks intact.

Stop when the target is met or the bottleneck moves outside scope. Also stop
when measurement cannot distinguish improvement from noise or the likely
benefit no longer justifies cost and risk.

## Example

Target: reduce checkout API p95 latency for a 50-item cart in staging from the
420 ms baseline to at most 300 ms, without increasing the error rate by more
than 0.1 percentage points. Compare the same warm-cache workload across 20
runs, change one candidate at a time, and stop when the target is met or the
confidence interval overlaps the baseline.
