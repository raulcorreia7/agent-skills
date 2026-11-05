# Retry Controls

## Example

Route each retryable failure class to the policy ID in the task's existing
failure contract:

```yaml
failure:
  classify: ["transient", "permanent"]
  transitions:
    transient: "retry.validate"
    permanent: "terminal.failed"
```

Define and bind that policy:

```yaml
retry_policies:
  - id: "retry.validate"
    node: "validate"
    retry_on: ["transient"]
    max_attempts: 3
    reentry_node: "validate"
    exhausted_to: "terminal.failed"
    safety: "The task is read-only"

node_controls:
  validate:
    retry_policy: "retry.validate"
```

The policy's `node` must equal the `node_controls` key and identify the task
whose failure transition names the policy. `retry_on` must contain only failure
classes declared by that task and routed to this policy. A retry cycle is valid
only when its `max_attempts`, `reentry_node`, `exhausted_to`, and `safety` are
present. Every node, policy, and terminal ID must resolve in the emitted graph.
