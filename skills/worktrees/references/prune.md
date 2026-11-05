# Prune Worktree Records

Dry-run first:

```bash
git worktree prune -n
git worktree prune
```

Prune removes stale administrative records. It is not branch cleanup. Run the
real prune only after review and approval of the dry-run.

With Worktrunk, preview merged-worktree and branch cleanup with
`wt step prune --dry-run`. The real `wt step prune` deletes branches, so it
needs separate approval of that preview.
