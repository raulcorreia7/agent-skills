# CLI execution

## Resolve the command

Reuse a project script, a command on `PATH`, or
`node_modules/.bin/designmd`. Preserve project-script runner syntax.

If no local command exists, ask for approval before you run this pinned command:

```text
npx -p @google/design.md@0.4.0 designmd
```

Do not use `npx` to probe. For conditional lint after authoring, updating, or
export, skip lint when no local command exists. Do not acquire a tool only for
that check.

## Commands

- **Lint:** Run `designmd lint <file>`. Exit code `0` means no error finding;
  exit code `1` means an error finding. Preserve finding severity.
- **Diff:** Run `designmd diff <before> <after>`. Exit code `1` means that the
  later file has more errors or warnings and is a regression.
- **Export:** Run `designmd export --format <format> <file>` with
  `json-tailwind`, `css-tailwind`, `tailwind`, or `dtcg`. Select an explicit
  destination and get approval before replacement.
- **Specification:** Run `designmd spec`, `designmd spec --rules`, or
  `designmd spec --rules-only --format json` when the requested result needs
  the CLI form.
