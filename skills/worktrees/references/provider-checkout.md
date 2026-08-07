# Provider Review Checkout

Identify the provider from the request or configured remote before checking its
tooling. If it is ambiguous, ask the user.

Check only the selected CLI. Provider inspection and checkout can require
authentication or network approval.

Create a clean detached worktree before the provider-specific checkout:

```bash
git worktree add --detach "<path>" HEAD
git -C "<path>" status --short --branch
```

Run the selected provider command inside that worktree. Report the final path,
branch or detached state, tracking state, and cleanup. If checkout fails,
inspect the detached worktree. Remove it only when clean and within the approved
boundary.
