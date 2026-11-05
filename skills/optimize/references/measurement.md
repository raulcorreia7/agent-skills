# Optimization Measurement

## Define the claim

Write the target as a measurable comparison with a boundary and a constraint.
Prefer user- or system-visible measures over internal counters. Record the
workload, environment, versions, sample size, warm-up, cache state, variance,
and known noise when they affect the result.

## Baselines and proxies

- Measure the current path before you choose an intervention.
- Use representative workloads, existing traces, CI history, or controlled
  experiments.
- When direct measurement is unavailable, state what the chosen proxy can and
  cannot prove.
- Compare equivalent inputs and environments. Label cold and warm results.

## Evidence ladder

This is the one ladder for local and external evidence. Prefer the highest
rung available; it ranks confidence, not the order you collect in.

1. A representative workload measured directly in the target environment.
2. Owned telemetry within the approved scope: production metrics, traces,
   profiles, cost and usage data, resource inventory, quotas, and
   configuration.
3. Controlled experiments and repeatable load tests or microbenchmarks.
4. Comparable CI history, profiles, plans, and configuration from a similar
   environment.
5. Primary specifications and current vendor documentation for the exact
   service, region, SKU, version, tier, or tool: limits, pricing, guidance.
6. Reproducible upstream benchmarks, release notes, and issue records that
   disclose their workload and environment.
7. Independent research or benchmarks whose method and inputs are close
   enough to judge applicability.
8. Explicit estimates or engineering models with sensitivity ranges.
9. Secondary articles, for discovery only. Check each consequential claim
   against a higher rung.

For each piece of evidence, record the source, collection time, scope,
dimensions, aggregation, workload, environment, versions, and known
confounders. Keep correlation apart from causation. Read provider-native
inventory, metrics, tracing, billing, and quota interfaces rather than
screenshots or copied values.

## Rank and verify

Rank candidates by expected impact, effort, risk, confidence, reversibility,
maintenance cost, and validation plan. Change one relevant variable at a time
when practical, re-measure, and keep correctness and safety checks intact.

Stop when the target is met or the bottleneck moves outside scope. Also stop
when measurement can't tell improvement from noise, or when the likely benefit
no longer justifies the cost and risk.

## Example

Target: reduce checkout API p95 latency for a 50-item cart in staging from the
420 ms baseline to at most 300 ms, without raising the error rate by more than
0.1 percentage points. Compare the same warm-cache workload across 20 runs,
change one candidate at a time, and stop when the target is met or the
confidence interval overlaps the baseline.

Read `sources.yml` only to re-verify the dated sources behind this reference.
