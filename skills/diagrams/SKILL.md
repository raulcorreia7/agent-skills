---
name: diagrams
description: Designs, refactors, renders, and validates Mermaid, Graphviz DOT, and D2 diagrams. Use when a diagram is the primary deliverable.
---

# Diagrams

## Job

Create the smallest source-backed diagram that answers one reader question on
its target platform.

## Steps

1. Define the reader question, evidence, scope, destination, target renderer,
   and editability requirement. Confirm that a diagram is better than prose or
   a table. Complete when the reader question and destination are named and a
   diagram is confirmed as the better form, or the stop reason is stated.
2. Select Mermaid or Graphviz DOT; use D2 only when the user explicitly
   requests it. Select one diagram family and one abstraction level, then load
   their references. Complete when the language, family, and abstraction level
   are chosen and their references are read.
3. Draft canonical source with explicit labels, direction, boundaries, and
   relationships. Include only elements that support the reader question.
   Apply visual style after the structure is accurate. Complete when every
   element and relationship traces to evidence and supports the reader
   question.
4. Add a title and accessible description. Give each meaning a text or shape
   route that does not depend only on color or position. Complete when the
   title and description exist and no meaning relies on color or position
   alone.
5. Validate. Syntax and theme belong to the renderer and any project schema.
   If the user requests validation, run the applicable syntax or render check.
   Otherwise, run a small existing check only when it addresses a material
   risk. Complete when every selected check has a recorded result.
6. Render when the output needs an image. For a standard local render, use
   `<skill-root>/scripts/render.py`, where `<skill-root>` is the directory that
   contains this `SKILL.md`, and read `references/delivery/render-helper.md`.
   Complete when the SVG or PNG exists at its destination, or no render is
   needed.

## Flow

```text
input ← reader question, evidence, destination, target renderer
frame → select → draft → describe → validate → render
diagram beats prose or a table? yes → continue | no → stop and recommend prose or a table
loop: draft → check against evidence → until every element is evidenced
stop: source answers the reader question, selected checks have results, target-specific uncertainty is explicit
```

## References

- Read `references/languages.md` only when the language is not already selected.
- For Mermaid, read the trigger-to-file map in
  `references/mermaid/index.md`, then `references/mermaid/core.md` and only the
  selected family leaf.
- For Graphviz DOT, read the trigger-to-file map in
  `references/graphviz/index.md`, then `references/graphviz/core.md` and only
  the selected engine, pattern, or formal-model leaves.
- For explicitly requested D2 work, read the trigger-to-file map in
  `references/d2/index.md`, then `references/d2/core.md` and only an applicable
  pattern leaf.
- For visual presentation, read `references/design/visual.md`. Use a project
  `DESIGN.md` when present. For fixed bundled styling, read the already selected
  `references/design/*.DESIGN.md`; use `references/design/index.md` only when a
  theme still needs selection or comparison. Load a fixed theme only for an
  output that requires fixed styling. Read `references/design/icons.md` or
  `references/design/edge-labels.md` only when that feature is present.
- For rendering, tool readiness, export, or destination compatibility, read the
  trigger-to-file map in `references/delivery/index.md`, then only the selected
  delivery leaves. Before rendering unreviewed source, configuration, fonts,
  icons, images, imports, or includes, read
  `references/delivery/security.md`.
- Read `references/sources.yml` only for versions, licenses, or provenance.

## Guardrails

- Keep unverified systems, dependencies, ownership, flows, states, and platform
  support out of the diagram.
- Keep canonical source with each delivered image.
- Obtain explicit approval before source goes to a public rendering service.

## Composition

- Use `design-md` when authoring or validating a project `DESIGN.md` is the
  primary deliverable; this skill consumes it as the project design input.

## Output

- Canonical source or targeted edits
- SVG or PNG when rendered output is necessary
- Accessible title and description
- Evidence, assumptions, and target decisions
- Validation or inspection results for checks that ran
