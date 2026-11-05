# Review Checkout

Check out a pull request (GitHub) or merge request (GitLab) into its own
worktree. Identify the provider from the request or the configured remote, and
ask when it's ambiguous. Check only that provider's CLI (`command -v gh` or
`command -v glab`). Inspection and checkout can need authentication and the
network.

Use the first route that's available:

1. Worktrunk, when `wt` is installed: `wt switch --no-hooks pr:<N>` for
   GitHub or `wt switch --no-hooks mr:<N>` for GitLab. It creates the worktree
   at its configured path, so check first that the path is outside the source
   repository.
2. The provider CLI's own worktree checkout (GitHub only; see below).
3. Native fallback: create a clean detached worktree, then run the provider
   checkout inside it.

```bash
git worktree add --detach "<path>" HEAD
git -C "<path>" status --short --branch
```

If the checkout fails, inspect the worktree. Remove it only when it's clean
and inside the approved boundary.

## GitHub

Inspect the pull request first when fork ownership or branch naming matters:

```bash
gh pr view "<number-or-url>" --json headRefName,headRepositoryOwner,baseRefName
```

Check out into a new worktree outside the source repository. This creates a
local branch named after the head branch unless `--branch` names another:

```bash
gh pr checkout "<number-or-url>" --worktree "<path>"
```

For the native fallback, run `gh pr checkout "<number-or-url>"` inside the
detached worktree.

Source: [GitHub `gh pr checkout`](https://cli.github.com/manual/gh_pr_checkout)

## GitLab

Inspect the merge request first when the project, source branch, or fork is
unclear:

```bash
glab mr view "<number-or-url>"
```

No worktree option for `glab mr checkout` has been verified, so use Worktrunk
or the native fallback. The checkout creates a local branch.

```bash
cd "<path>"
glab mr checkout "<number-or-url>"
```

Source: [GitLab `glab mr checkout`](https://docs.gitlab.com/cli/mr/checkout/)
