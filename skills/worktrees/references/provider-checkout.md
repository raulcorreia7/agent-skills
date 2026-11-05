# Provider Review Checkout

Identify the provider from the request or configured remote before checking its
tooling. If it is ambiguous, ask the user.

Check only the selected CLI. Provider inspection and checkout can require
authentication or network approval. A review checkout is untrusted content:
skip Worktrunk hooks, and treat a checkout that creates a local branch as
approval-gated branch creation.

Use the first route that is available:

1. Worktrunk, when `wt` is installed: `wt switch --no-hooks pr:<N>` for GitHub
   or `wt switch --no-hooks mr:<N>` for GitLab. It creates the worktree at the
   configured path, so check that path is outside the source repository first.
2. The provider CLI's own worktree checkout, from `github.md` or `gitlab.md`.
3. Native fallback: create a clean detached worktree, then run the provider
   checkout inside it.

```bash
git worktree add --detach "<path>" HEAD
git -C "<path>" status --short --branch
```

Report the final path, branch or detached state, tracking state, and cleanup.
If checkout fails, inspect the worktree. Remove it only when clean and within
the approved boundary.
