# Language Selection

Choose from the destination backward. Prefer the supported language that
preserves the required semantics with the least notation. Mermaid and Graphviz
DOT are the default authoring languages.

| Language | Prefer when | Delivery |
|---|---|---|
| Mermaid | Markdown-native flows, interactions, models, plans, and small charts | Use native rendering when the exact family works. Otherwise retain source and publish PNG |
| Graphviz DOT | Graph topology, automata, dependencies, clusters, ports, or layout-engine control | Retain source and publish PNG unless the destination has a verified renderer |

## Decision Rules

- Use Mermaid when native, in-place editing matters.
- Use DOT when topology or layout constraints are central.
- For state models, use Mermaid for compact software lifecycles and DOT for
  formal notation, accepting states, ports, or layout control.
- Select the notation that makes relationships least ambiguous, not the
  language that merely offers the required shapes.

Evaluate D2 only when the user explicitly requests it and automatic composition
or nested architecture offers a concrete advantage. Require a pinned team
renderer and verified delivery before adoption.

## Migration

First simplify or split the current diagram. If migration still helps, present
the proposed language, fidelity gained, tooling and delivery impact, editability,
and any construct that cannot map exactly. Proceed after user alignment.

Official references: [Mermaid](https://mermaid.js.org/intro/syntax-reference.html)
and [Graphviz DOT](https://graphviz.org/doc/info/lang.html).
