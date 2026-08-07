---
name: diagrams
description: Designs, refactors, renders, and validates Mermaid, Graphviz DOT, and D2 diagrams. Use when a diagram is the primary artifact.
---

# Diagrams

## Job

Create the smallest source-backed diagram that answers one reader question on
its target platform.

Resolve `<skill-root>` as the directory that contains this `SKILL.md`.

## Steps

1. Define the reader question, evidence, scope, destination, target renderer,
   and editability requirement.
2. Confirm that a diagram is better than prose or a table. Select Mermaid or
   Graphviz DOT. Use D2 only when the user explicitly requests it.
3. Select one diagram family and one abstraction level. Include only elements
   that support the reader question.
4. Draft canonical source with explicit labels, direction, boundaries, and
   relationships. Apply visual style after the structure is accurate.
5. Add a title and accessible description. Give each meaning a text or shape
   route that does not depend only on color or position.
6. Syntax and theme belong to the renderer and any project schema. If the user
   requests validation, run the applicable syntax or render check and record
   its result. For a standard local render, use the bundled
   `<skill-root>/scripts/render.py` and read
   `references/delivery/render-helper.md`. Otherwise, run a small existing
   check only when it addresses a material risk. This skill owns when to
   diagram and which family to use.
7. Stop when the source answers the reader question, the selected checks have
   results, and target-specific uncertainty is explicit.

## References

- Read `references/languages.md` only when the language is not already selected.
- For Mermaid, read the trigger-to-file map in
  `references/mermaid/index.md`, then `references/mermaid/core.md` and only the
  selected family leaf.
- For Graphviz DOT, read the trigger-to-file map in
  `references/graphviz/index.md`, then `references/graphviz/core.md` and only
  the selected engine, pattern, or formal-model leaf.
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
  delivery leaf. Before rendering unreviewed source, configuration, fonts,
  icons, images, imports, or includes, read
  `references/delivery/security.md`.
- Read `references/sources.yml` only for versions, licenses, or provenance.

## Guardrails

- Keep unverified systems, dependencies, ownership, flows, states, and platform
  support out of the diagram.
- Keep canonical source with each delivered image.
- Obtain approval before source goes to a public rendering service.

## Output

- Canonical source or targeted edits
- SVG or PNG when rendered output is necessary
- Accessible title and description
- Evidence, assumptions, and target decisions
- Validation or inspection results for checks that ran
