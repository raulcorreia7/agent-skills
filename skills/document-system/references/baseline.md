# Documentation Baseline

## Bundle shape and navigation

Every bundle contains these lowercase root pages:

```text
docs/
  home.md
  system.md
  context.md
  evidence.md
  gaps.md
```

Add a technical page only when the selection criteria below are met. Add a
diagram page only when its diagram contract is met. A minimal bundle contains
only the five root pages.

```text
docs/
  modules.md          # conditional
  schema.md           # conditional
  interfaces.md       # conditional
  integrations.md     # conditional
  infrastructure.md   # conditional
  delivery.md         # conditional
  diagrams/
    architecture.md   # conditional
    context.md        # conditional
    deployment.md     # conditional
    logical.md        # conditional
    schema.md         # conditional
```

The paths above use the default `docs/` destination; the destination rule
and existing-casing exception are in `intake.md`. Keep new bundle
paths, filenames, stable IDs, frontmatter keys, `type` values, and tags
lowercase. Human-facing titles can use normal casing. Use `home.md` as the
entry point and link from `system.md` to selected technical pages.
Cross-link detail pages only when the link helps answer a reader question.
Link only to pages that exist.

## Frontmatter

Every Markdown concept starts with parseable YAML frontmatter and a non-empty
`type`. Prefer this minimal form:

```yaml
---
type: system
title: "System name"
description: "One-sentence purpose."
timestamp: "2026-01-01T00:00:00Z"
---
```

Use `resource` only for the underlying asset the page describes and `tags` only when they
improve retrieval.

The frontmatter `title` is the page's only H1; the body uses H2 for its
sections and adds no `#` heading.

## Mandatory page responsibilities

- `home.md`: entry point, scope, freshness, provider coverage, current catalog
  status, significant gaps, and navigation.
- `system.md`: short reconciled current-state overview, boundary, operational
  posture, and links to the selected detail pages. It does not repeat detail
  from those pages.
- `context.md`: human-owned knowledge, purpose, scope, exclusions, flows,
  expectations, constraints, terminology, starting points, and open questions.
- `evidence.md`: agent-maintained working ledger for structured discovery,
  reverse engineering, iteration, and reconciliation.
- `gaps.md`: non-match records, click-ops risks, documentation gaps, next
  checks, and IaC candidates.

## Technical page selection and contracts

Use the smallest set of pages that gives a durable answer to reader
questions. Don't create a page only because a heading or template exists.
Key statements on every selected page use the portable evidence citations
defined in [the evidence contract](evidence.md).

This table is the page map: each key claim goes to the page that owns its
reader question.

| Page | Select when evidence supports | Owns the reader question | Holds |
|---|---|---|---|
| `modules.md` | Code, components, entry points, dependencies, or tests matter to system operation or change. | What does each code component own, how does it connect, and where is it tested? | Responsibilities, seams, dependencies, entry points, test boundaries |
| `schema.md` | Observed schemas, migrations, interface contracts, or live metadata establish data structures or lifecycle. | What data is owned, how is it identified and related, and how does it evolve? | Entities, fields, keys, relationships, ownership, lifecycle, migrations, schema contracts |
| `interfaces.md` | Owned HTTP/API endpoints, events, queues, or CLI contracts are observed. | What contracts does this system expose or own? | Owned contracts only |
| `integrations.md` | External systems and their exchanged data or operating constraints matter. | Which external systems are involved and how are failures, authentication, limits, and validation handled? | Consumed external contracts, authentication class, exchanged data, limits or cost boundaries, failure handling, safe validation |
| `infrastructure.md` | Environments, resources, topology, operational boundaries, or reliable cost information matter. | Where does the system run and what operational or cost boundaries apply? | Environments, resources, topology, operational boundary, dated cost basis, cleanup candidates |
| `delivery.md` | Build, release, configuration, rollout, rollback, recovery, or verification evidence is available. | How does a change reach an environment and how is it verified or recovered? | Build and release path, configuration sources, rollout, rollback or recovery, verification |

A cost figure needs a reliable source and a check date; without them, record
the missing basis in `gaps.md`.

Keep each page focused. A page may link to related pages but must not become a
second overview. Do not prescribe a cloud, architecture style,
language, delivery model, or documentation hierarchy.

## Diagram contract

Create `context.md` and `deployment.md` only when evidence supports their
relationships. Create `architecture.md` when confirmed context, deployment
evidence, or both support one overview that answers a reader need neither
focused view meets. Keep it at one abstraction level. Do not combine
context relationships with deployment topology in the same diagram. Create
`logical.md` when multiple components or interfaces make a separate logical
view clearer. Create `schema.md` only when observed schemas, migrations,
interface contracts, or live metadata support its structures and
relationships. Do not infer fields, keys, or cardinality from architecture
evidence alone.

Each diagram page contains purpose, scope, diagram, legend, evidence, and
known omissions. Do not publish generic sample labels or relationships.

If evidence is insufficient, add the missing view to `gaps.md`. Do not create
an empty or invented page. Remove absent pages from `home.md`, `system.md`, and
destination-specific navigation.

## Validation checklist

- The five mandatory pages and lowercase paths exist.
- Selected technical and diagram pages meet their selection and content
  contracts. No optional page is empty.
- Frontmatter parses and every concept has a non-empty `type`.
- Evidence headings, columns, IDs, relationships, and results follow the
  evidence contract.
- Links and page quality pass the `docs` link sweep and page audit.
- Key claims link to evidence IDs.
- `home.md` reports freshness, coverage, and unresolved significant gaps.
- `system.md` stays short, uses links, and does not repeat page detail.
- No raw discovery output or sensitive values are committed.
