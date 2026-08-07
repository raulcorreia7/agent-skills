# GitHub Review Checkout

Check `command -v gh`, then inspect the pull request before checkout when fork
ownership or branch naming matters:

```bash
gh pr view "<number-or-url>" --json headRefName,headRepositoryOwner,baseRefName
cd "<path>"
gh pr checkout "<number-or-url>"
```

Source: [GitHub `gh pr checkout`](https://cli.github.com/manual/gh_pr_checkout)
