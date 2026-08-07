# Evidence Contract

`docs/evidence.md` is the agent-maintained, normalized working ledger for
inventory, reverse engineering, iteration, and comparison. It is separate from
the human-maintained `context.md` and the clean synthesized `system.md`. Keep
exactly these top-level sections in this order: `coverage`, `sources`,
`elements`, `relationships`, and `reconciliation`.

## Source roles and normalization

Treat sources according to the claim they support:

- human-confirmed context supports intended purpose and behavior.
- source code and contracts support implemented behavior.
- pipelines and deployment configuration support delivery paths.
- reviewed live metadata supports observed deployed state.
- existing documentation supports a claim only when corroborated or explicitly
  identified as historical context.

Do not apply one global source precedence. Preserve observation times and
conflicts. Store normalized evidence only. Before discarding a raw response,
preserve the minimum non-sensitive facts, stable IDs, canonical locators,
observation time, and coverage limits needed to review the resulting claims.

## Stable IDs

Use lowercase kebab-case IDs with a type prefix:

- sources: `src-<name>`
- elements: `sys-<name>`, `cmp-<name>`, `ifc-<name>`, `res-<name>`
- claims: `clm-<name>`

Keep IDs stable across refreshes. Do not encode mutable display names,
environments, regions, or timestamps when a stable canonical identifier exists.

## Portable citations

Use the stable ID as the link text and link it to the owning section in
`evidence.md`. This keeps citations valid in Markdown renderers without custom
HTML anchors:

- source ID: `[src-repository](evidence.md#sources)`
- element ID: `[cmp-api](evidence.md#elements)`
- claim ID: `[clm-delivery](evidence.md#reconciliation)`

From a page in `docs/diagrams/`, use `../evidence.md` instead. Separate multiple
citations with commas. In `evidence.md` itself, use the unlinked stable ID.
Do not use a name, URL, or bare section link as a substitute for the ID. The
source or element row owns its canonical locator.

## Coverage

| provider | authorized scope | status | checked-at | limitation |
|---|---|---|---|---|

Use `complete`, `partial`, `unavailable`, or `out-of-scope` for coverage status.
Coverage describes what was inspected, not whether the system is correct.

## Sources

| source id | kind | locator | observed-at | coverage |
|---|---|---|---|---|

Typical source kinds include `human-context`, `repository`, `pipeline`,
`deployment-config`, `live-metadata`, `existing-doc`, and `supplied-export`.
Locators should be canonical URLs, repository paths, or provider identifiers.
Never embed credentials or secret-bearing query values.

## Elements

| element id | kind | subtype | name | environment | canonical locator | source ids |
|---|---|---|---|---|---|---|

Allowed kinds:

- `system`: the documented system or business capability.
- `component`: deployable software, app, plugin, flow, job, pipeline, or data
  product.
- `interface`: API, event, connector, file exchange, or data contract.
- `resource`: cloud, platform, SaaS, storage, database, identity, or
  infrastructure dependency.

Use `subtype` for provider-specific distinctions. A repository or pipeline is a
source unless it is also an operationally significant system element.

## Relationships

| source element | relationship | target element | evidence ids | status |
|---|---|---|---|---|

Allowed relationship values:

- `part-of`
- `depends-on`
- `provides`
- `consumes`
- `deployed-to`
- `sourced-from`

Use `expected`, `observed`, or `both` for relationship status. Evidence IDs in
this table refer to source IDs that support the relationship.

Use directional relationships. Create the reverse row only when it conveys a
different required query, not mechanically. Reader pages cite each
relationship through the source IDs in its `evidence ids` cell.

## Reconciliation

| claim id | context reference | expected state | observed state | result | evidence ids | next check |
|---|---|---|---|---|---|---|

Allowed results:

| Result | Meaning |
|---|---|
| `match` | Context and evidence agree |
| `mismatch` | Both exist but disagree |
| `context-only` | Expected but not observed |
| `evidence-only` | Observed but not expected |
| `unresolved` | Evidence is insufficient |
| `out-of-scope` | Deliberately excluded |

A reconciliation row must cover each material element and relationship or use
it as direct support. `gaps.md` is a reader-facing view of non-match rows.
`evidence.md` remains canonical.

## Sensitive data

Operational names, canonical resource IDs, resource groups, regions,
environments, repository/pipeline links, and dependency endpoints are allowed
when needed. Exclude secret values, tokens, connection strings, credentials,
customer data, and unnecessary exploitable configuration. Redact the value, not
the existence of the configuration or relationship.
