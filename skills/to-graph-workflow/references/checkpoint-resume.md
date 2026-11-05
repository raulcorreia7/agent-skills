# Checkpoint And Resume Controls

## Example

Change each captured output's declaration in its owning task to checkpoint
persistence:

```yaml
outputs:
  - id: "implementation.result"
    type: "change-set"
    persistence: "checkpoint"
```

Then define the checkpoint and its resume rule:

```yaml
checkpoints:
  - id: "checkpoint.implemented"
    after: ["implement"]
    captures:
      outputs: ["implementation.result"]
      artifact_snapshots:
        - artifact: "source.module"
          snapshot: "recoverable content and digest"
    retention: "until-terminal"
    integrity: "verify artifact and input digests"

resume:
  - from_checkpoint: "checkpoint.implemented"
    validate: ["checkpoint integrity passes", "inputs still match"]
    restore: ["implementation.result", "source.module"]
    continue_at: "validate"
    invalid_to: "terminal.failed"
```

Reference each checkpoint from exactly one resume rule. Every captured output
must declare `persistence: checkpoint` in its owning task. A captured artifact
snapshot declares the artifact ID and the recoverable snapshot material.
Restore only captured state and validate it before execution continues. Every
node, output, artifact, checkpoint, and terminal ID must resolve in the emitted
graph.
