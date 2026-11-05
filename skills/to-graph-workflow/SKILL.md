---
name: to-graph-workflow
description: Manual invocation only. Convert an approved implementation-ready plan into an orchestrator-ready execution graph.
---

# To Graph Workflow

Convert a settled plan into a platform-neutral execution graph. Keep plan
validation separate from graph compilation. Do not implement the plan.

## Workflow

1. Validate the plan.
   - Identify the goal, scope, constraints, acceptance criteria, affected
     artifacts, dependencies, approvals, and recovery expectations.
   - Confirm that no material product, architecture, security, data, rollout,
     or ownership decision remains unmodeled.
   - Stop and return a readiness report when an open decision can change the
     graph and its outcomes are not specified. Treat the plan as ready when
     material decisions are settled or represented by an explicit gate with a
     deterministic branch for each outcome.

2. Establish the registries.
   - Give every goal, artifact, task, checkpoint, and gate that the plan uses
     a stable ID. Declare each set of allowed state values once. Do not add
     unused registry entries.
   - Record artifact ownership and write sets before adding concurrency.
   - Define the initial state and the terminal success and failure states.
     This step is complete when every task input and output can refer to a
     registry entry or a predecessor output.

3. Compile atomic nodes.
   - Give every node one class: `task`, `gate`, `join`, or `terminal`.
   - For a task, select an operation from `inspect`, `design`, `prepare`,
     `implement`, `generate`, `configure`, `migrate`, `test`, `validate`,
     `review`, `repair`, `integrate`, `document`, `release`, `observe`,
     `rollback`, or `notify`. Use a custom operation only when the core does
     not express its execution semantics.
   - Give each task, gate, and join typed inputs and outputs, preconditions,
     completion criteria, and deterministic outcome transitions. Give each
     terminal a status, condition, and retained outputs. Give each task one
     outcome, one owner, declared reads, writes, side effects, failure
     behavior, and an idempotency strategy.
   - Split a node when it has multiple owners, independent failure modes, or
     unrelated write sets. Also split it when one check cannot verify all its
     completion criteria. Map each acceptance criterion and planned change to
     at least one node.

4. Connect control flow.
   - Default to a directed acyclic graph. Use fan-out only for task nodes with
     independent write sets. Model fan-in as a `join` node that states what it
     waits for and how it reconciles results.
   - Add edge conditions for outcomes other than unconditional success.
   - Use cycles only for bounded retry or repair. State the retry limit, the
     repair action, the re-entry node, and the exhausted-retry destination.
   - Model human, credentialed, cost-affecting, destructive, production, and
     external approvals as `gate` nodes.
   - Add checkpoints only when resume or recovery is material. Typical
     locations are after an expensive or irreversible boundary and before an
     approval gate. This step is complete when every node is reachable from an
     entry node and can reach a terminal state.

5. Prove the graph.
   - Check dependency order, write-set conflicts, missing producers, unused
     outputs, and uncovered acceptance criteria. Also check for unbounded
     loops, orphan nodes, unsafe retries, and unreachable terminal states.
   - Define resume behavior for every present checkpoint. Define recovery only
     for material partial writes, failed integration, rejected approval, or
     retry exhaustion that the graph can encounter.
   - Complete the graph only when the scheduler can use declared state alone.
     Give every failure a deterministic next state.

6. Emit the contract and views.
   - After readiness passes, read
     [execution-contract.md](references/execution-contract.md) before emitting
     YAML. It defines the required top-level shape, task and terminal
     contracts, node lifecycle, persistence, and consistency checks.
   - If the graph contains a gate, also read
     [gate-nodes.md](references/gate-nodes.md).
   - If the graph contains a join, also read
     [join-nodes.md](references/join-nodes.md).
   - If a node has a bounded retry or repair loop, read
     [retry-controls.md](references/retry-controls.md).
   - If execution must resume from a checkpoint, read
     [checkpoint-resume.md](references/checkpoint-resume.md).
   - If the graph requires compensating or rollback recovery, read
     [recovery-controls.md](references/recovery-controls.md).
   - Add one concise view only when requested or when it materially improves
     scheduling, ownership, or review. Use ASCII for a zero-tool terminal
     view, Mermaid for routine Markdown, and Graphviz DOT for dense graphs or
     explicit layout control. Produce multiple formats only when requested.
     Derive every view from YAML and keep detailed contracts there. Show node
     class and task operation without copying detailed node contracts. Show
     gates, joins, conditional branches, bounded loops, material checkpoints,
     and all terminal states. Return the selected source and compare its IDs,
     edge directions, conditions, joins, gates, and terminal states with YAML.
   - When the user requests a rendered Mermaid or Graphviz artifact, read
     [rendering.md](references/rendering.md). Return the selected source even
     when rendering is unavailable.

## Guardrails

- Keep the graph platform-neutral. Put runtime-specific configuration in
  `extensions` without making it part of the core contract.
- Assign one writer to an artifact at a time. Serialize tasks or add an
  integration owner when write sets overlap.
- Make retries safe through idempotency, compensation, or a clean checkpoint.
- Represent missing authority as a gate or blocked terminal, not an assumed
  approval.

## Output

Return:

1. A plan-readiness result. If the plan is not ready, include only the blocking
   decisions and the evidence needed to settle them.
2. For a ready plan, one complete YAML execution graph that follows the
   contract, with all placeholders resolved.
3. When a view is requested or materially useful, one concise ASCII, Mermaid,
   or Graphviz DOT view derived from the YAML.
4. A YAML or compact table mapping. Map each plan item and acceptance criterion
   to its task nodes and verification output.
5. Any residual scheduling, ownership, approval, or recovery risk.
6. When rendering was requested, the rendered artifact and the render command
   and result.
