# Graphviz Clusters

Use clusters for meaningful boundaries such as trust zones or deployment units,
not decoration.

```dot
// engine: dot
digraph trust_boundary {
  graph [rankdir=TB, compound=true, label="Checkout trust boundaries"];
  node [shape=box, style="rounded,filled"];
  user [label="Customer", shape=oval];
  audit [label="Audit store", shape=cylinder];
  subgraph cluster_public {
    label="Public zone";
    waf [label="Web application firewall"];
    gateway [label="API gateway"];
    waf -> gateway [label="filtered request"];
  }
  subgraph cluster_private {
    label="Private zone";
    service [label="Order service"];
    database [label="Order database", shape=cylinder];
    service -> database [label="writes order"];
  }
  user -> waf [label="HTTPS"];
  gateway -> service [label="validated request",
                      ltail=cluster_public, lhead=cluster_private];
  service -> audit [label="records decision"];
}
```

Set `compound=true` before `lhead` or `ltail`. Point edges at real nodes; those
attributes only adjust boundary clipping. Label every cluster, keep its border
visible, and nest only when hierarchy matters. Dense cross-cluster edges signal
that the view should split.

Sources: [DOT language](https://graphviz.org/doc/info/lang.html) and
[attributes](https://graphviz.org/doc/info/attrs.html).
