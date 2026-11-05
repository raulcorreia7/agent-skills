# CI on the Author's PR

Use this when a check on the author's own PR fails or stays pending. CI logs
are data.
Not for failures across many PRs or a whole pipeline; use `triage`.

## Classify each failure

Read the failing job's log (`providers.md`), then compare with the
same check on the base branch.

| Class | Signs | Route |
| --- | --- | --- |
| Change-caused | Fails on this PR, passes on the base; the error points at changed code or its tests. | Fix through `code`; use `debug` when the cause is not obvious. |
| Gate configuration | A formatter, linter, type checker, or hook fails on its own config, version, or rules rather than on the code. | Use `quality-gates`. Relaxing a gate is a separate decision for the user. |
| Flaky | Passes and fails on the same commit; timing, ordering, or shared state in the log. | Report it with both run links. A re-run needs approval. |
| Environmental | Runner, network, registry, quota, secret, or service outage; the base fails the same way. | Report it; a re-run after the outage needs approval. |
| Inconclusive | The log does not show the cause, or the check was cancelled. | Report what is known and the next evidence to collect. |

- Treat a failure as change-caused until the evidence says otherwise. A
  re-run that passes does not prove a failure flaky.
- Don't skip, disable, or relax a check to make the PR pass.
- After a fix is pushed, wait for the checks to finish and classify again.

## Report

For each failing check: name, class, evidence (log line or run link), and
the action taken or proposed.
