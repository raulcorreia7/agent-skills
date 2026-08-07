# Prune Worktree Records

Dry-run first:

```bash
git worktree prune -n
git worktree prune
```

Prune removes stale administrative records. It is not branch cleanup. Run the
real prune only after review and approval of the dry-run.
