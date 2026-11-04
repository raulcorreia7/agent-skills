---
name: docs
description: "Creates, edits, audits, or validates standalone documentation: guides, references, runbooks, specifications, and ADRs. Use when standalone documentation is the primary deliverable. Not for source comments or in-code API documentation; use comments. Not for coordinated system bundles; use document-system."
---

# Docs

## Job

Create source-backed documentation that lets the reader complete the next task.

## Modes

| Mode | Use when | Load |
| --- | --- | --- |
| `author` | Creating or editing a page | `references/doc-shapes.md` when the document shape is not already set |
| `full audit` | A full standalone documentation audit | `references/information-architecture.md`, `references/page-quality.md`, `references/link-validation.md`, `references/content-deduplication.md` |
| `reorganize` | A navigation or documentation-tree reorganization | `references/information-architecture.md` |
| `page audit` | A page-level quality or correctness audit | `references/page-quality.md` |
| `link sweep` | Checking links in a documentation scope | `references/link-validation.md` |
| `cleanup` | Duplicate or stale-content cleanup | `references/content-deduplication.md` |
| `agent surface` | Agent-readable documentation surfaces such as `llms.txt` | `references/llms-txt.md` |

`full audit`, `page audit`, and `link sweep` are read-only: return findings and edit
only when the user separately requests an edit. `reorganize` and `cleanup`
start read-only; their reference states when to apply changes.

## Steps

1. Identify the reader, document type, source of truth, mode, write boundary,
   and target location. Ask for the destination when ambiguity changes paths,
   page casing, navigation metadata, link syntax, or renderer constraints.
   Complete when the mode, reader, destination, and write boundary are set.
2. Inspect nearby navigation, links, generated ownership, terminology, and
   canonical sources, and load the mode's references. Complete when each
   material claim has an evidence route.
3. Write or assess. When writing, put the outcome or first action before
   supporting explanation, and remove stale or duplicate local copies when the
   write boundary permits it. Add examples, tables, troubleshooting, or a
   diagram only when they reduce a real reader decision or failure risk.
   Complete when each requested page is drafted or each finding is recorded
   with its evidence.
4. Validate links, commands, examples, Markdown, diagrams, and source-backed
   claims in proportion to the change. Complete when every selected check has a
   result.

## Flow

```text
input ← request, target docs, canonical sources
scope → gather evidence → write | assess → validate
read-only mode? yes → findings, no edits | no → edit within the write boundary
loop: validate → fix → until the selected checks pass
stop: the reader can find the page, perform its primary task, and tell verified facts from assumptions
```

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
