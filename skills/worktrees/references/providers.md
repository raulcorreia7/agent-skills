# Worktree Providers

Select by request: use Worktrunk by default; use simgit only for an explicit
copy-on-write or low-disk request after its pilot passes; use native Git only
as the fallback. Keep the native Git preflight and the skill's path and cleanup
guardrails for every provider.

For the operations below, these provider commands replace the native commands
in the operation references. Read those references for their guardrails and
verification. Use native Git when the selected provider does not support an
operation.

## Worktrunk

Use Worktrunk for normal agent and human worktree workflows when `wt` is
available. It is the primary provider for creation, switching, launch, and
cleanup. Use `wt switch --create`, `wt list`, and `wt remove` for the matching
operations.

Use `wt remove --no-delete-branch --foreground` by default. Get approval before
you use `--clobber`, `--force`, `-D`, or `--reap`.

Inspect Worktrunk's path configuration before creation. Ensure its destination
is outside the source repository, report the actual path after creation, and do
not change the template unless the user requests that configuration.

Use its ignored-file copy step only when the repository explicitly selects the
files and the filesystem supports the desired copy-on-write behavior.

### Bootstrap rules

Apply these when a repository prepares new worktrees through hooks.

- Pass `--config <file>` to every `wt` call inside a hook. The flag sets the
  config path for the invoking process only, so a nested `wt step ...` reads the
  default user config and silently ignores your exclude list. Keep shared
  settings in the project config, which every process in the repository reads,
  or export `WORKTRUNK_CONFIG_PATH`, which hook children inherit.
- Exclude patterns match one ignored entry at a time, with no parent
  propagation: `dir/` excludes the `dir` entry, while `dir/*` covers the entries
  inside a partly tracked directory. Check the result with
  `wt step copy-ignored --dry-run` from a worktree.
- Table keys in a hook run concurrently, and a failed step aborts the rest of
  the pipeline. Keep ordered steps in one string hook or in `[[hook]]` pipeline
  blocks, make every step idempotent, and guard best-effort steps so a failed
  copy cannot skip an essential later step.
- Never copy a directory another process is writing: a source file that vanishes
  mid-copy aborts the copy.
- Prefer the filesystem's own copy-on-write for large trees (reflink on btrfs
  and XFS, clone on APFS, block clone on ReFS), and verify it with a probe copy
  (GNU `cp --reflink=always`, macOS `cp -c`) before relying on it. Without it,
  link large read-only assets where the platform permits (Windows symlinks can
  need Developer Mode, otherwise copy them) and skip regenerable caches when a
  cold rebuild is cheap.
- Never hardlink build outputs: compilers rewrite files in place and would
  corrupt the primary checkout.
- Link only ignored paths (`git check-ignore`) so tracked files stay real, and
  test the existing link target first to keep the step idempotent.
- A copied virtual environment or runtime can still resolve absolute paths to
  the primary checkout: run project code against the worktree instead, or
  reinstall dependencies in place.
- Call `command wt` from scripts and agents in POSIX shells; the shell wrapper
  changes the caller's directory.
- Diagnose hook failures from Worktrunk's command log at
  `<git-common-dir>/wt/logs/commands.jsonl`, which records each hook command
  with its exit status.
- Plain `git worktree` covers the essentials portably: tracked files only, so a
  new worktree is already minimal, plus bootstrap from a `post-checkout` hook,
  which `git worktree add` fires with a null old ref, or from a small POSIX
  setup script (Git for Windows runs it through its bundled `sh`). Worktrunk
  adds the ignored-file copy, declarative lifecycle hooks, and the
  `list`/`merge`/`remove` UX.

Use native `git worktree prune` for stale Git registrations. Use
`wt step prune` only after explicit approval because it removes merged
worktrees and branches.

## Simgit

Use simgit when the request requires low disk use through copy-on-write and a
disposable pilot has passed for the current filesystem and repository shape.
Pass `--require-cow` to every `sg worktree add` or `sg worktree run` command so
the operation fails instead of creating a normal checkout.

Pass an explicit approved path outside the source repository. Do not use
simgit's default path under `.git/simgit/worktrees/`.

Use `sg worktree add --require-cow`, `sg worktree list`, and `sg worktree
remove` for creation, inspection, and removal. Use `sg worktree repair` or
`sg worktree prune` only with the matching maintenance or prune guardrails.

Get approval before you use `sg worktree remove --force` or `--delete-branch`.
Use native `git worktree prune -n` to inspect stale registrations. Get approval
before `sg worktree prune`; its `--all` option deletes cached baselines.

Before the first real workload, verify a disposable worktree's linked Git
registration, edit isolation, cleanup, and physical disk use. Resolve whether
ignored, generated, private, or user-owned files are present before allowing
them in an agent worktree.

Do not copy or share user-owned files by default. Treat generated outputs,
build products, and mutable caches as repository-specific state that needs
explicit task intent.

## Native Git

Use native `git worktree` when Worktrunk is unavailable or unsuitable and
simgit cannot provide the requested copy-on-write behavior. Report that the
result is a compatibility fallback.
