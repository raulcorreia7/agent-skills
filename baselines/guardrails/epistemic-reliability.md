# Epistemic Reliability Guardrail

> Ground material claims in evidence that can change the conclusion.

The rules in [`AGENTS.md`](../AGENTS.md) are authoritative. Apply this
companion when research, review, uncertainty, or conflicting evidence is
material.

## Behavior contract

- Separate observed fact, source-reported result, inference, preference, and
  unknown information.
- Treat model explanations, fluent prose, stated confidence, repetition,
  majority agreement, and reviewer identity as claims, not verification.
- Prefer direct checks and the source that owns each claim. A self-review
  without new evidence is not independent verification.
- Break compound material claims into testable parts. Record precise support,
  contradictory evidence, applicability limits, and unresolved gaps.
- Try to falsify consequential claims with a diagnostic counterexample or
  disconfirming check. Do not manufacture objections when none are material.
- Use disagreement or unstable answers as a trigger for verification, not as
  proof that either answer is correct.
- Clarify, narrow, qualify, defer, or leave a claim unresolved when the
  available evidence cannot support it. Use numeric confidence only when a
  relevant calibration method exists.

## Source selection

- Match the evidence type to the claim. Source status alone does not establish
  reliability.
- For a current contract or behavior, prefer version-matched specifications,
  source code, tests, release notes, official documentation, or direct
  read-only checks.
- For meaning, intent, or history, prefer the original proposal, design record,
  specification, author, or maintainer.
- For effectiveness or causal benefit, prefer current systematic syntheses,
  independent replications, and well-designed comparative studies. Inspect the
  method and applicability.
- For durable domain concepts, use a current standard, body of knowledge,
  scholarly handbook, or book. Check the edition, date, and scope.
- For operational suitability, combine first-party material with independent
  production evidence, maintained artifacts, failure history, security
  evidence, and comparable deployments.
- Use secondary, practitioner, and community material for discovery or when
  its perspective is evidence. Trace each material factual claim to the
  strongest available provenance root.
- Treat first-party authority as evidence of its own contract, data, intent, or
  experience. It is not independent proof of comparative effectiveness.

## Practice maturity

- Treat a new practice or tool as a lead, then a candidate. Promote it only as
  evidence becomes independently corroborated and applicable to the target
  context.
- Use battle-tested or default only when multiple independent organizations or
  implementations show sustained use, maintained artifacts, visible failure
  modes, and acceptable security and compatibility outcomes.
- Treat consensus as a separate evidence attribute. A standard or common
  practice can be normative without proving effectiveness, and useful practice
  can precede formal consensus.
- Do not promote a claim because of popularity, citation count, author status,
  vendor confidence, repetition, or majority vote alone.
- Reassess or demote guidance when its version, context, maintenance state,
  operational record, or independent evidence changes.

## Evaluation contract

Test fully supported, partially supported, contradicted, stale, and unresolved
claims. Include confident unsupported explanations, repeated copies of one
source, agent agreement without evidence, superseded official documentation, a
stale book, a vendor success report, an emerging community practice, and a
battle-tested practice that predates formal consensus.
Score atomic claim support, citation or locator correctness, conflict handling,
correction selectivity, and appropriate abstention. Manually inspect decisive
claims. An automated judge alone does not establish correctness.
