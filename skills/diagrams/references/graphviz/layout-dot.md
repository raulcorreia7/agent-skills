# Graphviz `dot` Layout

Use `dot` for layered directed processes, dependencies, and hierarchies.

```dot
// engine: dot
digraph checkout_pipeline {
  graph [rankdir=TB, bgcolor="#f8fafc", pad=0.35, nodesep=0.65, ranksep=0.75,
         label="Checkout pipeline", labelloc=t, fontsize=20,
         fontcolor="#0f172a"];
  node [shape=box, style="rounded,filled", penwidth=1.8,
        fontsize=12, margin="0.18,0.12"];
  edge [color="#64748b", fontcolor="#334155", fontsize=10,
        penwidth=1.6, arrowsize=0.8];
  cart [label="Cart", fillcolor="#f8fafc", color="#64748b", fontcolor="#0f172a"];
  validate [label="Validate order", fillcolor="#dbeafe", color="#2563eb", fontcolor="#172554"];
  authorize [label="Authorize payment", fillcolor="#dbeafe", color="#2563eb", fontcolor="#172554"];
  confirm [label="Confirm order", fillcolor="#dcfce7", color="#16a34a", fontcolor="#14532d"];
  cart -> validate [label="checkout"];
  validate -> authorize [label="valid"];
  authorize -> confirm [label="approved"];
}
```

Run `dot -Tpng input.dot -o output.png`. Use `rankdir`, `rank`, `nodesep`,
`ranksep`, `minlen`, `weight`, and `constraint` carefully. Back edges and wide
layers are common failure modes.

Source: [`dot` layout](https://graphviz.org/docs/layouts/dot/).
