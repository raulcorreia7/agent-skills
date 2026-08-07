# Reconciliation

For every material intended claim and every material observed element or
relationship:

1. Link context and evidence with stable IDs.
2. Assign one allowed reconciliation state.
3. Record the smallest next check for every non-`match` state.
4. Ask a targeted human question or run another bounded discovery pass when it
   can resolve a material gap.
5. Stop the cycle when the reconciliation classifies all material items, even
   if visible gaps remain.

A publishable baseline can contain non-match states. Catalog completion is a
stricter gate: no material `unresolved`, `context-only`, or unexplained
`evidence-only` records remain.

## Example

`clm-api-access` links to `context.md#constraints`, which says the API is
private. `src-gateway` shows a public route, so record `mismatch` and use
"Confirm whether public access is intentional" as the next check.
