# Graphviz Labeled Transition Systems

Use DOT for a labeled transition system when graph-level control matters more
than UML composite states or entry and exit actions.

```dot
// engine: dot
digraph order_lts {
  graph [rankdir=LR, label="Order lifecycle"];
  node [shape=circle, style=filled];
  start [shape=point, width=0.12, label=""];
  open [label="Open"];
  paid [label="Paid"];
  shipped [label="Shipped"];
  cancelled [label="Cancelled", shape=doublecircle];
  complete [label="Complete", shape=doublecircle];
  start -> open;
  open -> paid [label="authorize"];
  paid -> shipped [label="dispatch"];
  shipped -> complete [label="deliver"];
  open -> cancelled [label="cancel", style=dashed];
  paid -> cancelled [label="refund", style=dashed];
}
```

State whether double circles mean accepting, terminal, or another domain
property; an LTS does not define that convention. Label every transition and
keep domain notation primary. Use Mermaid state diagrams when UML semantics are
more important than graph layout control.

Sources: [DOT language](https://graphviz.org/doc/info/lang.html) and
[node shapes](https://graphviz.org/doc/info/shapes.html).
