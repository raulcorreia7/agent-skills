# Recovery Controls

## Example

Declare the recovery action as a complete task node:

```yaml
nodes:
  - id: "rollback.integration"
    class: "task"
    operation: "rollback"
    objective: "Restore the release artifact after failed integration"
    owner: "release-engineer"
    inputs:
      - ref: "integration.result"
        type: "integration-result"
        required: true
    outputs:
      - id: "rollback.integration.result"
        type: "recovery-result"
        persistence: "terminal"
    reads: ["release.bundle"]
    writes: ["release.bundle"]
    side_effects: ["restore release artifact"]
    authority: "repository write access"
    preconditions: ["Integration failed after partially updating release.bundle"]
    completion:
      all: ["release.bundle matches its pre-integration snapshot"]
    failure:
      classify: ["permanent"]
      transitions:
        permanent: "terminal.failed"
    idempotency:
      key: "workflow.id + node.id + checkpoint-digest"
      replay: "reuse a matching successful recovery result"
```

Bind the failed task to the recovery policy and its action node:

```yaml
recovery_policies:
  - id: "recover.integration"
    trigger: "integration.status == 'failed'"
    action_node: "rollback.integration"
    succeeds_to: "terminal.failed"
    fails_to: "terminal.failed"

node_controls:
  integration:
    recovery_policy: "recover.integration"
```

The policy trigger, `node_controls` key, and failed task ID must agree. The
action is a declared task node. Both recovery outcomes have explicit
destinations. Every node, artifact, output, policy, and terminal ID must resolve
in the emitted graph.
