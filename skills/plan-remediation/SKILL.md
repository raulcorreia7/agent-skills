---
name: plan-remediation
description: Manual invocation only. Plans evidence-backed remediation for code, plans, codebases, and infrastructure across stabilization, root-cause correction, and recurrence reduction.
---

# Plan remediation

## Job

Produce a read-only remediation plan for code, a plan, a codebase, or
infrastructure. Accept an artifact, stable locator, finding set, or evidence
packet. Do not edit, deploy, publish, or change a live system.

## Inputs

Establish the evidence boundary, desired state, supplied findings, access
authority, and coverage limits.

## Steps

1. Resolve the input, evidence boundary, desired state, and supplied findings.
   Without a problem statement or target, inspect the supplied input read-only;
   identify two to four evidence-backed candidates with preliminary severity and
   evidence; ask one selection question; recommend the highest-severity,
   highest-confidence candidate; and continue only after the target is explicit.
2. Verify each selected finding against the input, local and supplied evidence,
   and current authoritative external sources when a version, vulnerability,
   standard, or infrastructure behavior is material and network research is
   authorized. Separate fact, source-reported result, inference, unknown, and
   coverage limit. Reject unsupported candidates.
3. Normalize verified findings to `Critical`, `High`, `Medium`, or `Low`.
   Preserve source labels. Map `P0`, `P1`, `P2`, and `P3` to `Critical`, `High`,
   `Medium`, and `Low`.
4. Give each finding only evidence-supported `Stabilize`, `Correct`, and
   `Prevent` actions. Name the outcome, owner or owning location, dependencies,
   authority gate, acceptance evidence, and rollback or recovery condition.
   Mark a horizon `Not required` with evidence rather than inventing work.
5. Build one portfolio order: ongoing harm or active exposure, severity,
   dependency gates, blast radius or exploitability, confidence, then the
   smallest reversible action that unlocks later proof. A low-severity easy fix
   never displaces unresolved Critical work.
6. Finish when every selected finding is verified or rejected, each retained
   finding has applicable horizons and proof, and the portfolio has one
   executable dependency order.

## References

Read [remediation practices](references/practices.md) only when source rationale
or a detailed example is material.

## Severity

- `Critical`: data loss, security break, production outage, or broken public
  contract.
- `High`: likely bug or regression, unsafe migration, or essential protection
  gap.
- `Medium`: maintainability, confidence, ownership, documentation, or
  operational risk.
- `Low`: localized improvement with limited impact.

## Horizons

- **Stabilize:** Reduce immediate risk and establish trustworthy evidence with
  the smallest reversible action, such as bounded characterization or regression
  tests, rollback, isolation, access restriction, credential revocation, or a
  minimal current-state runbook.
- **Correct:** Repair the affected state and demonstrated root cause under
  evidence. Refactor, introduce a seam, replace a dependency, or revise a plan
  only when observed coupling, change spread, testability, ownership, or failure
  behavior justifies it.
- **Prevent:** Reduce recurrence likelihood and verify durable controls. Select
  only applicable ownership, CI evidence, regression protection, lifecycle
  documentation, dependency policy, observability, least privilege,
  policy-as-code, or temporary-control retirement.

## Guardrails

- Treat exploitation, unauthorized access, data or secret leakage, and suspected
  persistence as an incident requiring immediate escalation, evidence
  preservation, containment, eradication, trusted recovery, and monitoring. A
  vulnerability ticket alone is insufficient.
- When no compromise is known, remediate vulnerabilities by identifying,
  prioritizing, acquiring or designing, applying through the approved change
  path, and verifying the affected population.
- Use complexity, coupling, coverage, churn, scanner counts, and documentation
  age as triage evidence, never universal targets.
- Make temporary controls explicit with an owner, review point, and removal
  condition. A workaround is not permanent closure.
- Protect credentials and sensitive values. Cite locations and credential
  types, never values.
- Keep external search and live evidence within the user's authority. Keep the
  plan read-only, even when urgent action is recommended.

## Output

- Input, target, desired state, evidence boundary, and coverage limits.
- Verified severity-ordered findings; rejected candidates and reasons.
- Per finding: evidence and consequence, then `Stabilize`, `Correct`, and
  `Prevent` actions with proof, owner or location, dependencies, gates, and
  rollback or recovery.
- One dependency-aware portfolio priority order and immediate escalation notice
  when active harm is plausible.
- Unknowns, residual risk, and source-backed assumptions.
- A self-contained response by default. Write a file only when the user
  explicitly requests persistence and names or approves the destination.
