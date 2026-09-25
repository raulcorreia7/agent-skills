---
name: scripts
description: Builds or explains developer automation. Use when automation is the primary artifact.
---

# Scripts

## Job

Build automation with an explicit command contract and predictable side
effects.

## Steps

1. Inspect existing entrypoints, task runners, manifests, lockfiles, and target
   environments. Define the job, inputs, outputs, side effects, retries, and
   success result. Classify the automation as missing, partial, or already
   sufficient; record unresolved items as assumptions.
2. Select the smallest suitable existing platform and read its guide below.
   State the runner and portability boundary.
3. If automation is missing or partial, implement one entrypoint. If already
   sufficient, skip the edit. Keep load time, discovery, and planning read-only.
   Validate targets before mutation, preview broad changes, and give each side
   effect one visible owner.
4. Run the existing aggregate check when available. Otherwise run only
   supported, non-overlapping checks for material risk: formatting, static
   analysis, strict typing, dependency validation, and focused behavior
   verification. Do not add a second tool for an owned job. For an
   already-satisfied request, stop after this check and report no change.

## Flow

```text
job, IO, effects, success ← define
classify → missing | partial | sufficient
missing | partial → one entrypoint; sufficient → skip
check ← aggregate | supported checks
stop: request satisfied + result recorded
```

## References

Read each applicable implementation guide:

- `references/bash.md` for non-trivial Bash or Unix-local orchestration.
- `references/powershell.md` for PowerShell or Windows automation.
- `references/python.md` for a Python command-line tool.
- `references/xonsh.md` for a script that mixes Python logic with subprocess
  orchestration across POSIX and Windows.
- `references/zx.md` for TypeScript or Node automation that uses or evaluates
  `zx`.
- For another Node or TypeScript runtime, use repository evidence to define its
  invocation, module format, and portability boundary; do not apply `zx`
  conventions by default.
- `references/batch.md` only when `.bat`, `.cmd`, or `cmd.exe` compatibility is
  required.

Read these references only for their named branch:

- `references/cli.md` before implementing a public or team-facing command.
  Define its arguments, validation, streams, exit codes, mutation gates, and
  interrupt behavior.
- `references/script-pipeline.md` when discovery, planning, execution, and
  verification are distinct stages that need separate review or testing.
- `references/tooling.md` when deciding where caches, temporary files,
  generated output, reports, or task-runner state belong.
- `references/sources.yml` only when maintaining or re-verifying this skill's
  external guidance.

## Guardrails

- Keep secrets out of arguments, logs, generated files, and command history.
- Resolve and validate each write or delete target at the mutation boundary.
- Keep verification read-only. Obtain approval before networked dependency
  checks, and do not use automatic audit fixes or dependency upgrades as checks.
- Keep application behavior changes out of automation work; this skill retains
  automation ownership.

## Output

- The script or automation change and its invocation.
- The command contract: inputs, outputs, side effects, and exit behavior.
- The check command and result, or why no safe relevant check was run.
- Portability limits and unresolved material behavior.
