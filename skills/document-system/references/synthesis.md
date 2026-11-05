# Synthesis

Generate reader pages from the evidence ledger; don't copy discovery output.
Put each key claim in the page that owns its reader question, using the page
map in `baseline.md`.

`system.md` links to page-owned tables, contract details, topology, and
delivery steps instead of repeating them. Derive `gaps.md` from non-match
records and keep its IDs aligned with `evidence.md`.

## Decisions

Record only architecturally significant choices, in the page that owns the
reader question, with context, decision, status, and consequences. Do not
create a decision record for routine implementation choices.

## Example

An observed `POST /checkout` contract belongs in `interfaces.md`. Its outbound
payment-provider call belongs in `integrations.md`. `system.md` summarizes the
checkout capability and links to both pages instead of copying either contract.
