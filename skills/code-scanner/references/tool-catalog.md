# Tool catalog

`<skill-root>` is the directory that holds `SKILL.md`. Examples scan `.`; use
the target path instead.

## Runner order

Each example shows the native command. Run it with the first runner that
works:

1. The native binary, when `command -v <tool>` finds it.
2. `uvx` or `npx`, for the Python and Node tools (lizard, jscpd, pip-audit,
   c8). Each downloads a package, so it needs approval.
3. The toolbox image below, for the binaries pinned in `tools.txt` and
   semgrep. Building it pulls layers, so it needs approval.
4. `<skill-root>/fetch-tools <temp-dir> <tool>`, which downloads the pinned,
   checksummed binary into a temporary directory. It needs approval.
5. None of these: report the family as unmeasured, naming the missing command.

Install nothing into the system.

## Toolbox image

The image, built from `<skill-root>/Dockerfile`, holds every binary pinned in
`tools.txt`, plus semgrep, git, ripgrep, and ctags.

```sh
docker build -t code-scanner:latest <skill-root>     # once; pulls layers
<skill-root>/code-scanner . trivy fs                  # scans . mounted at /src
<skill-root>/code-scanner . semgrep scan --config p/default /src/apps
```

- The wrapper mounts the target read-only at `/src` and appends `/src` unless
  an argument already names it.
- Scanner caches persist in the `code-scanner-cache` volume, so the second
  vulnerability scan is fast.
- Write reports on the host: `... --format json > trivy.json`.
- `permission denied ... docker.sock`: the user is not in the `docker` group.
  Ask them to add it; do not use `sudo`.
- A Git worktree's history is outside the mount. Run Git-history scans
  (`gitleaks git`, `trufflehog git`) natively or on the main checkout.

## Reading results

- Ask for JSON, then count and filter with `jq`. Show the user the summary,
  not raw output.
- Treat a hit as a lead: confirm each secret or CVE in the file before you
  report it. Tests, fixtures, and docs often hold fake keys.

## Complexity

| Tool | Covers | Example |
|---|---|---|
| lizard | Most languages | `uvx lizard -w -C 20 -L 100 -s cyclomatic_complexity .` |

`-w` prints only functions over a gate. Fall back to the repo's configured
linter rule when lizard cannot parse the language.

## Duplication

| Tool | Covers | Example |
|---|---|---|
| jscpd | Most languages | `npx jscpd . --min-tokens 50 -i "**/node_modules/**,**/dist/**"` |

Use the repo's jscpd config when one exists. Expect clones in generated files
and per-type schemas; report them as such, not as defects.

## Churn

| Tool | Example |
|---|---|
| git | `git log --since=6.months.ago --name-only --format= -- . \| sort \| uniq -c \| sort -rn \| head` |
| git | `git log --since=6.months.ago --numstat --format= -- <path>` |

A hotspot is a top-churned file that also holds a complexity offender.

## Coverage

Run only after the user confirms the command: it runs the test suite. Use the
repo's own coverage task when one exists. Report line and branch rates.

| Ecosystem | Example |
|---|---|
| Python | `coverage run --branch -m pytest && coverage report -m` |
| Go | `go test -coverprofile=cover.out ./... && go tool cover -func=cover.out` |
| Rust | `cargo llvm-cov --summary-only` |
| JS/TS | `npx vitest run --coverage`, or `npx c8 <test command>` |

When the repo has no coverage setup, report "no coverage configured" instead
of adding one.

## Dependencies

| Tool | Covers | Example |
|---|---|---|
| osv-scanner | Lockfiles of most ecosystems | `osv-scanner scan source -r --format json . > osv.json` |
| trivy | Lockfiles and OS packages | `trivy fs --scanners vuln --severity HIGH,CRITICAL --ignore-unfixed .` |
| npm, pip, cargo | One ecosystem | `npm audit --json`, `uvx pip-audit`, `cargo audit --json` |

A finding is introduced only when the change edits the lockfile that holds the
package.

## Secrets

| Tool | Scans | Example |
|---|---|---|
| gitleaks | Files | `gitleaks dir . --no-banner` |
| gitleaks | Commits | `gitleaks git . --log-opts="$base..HEAD" --no-banner` |
| trufflehog | Files | `trufflehog filesystem . --no-verification --no-update` |
| trufflehog | Commits | `trufflehog git file://. --since-commit "$base" --no-verification --no-update` |

`$base` is the merge base from `workflows.md` › PR or branch. gitleaks matches
patterns offline. trufflehog with `--no-verification` does too and reports
every hit as unverified. Verification sends each candidate secret to its
provider, so run it (drop `--no-verification`, add `--results=verified`)
only with approval. A verified hit is a live credential.

## Static analysis

| Tool | Covers | Example |
|---|---|---|
| semgrep | 30+ languages | `semgrep scan --config p/default --metrics=off --json .` |
| ruff | Python | `ruff check .` |
| shellcheck | Shell | `shellcheck <files>` |
| gosec | Go | `gosec ./...` |
| hadolint | Dockerfiles | `hadolint --failure-threshold warning Dockerfile` |

Add the stack's packs to `p/default` (`--config p/default --config p/python`):

| Stack | Packs |
|---|---|
| TypeScript, JavaScript | `p/typescript`; servers add `p/nodejs` or `p/expressjs` |
| Python | `p/python`; add `p/django` or `p/flask` |
| Go | `p/golang` |
| Java | `p/java` |

`p/react` and `p/nextjs` hold almost no public rules. `--config auto` needs
`--metrics=on`. Every pack downloads rules.

## Containers and IaC

| Tool | Covers | Example |
|---|---|---|
| trivy | Dockerfile, Kubernetes, Terraform, CloudFormation, Helm | `trivy config --severity HIGH,CRITICAL .` |
| trivy | Images | `trivy image --severity HIGH,CRITICAL <image>` |

## Experimental

ripwire only corroborates or ranks findings from the tools above; never gate
on it alone.

```sh
ripwire . --quality-panel   # also: --hotspots --clones --deps --metrics --quality-delta
```
