---
name: code-scanner
description: "Manual invocation only. Run scanner checks — complexity, duplication, churn, coverage, dependencies, secrets, SAST — and report thresholded findings. Not audit verdicts or change review."
---

# Code Scanner

## Job

Run scanner checks and report thresholded findings.

## Depth

| Depth | Contract |
|---|---|
| `quick` | Triage the highest-value offenders across families |
| `focused` | Examine one selected family in depth with exact verify commands |
| `deep` | Build a full matrix across all seven families with unknowns and limits |

## Families

| Family | Signal |
|---|---|
| complexity | Functions over the complexity/size gates |
| duplication | Clone blocks over the duplication gate |
| churn | Top-churned files intersecting complexity offenders |
| coverage | Line + branch rates under the coverage gates |
| dependencies | Known vulnerabilities, criticals/highs first |
| secrets | Leaked credentials or tokens |
| SAST/containers | Lint, static-analysis, and image/config findings |

## Steps

1. Resolve depth (default `quick`) and families (default all), then load
   only `references/tool-catalog.md` plus `references/workflows.md`.
   Complete when each in-scope family points at catalog commands.
2. Run those commands: native binary or `uvx`/`npx` first, toolbox image
   for missing binaries, nothing installed into the system. Complete when
   each family has output or a named unmeasured reason.
3. Threshold every result with the workflow gates, flaggable per
   invocation. Complete when each result is flagged or clean.
4. Report rows of file:line, metric value, threshold, and verify command,
   naming unknowns and coverage limits. Complete when each in-scope family
   has a row or a stated limit.
5. Run coverage only after the user confirms the announced command, never
   as a `quick` or `deep` side effect. Complete when coverage is run or
   listed pending.

## Guardrails

- Keep the scan read-only; coverage executes the test suite, so run it only
  after explicit confirmation.
- Use native binaries, `uvx`/`npx`, or the bundled toolbox for missing
  binaries: run the `code-scanner` wrapper, take commands from `help.txt`, build
  its image from `Dockerfile`, and provision pinned binaries with
  `fetch-bin.sh`. Install nothing into the system.
- Treat thresholds as signals, not verdicts.
- Report tool findings, quantitative and qualitative. Send audit verdicts to
  `audit`, change verdicts to `review`, fixes to `code`/`refactor`.

## Composition

- Keep threshold ordering here. Hand fixes to `code`/`refactor`, audit verdicts
  to `audit`, change verdicts to `review`. Use parallel `to-plan` only for a
  requested delegated plan.
- Send verified finding sets to `plan-remediation` when horizon planning or a
  portfolio order is the next deliverable.

## Output

- Depth, families, and evidence limits
- Ranked findings table: file:line, metric value, threshold, verify command
- Unknowns, unmeasured families, and coverage limits
- Single next-measurement or fix owner per finding
