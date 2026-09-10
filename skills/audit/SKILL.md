---
name: audit
description: Manual invocation only. Read-only inspection of repository or system state across project, test, dependency, security, delivery, infrastructure, operations, and cloud concerns.
---

# Audit

## Job

Inspect repository or system state within a read-only boundary.

## Depth

Depth and scope are independent. Default to `quick` and `project` when
unspecified.

| Depth | Contract |
|---|---|
| `quick` | Triage the highest-value evidence and material unknowns |
| `focused` | Examine selected domains with representative evidence and proportionate checks |
| `deep` | Build a coverage matrix and document stronger evidence limits and residual uncertainty |

## Modes

| Mode | Focus |
|---|---|
| `project` | Repository shape, ownership, build, interfaces, and stale signals |
| `tests` | Confidence, gaps, flakes, fixtures, and CI reliability |
| `dependencies` | Supply chain, ownership, versions, licenses, update pressure, and unnecessary weight |
| `security` | Auth, secrets, privacy, inputs, exposure, logging, abuse paths, and data handling |
| `delivery` | CI/CD, releases, migrations, rollout, rollback, artifacts, and promotion |
| `infra` | IaC, resources, environments, configuration, policy, and drift signals |
| `operations` | SRE, observability, reliability, incident readiness, capacity, and cost signals |
| `cloud` | Explicitly approved live metadata correlated with owned code and configuration |
| `inspect` | Source-backed maps and selected artifacts rather than ranked issues |
| `full` | Cross-domain synthesis of `project`, `tests`, `dependencies`, `security`, `delivery`, `infra`, and `operations`; `cloud` remains separate |

## Steps

1. Resolve scope and depth. Default to `quick` + `project`. Ask only when
   the boundary changes risk, cost, access, or deliverable.
2. Route supplied changes and designs to the change-assessment workflow. Route
   standalone documentation audits to `docs`.
3. Load only the reference for the selected mode:
   - `project`: read `references/project.md`.
   - `tests`: read `references/tests.md`.
   - `dependencies`: read `references/dependencies.md`.
   - `security`: read `references/security.md`.
   - `delivery`: read `references/delivery.md`.
   - `infra`: read `references/infrastructure.md`.
   - `operations`: read `references/operations.md`.
   - `inspect`: read `references/inspect.md`.
   - `full`: read all seven local domain references above. Do not include
     `cloud` implicitly.
   - `cloud`: obtain explicit approval for the live-system scope, then read
     `references/live-systems.md` before a query.
4. Inspect local evidence before live or approval-gated evidence. Map only the
   entrypoints, owners, contracts, data, tests, configuration, infrastructure,
   delivery, and operations that fit the selected scope.
5. Separate facts, evidence-backed inferences, unknowns, and coverage limits.
6. Rank by impact, confidence, blast radius or exploitability, and verification
   path. Do not inflate style preferences.
7. Recommend the smallest follow-up. Finish when each selected domain has
   evidence, a finding or no-finding result, and a stated coverage limit.

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

- Keep severity ordering here. Hand approved follow-up work to its artifact
  owner. Use parallel `to-plan` only for a requested delegated plan.

## Output

- Scope, mode, depth, and evidence limits
- Coverage matrix: selected domains, evidence, no-finding results, and omitted
  or approval-gated domains
- Summary and severity-ordered findings
- Maps or selected artifacts when useful
- Unknowns, approval-gated evidence, and residual risk
- Focused follow-up owners
