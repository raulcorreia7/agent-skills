---
name: document-system
description: Manual invocation only. Coordinated reader-first system documentation from confirmed intent and observed evidence.
---

# Document System

## Job

Turn confirmed context and observed evidence into a source-backed system bundle.

## Steps

1. Intake. Inspect repository guidance and existing documentation. Establish
   the boundary, exclusions, outcomes, seeds, documentation destination, and
   authorized live discovery. Read `references/intake.md` before bootstrap
   intake or while any of these is unsettled. Ask for the destination when
   ambiguity changes paths, navigation metadata, link syntax, or renderer
   constraints. Propose human-owned intended state in `docs/context.md`; never
   overwrite it from observed evidence or use it as scratch space. Complete when
   the boundary, destination, and discovery authorization are confirmed
   and `docs/context.md` holds the proposed intended state.
2. Discovery. Read `references/discovery.md` before repository or authorized
   live discovery, and `references/evidence.md` before you create or change
   `docs/evidence.md`, its IDs, element kinds, relationships, or reconciliation
   records. Trace approved material dependencies within the boundary. Keep
   normalized observations and their minimum non-sensitive review locators in
   `docs/evidence.md`. Discard raw responses only after this evidence is
   captured; never commit raw responses. Complete when every material
   dependency within the boundary has a normalized observation with a locator
   or a recorded gap.
3. Reconciliation. Read `references/reconciliation.md` before substantial
   reconciliation. Complete when every material context claim is recorded as
   `match`, `mismatch`, `context-only`, `evidence-only`, `unresolved`, or
   `out-of-scope`.
4. Synthesis. Read `references/baseline.md` before selecting, creating,
   materially revising, migrating, or validating bundle pages, and
   `references/synthesis.md` before generating or materially revising reader
   pages. Select optional technical pages from the evidence, then read
   `references/assets.md` for the mandatory and selected templates. Generate
   the reader-first `docs/system.md`, selected detail pages, `docs/gaps.md`,
   and evidence-backed diagrams. Read `references/migration.md` only when
   existing documentation will move, merge, or be retired; migrate useful
   content into the page that owns the reader question. Complete when every
   selected page exists with no `{{...}}` token left and each reader question
   has one owning page.
5. Validation. Validate mandatory and selected-page contracts, navigation,
   destination ordering, renderer constraints, coverage, unresolved material
   gaps, sensitive-data exclusion, and dated cost provenance. Stop at IaC
   candidates in `gaps.md`; IaC work is approval-gated. Complete when every
   check has a result and the report states whether the result is a partial
   baseline or a complete catalog.

## Flow

```text
input ← repository guidance, existing docs, confirmed intent, authorized discovery scope
intake → discovery → reconciliation → synthesis → validation
each phase → read its leaf first
context.md ← human-owned intent; evidence.md ← normalized observations
material gaps remain? yes → partial baseline with visible gaps | no → complete catalog
stop: validation reported; IaC candidates wait in gaps.md
```

## Provenance

Read `references/sources.md` only to explain, review, or refresh the
workflow's external design provenance.

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

## Output

- A lowercase `docs/` bundle with `home.md`, `system.md`, `context.md`,
  `evidence.md`, `gaps.md`, selected evidence-backed technical pages, required
  diagrams when evidence permits, portable Markdown navigation, and valid
  destination-specific navigation metadata when applicable
- Source-backed reconciliation with coverage and unresolved gaps visible
- Validation results, missing provider coverage, and residual documentation risk
