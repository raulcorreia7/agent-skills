# Graphviz `twopi` Layout

Use `twopi` for a radial hierarchy around one meaningful center.

```dot
// engine: twopi
graph incident_scope {
  graph [layout=twopi, root=incident, ranksep=1.5, overlap=false,
         bgcolor="#f8fafc", pad=0.35, label="Checkout incident scope",
         labelloc=t, fontsize=20, fontcolor="#0f172a"];
  node [shape=box, style="rounded,filled", penwidth=1.8];
  edge [color="#94a3b8", penwidth=1.5];
  incident [label="Checkout incident"];
  customer [label="Customer impact"];
  services [label="Affected services"];
  response [label="Response"];
  checkout [label="Checkout blocked"];
  abandonment [label="Cart abandonment"];
  tickets [label="Support tickets"];
  web [label="Web"];
  orders [label="Orders"];
  payments [label="Payments"];
  support [label="Support"];
  sre [label="SRE"];
  incident_commander [label="Incident commander"];
  incident -- {customer services response};
  customer -- {checkout abandonment tickets};
  services -- {web orders payments};
  response -- {support sre incident_commander};
}
```

Run `twopi -Tpng input.dot -o output.png`. Set a meaningful `root`. Radial
distance indicates levels, not elapsed time or quantitative magnitude. Long
labels commonly collide around rings.

Source: [`twopi` layout](https://graphviz.org/docs/layouts/twopi/).
