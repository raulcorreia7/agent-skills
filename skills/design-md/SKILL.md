---
name: design-md
description: Authors, updates, lints, compares, exports, and explains Google DESIGN.md files under the pinned specification. Use when a DESIGN.md or a design-token file in that format is the primary deliverable.
---

# DESIGN.md

## Job

Manage a Google DESIGN.md under the pinned specification for the selected mode.

## Modes

| Mode | Use when | Load |
| --- | --- | --- |
| `author` or `update` | Creating or revising a DESIGN.md | [the pinned specification](references/spec.md) |
| `lint`, `diff`, or `export` | Running a `designmd` command | [CLI execution](references/cli.md) |
| `explain` | Answering a specification question | [the pinned specification](references/spec.md) |

## Steps

1. Select the mode and resolve its input, output, and requested result.
   Complete when the mode, input file, and expected output are named.
2. Follow the mode's section below. Complete when that section's completion
   condition holds.

## Author or update

Inspect the current DESIGN.md, design tokens, theme and component styles, brand
documents, and supplied assets. Resolve conflicting evidence before you write.

Write tokens as normative values and explain their purpose in the Markdown
body. Use the specified section order. List an intentional missing token group
in `omitted`. For an update, preserve valid unknown sections, token names, and
extensions outside the requested change.

Complete when the file follows the pinned format and each design decision has
project evidence or user direction.

## Lint, diff, or export

Run the applicable command. Complete `lint` by reporting its findings, `diff`
by identifying any regression, and `export` when the requested format exists
at its destination.

## Explain specification

Use the CLI only for its command or JSON form. Complete when the answer or
validation result cites the applicable pinned format rule.

## References

- Read [the pinned specification](references/spec.md) also for explicit manual
  validation.
- Read [CLI execution](references/cli.md) before any mode runs `designmd`.
- Read [sources.yml](references/sources.yml) only to maintain the bundled
  upstream material.
- Read [LICENSE.txt](references/LICENSE.txt) only to redistribute the bundled
  material or review its license terms.

## Guardrails

- Record only values, rules, and rationale supported by project evidence or
  user direction.
- Run lint only on user request or when it controls a material format or export
  risk.

## Output

- `author` or `update`: the created or revised DESIGN.md and unresolved design
  choices.
- `lint` or `diff`: the command result and findings.
- `export`: the exported file and its format.
- `explain`: the answer or explicit validation result from the pinned
  specification.
