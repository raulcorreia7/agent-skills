# Delegation Briefs

Load for `parallel` mode. The parent owns scope, collision control,
integration, and final quality.

Slices run in isolated contexts when the harness can run parallel agents.
Without that capability, the same briefs run in order in one context; the
ownership and collision rules still hold.

## Brief template

Every slice gets one brief with all of these fields.

```text
Objective: <one bounded, observable outcome>
Mode: <read-only | planning | review | edit | validation>

Owned scope:
- <exact paths, package, contract, or responsibility>

Inputs and dependencies:
- <approved decisions, upstream outputs, and slices that must finish first>

Allowed mutations:
- <none, source paths, or explicitly approved external state>

Boundaries:
- keep work inside the owned scope;
- preserve concurrent changes;
- leave unassigned product, contract, and architecture decisions to their owner;
- require explicit approval for staging, commits, publication, deployment, and external mutations.

Validate:
- <slice-local commands or observable checks>

Return:
- evidence or files changed;
- behaviour or decisions produced;
- checks run and results;
- risks, conflicts, and handoff data.
```

Add what the mode needs:

- `read-only`: ask for facts, inferences, unknowns, and approval-gated checks.
- `planning`: ask for constraints, dependencies, risks, and open decisions.
- `review`: ask for blocking and non-blocking findings with artifact evidence.
- `edit`: name the exact files and the expected behaviour or output.
- `validation`: name the commands, expected signals, and likely failure owners.

## Mode boundaries

- `read-only`: inspect or map; change no files or external systems.
- `planning`: produce bounded planning input; don't implement.
- `review`: report evidence-backed findings; don't fix them.
- `edit`: change only the assigned, disjoint write set; adapt to concurrent work
  and never revert another slice.
- `validation`: run the assigned checks; change source only when the brief
  includes validation setup or fixes.

## Dependency and collision rules

- Give shared contracts, schemas, migrations, generated files, lockfiles,
  catalogs, and integration surfaces one owner each.
- Consumers wait for the owner's explicit output. Edit globs and generated
  output never overlap.
- Separate exploration from mutation when that helps; report unexpected
  overlap.

## Parent synthesis

Before completion, reconcile assumptions and overlapping diffs, remove
duplicate findings, and record unowned residual risk. Run integration only on
request or when it cheaply addresses a significant risk.
