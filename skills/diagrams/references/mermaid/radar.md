# Mermaid Radar Chart

Use `radar-beta` for a few entities across a small common set of dimensions.
Define axis IDs and labels, curve values, and explicit scale and legend
controls when comparisons require stability.

```mermaid
radar-beta
    title Checkout quality profile
    axis latency["Latency"], resilience["Resilience"], operability["Operability"], cost["Cost efficiency"]
    curve current["Current"]{72, 58, 64, 81}
    curve target["Target"]{85, 85, 80, 78}
    min 0
    max 100
    ticks 5
    showLegend true
```

Use identical scales and direction for every axis. Avoid area-based conclusions
and many overlapping curves. Preserve the underlying values in accessible
text. This family is renderer-sensitive.

Source: [Mermaid radar chart](https://mermaid.js.org/syntax/radar.html).
