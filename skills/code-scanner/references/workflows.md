# Workflows

Commands live in the sibling `tool-catalog.md`. Every finding row has file:line,
metric value, threshold, and verify command. All gates are flaggable per invocation.

## Gates

| Gate | Value | Source |
|---|---|---|
| Cyclomatic complexity (CCN) | warn at CCN > 15 | lizard documented default (`lizard --help`: `-C/--CCN`, default 15) |
| Function length | lizard warns at length > 1000 (`lizard --help`: `-L/--length`, default 1000); skill fallback flags functions > 80 lines for review | tool default + fallback, marked as such |
| Duplication | gate on the repo's configured `jscpd --threshold`; fallback flags any clone block at default sensitivity or file duplication > 5% | fallback, marked as such (tool source silent on a universal gate) |
| Line coverage | flag at < 80% | fallback from documented industry practice, marked as such |
| Branch coverage | flag at < 70% | fallback from documented industry practice, marked as such |
| Churn hotspot | top-decile churn intersecting a complexity offender | defined here: `git log` top commit count / added+deleted lines ∩ CCN offender |

Where a source is silent, the CCN > 15, function > 80 lines, line < 80% /
branch < 70% fallbacks apply and are marked as such above.

## quick

Triage only. Run: lizard top-10 offenders, git top-churn files,
osv-scanner criticals/highs, gitleaks quick pass. Output is a ranked table
with file:line, metric value, threshold, verify command.

## focused

One selected family deep, including coverage on confirmation: run only that
family's catalog commands, report line + branch rates for coverage, name the
single next measurement or fix owner.

## deep

Full matrix across all seven families with the same per-row shape plus an
explicit unknowns/coverage-limits list. Coverage still requires
confirmation: list its command as pending until confirmed.
