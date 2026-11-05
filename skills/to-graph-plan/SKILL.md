---
name: to-graph-plan
description: Manual invocation only. Compile an approved implementation-ready plan into a minimal, dependency-valid implementation DAG.
---

# To graph plan

## Job

Compile an approved implementation-ready plan into a tool-neutral YAML DAG. Do not revise the plan or implement its work.

## Steps

1. Resolve the plan's outcomes, acceptance evidence, dependencies, authority decisions, and material recovery conditions. Return only the unresolved decision when any of these prevent compilation.
2. Create the smallest nodes that preserve one outcome and its proof. Group independent work into ascending implementation phases; make every planned dependency explicit with `depends_on`.
3. Add `gate` only for a material authority decision. Add `recovery` only when partial change, rejection, or failure needs a defined recovery path. Put runtime-specific data only in `extensions`.
4. Check that IDs are unique; every dependency names a node; no node depends on itself; dependencies precede their dependents by phase; and the graph is acyclic. Check that every plan outcome has acceptance evidence in `done_when`.
5. Emit the YAML. The interchange shape is [the schema](references/graph.schema.json); validate against it rather than restating fields in prose. Finish when the YAML has one executable dependency order and each node has evidence of completion.

## Guardrails

- Keep the core tool-neutral. Do not add scheduler, retry, rendering, persistence, or runtime metadata.
- Do not invent gates, recovery work, owners, or plan decisions.
- A gate states the decision, authority, and approval evidence; an absent authority remains a blocking gate, not an assumed approval.

## Output

Return either the blocking decision or YAML in this shape:

```yaml
version: 1
nodes:
  - id: inspect-contract
    phase: 1
    outcome: Confirm the affected public contract.
    depends_on: []
    done_when: Contract evidence identifies the required change.
  - id: implement-change
    phase: 2
    outcome: Deliver the approved change.
    depends_on: [inspect-contract]
    done_when: The stated acceptance check passes.
```

Each node requires `id`, `phase`, `outcome`, `depends_on`, and `done_when`. It may also contain `gate`, `recovery`, `owner`, and `extensions`.