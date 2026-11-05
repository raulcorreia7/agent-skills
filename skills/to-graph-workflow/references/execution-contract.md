# Execution Graph Contract

Emit one YAML document as the executable source of truth after the source plan
passes the readiness check.

## Contents

- Core state model and output persistence
- Minimal executable profile
- Task and terminal node contracts
- Consistency checks

## Core State Model

Each declared node has an intrinsic runtime state at `<node-id>.status`. The
scheduler creates that state from `nodes`; do not repeat it in `registry`.

```yaml
state_model:
  node_status:
    initial: "pending"
    allowed: ["pending", "ready", "running", "succeeded", "failed", "blocked", "skipped"]
    transitions:
      pending: ["ready", "blocked", "skipped"]
      ready: ["running", "blocked", "skipped"]
      running: ["succeeded", "failed", "blocked"]
      failed: ["ready"]
      blocked: ["ready", "skipped"]
      succeeded: []
      skipped: []
```

A task becomes `ready` when its preconditions and incoming edge conditions are
true. It becomes `succeeded` only when all completion criteria pass and its
declared outputs exist. A failure transition, gate decision, join rule, retry
policy, or recovery policy determines the next state for every other outcome.
A terminal node derives the workflow result: `success`, `failure`, or
`blocked`.

Output persistence uses these values:

- `ephemeral`: available only during the current node attempt; do not reference
  it from a later node or replay rule.
- `workflow`: retained for downstream nodes and matching replay until the
  workflow reaches a terminal.
- `checkpoint`: retained across resume from its declared checkpoint.
- `terminal`: retained as workflow evidence after completion.

Declare `workflow.goal` as an object with a stable `id`, an observable
`statement`, and the acceptance-criterion IDs that prove it.

## Minimal Profile

Replace the illustrative values. Do not leave placeholders in the final graph.

```yaml
schema_version: "1.0"
workflow:
  id: "implement-feature"
  title: "Implement feature"
  goal:
    id: "goal.feature-implemented"
    statement: "The requested behavior passes focused validation"
    acceptance_criteria: ["AC-1"]
  source_plan: "docs/implementation-plan.md"
  assumptions: []
  constraints: []
  acceptance_criteria:
    - id: "AC-1"
      statement: "The requested behavior passes focused validation"
      verified_by: ["validate.result"]

registry:
  artifacts:
    - id: "source.module"
      type: "file"
      location: "src/module.py"
      owner: "implementer"
      lifecycle: "update"

state_model:
  node_status:
    initial: "pending"
    allowed: ["pending", "ready", "running", "succeeded", "failed", "blocked", "skipped"]
    transitions:
      pending: ["ready", "blocked", "skipped"]
      ready: ["running", "blocked", "skipped"]
      running: ["succeeded", "failed", "blocked"]
      failed: ["ready"]
      blocked: ["ready", "skipped"]
      succeeded: []
      skipped: []

nodes:
  - id: "inspect"
    class: "task"
    operation: "inspect"
    objective: "Resolve the exact implementation surface"
    owner: "implementer"
    inputs:
      - ref: "workflow.source_plan"
        type: "plan"
        required: true
    outputs:
      - id: "inspect.result"
        type: "evidence-set"
        persistence: "workflow"
    reads: ["source.module"]
    writes: []
    side_effects: []
    authority: "read-only repository access"
    preconditions: ["The source plan is ready"]
    completion:
      all:
        - "Every affected artifact and applicable constraint is identified"
    failure:
      classify: ["permanent"]
      transitions:
        permanent: "terminal.failed"
    idempotency:
      key: "workflow.id + node.id + input-digest"
      replay: "reuse matching persisted output"
  - id: "implement"
    class: "task"
    operation: "implement"
    objective: "Implement the requested behavior"
    owner: "implementer"
    inputs:
      - ref: "inspect.result"
        type: "evidence-set"
        required: true
    outputs:
      - id: "implementation.result"
        type: "change-set"
        persistence: "workflow"
    reads: ["source.module"]
    writes: ["source.module"]
    side_effects: ["repository write"]
    authority: "repository write access"
    preconditions: ["The implementation surface is identified"]
    completion:
      all:
        - "The requested behavior is implemented"
    failure:
      classify: ["permanent"]
      transitions:
        permanent: "terminal.failed"
    idempotency:
      key: "workflow.id + node.id + input-digest"
      replay: "reuse matching persisted output and verify its artifact digest"
  - id: "validate"
    class: "task"
    operation: "validate"
    objective: "Verify the requested and preserved behavior"
    owner: "implementer"
    inputs:
      - ref: "implementation.result"
        type: "change-set"
        required: true
    outputs:
      - id: "validate.result"
        type: "verification-result"
        persistence: "terminal"
    reads: ["source.module"]
    writes: []
    side_effects: []
    authority: "read and test access"
    preconditions: ["The implementation is complete"]
    completion:
      all:
        - "AC-1 is verified"
    failure:
      classify: ["permanent"]
      transitions:
        permanent: "terminal.failed"
    idempotency:
      key: "workflow.id + node.id + input-digest"
      replay: "reuse matching terminal evidence"
  - id: "terminal.succeeded"
    class: "terminal"
    objective: "Record successful completion"
    inputs: ["validate.result"]
    terminal:
      status: "success"
      condition: "AC-1 is verified"
      outputs: ["validate.result"]
  - id: "terminal.failed"
    class: "terminal"
    objective: "Record unrecoverable failure"
    inputs: []
    terminal:
      status: "failure"
      condition: "A task reaches a permanent failure"
      outputs: []

edges:
  - from: "inspect"
    to: "implement"
    condition: "inspect.status == 'succeeded'"
    passes: ["inspect.result"]
  - from: "implement"
    to: "validate"
    condition: "implement.status == 'succeeded'"
    passes: ["implementation.result"]
  - from: "validate"
    to: "terminal.succeeded"
    condition: "validate.status == 'succeeded'"
    passes: ["validate.result"]

control:
  entry_nodes: ["inspect"]
```

## Node Classes

Every node has `id`, `class`, and `objective`. Every nonterminal node has typed
inputs and outputs, preconditions, completion semantics, and deterministic
outcome transitions. Terminals declare the result and reference the retained
outputs that they record. Apply the following additional contract for each
class:

- `task`: declare `operation`, `owner`, reads, writes, side effects, authority,
  preconditions, failure classification and transitions, and idempotency. Route
  success through an outgoing edge and route every classified failure through
  `failure.transitions`.
- `terminal`: declare a `success`, `failure`, or `blocked` status, its condition,
  and retained outputs. A terminal has no outgoing transition.

## Consistency Checks

- Every node, artifact, state, output, policy, checkpoint, and terminal
  reference resolves. `<node-id>.status` resolves through `state_model`.
- Every downstream or replayed output has `workflow`, `checkpoint`, or
  `terminal` persistence.
- Every node is reachable from an entry node and can reach a terminal.
- Every failure class, gate decision, join outcome, retry exhaustion, invalid
  checkpoint, and recovery outcome has a deterministic destination.
- Every acceptance criterion names a verification output.
- The workflow goal has a stable ID and names only declared acceptance
  criteria.
- No concurrent nodes write the same artifact without a declared integration
  owner or serialization edge.
- Custom operations define their inputs, outputs, side effects, authority,
  completion, retry, and idempotency semantics.

Add domain fields only under `extensions`. Preserve the meaning of the core
fields.
