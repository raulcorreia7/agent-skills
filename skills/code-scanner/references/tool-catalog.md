# Tool catalog

`<skill-root>` is the directory that holds `SKILL.md`. `bounded` means
`<skill-root>/scripts/bounded`, and `$tree` is a `scripts/clean-tree` export of
the target (see Resource limits). Every command runs through `bounded` or the
toolbox.
Commands that read Git history or a short list of changed files run on the
repository instead of `$tree`.

## Contents

- Runner order
- Toolbox image
- Installing locally
- Resource limits
- Reading results
- Complexity, Duplication, Churn, Coverage
- Dependencies, Secrets, Static analysis, Containers and IaC
- Experimental

## Runner order

Each example shows the native command. Run it with the first runner that
works:

1. The native binary, when `command -v <tool>` finds it.
2. `uvx` or `npx`, for the Python and Node tools (lizard, jscpd, pip-audit,
   c8). Each downloads a package, so it needs approval.
3. The toolbox image below, for every scanner the Dockerfile pins. Building
   it pulls layers, so it needs approval.
4. None of these: report the family as unmeasured, naming the missing command
   and pointing the user to Installing locally.

Install nothing into the system.

## Toolbox image

The image, built from `<skill-root>/Dockerfile`, holds every scanner below
plus git, ripgrep, and ctags. The Dockerfile is the one place versions are
pinned: an `ARG <TOOL>_VERSION` and `ARG <TOOL>_SHA256` pair per binary, and
`ADD --checksum` rejects a download whose hash differs.

```sh
# once; pulls layers. A builder limited to two build steps at a time:
cfg="${TMPDIR:-/tmp}/code-scanner-buildkitd.toml"
printf '[worker.oci]\n  max-parallelism = 2\n' > "$cfg"
docker buildx inspect code-scanner-builder >/dev/null 2>&1 ||
  docker buildx create --name code-scanner-builder --driver docker-container \
    --buildkitd-config "$cfg"
docker buildx build --builder code-scanner-builder --load -t code-scanner:latest <skill-root>
<skill-root>/scripts/code-scanner "$tree" trivy fs --parallel 2   # scans $tree mounted at /src
<skill-root>/scripts/code-scanner "$tree" semgrep scan --jobs 2 --max-memory 1500 --config p/default /src
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

## Installing locally

The skill installs nothing. A user who wants native binaries installs them
from each project's own instructions, at the version the Dockerfile pins:

| Tool | Install instructions |
|---|---|
| osv-scanner | <https://google.github.io/osv-scanner/installation/> |
| trivy | <https://trivy.dev/docs/latest/getting-started/installation/> |
| gitleaks | <https://github.com/gitleaks/gitleaks#installing> |
| trufflehog | <https://github.com/trufflesecurity/trufflehog#floppy_disk-installation> |
| hadolint | <https://github.com/hadolint/hadolint#install> |
| gosec | <https://github.com/securego/gosec#installation> |
| semgrep | <https://semgrep.dev/docs/getting-started/cli> |
| lizard, jscpd, c8, pip-audit | Run through `uvx` or `npx`; nothing to install |

## Resource limits

Scanners walk every file under the target and some start one worker per CPU.
On a working checkout that is millions of files (`node_modules`, build output,
nested worktrees under `.claude/worktrees/`) against a few thousand tracked
ones, which can exhaust memory and freeze the machine. These rules are on by
default:

1. **Scan a clean tree.** `tree=$(<skill-root>/scripts/clean-tree <repo> [ref] [path...])`
   exports only tracked files. Scan `$tree`, then `rm -rf "$tree"`. It leaves
   out uncommitted changes and submodule contents: commit first, or scan the
   checkout with `--skip-dirs`/`-i` excludes for `node_modules`, `dist` and
   `.claude`; report submodules as unscanned. History scans (`gitleaks git`,
   `trufflehog git`) run on the real repository.
2. **Run every native, `uvx` or `npx` command through
   `<skill-root>/scripts/bounded`.** It runs the command in a systemd user scope with a
   soft memory ceiling (`MemoryHigh`, default 25% of RAM: the kernel throttles
   and swaps instead of killing), a hard backstop (`MemoryMax`, default 50% of
   RAM), and a low CPU weight that still uses idle cores at full speed.
   Without systemd user scopes it refuses to run: use the toolbox, whose
   wrapper `code-scanner` applies the container equivalent.
3. **One scanner at a time, one project at a time.** In a monorepo, scan one
   project directory per run, never the root with every family in parallel.
   Run moon with `--concurrency 2`.
4. **Cap each tool's own parallelism**, as the commands below do: semgrep
   `--jobs 2 --max-memory 1500`, trivy `--parallel 2`, trufflehog
   `--concurrency 2`.

Raise the ceilings for one run when a scan needs more:
`CODE_SCANNER_MEM_SOFT` (`bounded` only), `CODE_SCANNER_MEM_HARD`, and
`CODE_SCANNER_SWAP`, as a size such as `8G` (`bounded` also takes `60%`). Lift all limits with `CODE_SCANNER_FORCE=1` only when the user
explicitly asks to force it.

A machine without an OOM daemon freezes under memory pressure instead of
killing the culprit. Desktop Ubuntu and Fedora enable `systemd-oomd` for this.
When `systemctl is-active systemd-oomd earlyoom` reports both inactive, tell
the user and offer `sudo systemctl enable --now systemd-oomd`; do not run it.

A true soft ceiling for the toolbox needs a systemd slice, which takes sudo
once. Offer it; do not run it:

```sh
sudo systemctl set-property --runtime code-scanner.slice MemoryHigh=4G MemoryMax=8G CPUWeight=20
export CODE_SCANNER_CGROUP_PARENT=code-scanner.slice
```

## Reading results

- Ask for JSON, then count and filter with `jq`. Show the user the summary,
  not raw output.
- Treat a hit as a lead: confirm each secret or CVE in the file before you
  report it. Tests, fixtures, and docs often hold fake keys.

## Complexity

| Tool | Covers | Example |
|---|---|---|
| lizard | Most languages | `bounded uvx lizard -w -C 20 -L 100 -s cyclomatic_complexity "$tree"` |

`-w` prints only functions over a gate. Fall back to the repo's configured
linter rule when lizard cannot parse the language.

## Duplication

| Tool | Covers | Example |
|---|---|---|
| jscpd | Most languages | `bounded npx jscpd "$tree" --min-tokens 50 -i "**/node_modules/**,**/dist/**,**/coverage/**"` |

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
| Python | `bounded coverage run --branch -m pytest && coverage report -m` |
| Go | `bounded go test -p 2 -coverprofile=cover.out ./... && go tool cover -func=cover.out` |
| Rust | `bounded cargo llvm-cov --summary-only -j 2` |
| JS/TS | `bounded npx vitest run --coverage --maxWorkers=2`, or `bounded npx c8 <test command>` |

When the repo has no coverage setup, report "no coverage configured" instead
of adding one.

## Dependencies

| Tool | Covers | Example |
|---|---|---|
| osv-scanner | Lockfiles of most ecosystems | `bounded osv-scanner scan source -r --format json "$tree" > osv.json` (skips gitignored paths by default) |
| trivy | Lockfiles and OS packages | `bounded trivy fs --parallel 2 --skip-dirs '**/node_modules' --skip-dirs '**/dist' --scanners vuln --severity HIGH,CRITICAL --ignore-unfixed "$tree"` |
| npm, pip, cargo | One ecosystem | `bounded npm audit --json`, `bounded uvx pip-audit`, `bounded cargo audit --json` |

A finding is introduced only when the change edits the lockfile that holds the
package.

## Secrets

| Tool | Scans | Example |
|---|---|---|
| gitleaks | Files | `bounded gitleaks dir "$tree" --max-target-megabytes 5 --no-banner` |
| gitleaks | Commits | `bounded gitleaks git . --log-opts="$base..HEAD" --no-banner` |
| trufflehog | Files | `bounded trufflehog filesystem "$tree" --concurrency 2 --no-verification --no-update` |
| trufflehog | Commits | `bounded trufflehog git file://. --since-commit "$base" --concurrency 2 --no-verification --no-update` |

`$base` is the merge base from `workflows.md` › PR or branch. gitleaks matches
patterns offline. trufflehog with `--no-verification` does too and reports
every hit as unverified. Verification sends each candidate secret to its
provider, so run it (drop `--no-verification`, add `--results=verified`)
only with approval. A verified hit is a live credential.

## Static analysis

| Tool | Covers | Example |
|---|---|---|
| semgrep | 30+ languages | `bounded semgrep scan --jobs 2 --max-memory 1500 --config p/default --metrics=off --json "$tree"` |
| ruff | Python | `bounded ruff check "$tree"` |
| shellcheck | Shell | `bounded shellcheck <files>` |
| gosec | Go | `bounded gosec ./...` (run from `$tree`) |
| hadolint | Dockerfiles | `bounded hadolint --failure-threshold warning Dockerfile` |

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
| trivy | Dockerfile, Kubernetes, Terraform, CloudFormation, Helm | `bounded trivy config --severity HIGH,CRITICAL "$tree"` |
| trivy | Images | `bounded trivy image --parallel 2 --severity HIGH,CRITICAL <image>` |

## Experimental

ripwire only corroborates or ranks findings from the tools above; never gate
on it alone.

```sh
bounded ripwire . --quality-panel   # also: --hotspots --clones --deps --metrics --quality-delta
```
