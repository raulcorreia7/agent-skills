# Worktree Providers

The commands below replace the native commands in the operation references.
Keep those references for their checks and verification, and use native Git
for any operation the provider doesn't support. When the result comes from
native Git because a provider was unsuitable, report it as a fallback.

## Worktrunk

Use `wt switch --create`, `wt list`, and `wt remove` for creation, switching,
listing, and cleanup. Remove with `wt remove --no-delete-branch --foreground`
by default.

- Project hooks (pre-switch, pre-start, post-start, post-switch, pre-remove,
  post-remove) run commands from the repository's Worktrunk configuration.
  `--no-hooks` on `wt switch` and `wt remove` skips them.
- `-y`/`--yes` skips every approval prompt, including unapproved hook
  commands.
- Inspect Worktrunk's path configuration before creation, make sure the
  destination is outside the source repository, and report the actual path
  afterwards. Change the path template only on request.
- Use the ignored-file copy step only when the repository selects the files
  explicitly and the filesystem supports the copy-on-write behaviour wanted. A
  copy doesn't save disk space on every filesystem.
- For stale Git registrations, use native `git worktree prune`.

## Simgit

Before the first `sg` command, confirm that `sg --help` names simgit; another
tool, such as ast-grep, can install the same `sg` name. If it doesn't, report
simgit as unavailable.

- Pass `--require-cow` to every `sg worktree add` and `sg worktree run`, so
  the operation fails instead of making a normal checkout.
- Pass an explicit, approved path outside the source repository, not simgit's
  default under `.git/simgit/worktrees/`.
- Use `sg worktree add --require-cow`, `sg worktree list`, and
  `sg worktree remove` to create, inspect, and remove. Use `sg worktree repair`
  and `sg worktree prune` only with the matching checks in `maintain.md`.
- `sg worktree remove --force` and `--delete-branch` need approval.
  `sg worktree prune` needs approval; its `--all` option deletes cached
  baselines. Inspect stale registrations with `git worktree prune -n`.

Pilot: before the first real workload, verify on a disposable worktree its
linked Git registration, edit isolation, cleanup, and physical disk use. Find
out whether ignored, generated, private, or user-owned files are present before
allowing them in an agent worktree. Don't copy or share user-owned files by
default; generated outputs, build products, and mutable caches need explicit
task intent.
