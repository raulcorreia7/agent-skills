# Join Nodes

Declare `wait_for`, a policy of `all_succeeded`, `all_terminal`, or a stated
threshold, and a reconciliation rule. Give unmet and failed policies
deterministic destinations.

## Example

Use these exact nested fields for a two-branch quality join:

```yaml
nodes:
  - id: "join.quality"
    class: "join"
    objective: "Reconcile parallel quality results"
    inputs:
      - ref: "test.result"
        type: "verification-result"
        required: true
      - ref: "review.result"
        type: "verification-result"
        required: true
    outputs:
      - id: "join.quality.result"
        type: "verification-result"
        persistence: "workflow"
    preconditions: ["Both quality tasks have reached a terminal state"]
    completion:
      all: ["The join policy is evaluated and recorded"]
    join:
      wait_for: ["test", "review"]
      policy: "all_succeeded"
      reconcile: "retain both verification results"
      satisfied_to: "terminal.succeeded"
      unsatisfied_to: "terminal.failed"
```

Give the satisfied and unsatisfied policy outcomes deterministic destinations.
Every node, output, and terminal ID must resolve in the emitted graph.
