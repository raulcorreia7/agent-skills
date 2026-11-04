---
name: plan-remediation
description: Manual invocation only. Plans evidence-backed remediation for code, plans, codebases, and infrastructure across stabilization, root-cause correction, and recurrence reduction.
---

# Plan remediation

## Job

Produce a read-only remediation plan for code, a plan, a codebase, or
infrastructure from an artifact, stable locator, finding set, or evidence
packet. Leave code, deployments, publications, and live systems unchanged, even
when urgent action is recommended.

## Steps

1. Resolve the input, evidence boundary, desired state, access authority,
   coverage limits, and supplied findings. Without a problem statement or
   target, inspect the supplied input read-only, identify two to four
   evidence-backed candidates with preliminary severity and evidence, and
   recommend the highest-severity, highest-confidence candidate. Complete when
   the target and the selected findings are explicit.
2. Verify each selected finding against the input, local and supplied evidence,
   and current authoritative external sources when a version, vulnerability,
   standard, or infrastructure behavior matters and network research is
   authorized. Separate fact, source-reported result, inference, unknown, and
   coverage limit. Normalize each verified finding to the severity scale below,
   preserving its source label; map `P0`, `P1`, `P2`, and `P3` to `Critical`,
   `High`, `Medium`, and `Low`. Complete when every selected finding is
   verified with a severity and source label, or rejected with a reason.
3. Give each finding only evidence-supported `Stabilize`, `Correct`, and
   `Prevent` actions. Name the outcome, owner or owning location, dependencies,
   authority gate, acceptance evidence, and rollback or recovery condition.
   Read [security response](references/security-response.md) when a finding
   involves a vulnerability, exploitation, unauthorized access, data or secret
   leakage, or suspected persistence. Complete when each retained finding has
   each horizon planned with proof or marked `Not required` with evidence.
4. Build one portfolio order: ongoing harm or active exposure, severity,
   dependency gates, blast radius or exploitability, confidence, then the
   smallest reversible action that unlocks later proof. A low-severity easy fix
   never displaces unresolved Critical work. Complete when the portfolio has
   one executable dependency order.

## Flow

```text
input ← artifact, locator, finding set, or evidence packet
target explicit? yes → continue | no → 2–4 candidates, recommend one, ask
verify → reject unsupported → severity ← map(source labels)
per finding: Stabilize, Correct, Prevent (evidence-supported or Not required)
portfolio ← harm → severity → gates → blast radius → confidence → reversible unlock
stop: every finding verified or rejected, horizons proven, one dependency order
```

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

## Practices

Read [remediation practices](references/practices.md) only when source rationale
or a detailed example matters.

## Guardrails

- Use complexity, coupling, coverage, churn, scanner counts, and documentation
  age as triage evidence, never universal targets.
- Make temporary controls explicit with an owner, review point, and removal
  condition. A workaround is not permanent closure.
- Protect credentials and sensitive values. Cite locations and credential
  types, never values.
- Keep external search and live evidence within the user's authority.

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
