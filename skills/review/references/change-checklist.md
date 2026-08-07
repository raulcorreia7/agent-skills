# Change Review Patterns

## Review Stance

- Favor a pass when the change improves repository health and has no blocking
  correctness, security, data, migration, compatibility, or confidence issue.
- Let automation handle formatting. Spend human or agent attention on behavior
  and risk.
- For huge reviews, ask for a split or give high-level risk direction first.
- For human-facing commands and workflows, check discoverability, safe defaults,
  familiar language, actionable errors, and recovery paths.

## Surface

| Area | Check |
|---|---|
| Behavior | Expected outcome, edge cases, failure paths |
| Contracts | APIs, schemas, types, config, migrations, versioning |
| Data | Persistence, idempotency, concurrency, rollback |
| Security | Auth/authz, input handling, secrets, injection, resource limits |
| Tests | Meaningful assertions, regression seams, flake risk |
| Maintainability | Names, ownership, shared change obligations, boundaries, pattern fit, abstraction and navigation cost, common-path discoverability |
| Necessity | Every changed surface has a current reason tied to the stated intent. No abandoned, speculative, duplicate, or unrelated work remains. |
| Operations | Logging, metrics, rollout, fallback, supportability |
| Documentation | Changed behavior and contracts, commands/examples, versions, freshness, navigation, runbooks, diagrams, release notes |

## Documentation Freshness

- Identify documentation owners affected by behavior, API/schema, config,
  command/setup, dependency, deployment, operational, or support changes.
- Verify commands, examples, versions, screenshots/diagrams, links, defaults,
  prerequisites, rollout, rollback, and troubleshooting against the change.
- Treat missing required documentation and materially stale claims as findings.
  Do not require documentation churn for internal changes with no reader-facing
  or operational impact.
- A modified README, generated reference, or changelog does not prove freshness.
  Inspect the claims that the change invalidates.

## Specialist Triggers

Recommend specialist review for auth/authz, secrets/crypto, database migrations,
public APIs, dependencies/licenses, UI/accessibility, infra/deployment, privacy,
legal, or regulated data.

## Sources

- [Google Engineering Practices: reviewing a changelist](https://google.github.io/eng-practices/review/reviewer/looking-for.html)
- [OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/)
