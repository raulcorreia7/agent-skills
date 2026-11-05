# GitHub Review Checkout

Check `command -v gh`, then inspect the pull request before checkout when fork
ownership or branch naming matters:

```bash
gh pr view "<number-or-url>" --json headRefName,headRepositoryOwner,baseRefName
```

Without Worktrunk, check out into a new worktree outside the source
repository. This creates a local branch named after the head branch unless
`--branch` names another:

```bash
gh pr checkout "<number-or-url>" --worktree "<path>"
```

For the native fallback, run `gh pr checkout "<number-or-url>"` inside the
detached worktree from `provider-checkout.md`.

Source: [GitHub `gh pr checkout`](https://cli.github.com/manual/gh_pr_checkout)
