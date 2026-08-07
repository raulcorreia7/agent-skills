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
only the five root pages and has no empty optional pages.

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

Keep new bundle paths, filenames, stable IDs, frontmatter keys, `type` values,
and tags lowercase. Preserve existing destination-specific path and filename
casing unless an approved migration explicitly changes it. Human-facing titles
can use normal casing. Use portable Markdown links for navigation. Use
`home.md` as the concise entry point. Link from `system.md` to selected
technical pages. Cross-link detail pages only when the link helps answer a
reader question. Navigation links target existing pages only.

If the destination is ambiguous and changes paths, navigation metadata, link
syntax, or renderer constraints, ask before adding destination-specific
artifacts. Otherwise, keep the portable baseline and add none.

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

Use `resource` only for a canonical underlying asset and `tags` only when they
improve retrieval.

## Mandatory page responsibilities

- `home.md`: concise entry point, scope, freshness, provider coverage, current
  catalog status, material gaps, and navigation.
- `system.md`: short reconciled current-state overview, boundary, operational
  posture, and links to the selected detailed pages. It does not duplicate
  detailed technical reference material.
- `context.md`: human-maintained knowledge, purpose, scope, exclusions, flows,
  expectations, constraints, terminology, starting points, and open questions.
  AI changes remain proposals until confirmed.
- `evidence.md`: agent-maintained working ledger for structured discovery,
  reverse engineering, iteration, and reconciliation.
- `gaps.md`: non-match records, click-ops risks, documentation gaps, next
  checks, and IaC candidates.

## Technical page selection and contracts

Use the smallest set of pages that provides a durable answer to reader
questions. Do not create a page solely because a heading or template exists.
Material statements on every selected page use the portable evidence citations
defined in [the evidence contract](evidence.md). Do not expose raw provider
output, credentials, secret-bearing configuration, customer data, or
unnecessary exploitable detail.

| Page | Select when evidence supports | Owns the reader question |
|---|---|---|
| `modules.md` | Code, components, entry points, dependencies, or tests are material to system operation or change. | What does each code component own, how does it connect, and where is it tested? |
| `schema.md` | Observed schemas, migrations, interface contracts, or live metadata establish data structures or lifecycle. | What data is owned, how is it identified and related, and how does it evolve? |
| `interfaces.md` | Owned HTTP/API endpoints, events, queues, or CLI contracts are observed. | What contracts does this system expose or own? |
| `integrations.md` | External systems and their exchanged data or operating constraints are material. | Which external systems are involved and how are failures, authentication, limits, and validation handled? |
| `infrastructure.md` | Environments, resources, topology, operational boundaries, or reliable cost information are material. | Where does the system run and what operational or cost boundaries apply? |
| `delivery.md` | Build, release, configuration, rollout, rollback, recovery, or verification evidence is available. | How does a change reach an environment and how is it verified or recovered? |

Use `modules.md` for responsibilities, seams, dependencies, entry points, and
test boundaries. Use `schema.md` for entities, fields, keys, relationships,
ownership, lifecycle, migrations, and schema contracts. Link it to
`diagrams/schema.md` only when that diagram exists. Use `interfaces.md` only
for owned contracts. Describe consumed external contracts in `integrations.md`
when that distinction helps. Use `integrations.md` for authentication class,
exchanged data, limits or cost boundaries, failure handling, and safe
validation. Use `infrastructure.md` for environments, resources, topology,
operational boundary, dated cost basis, and cleanup candidates. Cost figures
require a reliable source and check date. Otherwise record the missing basis in
`gaps.md`. Use `delivery.md` for build/release path, configuration sources,
rollout, rollback or recovery, and verification.

Keep each page focused. A page may link to related pages, but it must not become
a second catch-all overview. Do not prescribe a cloud, architecture style,
language, delivery model, or documentation hierarchy.

## Diagram contract

Create `context.md` and `deployment.md` only when evidence supports their
relationships. Create `architecture.md` when confirmed context, deployment
evidence, or both support one overview that answers a reader need not already
met by either focused view. Keep it at one abstraction level. Do not combine
context relationships with deployment topology in the same diagram. Create
`logical.md` when multiple components or interfaces make a separate logical
view materially clearer. Create `schema.md` only when observed schemas,
migrations, interface contracts, or live metadata support its structures and
relationships. Do not infer fields, keys, or cardinality from architecture
evidence alone.

Each diagram page contains purpose, scope, diagram, legend, evidence, and
known omissions. Replace every template placeholder, including Mermaid node
and relationship labels. Do not publish generic sample labels or relationships.

If evidence is insufficient, add the missing view to `gaps.md`. Do not create
an empty or invented page. Remove absent pages from `home.md`, `system.md`, and
destination-specific navigation.

## Validation checklist

- The five mandatory pages and lowercase paths exist.
- Selected technical and diagram pages meet their selection and content
  contracts. No empty optional pages exist.
- Frontmatter parses and every concept has a non-empty `type`.
- Evidence headings, columns, IDs, relationships, and results follow the
  evidence contract.
- Internal Markdown links resolve and navigation links only target existing
  pages.
- Material claims link to evidence IDs.
- `home.md` reports freshness, coverage, and unresolved material gaps.
- `system.md` remains short, uses links, and does not duplicate detailed content.
- No raw discovery output or sensitive values are committed.
