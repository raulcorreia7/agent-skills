# GitLab Review Checkout

Check `command -v glab`. Inspect the merge request first when the project,
source branch, or fork is unclear:

```bash
glab mr view "<number-or-url>"
cd "<path>"
glab mr checkout "<number-or-url>"
```

Source: [GitLab `glab mr checkout`](https://docs.gitlab.com/cli/mr/checkout/)
