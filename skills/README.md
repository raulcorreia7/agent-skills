# Skill Catalog

> Choose the smallest skill that owns the requested outcome.

Skills marked `implicit` can activate from a matching request. Request `manual`
skills explicitly by name. Compose skills only when their jobs are independently
useful.
The primary skill owns the final deliverable.

## Install

Install one skill for the current repository, or install all skills for the
current user:

```text
python skills.py install ast-grep
python skills.py install --all --global
```

## Build

| Skill | Invocation | Use |
|---|---|---|
| [`code`](code/SKILL.md) | `implicit` | Implement or explain application behavior |
| [`refactor`](refactor/SKILL.md) | `manual` | Restructure code while preserving behavior |
| [`scripts`](scripts/SKILL.md) | `implicit` | Build scripts, CLI helpers, and developer automation |
| [`create-tests`](create-tests/SKILL.md) | `implicit` | Create or improve a primary test deliverable |

## Research, inspect, and improve

| Skill | Invocation | Use |
|---|---|---|
| [`research-highquality`](research-highquality/SKILL.md) | `manual` | Research broad or contested questions with traceable evidence |
| [`ingest-sources`](ingest-sources/SKILL.md) | `implicit` | Acquire and prepare material external sources with provenance, safety, and retention controls |
| [`ast-grep`](ast-grep/SKILL.md) | `implicit` | Find code structures or author ast-grep rules |
| [`debug`](debug/SKILL.md) | `implicit` | Isolate an evidence-backed failure cause |
| [`audit`](audit/SKILL.md) | `manual` | Inspect repository or system state within a read-only boundary |
| [`optimize`](optimize/SKILL.md) | `manual` | Rank evidence-backed improvements to a measurable target |
| [`code-scanner`](code-scanner/SKILL.md) | `manual` | Run code scans |
| [`triage`](triage/SKILL.md) | `manual` | Triage bugs, issues, tickets, and PRs into owned next actions |

## Review

| Skill | Invocation | Use |
|---|---|---|
| [`adversarial-review`](adversarial-review/SKILL.md) | `manual` | Run two isolated artifact reviews and adjudicate their evidence |
| [`review`](review/SKILL.md) | `manual` | Assess supplied changes, PRs, and designs against evidence |

## Decide and plan

| Skill | Invocation | Use |
|---|---|---|
| [`discuss-architecture`](discuss-architecture/SKILL.md) | `manual` | Align system boundaries and architecture trade-offs |
| [`to-prd`](to-prd/SKILL.md) | `manual` | Produce source-backed, decision-ready requirements |
| [`to-plan`](to-plan/SKILL.md) | `manual` | Produce an implementation-ready plan |
| [`to-issues`](to-issues/SKILL.md) | `manual` | Decompose an approved PRD or plan into issue drafts |
| [`plan-remediation`](plan-remediation/SKILL.md) | `manual` | Plan evidence-backed remediation across three horizons |

## Document and explain

| Skill | Invocation | Use |
|---|---|---|
| [`clear-writing`](clear-writing/SKILL.md) | `implicit` | Write, rewrite, or review prose |
| [`docs`](docs/SKILL.md) | `implicit` | Create, edit, audit, or validate standalone documentation |
| [`comments`](comments/SKILL.md) | `implicit` | Maintain comments and source API documentation |
| [`design-md`](design-md/SKILL.md) | `implicit` | Work with Google DESIGN.md files |
| [`document-system`](document-system/SKILL.md) | `manual` | Build a coordinated, evidence-backed system documentation set |
| [`diagrams`](diagrams/SKILL.md) | `implicit` | Create or validate Mermaid, Graphviz DOT, or D2 diagrams |

## Git and workspace

| Skill | Invocation | Use |
|---|---|---|
| [`git`](git/SKILL.md) | `implicit` | Inspect Git, draft text, or run an approved Git workflow |
| [`worktrees`](worktrees/SKILL.md) | `manual` | Manage Git worktrees and provider review checkouts |
