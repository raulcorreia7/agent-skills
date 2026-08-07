# Graphviz Semantic Shapes

Use a small familiar shape vocabulary as supplementary meaning.

```dot
// engine: dot
digraph semantic_shapes {
  graph [rankdir=TB, label="Alert triage"];
  node [style="filled"];
  actor [label="Support engineer", shape=oval];
  process [label="Investigate alert", shape=box, style="rounded,filled"];
  decision [label="Customer\nimpact?", shape=diamond];
  data [label="Incident record", shape=cylinder];
  close [label="Close alert", shape=box, style="rounded,filled"];
  actor -> process [label="opens"];
  process -> decision [label="assesses"];
  decision -> data [label="YES"];
  decision -> close [label="NO"];
}
```

Labels carry primary meaning; shapes reinforce category. Avoid exotic shapes
merely because Graphviz provides them. Check long text for crowding or clipping.

Source: [Graphviz node shapes](https://graphviz.org/doc/info/shapes.html).
