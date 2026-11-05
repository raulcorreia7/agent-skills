# Code Comment And API Documentation Guidance

Use comments for non-obvious contracts, constraints, risk, and rationale.

## Classification examples

The classes are defined in the skill.

| Comment | Class | Reason |
|---|---|---|
| `# The provider drops the first TLS handshake; retry once.` above a retry | keep | External quirk the code can't show |
| `# Returns the user.` on a function that returns `None` when the user is missing | revise | The contract is incomplete |
| `# Increment the counter.` above `count += 1` | remove | Narrates the visible mechanics |
| `# Changed in 2021 to fix the login bug.` | remove | History that Git owns |
| No comment on a public `send()` that isn't safe to call from two threads | add | A concurrency constraint callers can't infer |

Prefer clear code and enforceable contracts. Don't refactor only to avoid a
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
