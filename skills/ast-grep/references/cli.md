# ast-grep CLI

Checked against `ast-grep --help` for version 0.44.1. Run `ast-grep <command>
--help` when the installed version differs.

## Search

| Task | Command |
| --- | --- |
| Direct pattern | `ast-grep run --lang <language> --pattern '<pattern>' <path>` |
| Ad hoc rule | `ast-grep scan --inline-rules '<rule-yaml>' <path>` |
| Retained rule file | `ast-grep scan --rule <rule.yml> <path>` |
| Parsed pattern tree | `ast-grep run --lang <language> --pattern '<pattern>' --debug-query=ast <path>` |

`--inline-rules` and `--rule` are mutually exclusive. Separate several inline
rules with `---`.

## Scope and output

- `--globs '<glob>'` includes or excludes paths with `.gitignore` syntax;
  prefix `!` to exclude, and repeat the flag for several globs. It overrides
  the other ignore rules, and a later glob wins over an earlier one.
- `--json=compact` prints one single-line array, the smallest output to read
  or pipe into `jq`. `--json=stream` prints one object per line. The value
  needs `=`; bare `--json` pretty-prints.
- `--files-with-matches` lists only the matching paths.
- `-C <num>` adds context lines to text output.
- `--update-all` and `--interactive` rewrite files; use them only for a
  requested codemod.

## Testing a rule file

`ast-grep test` checks rules listed in a project's `sgconfig.yml`:

```yaml
# sgconfig.yml
ruleDirs: [rules]
testConfigs:
  - testDir: rule-tests
```

```yaml
# rule-tests/no-console-log-test.yml
id: no-console-log
valid:
  - console.warn('x')
invalid:
  - console.log('x')
```

Run `ast-grep test --skip-snapshot-tests` to check that every `valid` case
misses and every `invalid` case matches. Add `--filter <regex>` to run one
rule's cases. Plain `ast-grep test` also compares output snapshots under
`__snapshots__` and fails when none exist; `--update-all` writes them, so use
it only when the user wants snapshots kept.
