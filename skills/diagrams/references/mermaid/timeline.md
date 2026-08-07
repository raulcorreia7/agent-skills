# Mermaid Timeline

Use `timeline` for chronological events when duration and dependencies are not
the question. Sections group periods or themes and events can carry several
lines of detail.

```mermaid
timeline
    title Ordering platform evolution
    section Foundation
      2024 : Initial order API
           : Manual fulfilment
      2025 : Event-driven fulfilment
    section Resilience
      2026 Q1 : Regional failover tested
      2026 Q3 : Planned: active-active checkout
```

Keep granularity consistent within a section and distinguish planned from
historical events in labels or separate views. Control density through scope,
label length, sections, and viewport rather than spacer content or CSS nudges.

Source: [Mermaid timeline](https://mermaid.js.org/syntax/timeline.html).
