---
name: review
description: Manual invocation only. Evidence-backed assessment of supplied changes, pull requests, system designs, architecture documents, and ADRs.
---

# Review

## Job

Review the supplied artifact against its intent and available evidence. Keep
the artifact unchanged. Review is residual risk: do not use it for style,
format, commit grammar, or quality-gate configuration that a formatter,
linter, schema, or CI should own.

## Priorities

Use these priorities in every review mode. State the source label and the
normalized severity together. Do not use a lower priority to soften a material
defect.

| Priority | Meaning |
|---|---|
| `P0` | Immediate risk of data loss, security compromise, outage, or a broken public contract |
| `P1` | Material correctness or safety defect that blocks acceptance |
| `P2` | Material risk that should be addressed soon but does not block acceptance |
| `P3` | Localized, non-blocking improvement; keep optional suggestions separate when they are not defects |

## Steps

1. Establish the artifact, purpose, scope, material exclusions, contracts, and
   available validation evidence. Ask only when a missing answer changes risk
   or the review boundary.
2. Select and load one review branch:
   - For a diff, branch, commit set, or implementation, read `references/change.md`.
   - For a PR/MR or story-backed change, read `references/pull-request.md` and
     also `references/change.md` when substantive implementation is present.
   - For a system design, architecture document, ADR, or system structure, read
     `references/architecture.md`.
3. For a non-trivial, security-sensitive, public-contract, migration, or large
   implementation, also read `references/change-checklist.md`. Inspect only the
   evidence needed to verify material claims.
   If the implementation adds, changes, selects, repairs, or relies on tests,
   also read `references/test-evidence.md`.
   For requested public PR/MR review text, read
   `references/review-comments.md`.
4. Run a small safe existing check only when it resolves a material review
   question. Classify failures as change-caused, pre-existing, environmental,
   or inconclusive.
5. Separate defects, material risks, questions, and optional suggestions.
   For each suspected finding, identify the violated criterion or contract,
   precise locator, observable consequence, and confirming or disconfirming
   evidence. Reject a finding when it does not survive the falsification
   attempt. Verify each remaining finding or label it uncertain. Account for
   each material part of the supplied artifact. Assign each finding `P0`
   through `P3` from the table above.

## Guardrails

- Keep review read-only. Return proposed fixes or review text as output.
- Obtain explicit approval before any external review action.
- Label speculation and incomplete checks. Reserve verified findings for
  evidence-backed defects.
- Assess correctness, completeness, relevance, and evidence independently of
  report length, polish, format, confidence, or finding count.

## Output

- A mode-appropriate verdict and `P0`-through-`P3` ordered, evidence-backed findings
- Material questions, reviewed coverage, and residual risk
- Copy-pasteable review text only when the user requests it for a PR/MR
