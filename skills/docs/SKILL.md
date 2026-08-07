---
name: docs
description: Creates, edits, audits, or validates standalone documentation. Use for guides, references, runbooks, and specifications, not source comments or coordinated system bundles.
---

# Docs

## Job

Create source-backed documentation that lets the reader complete the next task.

## Steps

1. Identify the reader, document type, source of truth, requested branch, write
   boundary, and target location. Ask for the destination when ambiguity
   changes paths, page casing, navigation metadata, link syntax, or renderer
   constraints.
2. Inspect nearby navigation, links, generated ownership, terminology, and
   canonical sources. Continue when each material claim has an evidence route.
3. Select the branch and load only its matching references:
   - Read `references/doc-shapes.md` when the document shape is not already set.
   - For a full standalone documentation audit, read
     `references/information-architecture.md`, `references/page-quality.md`,
     `references/link-validation.md`, and
     `references/content-deduplication.md`.
   - Read `references/information-architecture.md` for a navigation or
     documentation-tree reorganization.
   - Read `references/page-quality.md` for a page-level quality or correctness
     audit.
   - Read `references/link-validation.md` for a link sweep.
   - Read `references/content-deduplication.md` for duplicate or stale-content
     cleanup.
   - Read `references/llms-txt.md` for agent-readable documentation surfaces.
   For an audit or validation request, stay read-only and return findings. Edit
   only when the user separately requests an edit.
4. For authoring or editing, put the outcome or first action before supporting
   explanation, write current contracts in present tense, link canonical facts,
   and remove stale or duplicate local copies when the write boundary permits
   it.
5. Add examples, tables, troubleshooting, or a diagram only when they reduce a
   real reader decision or failure risk.
6. Validate links, commands, examples, Markdown, diagrams, and source-backed
   claims in proportion to the change.
7. Stop when the target reader can find the page, perform its primary task, and
   distinguish verified facts from assumptions.

## Guardrails

- Mark unknown or inferred architecture, ownership, deployment, API, and
  configuration facts.
- Keep secrets, customer data, connection strings, and sensitive production
  detail out of documentation.
- Keep source comments with the comments owner and automation with the scripts
  owner.

## Output

- For authoring or editing: ready document or targeted edits; intended reader
  and purpose; evidence and assumptions; unverifiable claims and documentation
  risk.
- For audit or validation: scope; prioritized findings; supporting evidence;
  checks; assumptions; proposed changes; no edits.
