---
name: refactor
description: Manual invocation only. Restructures code while preserving observable behavior and public contracts.
---

# Refactor

## Job

Improve code structure. Preserve observable behavior and public contracts.

## Steps

1. Define the structural target, preserved behavior, public contracts, scope,
   and evidence boundary. Read
   [structural targets](references/structural-targets.md) when the target
   involves abstraction, modules, duplication, a named pattern or principle,
   inheritance, a smell, a metric, or change history. Stop for alignment when
   one is materially unclear.
2. Inspect callers, tests, types, configuration, data shape, side effects, and
   failure behavior. Before editing, map each material preservation claim to
   existing evidence. Do not add characterization tests unless the user asks.
3. Make one coherent structural change at a time. Keep compatibility logic at
   the boundary that owns the contract.
4. Assess each preservation claim with existing evidence. Run a small existing
   check when it efficiently addresses a material risk. Revert the local change
   when evidence shows a behavior difference.
5. Remove obsolete paths only after callers and evidence show no use.
6. Finish when the target structure exists, all callers use the intended path,
   and evidence supports every material preservation claim.

## Flow

```text
target, behavior, contracts ← define
claims ← map to existing evidence
loop: one structural change → assess → revert on behavior difference
remove obsolete paths only when callers and evidence agree
stop: target exists + every claim has evidence
```

## Guardrails

- Keep behavior changes out of refactoring; this skill preserves observable
  behavior and public contracts.
- Preserve public interfaces and data shape unless the user approves a change.
- Keep scope to the structural target and directly coupled cleanup.
- Treat a named pattern, smell, metric, or lower score as evidence to inspect,
  not as the structural target or proof of improvement.

## Output

- Refactored code and a preservation map that links each material claim to
  supporting evidence.
