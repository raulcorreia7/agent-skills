# Documentation Information Architecture

Start navigation changes and documentation-tree reorganizations read-only.
Propose disruptive moves and apply them only after approval of the structure
change.

## Reader model

Classify content by reader need:

| Type | Reader need |
|---|---|
| Tutorial | Learn through a guided path |
| How-to | Complete a task |
| Reference | Look up stable facts |
| Explanation | Understand context and trade-offs |

Organize around terms and questions readers recognize, not implementation
layout unless that is their natural navigation model.

## Inventory and navigation

- Find entry points, docs trees, wiki pages, navigation files, runbooks, ADRs,
  diagrams, API/config references, onboarding, and troubleshooting.
- Identify orphan pages, unexplained deep nesting, mixed concerns, unstable
  names, missing indexes, and navigation that does not match reader tasks.
- Preserve useful local conventions and generated navigation.

## Structure defaults

Use a local structure when it works. Otherwise prefer a shallow task-first tree:

```text
docs/
  getting-started.md
  how-to/
  reference/
  explanation/
  troubleshooting/
  architecture/
  runbooks/
  decisions/
```

Use domain or resource grouping when readers search by those concepts. Avoid
parallel trees that describe the same facts.

For a service or library with several durable documents, keep the root README
as the default task map. Add `docs/README.md` only when the docs tree has enough
independently navigable pages that local routing materially reduces search. Do
not duplicate root navigation or introduce a taxonomy made of thin pages.

For example, route reader tasks rather than mirroring the source tree:

| Reader task | Route |
|---|---|
| Make the first local request | `getting-started.md` |
| Recover a failed deployment | `runbooks/recover-deployment.md` |
| Look up configuration keys | `reference/configuration.md` |

Keep a small orientation diagram only when it helps. Split dense diagrams into
focused context, runtime, sequence, data/state, or trust-boundary views. Use the
`diagrams` skill when construction or renderer compatibility requires a
specialist pass.

Validate entry points, generated navigation, moved pages, and the resulting
task routes.

Source: [Diátaxis](https://diataxis.fr/).
