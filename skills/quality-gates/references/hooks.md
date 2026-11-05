# Hooks

A hook gives fast local feedback. Anyone can skip it with `--no-verify`, so CI
stays the enforcing gate and runs the same checks.

## Choice

1. Keep the hook manager the repository already uses (pre-commit, lefthook,
   husky, or a `core.hooksPath` directory). Add lefthook or husky only when it
   is already there.
2. Otherwise use the pre-commit framework: one checked-in
   `.pre-commit-config.yaml`, each hook repository pinned by `rev`.
3. Use a native hook in a committed `core.hooksPath` directory when the
   repository wants no hook dependency. Each developer must run
   `git config core.hooksPath <dir>` once; document that command.

## Rules

- Hooks check and format the staged files only, and finish in seconds. Put
  slow checks (full test suite, type checking a large tree) in a `pre-push`
  hook or in CI.
- Pin each hook `rev` to a release tag. Pick it from the hook repository's
  releases, or run `pre-commit autoupdate`; both fetch from the network.
- Match hook tool versions to the locked versions CI uses. When they can
  drift, use a `repo: local` hook that calls the project's own tool.
- `pre-commit install` writes into `.git/hooks` of the local clone, so ask
  before running it. A `pre-push` hook also needs
  `pre-commit install --hook-type pre-push`.

## pre-commit example

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: <release-tag>             # match the ruff version in the lock file
    hooks:
      - id: ruff-check
        args: [--fix]
      - id: ruff-format
  - repo: local
    hooks:
      - id: pyright
        name: pyright
        entry: uv run pyright
        language: system
        types: [python]
        pass_filenames: false
        stages: [pre-push]
```

Local fixes (`--fix`) are fine in a hook because the developer reviews the
change before committing; CI runs the check-only form.
