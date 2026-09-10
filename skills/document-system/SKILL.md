---
name: document-system
description: Manual invocation only. Coordinated reader-first system documentation from confirmed intent and observed evidence.
---

# Document System

## Job

Turn confirmed context and observed evidence into a source-backed system bundle.

## Steps

1. Inspect repository guidance and existing documentation. Establish the
   boundary, exclusions, outcomes, seeds, documentation destination, and
   authorized live discovery. Ask for the destination when ambiguity changes
   paths, navigation metadata, link syntax, or renderer constraints.
2. Load only the workflow leaf needed for the current phase:
   - Read `references/intake.md` before bootstrap intake or when scope,
     intended state, seeds, discovery authorization, or destination is
     unsettled.
   - Read `references/discovery.md` before repository or authorized live
     discovery.
   - Read `references/reconciliation.md` before substantial reconciliation.
   - Read `references/synthesis.md` before generating or materially revising
     reader pages.
   - Read `references/migration.md` only when existing documentation will move,
     merge, or be retired.
3. Propose human-owned intended state in `docs/context.md`. Never overwrite it
   from observed evidence or use it as scratch space.
4. Before you create or change `docs/evidence.md`, its IDs, element kinds,
   relationships, or reconciliation records, read `references/evidence.md`.
   Trace approved material dependencies within the boundary. Keep normalized
   observations and their minimum non-sensitive review locators in
   `docs/evidence.md`. Discard raw responses only after this evidence is
   captured. Never commit raw responses.
5. Reconcile each material context claim as `match`, `mismatch`,
   `context-only`, `evidence-only`, `unresolved`, or `out-of-scope`.
6. Before selecting, creating, materially revising, migrating, or validating
   bundle pages, read `references/baseline.md`. Select optional technical pages
   from the evidence.
   Generate the reader-first `docs/system.md`,
   selected detail pages, `docs/gaps.md`, and evidence-backed diagrams. Migrate
   useful existing documentation into the page that owns the reader question.
7. Before handoff, validate mandatory and selected-page contracts, navigation,
   destination ordering, renderer constraints, coverage, unresolved material
   gaps, sensitive-data exclusion, and dated cost provenance. Report whether
   the result is a partial baseline or complete catalog. Stop at IaC candidates
   in `gaps.md`; require separate approval for IaC work and for staging,
   pushing, PR creation, or Wiki publication.

## Flow

```text
intake → discovery → reconciliation → synthesis → validation
per phase → its leaf
context.md ← human-owned; evidence.md ← normalized observations
stop at IaC candidates; publish | migrate need approval
```

## Assets

Use the mandatory [home](assets/baseline/home.md),
[system](assets/baseline/system.md), [context](assets/baseline/context.md),
[evidence](assets/baseline/evidence.md), and
[gaps](assets/baseline/gaps.md) templates.

After page selection, load only each chosen technical template:

- `modules.md`: [modules](assets/technical-pages/modules.md)
- `schema.md`: [schema](assets/technical-pages/schema.md)
- `interfaces.md`: [interfaces](assets/technical-pages/interfaces.md)
- `integrations.md`: [integrations](assets/technical-pages/integrations.md)
- `infrastructure.md`:
  [infrastructure](assets/technical-pages/infrastructure.md)
- `delivery.md`: [delivery](assets/technical-pages/delivery.md)

After diagram selection, load only each chosen diagram template:

- `architecture.md`: [architecture](assets/diagram-pages/architecture.md)
- `context.md`: [context](assets/diagram-pages/context.md)
- `deployment.md`: [deployment](assets/diagram-pages/deployment.md)
- `logical.md`: [logical](assets/diagram-pages/logical.md)
- `schema.md`: [schema](assets/diagram-pages/schema.md)

A minimal bundle has no empty optional pages. Load a diagram template only when
its evidence contract is met. Replace placeholders and remove inapplicable
links. Keep portable Markdown links as the default navigation. Add
destination-specific navigation metadata only for a confirmed destination.
Replace every `{{...}}` token in a selected asset, including Mermaid node and
relationship labels. Do not publish generic sample labels or relationships.
Create the logical diagram only when it materially improves clarity.

## Guardrails

- Prefer canonical resource IDs and source links over name-only matches.
- Keep the order: context, discovery, reconciliation, synthesis, validation.
- Publish a useful baseline with visible gaps when the user accepts that scope.
- Declare the catalog complete only when no material `unresolved`,
  `context-only`, or unexplained `evidence-only` entries remain.
- Label unknown architecture, relationships, ownership, deployment, and intent.
- Keep sensitive and unnecessary exploitable data out of documentation.
- Keep cloud discovery read-only and within the authorized scope.
- Create pages and folders only for a concrete reader need.

## Composition

- Use `audit` for a deeper read-only inspection when explicitly requested.
- Use `docs` for documentation judgment not owned by this workflow.
- Use `diagrams` for substantive diagram selection or renderer validation.
- Remain usable without optional skills.
- Read `references/sources.md` only to explain, review, or refresh the
  workflow's external design provenance.

## Output

- A lowercase `docs/` bundle with `home.md`, `system.md`, `context.md`,
  `evidence.md`, `gaps.md`, selected evidence-backed technical pages, required
  diagrams when evidence permits, portable Markdown navigation, and valid
  destination-specific navigation metadata when applicable
- Source-backed reconciliation with coverage and unresolved gaps visible
- Validation results, missing provider coverage, and residual documentation risk
