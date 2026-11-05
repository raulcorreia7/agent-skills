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

## Steps

1. Resolve depth (default `quick`) and families (default all), then load
   only `references/tool-catalog.md` plus `references/workflows.md`.
   Complete when each in-scope family points at catalog commands.
2. Run those commands: native binary or `uvx`/`npx` first, toolbox image
   for missing binaries, nothing installed into the system. Complete when
   each family has output or a named unmeasured reason.
3. Threshold every result with the workflow gates, flaggable per
   invocation. Complete when each result is flagged or clean.
4. Run coverage only after the user confirms the announced command, never
   as a `quick` or `deep` side effect. Complete when coverage is run or
   listed pending.
5. Report rows of file:line, metric value, threshold, and verify command,
   naming unknowns and coverage limits. Complete when each in-scope family
   has a row or a stated limit, and unconfirmed coverage is marked pending.

## Flow

```text
for family in families except coverage:
    command ← native | uvx/npx | toolbox
    result ← run → flag against the gate
coverage → only after the user confirms the announced command | pending
report ← file:line, metric, threshold, verify command | unmeasured reason | coverage pending
```

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

## Guardrails

- Keep the scan read-only; coverage executes the test suite, so run it only
  after explicit confirmation.
- Get approval before network access: `uvx`/`npx` downloads, dependency and
  CVE lookups, registry rule sets such as `semgrep --config auto`, image
  builds that pull layers, and trufflehog secret verification, which sends
  candidate secrets to their providers. Run trufflehog with
  `--no-verification` otherwise.
- Install nothing into the system. Fill a missing binary with `uvx`/`npx`,
  the toolbox image (`Dockerfile`, `code-scanner` wrapper), or `fetch-tools`,
  in the catalog's runner order.
- Treat thresholds as signals, not verdicts.
- Report tool findings, quantitative and qualitative.

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
