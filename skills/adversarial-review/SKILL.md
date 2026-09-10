---
name: adversarial-review
description: Manual invocation only. Two isolated artifact reviews with evidence adjudication.
---

# Adversarial Review

## Job

Coordinate two independent reviews and adjudicate their evidence. Agreement is
not proof.

## Steps

1. Require an artifact or stable locator, purpose, scope, exclusions, and
   success criteria. When available, compose `review` for changes, PR/story
   intent, systems, designs, and ADRs; `docs` for documentation-only artifacts;
   or `audit` for bounded cross-domain inspections. Otherwise, read the [generic
   contracts](references/reviewer-contracts.md). Use them for plans, policies,
   prose, decisions, or any artifact without an available specialist contract.
   Continue only when the review basis is explicit and this skill owns isolation
   and synthesis.
2. Create one neutral packet: artifact or locator, inputs, constraints, local
   evidence locations, permitted checks, and evidence limits. Exclude
   conclusions, suspected findings, fixes, reviewer output, the requester's
   preferred outcome, and irrelevant authorship or ownership. Preserve source,
   status, corrections, and material counterevidence when history matters.
3. Start exactly two isolated parallel roles from that packet: a breaker for
   failures, omissions, unsafe assumptions, counterexamples, broken boundaries,
   and unhandled conditions; and a verifier to test the criteria and challenge
   assumptions, certainty, ambiguity, and false positives. Use fresh contexts
   when available; otherwise give each only the packet and its role contract.
   Do not share prompts, progress, or reports.
4. Validate both reports. Retry one unusable role once in a fresh isolated
   context with only the original packet. Each role produces at most one valid
   report.
5. If a required report remains unavailable, return an incomplete review naming
   missing roles and attempts. Do not adjudicate.
6. Normalize each material claim to its affected criterion, precise locator,
   evidence, consequence, and falsification attempt. Classify it as `confirmed`
   when local evidence supports claim and criterion, `disputed` when evidence or
   interpretation is materially inconclusive, or `rejected` when unsupported,
   duplicated, outside scope, or disproved. The adjudicator adds no independent
   findings. For a composed specialist report using another priority scale, read
   [adjudication](references/adjudication.md) to normalize it without losing the
   specialist label. Deduplicate overlap, preserve material disagreement, and
   finish when both reports and the synthesis meet the output contract.

## Guardrails

- Keep the review read-only and preserve the supplied artifact.
- Report preferences only when a stated criterion makes them material.
- Read `references/sources.yml` only to audit or update the rationale for two
  isolated roles.

## Output

For a completed review, return:

1. **Review basis:** Artifact, purpose, scope, criteria, and evidence boundary.
2. **Breaker report:** Full structured report without hidden reasoning.
3. **Verifier report:** Full structured report without hidden reasoning.
4. **Adjudicated synthesis:** Verdict, confirmed, disputed, and rejected
   findings; combined coverage; and residual uncertainty.

For an incomplete review, return only status, missing roles, and attempts.
Never present one report as completed.
