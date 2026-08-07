# Mermaid Wardley Map

Use `wardley-beta` for a value chain positioned by visibility and evolution.
Coordinates are `[visibility, evolution]`, not conventional `[x, y]`.

```mermaid
wardley-beta
    title Checkout value chain
    component Customer [0.95, 0.85]
    component Checkout [0.80, 0.62]
    component Payment [0.58, 0.76]
    component Compute [0.34, 0.92]
    Customer -> Checkout
    Checkout -> Payment
    Checkout -> Compute
```

Document observations behind placement. Do not confuse a strategic map with a
deployment architecture or present coordinates as objective measurements.
This family requires a current renderer.

Source: [Mermaid Wardley](https://mermaid.js.org/syntax/wardley.html).
