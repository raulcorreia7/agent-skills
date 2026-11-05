# Gate Nodes

Declare `authority_required`, `request`, `evidence`, and an output decision
enum of `approved`, `rejected`, or `unavailable`. Give each decision one
outgoing edge. `unavailable` must lead to a blocked or failure terminal.

## Example

Use these exact nested fields for a release gate:

```yaml
nodes:
  - id: "gate.release"
    class: "gate"
    objective: "Authorize release"
    inputs:
      - ref: "validate.result"
        type: "verification-result"
        required: true
    outputs:
      - id: "gate.release.decision"
        type: "enum"
        allowed: ["approved", "rejected", "unavailable"]
        persistence: "workflow"
    preconditions: ["Validation evidence is available"]
    completion:
      all: ["An authorized decision is recorded"]
    gate:
      authority_required: "release approver"
      request: "Approve the validated release"
      evidence: ["validate.result"]

edges:
  - from: "gate.release"
    to: "terminal.succeeded"
    condition: "gate.release.decision == 'approved'"
    passes: ["gate.release.decision"]
  - from: "gate.release"
    to: "terminal.failed"
    condition: "gate.release.decision == 'rejected'"
    passes: ["gate.release.decision"]
  - from: "gate.release"
    to: "terminal.blocked"
    condition: "gate.release.decision == 'unavailable'"
    passes: ["gate.release.decision"]
```

Every decision has exactly one outgoing edge. Every node, output, and terminal
ID must resolve in the emitted graph.
