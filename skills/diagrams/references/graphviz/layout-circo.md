# Graphviz `circo` Layout

Use `circo` when a cycle or ring is the subject.

```dot
// engine: circo
digraph approval_cycle {
  graph [layout=circo, bgcolor="#f8fafc", pad=0.35, overlap=false,
         splines=curved, mindist=1.8, label="Document lifecycle", labelloc=t];
  node [shape=box, style="rounded,filled", penwidth=1.8];
  edge [color="#64748b", arrowsize=0.8];
  draft [label="Draft"];
  review [label="Review"];
  approve [label="Approve"];
  publish [label="Publish"];
  archive [label="Archive"];
  draft -> review;
  review -> approve;
  approve -> publish;
  publish -> archive;
  archive -> draft [label="restore", style=dashed];
}
```

Run `circo -Tpng input.dot -o output.png`. Cross-ring chords and edge labels
can tangle. If the cycle is incidental to one dominant process, use `dot`.

Source: [`circo` layout](https://graphviz.org/docs/layouts/circo/).
