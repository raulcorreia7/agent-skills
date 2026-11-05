---
name: review
description: Manual invocation only. Assesses supplied changes, pull requests, system designs, architecture documents, and ADRs against their intent and evidence.
---

# Review

## Job

Review the supplied artifact against its intent and available evidence, and
keep the artifact unchanged. Review residual risk; leave style, format, commit
grammar, and quality-gate configuration to the formatter, linter, schema, or CI
that owns them.

## Modes

Select every mode that applies.

| Mode | Use when | Load |
| --- | --- | --- |
| `change` | A diff, branch, commit set, or implementation | `references/change.md` |
| `pull-request` | A PR/MR or story-backed change | `references/pull-request.md`, plus `references/change.md` when substantive implementation is present |
| `architecture` | A system design, architecture document, ADR, or system structure | `references/architecture.md` |

## Steps

1. Establish the artifact, purpose, scope, relevant exclusions, contracts, and
   available validation evidence. Load each selected mode's references, plus:
   - `references/change-checklist.md` for a non-trivial, security-sensitive,
     public-contract, migration, or large implementation;
   - `references/test-evidence.md` when the implementation adds, changes,
     selects, repairs, or relies on tests;
   - `references/review-comments.md` when the user requests public PR/MR
     review text.

   Complete when the review boundary is stated and every applicable reference
   is loaded.
2. Assess the artifact. Run a small safe existing check only when it resolves a
   key review question, and classify each failure as change-caused,
   pre-existing, environmental, or inconclusive. Separate defects, significant
   risks, questions, and optional suggestions. For each suspected finding,
   identify the violated criterion or contract, precise locator, observable
   consequence, and confirming or disconfirming evidence. Complete when each
   significant part of the artifact is accounted for and every check that ran is
   classified.
3. Falsify each suspected finding and reject the ones that do not survive.
   Verify each remaining finding or label it uncertain, and assign it a
   priority from the table below. Complete when every finding is verified or
   labelled uncertain, carries a priority and severity, and the verdict is
   `pass`, `findings`, or `not reviewable`.

## Flow

```text
input ← artifact, intent, scope, contracts, validation evidence
modes ← change | pull-request | architecture → load references
finding ← criterion + locator + consequence + evidence
falsified? yes → reject | no → verify or label uncertain → priority
stop: verdict ← pass | findings | not reviewable, with coverage and residual risk
```

## Priorities

Use these priorities in every mode, and state each with its severity, such as
`P1 (High)`. Rate a significant defect at the priority its evidence supports.
A confirmed `P0` or `P1` finding blocks acceptance; keep optional suggestions
that are not defects separate from findings.

Severity:

- `Critical`: data loss, security break, production outage, or broken public
  contract.
- `High`: likely bug or regression, unsafe migration, or essential protection
  gap.
- `Medium`: maintainability, confidence, ownership, documentation, or
  operational risk.
- `Low`: localized improvement with limited impact.

Review priorities map to severity: `P0` = Critical, `P1` = High, `P2` = Medium,
`P3` = Low.

## Guardrails

- Keep review read-only. Return proposed fixes or review text as output.
- Assess correctness, completeness, relevance, and evidence independently of
  report length, polish, format, confidence, or finding count.

## Output

- A `pass`, `findings`, or `not reviewable` verdict and priority-ordered,
  evidence-backed findings, in the selected mode's output order. When several
  modes apply, give one combined report in this order, omitting empty
  sections: Verdict, Findings (one list across modes, each labelled with its
  mode), Questions, Coverage, Checks, Residual risk.
- Key questions, reviewed coverage, and residual risk
- Copy-pasteable review text only when the user requests it for a PR/MR
