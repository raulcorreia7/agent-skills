# CLI Contracts

## Command Contract

- Give the command one job and make its common safe action obvious.
- Use verb subcommands for distinct operations and flags for modifiers.
- Follow repository and platform conventions. Use native PowerShell patterns
  for PowerShell commands.
- Define option precedence, environment inputs, accepted values, defaults,
  output stability, side effects, and retry behavior.
- Accept `--` to end option parsing when an operand can start with `-`.
- Keep machine-readable results stable and separate from diagnostics.

Use `--dry-run` or PowerShell `-WhatIf` to preview state changes. Use `--check`
to validate without changing the source. State whether the command replaces
existing output. Require explicit confirmation only when replacement is
surprising, broad, destructive, or difficult to recover. Routine generated
output can use atomic replacement by default.

## Streams and Exit Codes

- Send results to stdout or the PowerShell success stream. Send progress,
  warnings, and errors to diagnostic streams.
- Exit `0` for success and help. Use a consistent nonzero code for invalid
  usage. Add other codes only when a caller can act on them.
- Define broken-pipe, partial-output, and interruption behavior for commands
  used in pipelines.

## Mutation Gates

- Reject empty targets, filesystem roots, unresolved parents, and unexpectedly
  broad globs before a replacement or deletion.
- Scope writes to explicit targets. Use a temporary file and atomic replacement
  for generated output when practical.
- Make broad changes opt-in. Make noninteractive behavior explicit.
- Receive secrets through a protected channel instead of arguments or output.

## Help

Help states operands, defaults, accepted values, side effects, output,
environment inputs, and mutation gates. Each subcommand has applicable help.

```text
Usage:
  command [OPTIONS] INPUT

Create the requested result.

Options:
  -n, --dry-run   Show the planned changes.
  -h, --help      Show help and exit.

Examples:
  command check INPUT
  command render --output PATH INPUT
```

## Verification

Observe help, invalid input, result and diagnostic streams, and one refusal
path for a mutation command. Use a disposable fixture for any successful write:

```text
command --help                         # exit 0; help on the documented stream
command --definitely-invalid           # documented usage error; no mutation
command --dry-run FIXTURE               # plan only
command --output TEMP_PATH FIXTURE      # isolated successful result
```

Then run the repository's existing formatter, analyzer, and focused CLI test
through its task runner. Do not duplicate a language guide's tool commands here.
