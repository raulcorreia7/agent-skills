# Graphviz `sfdp` Layout

Use `sfdp` for large overview-scale undirected graphs.

```dot
// engine: sfdp
graph dependency_overview {
  graph [layout=sfdp, overlap=false, splines=true, bgcolor="#f8fafc",
         pad=0.35, start=42, label="Service dependency overview",
         labelloc=t, fontsize=20, fontcolor="#0f172a"];
  node [shape=circle, width=0.22, fixedsize=true, label="", style=filled,
        fillcolor="#cbd5e1", color="#94a3b8"];
  edge [color="#cbd5e1", penwidth=1.2];
  gateway [label="Gateway", shape=box, width=1.2, fixedsize=false];
  commerce [label="Commerce", shape=box, width=1.2, fixedsize=false];
  platform [label="Platform", shape=box, width=1.2, fixedsize=false];
  operations [label="Operations", shape=box, width=1.2, fixedsize=false];
  gateway -- {g1 g2 g3 g4};
  commerce -- {c1 c2 c3 c4 c5};
  platform -- {p1 p2 p3 p4 p5};
  operations -- {o1 o2 o3 o4};
  gateway -- {commerce platform};
  commerce -- platform;
  platform -- operations;
  commerce -- operations;
  c2 -- p3;
  p4 -- o2;
}
```

Run `sfdp -Tpng input.dot -o output.png`. Reduce label vocabulary and expose
detail through linked views. Do not claim that visual proximity alone proves
architectural coupling.

Source: [`sfdp` layout](https://graphviz.org/docs/layouts/sfdp/).
