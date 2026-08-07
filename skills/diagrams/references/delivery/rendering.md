# Rendering And Delivery

Canonical source is the reviewable artifact. A rendered image is a delivery
artifact, never the only editable copy.

## Delivery Order

1. Native source rendered by the destination.
2. Source rendered by a verified project plugin or build.
3. Locally rendered PNG with canonical source retained.
4. Text description, plus a data table for quantitative charts.

Use PNG when native rendering changes meaning, labels, hierarchy,
accessibility, or readability. Follow the repository convention or use matching
basenames such as `checkout.mmd` and `checkout.png`. Do not keep temporary
validation output.

## Validate And Review

1. Record the renderer and version.
2. Validate changed source and edited runnable examples.
3. If appearance changed, render one representative PNG.
4. Inspect it at destination size using `../design/visual.md`.
5. Retain and link canonical source and add accessible text.

Do not run format, engine, theme, platform, or size matrices unless the target
requires them. Parser success is not visual validation. File existence is not
success when the renderer failed.

Use the selected renderer guide for native commands or `render-helper.md` for
the bundled helper. The helper atomically replaces an existing output only
after a successful non-empty render. A failed batch retains outputs completed
before the failure; retry only after inspecting those results.

Sources: [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) and
[Graphviz command line](https://graphviz.org/doc/info/command.html).
