# External Contracts

- Identify the applicable protocol standard and supported version before
  designing a boundary. Preserve an established compatible contract unless
  the change includes a migration.
- Maintain generated code through its schema, template, configuration, or
  generator. Validate generated output for correctness and reproducibility.
- Use feature flags for rollout, rollback, experimentation, or temporary
  compatibility. Define the safe default, behavior in both states, ownership,
  and removal condition. Keep selection near one boundary.

Example—record a temporary compatibility flag as a complete contract:

| Field | Value |
|---|---|
| Flag | `orders.write_v2` |
| Safe default | Disabled |
| Disabled behavior | Write the established schema |
| Enabled behavior | Dual-write and verify the new schema |
| Owner | Orders team |
| Removal condition | All readers use v2 and rollback window ends |

Tests exercise both states through the public boundary.
