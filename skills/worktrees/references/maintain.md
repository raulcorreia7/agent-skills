# Inspect And Maintain A Worktree

```bash
git worktree list --porcelain
git -C "<worktree-path>" status --short --branch
git worktree move "<old-path>" "<new-path>"
git worktree repair "<path>"
git worktree lock --reason "<reason>" "<path>"
git worktree unlock "<path>"
```

Use `move` instead of a manual directory move. Use `repair` after an
unavoidable manual move. Locks are useful for removable drives, network mounts,
or worktrees that must not be pruned.
