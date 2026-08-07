# Mermaid Quadrant Chart

Use `quadrantChart` for two-axis prioritization. Declare meaningful endpoints,
name all quadrants, and place points with normalized `[x, y]` coordinates.

```mermaid
quadrantChart
    title Reliability work
    x-axis Lower effort --> Higher effort
    y-axis Lower impact --> Higher impact
    quadrant-1 Plan carefully
    quadrant-2 Do next
    quadrant-3 Defer
    quadrant-4 Opportunistic
    Add retry budget:::next: [0.28, 0.78]
    Multi-region writes:::plan: [0.82, 0.91]
    Rename dashboard:::defer: [0.18, 0.20]
    classDef next color:#15803D,stroke-color:#15803D,stroke-width:2px
    classDef plan color:#D97706,stroke-color:#D97706,stroke-width:2px
    classDef defer color:#64748B,stroke-color:#64748B,stroke-width:2px
```

Explain how positions were determined; do not present subjective placement as
measurement. Keep labels because color is supplementary. For a fixed PNG, use
the controlled profile in `core.md`; native host output remains valid without
it.

Source: [Mermaid quadrant chart](https://mermaid.js.org/syntax/quadrantChart.html).
