# Mermaid Swimlanes

Use `swimlane-beta` when ownership and handoffs matter. Top-level `subgraph`
blocks become lanes; flowchart nodes and edges define work. Directions include
`TB`, `BT`, `LR`, and `RL`.

```mermaid
swimlane-beta LR
    accTitle: Purchase approval
    accDescr: A requester submits a purchase, a manager approves it, and procurement creates the order.
    subgraph requester[Requester]
        draft[Prepare request]
        submit[Submit request]
        draft --> submit
    end
    subgraph manager[Manager]
        review{Approve?}
    end
    subgraph procurement[Procurement]
        create[Create purchase order]
    end
    submit -->|approval request| review
    review -->|approved| create
```

Keep one lane meaning and one flow direction. Put decisions in the owning lane,
label cross-lane handoffs, shorten labels before increasing lane width, and
keep the busiest lane near the primary path. Do not mix teams, phases, and
statuses as lane meanings. Split before arrows become difficult to trace.

Source: [Mermaid swimlanes](https://mermaid.js.org/syntax/swimlanes.html).
