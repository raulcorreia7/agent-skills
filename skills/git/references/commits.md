# Commit Messages

Use this fallback when the repository has no convention of its own. When the
repository runs commitlint or an equivalent hook, that hook owns the header
grammar.

```text
type: subject
type(scope): subject
type!: subject
type(scope)!: subject
```

- Write the subject in the imperative, lowercase unless it starts with a
  proper noun, with no final period.
- Keep one intent per commit when practical.
- Add a scope only when it gives stable grouping or search.
- Put work-item IDs and URLs in the body or footer, never the scope.
- For a version bump, give the exact version.

## Types

| Type | Use |
| --- | --- |
| `feat` | New capability |
| `fix` | Defect or broken behaviour |
| `docs` | Documentation-only change |
| `refactor` | Behaviour-preserving change to code shape |
| `test` | Test-only change |
| `ci` | CI or pipeline automation |
| `build` | Build, packaging, or dependency tooling |
| `perf` | Performance improvement |
| `revert` | Revert of a prior commit |
| `style` | Formatting-only change, when the repository uses it |
| `chore` | Residual maintenance with no clearer type |

Use `test`, not `tests`, and `ci:` rather than `chore(ci):`. `chore` is the
last resort.

Scopes are optional and open-ended. Prefer stable repository areas, such as
api, auth, ui, db, deps, docs, infra, repo, release, or testing, over
abbreviations, URLs, work-item IDs, and one-off names.

## Breaking changes

A change is breaking when consumers or dependent systems must change because
of an API, behaviour, compatibility, configuration, data, or operational
contract. Internal refactors and file moves that keep supported behaviour are
not breaking.

The fallback requires both markers: `!` before the colon and a
`BREAKING CHANGE:` footer. That's stricter than Conventional Commits, which
accepts either one.

```text
feat(api)!: require cursor pagination

BREAKING CHANGE: list endpoints now require cursor parameters.
```

## Body

The body says why the change was needed and what it affects; the diff already
shows how.

## Examples

```text
docs: clarify deployment runbook
feat(ui): add saved filters
fix(auth): reject expired tokens
ci: add pull request validation
build(deps): update lockfile
chore(release): prepare v0.3.2
```

Vague or mixed headers such as "Update stuff", "fix #1", or "build: change
dependencies and docs and runtime config" say nothing a reader can search for.

Sources: [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/),
[commitlint rules](https://commitlint.js.org/reference/rules.html), and reviewed
contribution conventions from pnpm, Nest, Nuxt, semantic-release, and Cypress
(retrieved 2026-07-09).
