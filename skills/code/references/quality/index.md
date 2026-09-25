# Quality Router

Read each leaf whose trigger applies. Repository contracts and measured
system behavior take precedence over general guidance.

| Trigger | Leaf |
|---|---|
| Change module boundaries, ownership, abstraction, duplication, inheritance, pattern use, a reusable interface, or a source of truth | [Architecture and maintainability](architecture-and-maintainability.md) |
| Consider a functional technique because the user requests it, the repository establishes it, or a concrete proposal depends on it | [Functional design](functional-design.md) |
| Optimize latency, throughput, memory, capacity, or cost | [Performance](performance.md) |
| Add, replace, remove, or evaluate a dependency | [Dependencies and supply chain](dependencies-and-supply-chain.md) |
| Add or change logs, metrics, traces, dashboards, or alerts | [Observability](observability.md) |
| Change a code-owned user interface or interaction | [Accessibility](accessibility.md) |
| Select or interpret a smell, churn or co-change signal, code-quality measure, or threshold | [Metrics and proxy limits](metrics-and-proxy-limits.md) |
| Apply formal methods to a bounded high-impact component | [High-assurance verification](high-assurance-verification.md) |

For a routine implementation with no matching trigger, continue without a
quality leaf.
