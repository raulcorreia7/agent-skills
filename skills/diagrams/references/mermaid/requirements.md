# Mermaid Requirement Diagram

Use `requirementDiagram` for traceability between requirements and design or
test elements. Requirements support `id`, `text`, `risk`, and `verifymethod`.
Relations include `contains`, `copies`, `derives`, `satisfies`, `verifies`,
`refines`, and `traces`.

```mermaid
requirementDiagram
    performanceRequirement checkout_latency {
        id: PERF_01
        text: Checkout responds within two seconds at p95
        risk: medium
        verifymethod: test
    }
    element load_test {
        type: automated test
        docref: tests/performance/checkout.md
    }
    load_test - verifies -> checkout_latency
```

Use stable requirement IDs and real verification artifacts. Do not invent
traceability to make the picture complete. Reduce scope and label length before
increasing the canvas.

Source: [Mermaid requirement diagram](https://mermaid.js.org/syntax/requirementDiagram.html).
