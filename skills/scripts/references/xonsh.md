# Xonsh Scripts

## Fit

Choose xonsh when a script mixes substantial Python logic with subprocess
orchestration and must run on both POSIX and Windows. Keep Bash, PowerShell, or
batch for small platform-local glue, and plain Python with `subprocess` when the
shell surface carries no value.

## Mode Ambiguity

A line that is only an expression runs in subprocess mode when its names are not
current variables, so `ls -l` runs a command. Keep that ambiguity impossible:

- Give Python variables names that are not commands, and command names that are
  not variables.
- Splice Python values with `@(expr)` instead of building command strings.
- Capture output with `$(...)`; use `!()` when exit status and streams matter.

## Shape

```xonsh
#!/usr/bin/env xonsh
# $ARG1..$ARGn are set in either mode; $ARGS is a list in Python mode only.

def main(args: list[str]) -> int:
    if not args:
        print("usage: script.xsh <path>")
        return 2

    print(f"handling {len(args)} argument(s)")
    return 0

main($ARGS)
```

Run it as `xonsh script.xsh <args>`, or use `xonsh -c '<code>'` for a one-liner.
Keep shared logic in imported `.py` modules so formatters, linters, types, and
tests own it, and leave the `.xsh` file a thin entrypoint.

## Command Safety

- Keep environment values typed: `$VAR` holds strings, numbers, or lists,
  `@.env` is the mapping, and `${expr}` looks up a computed name.
- Remember that `*PATH` and `*DIRS` names are `EnvPath` lists, not strings.
- Export to child processes only when intended, through `$UPDATE_OS_ENVIRON`.
- Splice arguments instead of assembling one raw command string.

## Verification

Exercise help and one disposable-fixture path:

```text
xonsh script.xsh --help              # usage on the documented stream
xonsh script.xsh FIXTURE             # expected result, isolated target
xonsh -c 'showcmd <command line>'    # inspect the parsed command
```

Then run the repository's existing formatter, analyzer, and focused checks for
the Python modules the script imports. Do not add a linter for the `.xsh` file
alone.
