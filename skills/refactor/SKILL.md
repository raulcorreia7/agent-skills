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
   inheritance, a smell, a metric, or change history. Complete when each of
   these is stated, or you have stopped for alignment on the
   one that is unclear.
2. Inspect callers, tests, types, configuration, data shape, side effects, and
   failure behavior. Before editing, map each key preservation claim to
   existing evidence. When a claim has none, propose the characterization tests
   that would cover it; adding them is approval-gated. Complete when every
   key claim maps to existing evidence or to approved characterization
   tests.
3. Make one coherent structural change at a time, keeping compatibility logic at
   the boundary that owns the contract. Assess each preservation claim with
   existing evidence, and run a small existing check when it efficiently
   addresses a significant risk. Revert the local change when evidence shows a
   behavior difference. Complete when the change is in place and no claim shows
   a behavior difference.
4. Remove obsolete paths only after callers and evidence show no use.
   Complete when the target structure exists, all callers use the intended
   path, and evidence supports every key preservation claim.

## Flow

```text
input ← structural target, behavior, contracts
claims ← map to existing evidence
unsupported claim? yes → propose characterization tests, wait for approval | no → continue
loop: one structural change → assess → revert on behavior difference
remove obsolete paths only when callers and evidence agree
stop: target exists + every claim has evidence
```

## Guardrails

- Keep scope to the structural target and directly coupled cleanup.

## Output

- Refactored code and a preservation map that links each key claim to
  supporting evidence.
