# External And Live Evidence

External evidence can test a claim, set constraints, select a method, or bound
an estimate. It doesn't replace workload measurement. Rank it on the evidence
ladder in `measurement.md`. The method is provider-neutral: pick sources and
read-only tools for the actual platform.

## Claim record

For each consequential claim, capture:

| Field | Question |
|---|---|
| Claim | What measurable statement are we testing? |
| Source | Where did the evidence come from, and which rung is it? |
| Freshness | When was it published, collected, or effective? |
| Match | Do workload, version, region, SKU, architecture, scale, and cache state match? |
| Measure | What statistic, aggregation, interval, dimensions, and sample size were used? |
| Result | Confirmed, weakened, rejected, or inconclusive? |
| Confidence | What uncertainty or bias remains? |
| Next check | What direct measurement would most reduce uncertainty? |

Example: "Service tier X supports the required 2,000 requests per second" uses
the current primary service limit for the exact region and tier. Record the
effective date, note that a documented maximum doesn't prove available quota,
mark the result `inconclusive`, and make an approved quota query the next
check.

## Public benchmarks and guidance

- Reproduce a key benchmark locally. Compare workload and method, not headline
  numbers.
- Keep throughput, latency, efficiency, and unit cost separate.
- Treat vendor guidance as a prompt to investigate, and check the mechanism.
- Record the date, version, platform, hardware or SKU, region, dataset,
  concurrency, warm-up, duration, and exclusions.

## Prices, limits, and capacity

Pricing, quotas, capacity, service limits, availability, and product behaviour
are current external facts. Check them for the exact currency, agreement,
region, SKU, tier, effective date, and usage model. A public retail price
isn't the organization's negotiated or realized cost, and a documented maximum
isn't the current quota or available regional capacity. Model uncertainty with
ranges and sensitivity analysis: show which assumption changes the
recommendation, and drop false precision.

## Live telemetry and inventory

- Confirm the scope and data classification first. Start with inventory and
  aggregates, then narrow.
- Leave out secrets, customer payloads, personal data, tokens, connection
  strings, and identifiers the claim doesn't need. Redact what you keep.
- Missing permissions, dimensions, retention, sampling, or aggregation are
  evidence limits, not proof that no problem exists.
- Changing capacity, scale, SKU, placement, quota, retention, reservations,
  routing, or monitoring just to measure is itself an approval-gated change.
