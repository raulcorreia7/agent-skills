# Inspect Mode Reference

Build a source-backed inspection or map instead of a ranked issue audit.
Select only the sections that fit the requested scope.

## Discovery Checklist

Use selectively. Do not force every item into small projects.

### Repo And Docs

- Root guidance, READMEs, contribution docs, ownership docs.
- Docs, ADRs, runbooks, diagrams, API docs, changelogs.
- Layout: services, packages, apps, libraries, scripts, tools, tests, infra.
- Build/workflow: manifests, lock files, Makefiles, task runners, CI.

### Code And Runtime

- Entrypoints: web, API, worker, CLI, job, function, plugin, scheduler.
- Boundaries: APIs, modules, adapters, queues, events, file formats, DB access.
- Data: schemas, migrations, seeds, fixtures, external APIs, storage, caches.
- Failure: retries, timeouts, logging, user-visible errors.
- Tests: fastest safe checks, seams, fixtures, e2e, live-resource boundaries.

### Config And Deployment

- Env vars, config files, secret refs, flags.
- Docker, containers, packaging.
- CI/CD, gates, releases, deployments, rollback hints.
- IaC, cloud scripts, Kubernetes, Helm.
- Environments: local, dev, test, staging, production, DR.

### Operations

- Logs, metrics, traces, dashboards, alerts.
- Health/readiness, backups/restore, scaling, quotas.
- Identity, authz, network exposure, dependency scanning.
- Ownership, escalation, support channels.

## Artifact Catalog

Choose the smallest useful artifact set.

| Artifact | Use when |
|---|---|
| Discovery report | Scope is unclear or exploratory |
| Project overview | Onboarding or first contact |
| System map | Multi-service/module/runtime boundaries matter |
| Developer workflow | Setup/build/test/debug is unclear |
| Configuration reference | Settings, env, or config are scattered |
| Deployment/infra overview | IaC, release, environments, or rollback matter |
| Operations notes | Logs, alerts, dashboards, or support paths matter |
| Risk register | Gaps should drive follow-up |
| ADR candidate list | Decisions need durable capture |

## Risk Register Shape

| Risk | Evidence | Impact | Next workflow |
|---|---|---|---|
