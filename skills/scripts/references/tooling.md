# Tool-State Placement

## Placement

Use native tool defaults and existing repository conventions. Override a
default for sandboxing, debugging, reproducibility, or reliable cleanup.

Common local-only shapes when the repository has no convention:

- `.cache/<tool>/` for reusable caches and downloaded indexes.
- `.tmp/<task>/` for disposable command scratch space.
- `.reports/<tool>/` for inspectable local reports.
- `.artifacts/<task>/` for local workflow outputs.

For example, keep a reusable dependency index at
`.cache/dependency-audit/index.json` and one-run extraction state under
`.tmp/dependency-audit/`.

Use established tracked output directories such as `dist/`, `build/`,
`target/`, or `coverage/` when the project intentionally owns them.

Use language-native secure temporary-file APIs when content can be sensitive.
Do not place credentials or secret-bearing diagnostics in caches, reports, or
artifacts.

## Ignore Rules

- Group rules by ownership and purpose, not chronology.
- Prefer narrow directory rules over one-off generated filenames.
- Keep negations next to the rule they reopen.
- Do not ignore source, lockfiles, fixtures, documentation, or intentionally
  tracked generated artifacts.
- Remove obsolete state and ignore rules when ownership or paths change.

Verify a new local-only path without changing tracked source:

```bash
git check-ignore -v .cache/dependency-audit/index.json
git status --short
```

The first command must identify the intended narrow ignore rule; the second must
show that no unexpected generated file is tracked or unignored.
