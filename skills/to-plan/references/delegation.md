# Delegation Briefs

The parent owns scope, collision control, integration, and final quality.

## Slice Contract

Every brief contains:

| Field | Required content |
|---|---|
| Objective | One bounded, observable outcome |
| Mode | `read-only`, `planning`, `review`, `edit`, or `validation` |
| Ownership | Exact paths, packages, contracts, or responsibilities |
| Inputs | Evidence, decisions, and usable upstream outputs |
| Dependencies | Slices or contracts that must finish first |
| Mutation | Whether source or external state may change |
| Boundaries | Actions, paths, systems, and decisions outside the slice |
| Validation | Slice-owned commands or observable checks |
| Return | Changes, evidence, material checks, risks, and handoff data |

## Mode Boundaries

- `read-only`: inspect or map; do not change files or external systems.
- `planning`: produce bounded planning input; do not implement.
- `review`: report evidence-backed findings; do not fix them.
- `edit`: change only the assigned, disjoint write set; adapt to concurrent work
  and never revert another slice.
- `validation`: run assigned checks; change source only when the brief includes
  validation setup or fixes.

## Dependency And Collision Rules

- Assign one owner to shared contracts, schemas, migrations, generated files,
  lockfiles, catalogs, and integration surfaces.
- Make consumers wait for explicit owner output. Do not overlap edit globs or
  generated output.
- Separate exploration from mutation when useful; report unexpected overlap.

## Brief Template

```text
Objective: <one bounded outcome>
Mode: <read-only | planning | review | edit | validation>

Owned scope:
- <paths, package, contract, or responsibility>

Inputs and dependencies:
- <approved decisions or upstream outputs>

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
- behavior or decisions produced;
- checks run and results;
- risks, conflicts, and handoff data.
```

- For inspection, request facts, inferences, unknowns, and approval-gated checks.
- For planning, request constraints, dependencies, risks, and open decisions.
- For review, request blocking and non-blocking findings with artifact evidence.
- For an edit, include exact files and expected behavior or output.
- For validation, include commands, expected signals, and likely failure owners.

## Parent Synthesis

Before completion, reconcile assumptions and overlapping diffs, remove duplicate
findings, and record unowned residual risk. Run integration only on user request
or when it efficiently addresses material risk.
