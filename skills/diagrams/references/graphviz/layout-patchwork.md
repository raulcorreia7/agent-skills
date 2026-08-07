# Graphviz `patchwork` Layout

Use `patchwork` for a small hierarchical area or part-to-whole view.

```dot
// engine: patchwork
graph cost_allocation {
  graph [layout=patchwork, bgcolor="#ffffff", pad=0.2,
         label="Monthly cloud cost allocation", labelloc=t];
  node [shape=box, style=filled, color="#ffffff", penwidth=3,
        fontcolor="#ffffff", fontsize=16];
  compute [label="Compute\n42%", area=42, fillcolor="#2563eb"];
  database [label="Database\n28%", area=28, fillcolor="#0f766e"];
  observability [label="Observability\n18%", area=18, fillcolor="#7c3aed"];
  network [label="Network\n12%", area=12, fillcolor="#c2410c"];
}
```

Run `patchwork -Tpng input.dot -o output.png`. `area` controls rectangle size.
Print exact values and keep the dataset small. Area and labels, not hue, encode
magnitude. Use a charting workflow for substantial quantitative analysis.

Source: [`patchwork` layout](https://graphviz.org/docs/layouts/patchwork/).
