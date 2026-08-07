# Mermaid Cynefin Diagram

Use `cynefin-beta` for facilitated sense-making across Clear, Complicated,
Complex, Chaotic, and Confusion domains.

```mermaid
cynefin-beta
    title Operational decisions
    complex
        "Emergent customer behaviour"
    complicated
        "Capacity model tuning"
    clear
        "Routine certificate renewal"
    chaotic
        "Active payment outage"
    confusion
        "Unclassified latency spike"
    confusion --> complicated : "Evidence gathered"
```

Use the framework to frame inquiry, not to label people or permanently classify
work. This family requires a current renderer. Preserve the classification and
transition meaning in nearby text.

Source: [Mermaid Cynefin](https://mermaid.js.org/syntax/cynefin.html).
