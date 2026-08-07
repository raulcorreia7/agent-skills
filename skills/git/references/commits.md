# Commit Messages

Follow the repository's convention first. Prefer `commitlint` or an equivalent
hook in the consuming repository for header grammar. Otherwise use a concise
Conventional Commit-style header:

```text
type: subject
type(scope): subject
type!: subject
type(scope)!: subject
```

- Use an imperative or present-tense subject.
- Keep the first word lowercase unless it is a proper noun.
- Omit the final period.
- Keep one intent per commit when practical.
- Add a scope only when it improves stable grouping or search.
- Keep work-item IDs and URLs in the body or footer, not the scope.

## Types

| Type | Use |
|---|---|
| `feat` | New capability |
| `fix` | Defect or broken behavior |
| `docs` | Documentation-only change |
| `refactor` | Behavior-preserving code-shape change |
| `test` | Test-only change |
| `ci` | CI or pipeline automation |
| `build` | Build, packaging, or dependency tooling |
| `perf` | Performance improvement |
| `revert` | Revert a prior commit |
| `style` | Formatting-only change when locally useful |
| `chore` | Residual maintenance with no clearer type |

Use `test`, not `tests`. Prefer `ci:` over `chore(ci):`. Use `chore` only as a
fallback.

## Scopes

Scopes are optional and open-ended. Prefer stable repository areas such as
`api`, `auth`, `ui`, `db`, `deps`, `docs`, `infra`, `repo`, `release`, or
`testing`. Avoid random abbreviations, URLs, work-item IDs, and one-off names.

## Breaking Changes

A breaking change requires consumers or dependent systems to change because of
an API, behavior, compatibility, config, data, or operational contract.

- This repository's fallback convention requires `!` before the colon and a
  `BREAKING CHANGE:` footer. The convention is intentionally stricter than
  Conventional Commits, which permits either marker.
- Do not mark internal refactors or file moves as breaking when supported
  behavior is unchanged.

```text
feat(api)!: require cursor pagination

BREAKING CHANGE: list endpoints now require cursor parameters.
```

## Examples

```text
docs: clarify deployment runbook
feat(ui): add saved filters
fix(auth): reject expired tokens
test(api): cover pagination errors
ci: add pull request validation
build(deps): update lockfile
chore(release): prepare v0.3.2
refactor(api): simplify request parsing
```

Avoid vague or mixed headers such as `Update stuff`, `patch bump`, `fix #1`, or
`build: change dependencies and docs and runtime config`.

For version bumps, include the exact version. Keep generated changelog and
version output separate from unrelated changes. Do not rewrite pushed history
without explicit approval. Prefer `--force-with-lease` only when an approved
workflow genuinely requires a remote branch rewrite.

Sources: [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/),
[commitlint rules](https://commitlint.js.org/reference/rules.html), and reviewed
contribution conventions from pnpm, Nest, Nuxt, semantic-release, and Cypress
(retrieved 2026-07-09).
