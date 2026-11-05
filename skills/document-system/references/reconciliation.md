# Reconciliation

For every key intended claim and every relevant observed element or
relationship:

1. Link context and evidence with stable IDs.
2. Assign one allowed reconciliation state.
3. Record the smallest next check for every non-`match` state.
4. Ask a targeted human question or run another bounded discovery pass when it
   can resolve a significant gap.
5. Stop when every key item has a state, even if visible gaps remain.

A publishable baseline can contain non-match states. The stricter catalog
completion gate is in the skill's validation step.

## Example

`clm-api-access` links to `context.md#constraints`, which says the API is
private. `src-gateway` shows a public route, so record `mismatch` and use
"Confirm whether public access is intentional" as the next check.
