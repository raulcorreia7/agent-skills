---
name: audit
description: Manual invocation only. Inspects repository or system state read-only across project, test, dependency, security, delivery, infrastructure, operations, and cloud concerns.
---

# Audit

## Job

Inspect repository or system state within a read-only boundary.
Not for standalone documentation audits; use `docs`.

## Modes

Load only the reference for each selected mode.

| Mode | Focus | Load |
| --- | --- | --- |
| `project` | Repository shape, ownership, build, interfaces, and stale signals | `references/project.md` |
| `tests` | Confidence, gaps, flakes, fixtures, and CI reliability | `references/tests.md` |
| `dependencies` | Supply chain, ownership, versions, licenses, update pressure, and unnecessary weight | `references/dependencies.md` |
| `security` | Auth, secrets, privacy, inputs, exposure, logging, abuse paths, and data handling | `references/security.md` |
| `delivery` | CI/CD, releases, migrations, rollout, rollback, artifacts, and promotion | `references/delivery.md` |
| `infra` | IaC, resources, environments, configuration, policy, and drift signals | `references/infrastructure.md` |
| `operations` | SRE, observability, reliability, incident readiness, capacity, and cost signals | `references/operations.md` |
| `cloud` | Explicitly approved live metadata correlated with owned code and configuration | `references/live-systems.md`, after approval of the live-system scope and before any query |
| `inspect` | Source-backed maps and selected artifacts rather than ranked issues | `references/inspect.md` |
| `full` | Cross-domain synthesis of `project`, `tests`, `dependencies`, `security`, `delivery`, `infra`, and `operations` | All seven of those domain references; include `cloud` only when selected separately |

## Depth

Depth and mode are independent. Default to `quick` and `project` when
unspecified.

| Depth | Contract |
| --- | --- |
| `quick` | Triage the highest-value evidence and significant unknowns |
| `focused` | Examine selected domains with representative evidence and proportionate checks |
| `deep` | Build a coverage matrix and document stronger evidence limits and residual uncertainty |

## Steps

1. Resolve mode and depth. Route supplied changes and designs to the
   change-review workflow and standalone documentation audits away. Otherwise
   load each selected mode's reference. Complete when mode, depth,
   and boundary are stated and each selected reference is loaded, or the
   request is routed away.
2. Inspect local evidence before live or approval-gated evidence. Map only the
   entrypoints, owners, contracts, data, tests, configuration, infrastructure,
   delivery, and operations that fit the selected scope. Complete when each
   selected domain has mapped evidence or a stated coverage limit.
3. Give each claim its evidence state. Rank findings by impact, confidence,
   blast radius or exploitability, and verification path, and keep style
   preferences at their real impact. Complete when each finding has a severity
   and a rank.
4. Recommend the smallest follow-up for each finding. Complete when each
   selected domain has evidence, a finding or no-finding result, and a stated
   coverage limit, and each finding has a follow-up owner.

## Flow

```text
input ← scope, mode, depth (default quick + project)
change or design? → change-review workflow | docs only → docs | else continue
for mode in selected: evidence ← local → approval-gated live
result ← finding | no-finding + coverage limit
rank: impact, confidence, blast radius, verification path
stop: every selected domain has a result and coverage limit; every finding an owner
```

## Findings

For each finding, give its severity, evidence, verification path, smallest fix
direction, and confidence.

| Severity | Finding | Evidence | Verification path | Fix direction | Confidence |
|---|---|---|---|---|---|

Example:

| Severity | Finding | Evidence | Verification path | Fix direction | Confidence |
|---|---|---|---|---|---|
| High | Migration can run before backup verification | `deploy.yml:82` invokes the migration before the backup-check step | Trace the job dependency order and inspect the failed-check path | Make backup verification a required predecessor | High |

- `Critical`: data loss, security break, production outage, or broken public
  contract.
- `High`: likely bug or regression, unsafe migration, or essential protection
  gap.
- `Medium`: maintainability, confidence, ownership, documentation, or
  operational risk.
- `Low`: localized improvement with limited impact.

## Guardrails

- Keep the audit read-only. Treat production data and live systems as separate
  approval boundaries.
- Limit compliance and coverage claims to the available evidence.
- Identify sensitive locations and protect their values; cite locations and
  credential types, never values.

## Composition

- Use `plan-remediation` when the findings need a fix plan.
- Hand other approved follow-up work to its artifact owner.

## Output

- Scope, mode, depth, and evidence limits
- Coverage matrix: selected domains, evidence, no-finding results, and omitted
  or approval-gated domains
- Summary and severity-ordered findings
- Maps or selected artifacts when useful
- Unknowns, approval-gated evidence, and residual risk
- Focused follow-up owners
