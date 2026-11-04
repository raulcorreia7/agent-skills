---
name: adversarial-review
description: Manual invocation only. Runs two isolated reviews of an artifact and adjudicates their evidence.
---

# Adversarial Review

## Job

Coordinate two independent reviews and adjudicate their evidence. Agreement is
not proof.

## Steps

1. Require an artifact or stable locator, purpose, scope, exclusions, and
   success criteria. Pick the review basis: compose `review` for changes, PRs,
   designs, and ADRs; `docs` for documentation-only artifacts; `audit` for
   bounded cross-domain inspections. For plans, policies, prose, decisions, or
   anything without an available specialist, read
   [the generic contracts](references/reviewer-contracts.md). Complete when the
   review basis is explicit and the request needs isolation and synthesis.
2. Create one neutral packet: artifact or locator, inputs, constraints, local
   evidence locations, permitted checks, and evidence limits. Exclude
   conclusions, suspected findings, fixes, reviewer output, the requester's
   preferred outcome, and irrelevant authorship or ownership. Preserve source,
   status, corrections, and key counterevidence when history matters.
   Complete when the packet holds every listed input and none of the excluded
   material.
3. Start exactly two isolated parallel roles from that packet: a breaker for
   failures, omissions, unsafe assumptions, counterexamples, broken boundaries,
   and unhandled conditions; and a verifier to test the criteria and challenge
   assumptions, certainty, ambiguity, and false positives. Use fresh contexts
   when available; otherwise give each only the packet and its role contract.
   Complete when both roles have run from the same packet.
4. Validate both reports. Retry an unusable role once in a fresh isolated
   context with only the original packet; each role produces at most one valid
   report. If a required report is still missing, return an incomplete review
   naming the missing roles and attempts, and stop without adjudicating.
   Complete when both reports are valid or the incomplete review is returned.
5. Normalize each key claim to its affected criterion, precise locator,
   evidence, consequence, and falsification attempt. Classify it as `confirmed`
   when local evidence supports claim and criterion, `disputed` when evidence or
   interpretation is inconclusive, or `rejected` when unsupported,
   duplicated, outside scope, or disproved. The adjudicator adds no independent
   findings. For a composed specialist report using another priority scale, read
   [adjudication](references/adjudication.md) to normalize it without losing the
   specialist label. Deduplicate overlap and preserve substantive disagreement.
   Complete when every key claim is classified and the reports and
   synthesis meet the output contract.

## Flow

```text
input ← artifact, purpose, scope, criteria, evidence limits
basis → neutral packet → breaker ∥ verifier (isolated, packet only)
report usable? yes → continue | no → retry once in a fresh context
still missing? yes → stop: incomplete review, missing roles, attempts
claim ← confirmed | disputed | rejected; dedupe, no new findings
stop: both reports and the synthesis meet the output contract
```

## Sources

Read `references/sources.yml` only to audit or update the rationale for two
isolated roles.

## Guardrails

- Keep the review read-only and preserve the supplied artifact.
- Report preferences only when a stated criterion makes them matter.

## Output

For a completed review, return:

1. **Review basis:** Artifact, purpose, scope, criteria, and evidence boundary.
2. **Breaker report:** Full structured report without hidden reasoning.
3. **Verifier report:** Full structured report without hidden reasoning.
4. **Adjudicated synthesis:** Verdict, confirmed, disputed, and rejected
   findings; combined coverage; and residual uncertainty.

For an incomplete review, return only status, missing roles, and attempts.
Never present one report as completed.
