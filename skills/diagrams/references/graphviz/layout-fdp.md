# Graphviz `fdp` Layout

Use `fdp` for medium undirected clustered networks.

```dot
// engine: fdp
graph team_dependencies {
  graph [layout=fdp, overlap=false, splines=curved, bgcolor="#f8fafc",
         pad=0.35, K=1.0, start=42, label="Cross-team delivery dependencies",
         labelloc=t, fontsize=20, fontcolor="#0f172a"];
  node [shape=box, style="rounded,filled", penwidth=1.8, fontsize=12];
  edge [color="#94a3b8", penwidth=1.5];
  web [fillcolor="#e0e7ff", color="#4f46e5"];
  orders [fillcolor="#e0e7ff", color="#4f46e5"];
  catalog [fillcolor="#e0e7ff", color="#4f46e5"];
  data [fillcolor="#f3e8ff", color="#9333ea"];
  events [fillcolor="#f3e8ff", color="#9333ea"];
  identity [fillcolor="#f3e8ff", color="#9333ea"];
  security [fillcolor="#dcfce7", color="#16a34a"];
  sre [fillcolor="#dcfce7", color="#16a34a"];
  compliance [fillcolor="#dcfce7", color="#16a34a"];
  web -- orders -- catalog;
  data -- events -- identity;
  security -- sre -- compliance;
  orders -- events;
  catalog -- data;
  identity -- security;
  orders -- sre;
}
```

Run `fdp -Tpng input.dot -o output.png`. Tune `K` only when default spacing
fails. Filter, cluster, or split a dense network before styling.

Source: [`fdp` layout](https://graphviz.org/docs/layouts/fdp/).
