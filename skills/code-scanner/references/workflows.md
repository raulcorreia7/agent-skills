# Workflows

Commands come from `tool-catalog.md`. The repo's own config wins over these
gates, and the user can change any gate for one run.

## Gates

Gates flag what needs a look; they are not pass or fail verdicts.

| Gate | Flag when | Basis |
|---|---|---|
| Cyclomatic complexity | CCN > 20 | ESLint default; golangci-lint suggests 10–20 |
| Function length | > 100 lines | Above ESLint (50) and funlen (60) defaults, for legacy code |
| Duplication | > 3% of changed lines; whole repo is report-only | SonarQube new-code gate |
| Coverage | < 80% of changed lines, or < 60% for the project | SonarQube new-code gate; Google "acceptable" |
| Churn hotspot | Top-10% churned file that also fails the complexity gate | Defined here |
| Vulnerability | HIGH or CRITICAL (CVSS ≥ 7.0) with a fix available | CVSS bands; trivy `--ignore-unfixed` |
| Secret | Any hit that survives a look at the file | gitleaks and trufflehog pattern match; verification only with approval |
| IaC | HIGH or CRITICAL | trivy severity |

Safety-critical code needs stricter gates (CCN ≤ 10, full branch coverage);
use them only when the repo or user says so.

## Report row

Every finding is one row:

| file:line | Metric | Value | Gate | Verify |
|---|---|---|---|---|
| `src/page.tsx:88` | Function length | 245 lines | > 100 | `uvx lizard -w -L 100 src/page.tsx` |
| `pnpm-lock.yaml` | CVE-2026-1234 (lodash) | HIGH, fixed in 4.17.22 | HIGH+ with fix | `trivy fs --scanners vuln --severity HIGH,CRITICAL --ignore-unfixed .` |

A family with no rows gets one line: `clean` or `unmeasured: <reason>`.

## quick

Triage the worst offenders, one command per family:

```sh
uvx lizard -w -C 20 -L 100 -s cyclomatic_complexity . | head -10
git log --since=6.months.ago --name-only --format= | sort | uniq -c | sort -rn | head -10
trivy fs --scanners vuln --severity HIGH,CRITICAL --ignore-unfixed .
gitleaks dir . --no-banner
```

## focused

One family, in depth: run every catalog command for that family, report each
row with its verify command, and name one next measurement or fix owner.

## deep

Every family, with the same row shape, plus a list of unknowns and limits.

## PR or branch

Scan what the change adds, then label each finding `introduced` or
`pre-existing`:

```bash
# BASE overrides the default branch when origin/HEAD is unset.
base_ref=${BASE:-$(git symbolic-ref --quiet --short refs/remotes/origin/HEAD)}
: "${base_ref:?set BASE to the default branch, e.g. BASE=origin/main}"
base=$(git merge-base "$base_ref" HEAD)
mapfile -t files < <(git diff --name-only --diff-filter=AM "$base"...HEAD)

if (( ${#files[@]} )); then
  uvx lizard -w -C 20 -L 100 "${files[@]}"
  npx jscpd "${files[@]}" --min-tokens 50
  semgrep scan --config p/default --metrics=off "${files[@]}"
else
  echo "no added or modified files"
fi
gitleaks git . --log-opts="$base..HEAD" --no-banner
trufflehog git file://. --since-commit "$base" --no-verification --no-update
```

Dependency and IaC scanners read whole lockfiles and configs. Run them on the
repo, then keep only findings in files the change touches.
