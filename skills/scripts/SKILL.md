---
name: scripts
description: Builds or explains developer automation. Use when automation is the primary deliverable. Not for linter, hook, or CI gate setup; use `quality-gates`.
---

# Scripts

## Job

Build automation with an explicit command contract and predictable side
effects.

## Steps

1. Inspect existing entrypoints, task runners, manifests, lockfiles, and target
   environments. Define the job, inputs, outputs, side effects, retries, and
   success result. Complete when each is defined or recorded as an assumption.
2. Select the smallest suitable existing platform and read each applicable
   implementation guide:
   - `references/bash.md` for non-trivial Bash or Unix-local orchestration.
   - `references/powershell.md` for PowerShell or Windows automation.
   - `references/python.md` for a Python command-line tool.
   - `references/xonsh.md` for a script that mixes Python logic with
     subprocess orchestration across POSIX and Windows.
   - `references/zx.md` for TypeScript or Node automation that uses or
     evaluates `zx`. For another Node or TypeScript runtime, define its
     invocation, module format, and portability boundary from repository
     evidence instead of `zx` conventions.
   - `references/batch.md` only when `.bat`, `.cmd`, or `cmd.exe`
     compatibility is required.

   Complete when the runner and portability boundary are stated.
3. Implement one entrypoint. Keep load time, discovery, and planning read-only.
   Validate targets before mutation, preview broad changes, and give each side
   effect one visible owner. Read these references only for their branch:
   - `references/cli.md` before implementing a public or team-facing command.
     Define its arguments, validation, streams, exit codes, mutation gates, and
     interrupt behavior.
   - `references/script-pipeline.md` when discovery, planning, execution, and
     verification are distinct stages that need separate review or testing.
   - `references/tooling.md` when deciding where caches, temporary files,
     generated output, reports, or task-runner state belong.
   - `references/sources.yml` only when maintaining or re-verifying this
     skill's external guidance.

   Complete when the entrypoint implements every input, output, side effect,
   and exit behavior defined in step 1.
4. Run the existing aggregate check when available. Otherwise run only
   supported, non-overlapping checks for significant risk: formatting, static
   analysis, strict typing, dependency validation, and focused behavior
   verification. Use the one tool that already owns each job. Complete when
   each selected check passes, or the reason no safe relevant check ran is
   recorded.

## Flow

```text
input ← entrypoints, task runners, manifests, target environments
define contract → select platform → implement one entrypoint
check ← aggregate | supported non-overlapping checks
stop: contract implemented + each check passes or its absence is explained
```

## Guardrails

- Keep secrets out of arguments, logs, generated files, and command history.
- Resolve and validate each write or delete target at the mutation boundary.
- Keep verification read-only. Networked dependency checks are approval-gated;
  automatic audit fixes and dependency upgrades are changes, not checks.
- Keep application behavior changes out of automation work.

## Output

- The script or automation change and its invocation.
- The command contract: inputs, outputs, side effects, and exit behavior.
- The check command and result, or why no safe relevant check was run.
- Portability limits and significant unresolved behavior.
