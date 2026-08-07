# Graphviz Interactive Content

Graphviz supports `URL` or `href`, `tooltip`, `target`, `image`, and related
attributes, but behavior depends on the output format.

```dot
// engine: dot
digraph linked_diagram {
  graph [rankdir=LR];
  node [shape=box, style="rounded,filled"];
  runbook [label="Order recovery runbook",
           URL="https://example.invalid/runbooks/orders",
           tooltip="Open the order recovery runbook", target="_top"];
  service [label="Order service"];
  service -> runbook [label="is recovered with"];
}
```

PNG does not preserve links or tooltips, so keep useful links in surrounding
text. Before processing links, images, fonts, or externally supplied DOT, apply
`../delivery/security.md`. Review local assets and remote URLs explicitly.

Sources: [Graphviz attributes](https://graphviz.org/doc/info/attrs.html) and
[output formats](https://graphviz.org/docs/outputs/).
