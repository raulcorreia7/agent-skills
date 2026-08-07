# Mermaid Treemap

Use `treemap-beta` for hierarchical proportions. Indentation defines hierarchy
and quoted leaves carry numeric values.

```mermaid
treemap-beta
    "Checkout latency"
        "Application": 46
        "Database": 31
        "Payment provider": 23
    "Background processing"
        "Events": 18
        "Notifications": 12
```

State units and nesting semantics. Preserve values in accessible text. Avoid
rectangle comparisons when exact values matter or the hierarchy is shallow
enough for a bar chart. This family is renderer-gated.

Source: [Mermaid treemap](https://mermaid.js.org/syntax/treemap.html).
