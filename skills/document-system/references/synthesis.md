# Synthesis

Generate reader pages from the evidence ledger. Do not copy discovery output.
Put each material claim in the page that owns the reader question:

- code responsibilities, seams, dependencies, entry points, and tests go to
  `modules.md`.
- data structures, ownership, lifecycle, and migrations go to `schema.md`.
- owned HTTP/API, event, queue, and CLI contracts go to `interfaces.md`.
- external systems, exchanged data, authentication class, limits, failures,
  and safe validation go to `integrations.md`.
- environments, resources, topology, operational boundary, reliable dated cost
  basis, and cleanup candidates go to `infrastructure.md`.
- build, release, configuration, rollout, rollback or recovery, and
  verification go to `delivery.md`.

Keep `system.md` short: it states the reconciled current state and boundary,
then directs readers to selected detail pages. Do not duplicate page-owned
tables, contract details, topology, or delivery steps in the overview. Derive
`gaps.md` from non-match records and keep IDs aligned with `evidence.md`.

## Decisions

Record only architecturally significant choices, in the page that owns the
reader question, with context, decision, status, and consequences. Do not
create a decision record for routine implementation choices.

## Example

An observed `POST /checkout` contract belongs in `interfaces.md`. Its outbound
payment-provider call belongs in `integrations.md`. `system.md` summarizes the
checkout capability and links to both pages instead of copying either contract.
