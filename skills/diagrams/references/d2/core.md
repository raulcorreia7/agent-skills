# D2 Core

> **Status:** Preferred alternative under evaluation. Require a pinned team
> renderer and reviewed delivery path before team adoption.

D2 is strongest when automatic composition and nested architecture matter more
than native Markdown rendering. Keep `.d2` as the canonical source and publish
a reviewed PNG.

## Core Syntax

Objects have IDs and optional labels. Arrows create connections. Nested maps
create containers. Keep direction at the root for Dagre/ELK portability.

```d2
direction: right

customer: Customer {shape: person}
edge: Public edge {
  gateway: API gateway
}
application: Application environment {
  api: Order API
  queue: Order queue {shape: queue}
  worker: Order worker
  store: Order store {shape: cylinder}
}

customer -> edge.gateway: submits order
edge.gateway -> application.api: forwards HTTPS
application.api -> application.queue: publishes
application.queue -> application.worker: delivers
application.worker -> application.store: writes status
```

| Need | D2 construct | Guardrail |
|---|---|---|
| Reuse | `classes`, variables, substitutions | Prefer a small semantic style vocabulary |
| Composition | imports, layers, scenarios, steps | Keep imports local. Use multiple boards only when the states belong together |
| Rich nodes | `class`, `sql_table`, Markdown, code, LaTeX | Use `sql_table` for physical ER views. Confirm fonts, browser needs, and export behavior |
| Placement | root `direction`, grid, fixed `near` constants | Avoid manual positioning unless it expresses meaning |
| Assets | `icon`, `shape: image`, local path or URL | Keep a label and verify license, availability, and bundling |
| Bulk changes | globs and overrides | Keep selectors narrow and review every matched object |

Apply the trust boundary in `../delivery/security.md` before rendering
imports, assets, configuration, or source that was not reviewed in the current
task.

## Visual Styling

Apply the visual and accessibility rules in `../design/visual.md`.

For Class and ER diagrams, keep ordinary classes or tables in one data color
family. Let native headers, rows, PK/FK constraints, cardinality labels, and
row-level connections carry the structure. Add another color only for a named
semantic exception such as external ownership or active review.

## Layout Engines

| Engine | Use | Limits/dependencies |
|---|---|---|
| Dagre | Fast, simple directed hierarchy | Strictly hierarchical. Curved routes and container shims can look awkward |
| ELK | Nested, orthogonal, container-heavy architecture | Still hierarchical. Configuration and bends can grow quickly |
| TALA | Non-hierarchical architecture and guided composition | Separate proprietary plugin, license/token/outbound checks, no local validation here |

Set `direction` globally. Per-container direction, object-relative `near`, and
position locks are TALA-specific. Container width/height is ELK-specific.
Connections from an ancestor to its descendant do not work in Dagre.

Installation sources: [D2 install](https://d2lang.com/tour/install/),
[detailed install options](https://github.com/terrastruct/d2/blob/master/docs/INSTALL.md),
and [D2 repository README](https://github.com/terrastruct/d2/blob/master/README.md).
Language sources: [language tour](https://d2lang.com/tour/hello-world/),
[layout overview](https://d2lang.com/tour/layouts/),
[Dagre](https://d2lang.com/tour/dagre/),
[ELK](https://d2lang.com/tour/elk/),
[TALA](https://d2lang.com/tour/tala/),
[icons](https://d2lang.com/tour/icons/),
[composition](https://d2lang.com/tour/composition/),
[composition export formats](https://d2lang.com/tour/composition-formats/).
Runtime sources: [CLI](https://d2lang.com/tour/man/),
[exports](https://d2lang.com/tour/exports/), and
[TALA licensing](https://terrastruct.com/tala/).
