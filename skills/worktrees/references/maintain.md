# Maintain, Remove, and Prune Worktrees

Prefer porcelain output when parsing.

## Inspect and maintain

```bash
git worktree list --porcelain
git -C "<worktree-path>" status --short --branch
git worktree move "<old-path>" "<new-path>"
git worktree repair "<path>"
git worktree lock --reason "<reason>" "<path>"
git worktree unlock "<path>"
```

Use `move` rather than moving the directory by hand, and `repair` after an
unavoidable manual move. Lock a worktree on a removable drive or network
mount, or one that must not be pruned.

## Remove

Inspect the target, then remove it:

```bash
git -C "<worktree-path>" status --short --branch
git worktree remove "<worktree-path>"
```

Stop when the worktree is dirty. `--force` discards its changes, so use it only
once the data at risk is known and approved.

## Prune

Prune removes stale administrative records; it is not branch cleanup. Dry-run
first, and run the real prune only after the user approves that output:

```bash
git worktree prune -n
git worktree prune
```

Worktrunk's `wt step prune` removes merged worktrees and their branches and
runs their remove hooks. Preview it with `wt step prune --dry-run`; the real
run needs approval of that preview.

## Configuration

Change these only on request:

- `worktree.guessRemote=true` infers a unique matching remote branch.
- `worktree.useRelativePaths=true` helps when the main repository and all
  worktrees move together, if every Git version in use supports it.

Read the current repository-local value before changing it:

```bash
git config --local --get worktree.guessRemote
git config --local worktree.guessRemote true
```
