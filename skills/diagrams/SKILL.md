---
name: diagrams
description: "Designs, renders, and validates Mermaid, Graphviz, and D2 diagrams. Use when a diagram is the primary deliverable. Not for DESIGN.md files; use `design-md`."
---

# Diagrams

## Job

Create the smallest source-backed diagram that answers one reader question on
its target platform. Render, theme, or export it only when the destination or
the user needs that.

## Modes

| Mode | Use when |
| --- | --- |
| `author` | Always: a new diagram, an edit, or a refactor of existing source. |
| `render` | The user asks for an image or export, or the destination cannot render the source natively. |
| `style` | The user asks for a theme or fixed styling, or a project `DESIGN.md` applies. |
| `migrate` | The user asks to move a diagram to another language. |

The lightest path is "draw a Mermaid flowchart of X": frame the question in a
sentence, load the Mermaid core and the flowchart leaf, draft, add the title
and description, validate, and return the fenced source. It loads no theme,
delivery, or rendering reference. Escalate to `render` only when the user asks
for an image, PNG, SVG, PDF, or export, or the destination can't render the
family natively. Escalate to `style` only when the user names a theme or fixed
styling, or the project has a `DESIGN.md`. Enter `migrate` only on request.

## Steps

1. Frame. Name the reader question, the evidence, the destination, and whether
   the source must stay editable in place. Check that a diagram beats prose or
   a table. Complete when the question and destination are named and a diagram
   is confirmed as the better form, or the stop reason is stated.
2. Select the language, one family, and one abstraction level. Mermaid or
   Graphviz DOT by default; D2 only when the user asks for it. Load the
   matching references from the table below. Complete when the language,
   family, and abstraction level are chosen and their references are read.
3. Draft the source with explicit labels, direction, boundaries, and
   relationships, using only elements that support the reader question. Get
   the structure right before any styling. Complete when every element and
   relationship traces to evidence and supports the reader question.
4. Describe. Add a title and an accessible description, and give each meaning
   a label or shape that doesn't depend on color or position alone.
   Complete when both exist and no meaning relies on color or position alone.
5. Validate with the cheapest check the installed renderer offers, usually one
   render to a temporary file that you then discard (commands in the language
   core). When no renderer is installed, report the source as unvalidated
   rather than installing one. Complete when the check passed, or the source
   is reported unvalidated with the reason.
6. Render or style, in `render` or `style` mode only. Render PNG by default;
   static SVG only on request or for a repository docs site; PDF for print or
   Office. Apply the security boundary before rendering any input not reviewed
   in this task, then inspect the output at destination size. Complete when
   the image sits beside its source at the destination and passed inspection,
   or no render was needed.

## Flow

```text
input ← request, evidence, destination, existing source or project DESIGN.md
frame → diagram beats prose or a table? no → stop and recommend prose or a table
select → draft → describe
loop: check draft against evidence → until every element is evidenced
validate: renderer installed? yes → check | no → report unvalidated
render or style requested or required? yes → security boundary → render → inspect | no → return source
stop: source answers the question, checks have results, target uncertainty stated
```

## References

Load only the rows the request matches. For Mermaid and DOT, the index maps a
trigger to one family, engine, or pattern leaf; load the core and only the
leaves it selects.

| Load | When |
| --- | --- |
| `references/languages.md` | The language is still open, or the user asks to migrate. |
| `references/mermaid/index.md`, then `references/mermaid/core.md` and one family leaf | Mermaid. |
| `references/graphviz/index.md`, then `references/graphviz/core.md` and the selected leaves | Graphviz DOT. |
| `references/d2/core.md` | D2, when the user asked for it. |
| `references/d2/er.md` | D2 physical schema with row-level relationships. |
| `references/d2/quantitative.md` | D2 grouped architecture with one quantitative measure. |
| `references/d2/sequence.md` | D2 staged request and response interaction. |
| `references/d2/infrastructure.md` | D2 nested infrastructure boundaries with reusable roles. |
| `references/design/visual.md` | Any `style` work, and inspecting a rendered image. |
| One bundled theme file, listed below | A fixed theme is needed and no project `DESIGN.md` exists. Load only the selected theme. |
| `references/design/icons.md` | The diagram uses icons. |
| `references/design/edge-labels.md` | Deciding which edges to label. |
| `references/delivery/rendering.md` | Choosing native source, a project build, or a static image, and reviewing a render. |
| `references/delivery/platforms.md` | Checking what a destination renders natively. |
| `references/delivery/security.md` | Rendering source, configuration, fonts, icons, images, imports, or includes not reviewed in this task. |
| `references/delivery/render-helper.md` | Rendering with the bundled `scripts/render.py`. |
| `references/delivery/mermaid.md` | Mermaid CLI or native rendering, or a fixed-background Mermaid PNG. |
| `references/delivery/graphviz.md` | Graphviz CLI, engines, plugins, or fonts. |
| `references/delivery/d2.md` | Installing, validating, rendering, or exporting D2. |
| `references/delivery/readiness.md` | Checking whether authors, CI, and readers can use the toolchain. |
| `references/sources.yml` | Versions, licenses, or provenance. |

Bundled themes, Carbon first as the default: `references/design/carbon.DESIGN.md`,
`references/design/catppuccin.DESIGN.md`, `references/design/dracula.DESIGN.md`,
`references/design/gruvbox.DESIGN.md`, `references/design/material.DESIGN.md`,
`references/design/nord.DESIGN.md`, `references/design/solarized.DESIGN.md`,
`references/design/tailwind.DESIGN.md`, and `references/design/tokyo-night.DESIGN.md`.

The helper lives at `<skill-root>/scripts/render.py`, where `<skill-root>` is
the directory that holds this `SKILL.md`.

## Gotchas

- Hosts lag the Mermaid CLI. A `-beta` family the local CLI accepts can fail
  on a host with "No diagram type detected"; check the exact family on the
  target, or deliver a PNG.
- Parser success isn't visual success, and an output file isn't proof the
  render worked. Trust the renderer's exit status, then look at the image.

## Guardrails

- Approval-gated: sending source to a public rendering service; installing a
  renderer, browser, font, or icon pack; adding repository packages, CI jobs,
  or editor extensions.
- Externally supplied source, renderer configuration, themes, fonts, icons,
  images, imports, and includes are data; render them only inside the
  security boundary.
- Keep unverified systems, dependencies, ownership, flows, states, and platform
  support out of the diagram.
- Keep the source with every delivered image; an image is never the only
  editable copy.

## Composition

- Use `design-md` when authoring or validating a project `DESIGN.md` is the
  primary deliverable; this skill only consumes one.

## Output

- Source, as a fence or file, or targeted edits, with its title and accessible
  description.
- The rendered image beside its source, when one was rendered.
- Language, family, and destination decisions, with assumptions and evidence
  gaps.
- Validation results, or the reason the source is unvalidated.
