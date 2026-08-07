# Graphviz `neato` Layout

Use `neato` for small undirected networks and geometric relationships.

```dot
// engine: neato
graph service_affinity {
  graph [layout=neato, mode=KK, overlap=false, splines=curved,
         bgcolor="#f8fafc", pad=0.35, start=42,
         label="Orders service affinity", labelloc=t, fontsize=20,
         fontcolor="#0f172a"];
  node [shape=ellipse, style=filled, penwidth=1.8, fontsize=12];
  edge [color="#94a3b8", penwidth=1.5, len=1.4];
  orders [label="Orders", fillcolor="#4f46e5", color="#3730a3", fontcolor="#ffffff"];
  catalog [label="Catalog", fillcolor="#f8fafc", color="#64748b"];
  payments [label="Payments", fillcolor="#f8fafc", color="#64748b"];
  identity [label="Identity", fillcolor="#f8fafc", color="#64748b"];
  notifications [label="Notifications", fillcolor="#f8fafc", color="#64748b"];
  orders -- catalog;
  orders -- payments;
  orders -- identity;
  orders -- notifications;
}
```

Run `neato -Tpng input.dot -o output.png`. A numeric `start` is repeatable only
within a pinned build. Use `pos` with `-n` or `-n2` only when coordinates are
deliberately owned. Treat distance as a metric only when the model defines it.

Source: [`neato` layout](https://graphviz.org/docs/layouts/neato/).
