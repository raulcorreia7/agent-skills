# GitLab Review Checkout

Check `command -v glab`. Inspect the merge request first when the project,
source branch, or fork is unclear:

```bash
glab mr view "<number-or-url>"
```

No worktree option for `glab mr checkout` has been verified, so use Worktrunk
(`wt switch --no-hooks mr:<N>`) or the native fallback: run the checkout inside
the detached worktree from `provider-checkout.md`. It creates a local branch.

```bash
cd "<path>"
glab mr checkout "<number-or-url>"
```

Source: [GitLab `glab mr checkout`](https://docs.gitlab.com/cli/mr/checkout/)
