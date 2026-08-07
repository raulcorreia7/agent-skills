# Graphviz Fault Trees

```dot
// engine: dot
digraph checkout_fault_tree {
  graph [rankdir=TB, label="Fault tree: checkout unavailable"];
  node [shape=box, style="rounded,filled"];
  edge [dir=none];
  top [label="Checkout unavailable"];
  or_gate [label="OR", shape=circle, fixedsize=true, width=0.5];
  api [label="Order API unavailable"];
  payment [label="Payment authorization unavailable"];
  and_gate [label="AND", shape=circle, fixedsize=true, width=0.65];
  primary [label="Primary provider failed"];
  fallback [label="Fallback provider failed"];
  top -> or_gate;
  or_gate -> api;
  or_gate -> payment;
  payment -> and_gate;
  and_gate -> primary;
  and_gate -> fallback;
}
```

Preserve the domain's direction and gate semantics. Text in generic gate
circles is readable documentation, not formal interchange notation. Use a
specialized tool when standard glyphs, probability calculation, or
certification is required. Do not use color alone to distinguish faults.

Sources: [DOT language](https://graphviz.org/doc/info/lang.html) and
[node shapes](https://graphviz.org/doc/info/shapes.html).
