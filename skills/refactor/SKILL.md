---
name: refactor
description: "Restructures code while preserving observable behavior and public contracts. Use when behavior-preserving restructuring is the primary deliverable. Not for changing behavior; use `code`."
---

# Refactor

## Job

Move code to a stated structural target, such as one owner for a rule, a
safer change point, or a test seam, without changing observable behavior or
public contracts.

The lightest path is a local change inside one owner that existing checks
already cover: steps 1, 3, and 4 with no new tests. Escalate to step 2's
preservation map when the change crosses a module or public boundary, or when
a preservation claim has no existing evidence.

## Steps

1. Define the structural target, the behavior and contracts to preserve, and
   the scope. Read `references/structural-targets.md` when the target involves
   abstraction, modules, duplication, a named pattern or principle,
   inheritance, a smell, a metric, or change history. Complete when each is
   stated, or you've stopped to align on the one that's unclear.
2. Inspect callers, tests, types, configuration, data shape, side effects, and
   failure behavior. Map each key preservation claim to existing evidence.
   For a claim with none, propose the characterization tests that would cover
   it. Complete when every key claim maps to existing evidence or to approved
   characterization tests.
3. Make one coherent structural change at a time, keeping compatibility logic
   at the boundary that owns the contract. Check the affected claims after
   each change, running a small existing check where it covers a significant
   risk. Revert the change when evidence shows a behavior difference.
   Complete when the change is in place and no claim shows a difference.
4. Remove obsolete paths once callers and evidence show no use. Complete when
   the target structure exists, every caller uses the intended path, and
   evidence supports every key claim.

## Flow

```text
input ← structural target, behavior and contracts to preserve, scope
define target → map claims to evidence
unsupported claim? yes → propose characterization tests → approved? yes → add | no → narrow scope or stop
loop: one structural change → check claims → revert on a behavior difference → until target reached
remove obsolete paths only when callers and evidence agree
stop: target exists and every key claim has evidence
```

## Gotchas

- Informal contracts break silently: error text, log fields, ordering,
  default values, and exit codes count as behavior.
- A passing suite proves only what it asserts. Check that a test actually
  covers a claim before using it as that claim's evidence.
- Reflection, serialization, dependency injection, and string-based lookups
  hide callers from a text search; check them before removing a path.

## Guardrails

- Approval-gated: adding characterization tests, and changing a public
  interface or data shape even when the change is behavior-neutral.
- Keep scope to the structural target and directly coupled cleanup. Report a
  behavior bug you find instead of fixing it in the same change.

## Composition

- Not for behavior changes, including fixes for bugs the refactor exposes; use `code`.
- Not for finding why a behavior difference appeared; use `debug`.

## Output

- The refactored code.
- A preservation map linking each key claim to its evidence.
- Paths removed, paths kept for compatibility with their removal condition,
  and any behavior bugs found but not fixed.
