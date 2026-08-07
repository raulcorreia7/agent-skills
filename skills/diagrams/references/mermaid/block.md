# Mermaid Block Diagram

Use `block-beta` when an explicit grid communicates block architecture better
than automatic graph layout. `columns`, `space`, nested `block`, shapes, and
edges control composition. Prefer a flowchart when manual placement adds no
meaning.

```mermaid
block-beta
    columns 9
    client["Web client"] space api["Checkout API"] space queue[("Order queue")] space worker["Order worker"] space store[("Order store")]
    client --> api
    api --> queue
    queue --> worker
    worker --> store
```

Keep connected elements in adjacent cells. Use empty space deliberately and
inspect narrow output. A single-row pipeline keeps edges aligned; use multiple
rows only for real tiers or zones. Avoid spacer cells that force diagonal
edges.

Source: [Mermaid block diagrams](https://mermaid.js.org/syntax/block.html).
