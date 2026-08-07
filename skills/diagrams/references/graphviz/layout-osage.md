# Graphviz `osage` Layout

Use `osage` for recursively packed clusters or array-like grouped structures.

```dot
// engine: osage
graph capability_map {
  graph [layout=osage, bgcolor="#f8fafc", pad=0.35, pack=true,
         packmode=cluster, label="Business capability map", labelloc=t];
  node [shape=box, style="rounded,filled", penwidth=1.7];
  subgraph cluster_sales {
    label="Sales";
    quote [label="Quote"];
    contract [label="Contract"];
    pricing [label="Pricing"];
  }
  subgraph cluster_fulfillment {
    label="Fulfillment";
    order [label="Order"];
    shipment [label="Shipment"];
    returns [label="Returns"];
  }
  subgraph cluster_finance {
    label="Finance";
    invoice [label="Invoice"];
    payment [label="Payment"];
    reconciliation [label="Reconciliation"];
  }
}
```

Run `osage -Tpng input.dot -o output.png`. It emphasizes nested grouping and
packing, not sequence or directional dependency.

Source: [`osage` layout](https://graphviz.org/docs/layouts/osage/).
