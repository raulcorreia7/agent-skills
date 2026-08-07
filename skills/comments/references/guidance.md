# Code Comment And API Documentation Guidance

Use comments for non-obvious contracts, constraints, risk, and rationale.

## Classify The Comment

- **Keep:** durable contract, invariant, rationale, risk, or external quirk.
- **Rewrite:** useful intent that is vague, wordy, stale, or inconsistent with
  local language conventions.
- **Remove:** narration of visible mechanics, obsolete behavior, or history
  better owned by Git, an ADR, an issue, or documentation.
- **Add:** a public boundary or surprising local constraint lacks enough context
  to prevent misuse.

Prefer clear code and enforceable contracts. Do not refactor merely to avoid a
comment unless refactoring is in scope.

## Public API Documentation

Use native documentation for public APIs when signatures, types, and local
conventions do not establish the contract. Document only non-obvious purpose,
side effects, lifecycle, ordering, compatibility, concurrency, failure, or
safety behavior. Do not restate names, types, or obvious returns.

## Implementation Comments

Comment local context that future edits must preserve:

- invariants, ordering, ownership, lifecycle, or concurrency constraints.
- security, privacy, data safety, cost, migration, or compatibility rationale.
- external-system quirks and deliberate workarounds.
- generated-code and tooling boundaries.
- intentionally surprising trade-offs.

Keep comments close to constrained code. Put file-wide generated, parser,
ownership, migration, security, or tooling boundaries near the top. Keep broad
architecture and history in owned documentation.

## Freshness And Enforcement

- Update or remove nearby comments when behavior, intent, constraints, or
  contracts change.
- Treat stale comments as correctness risk.
- Pair enforceable safety, security, compatibility, and data rules with tests,
  types, assertions, validation, or linters when practical.
- Let comments explain rationale and constraints that enforcement cannot.

## Searchable Markers

Use established uppercase markers:

| Marker | Use |
|---|---|
| `NOTE:` | Durable context that prevents misuse |
| `WARNING:` | Real destructive, safety, security, or privacy footgun |
| `TODO:` | Planned follow-up with a known trigger |
| `FIXME:` | Known incorrect behavior intentionally left in place |
| `HACK:` | Deliberate workaround for a documented constraint |

Anchor `TODO`, `FIXME`, and `HACK` with an issue, owner, condition, or
verification/removal path. Avoid bare reminders. Prefer Ruff `TD`, ESLint
`no-warning-comments`, or the repository marker lint when one exists.

## Security, Privacy, And Links

- Never put secrets, tokens, credentials, customer data, or live operational
  values in comments. Secret scanning (gitleaks or equivalent) owns detection;
  this guidance only forbids putting them in comments.
- Explain trust, validation, authorization, retention, and privacy constraints
  that future edits could weaken.
- Link owned docs, ADRs, standards, upstream issues, or runbooks when needed.
  Retain enough local context to survive link rot.

Use concise, neutral, present-tense language.
