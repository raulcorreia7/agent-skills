# Documentation Link Validation

Validate links within the selected documentation scope.

## Sweep

- Inventory relative and absolute links, anchors, embedded assets, navigation
  files, and canonical source targets in scope.
- Check relative paths from each owning page, including case-sensitive paths.
- Check moved-page links, renamed anchors, missing assets, and descriptive link
  text.
- Prefer canonical source targets over local copies of facts that can drift.
- Update inbound links and generated navigation in the same approved change as
  a move.

Run the narrowest available link checker or docs build. When no checker exists,
resolve local targets and anchors directly. Record external targets that could
not be verified.

## Example

From `docs/runbooks/recover.md`, link to
`docs/reference/configuration.md` with the descriptive text "Configuration
reference" and the relative target `../reference/configuration.md`.

Resolve the target from the owning page, not the repository root.
