# Tool catalog

Native binary or `uvx`/`npx` first, toolbox image as fallback. Try the
primary; on a missing binary use the image instead of installing anything.
If Docker is also unavailable, report the family as unmeasured with the
exact missing command.

Fallback pattern (native-first default, image fills missing scanners):

```text
docker build -t code-scanner:latest skills/code-scanner
docker run --rm -v /abs/path/to/target:/src:ro code-scanner:latest <scanner-command> /src
```
Transparent wrapper (mounts and appends the target): `skills/code-scanner/code-scanner <path> <scanner-command>`.

The mount always uses an absolute host path with `:ro`.

## Language coverage

| Tool | Languages |
|---|---|
| `lizard` | C/C++, Java, C#, JS/TS, Python, Go, Rust, Ruby, PHP, Swift, Kotlin, and more |
| `jscpd` | 150+ formats, effectively all languages |
| `osv-scanner` | Go, npm, PyPI, crates, RubyGems, Maven, NuGet, Pub, Swift, plus OS packages |
| `semgrep` | 30+ languages, including Python, JS/TS, Go, Java, C/C++, Ruby, PHP, C# |
| `gitleaks`, `trufflehog` | language-blind, all text |
| `trivy` | language-blind deps and OS; config for Docker, Kubernetes, Terraform, CloudFormation |
| `ruff` | Python only |
| `shellcheck` | shell only |
| `gosec` | Go only |
| `git log` | language-blind, churn only |

## Complexity

| Tool | Command |
|---|---|
| `lizard` (primary) | `lizard <target>` |
| language linter (fallback) | the linter already configured for the repo |

## Duplication

| Tool | Command |
|---|---|
| `jscpd` (primary, 5.1.2: `-s, --silent` verified) | `jscpd <target> --silent` |

## Churn

| Tool | Command |
|---|---|
| `git log` (primary) | `git log --numstat --since=6.months.ago -- <paths>` |
| `git log` (primary) | `git log --format=%h\ %ad\ %s --date=short -- <paths>` |

Top-churned files = highest commit count / added+deleted lines.

## Coverage

Run at most the matching manifest command, on confirmation only. If the repo
has no coverage configured, report "no coverage configured" plus the setup
pointer instead of inventing config.

| Ecosystem | Command |
|---|---|
| Python | `coverage run -m pytest && coverage report -m && coverage xml -o coverage.xml` |
| Go | `go test -coverprofile=cover.out ./... && go tool cover -func=cover.out` |
| Rust | `cargo llvm-cov --summary` (fallback `cargo tarpaulin --out Xml`) |
| JS/TS | `npx vitest run --coverage` or `npx c8 <test-command>` where configured |

Report line + branch rates.

## Dependencies

| Tool | Command |
|---|---|
| `osv-scanner` (primary, native if present else toolbox) | `osv-scanner --recursive <dir>` |
| npm (fallback) | `npm audit --json` |
| Python (fallback) | `uvx pip-audit` |
| Rust (fallback) | `cargo audit --json` |

## Secrets

| Tool | Command |
|---|---|
| `gitleaks` (native if present else toolbox) | `gitleaks detect --source <dir>` |
| `trufflehog` (native if present else toolbox) | `trufflehog filesystem <dir>` |

## SAST and quality

| Tool | Command |
|---|---|
| `ruff` | `ruff check <dir>` |
| `shellcheck` | `shellcheck <files>` |
| `hadolint` (native if present else toolbox) | `hadolint <Dockerfile>` |
| `gosec` (native if present else toolbox) | `gosec <dir>` |

## Containers and IaC

| Tool | Command |
|---|---|
| `trivy` (native if present else toolbox) | `trivy fs --severity HIGH,CRITICAL <dir>` |
| `trivy` (native if present else toolbox) | `trivy config <dir>` |

## Experimental accelerators

Corroboration-only: use to corroborate or prioritize tool findings,
never as a sole gate.

- `ripwire <dir> --quality-panel`
- `ripwire <dir> --hotspots`
- `ripwire <dir> --clones`
- `ripwire <dir> --deps`
- `ripwire <dir> --metrics`
- `ripwire <dir> --quality-delta`

No other experimental tools in v1.

Tool homepages: lizard at lizard.ws, jscpd at github.com/kucherenko/jscpd,
osv-scanner at github.com/google/osv-scanner, gitleaks at
github.com/gitleaks/gitleaks, trufflehog at github.com/trufflesecurity/trufflehog,
semgrep at semgrep.dev, trivy at aquasec.github.io/trivy.
