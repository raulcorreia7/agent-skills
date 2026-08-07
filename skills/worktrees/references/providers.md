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
files and the filesystem supports the desired copy-on-write behavior. Do not
assume that a copy saves disk space on every filesystem.

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
