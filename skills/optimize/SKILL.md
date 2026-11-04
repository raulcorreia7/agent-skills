---
name: optimize
description: Manual invocation only. Evidence-backed optimization of performance, reliability, resources, cost, or operations against a measurable target.
---

# Optimize

## Job

Rank evidence-backed improvements to a measurable target before a behavior,
cost, or infrastructure change.

## Depth

Default to `quick`. Use `focused` or `deep` only for broader scope or requested
confidence.

- `quick`: inspect one target path with available local evidence, establish a
  baseline or labelled proxy, and rank the next measurement or change.
- `focused`: trace one selected domain, collect representative measurements,
  compare credible candidates, and state the selection check.
- `deep`: define system and data boundaries, use a coverage matrix for the
  applicable components and constraints, and report evidence limits and
  residual uncertainty before a broad recommendation.

Escalate only when the current depth cannot answer the target without hiding a
material uncertainty.

## Steps

1. Define one measurable target, the smallest scope that can explain or improve
   it, constraints, and trade-offs, and select the depth. Complete when the
   target, scope, and depth are stated, or the question that establishes the
   target is asked.
2. State each claim and the evidence needed to confirm, weaken, or reject it.
   Read `references/measurement.md`, then only the applicable scope reference:
   - Runtime code or a critical path: `references/runtime.md`.
   - Build or CI: `references/build-ci.md`.
   - Size or dependencies: `references/size-dependencies.md`.
   - Cost, capacity, or infrastructure:
     `references/cost-capacity-infrastructure.md`.
   - Cross-boundary system structure: `references/architecture.md`.
   - Process or lead time: `references/process.md`.

   Inspect local evidence first. Before external evidence supports or
   challenges a claim, read `references/external-evidence.md`, plus:
   - `references/external-benchmarks.md` for public benchmarks or guidance.
   - `references/live-evidence.md` before a live telemetry or inventory query.
   - `references/pricing-capacity.md` for prices, limits, quotas, or capacity.
   - `references/sources.yml` only to re-verify the dated provenance of these
     references.

   Complete when every claim has its evidence collected or its gap named.
3. Capture a baseline or label the strongest proxy and what it cannot prove.
   Profile or decompose enough to locate the bottleneck, then rank candidates by
   impact, effort, risk, confidence, reversibility, maintenance, and
   measurement. Complete when a baseline or labelled proxy exists, the
   bottleneck is located or its evidence gap stated, and candidates are ranked.
4. After explicit approval, use `scripts` for automation, `refactor` for
   behavior-preserving restructuring, or `code` for application behavior. Use
   `review`, `discuss-architecture`, or `to-plan` when assessment, alignment,
   or sequencing becomes the primary job. Re-measure when practical.
   Complete when the target is met or further work lacks likely value.

## Flow

```text
input ← measurable goal, smallest scope, depth
claims → evidence → baseline | labelled proxy → bottleneck
loop: rank → hand approved change to its owner → re-measure
stop: target met | further work lacks value
```

## Guardrails

- Require evidence before optimization.
- Keep general code, architecture, infrastructure, and design review with their
  owning skills.
- Treat public guidance, benchmarks, architectures, and list prices as context,
  not workload proof.
- Preserve correctness, maintainability, portability, security, privacy, and
  user experience.
- Weigh maintenance, security, license, stability, compatibility, ecosystem,
  and migration cost before a dependency-change recommendation.
- Keep cloud queries within the approved scope and protect sensitive data.

## Output

- Target, scope, depth, and baseline or evidence gap
- Claim register: source and locator, measured result or labelled proxy,
  confidence, applicability, freshness, and the next check that could falsify
  the claim
- Bottleneck findings and ranked recommendations
- Expected impact, trade-offs, and measurement plan
- Mutation risk and cost impact when relevant
- Stopping point and checks that materially informed it
