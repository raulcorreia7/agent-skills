# Remove A Worktree

Inspect the target before removal:

```bash
git -C "<worktree-path>" status --short --branch
git worktree remove "<worktree-path>"
```

Stop when the worktree is dirty. Use `--force` only after explicit approval and
only when the data-loss boundary is understood. Branch deletion is a separate
operation and is never implied by worktree removal.
