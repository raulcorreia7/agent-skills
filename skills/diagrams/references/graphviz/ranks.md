# Graphviz Ranks

Use ranks to align peers and stabilize reading order under `dot`.

```dot
// engine: dot
digraph release_flow {
  graph [rankdir=TB, label="Release decision flow"];
  node [shape=box, style="rounded,filled"];
  change [label="Change proposed"];
  tests [label="Automated checks"];
  review [label="Peer review"];
  deploy [label="Deploy"];
  { rank=same; tests; review; }
  change -> tests [label="validates"];
  change -> review [label="requests"];
  tests -> deploy [label="passes"];
  review -> deploy [label="approves"];
  tests -> review [style=invis, weight=10]; // stable peer order
}
```

`rank=same`, `rank=min`, `rank=max`, `rank=source`, and `rank=sink` affect
placement. Prefer semantic ranks over long invisible-edge chains. Comment every
invisible constraint and recheck the render because hidden constraints can
distort edge lengths.

Source: [Graphviz attributes](https://graphviz.org/doc/info/attrs.html).
