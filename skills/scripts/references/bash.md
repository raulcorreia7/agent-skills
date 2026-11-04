# Bash Scripts

## Fragile Behavior

- Start executables with `#!/usr/bin/env bash` unless deployment requires a
  fixed interpreter.
- Prefer `set -euo pipefail`. Add `-E` only when an inherited `ERR` trap is
  required. Handle expected non-zero statuses explicitly. Strict mode does not
  replace this handling.
- Use arrays for commands and flags. Quote expansions. Use `[[ ... ]]` for
  tests and `(( ... ))` for arithmetic.
- Avoid command substitution as an iteration mechanism. Prefer `readarray` or
  `while IFS= read -r` when line preservation matters.
- Keep tracing behind an explicit diagnostic gate and prevent secret exposure.
- Use traps for temporary files, locks, or background processes that require
  cleanup.

## Shape

```bash
#!/usr/bin/env bash
set -euo pipefail

usage() { printf 'Usage: %s check|render\n' "${0##*/}"; }

main() {
  case "${1:-}" in
    check) run_check ;;
    render) run_render ;;
    -h|--help) usage ;;
    *) usage >&2; return 2 ;;
  esac
}

main "$@"
```

## Long Commands

Build a long or conditional command as an array; it needs no continuations
and stays safe to quote. For a fixed command that must wrap, put one flag or
flag-value pair per line, indent continuations one level, and align the
backslashes in one column. A configured `shfmt` rewrites each backslash to one
space; follow it when it runs.

```bash
args=(--rm --name web -p 8080:80)
[[ -n "${ENV_FILE:-}" ]] && args+=(--env-file "$ENV_FILE")

docker run "${args[@]}" nginx
```

```bash
docker run                \
  --rm                    \
  --name web              \
  --publish 8080:80       \
  --volume "$PWD:/srv:ro" \
  nginx
```

## Verification

Use the repository's aggregate check first. Otherwise run syntax validation and
ShellCheck without replacing repository configuration or suppressing findings:

```bash
bash -n path/to/script
shellcheck path/to/script
```

Run the configured formatter in check or diff mode when one exists, followed by
the smallest existing behavior test. Do not introduce a formatter or override
its style flags for one script.
