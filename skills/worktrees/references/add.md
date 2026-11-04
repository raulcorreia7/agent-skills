# Add A Worktree

Resolve the repository name, base ref, branch, and destination explicitly.
Inspect remotes when `origin/HEAD` is missing. Use the current `HEAD` only after
you state that assumption.

Default native Git and simgit destination:

```text
../<repo-name>-worktrees/<branch-slug>
```

Build the branch slug: lowercase the branch, replace separators and unsafe path
characters with `-`, collapse repeated `-`, and trim edges. Reject an empty
slug, `.`, or `..`.

Create a branch from an explicit base:

```bash
git worktree add -b "<branch>" "<path>" "<base-ref>"
```

Adopt an existing local branch:

```bash
git worktree add "<path>" "<branch>"
```

Track an existing remote branch:

```bash
git worktree add --track -b "<local-branch>" "<path>" "<remote>/<branch>"
```

Create a detached review worktree:

```bash
git worktree add --detach "<path>" "<commit-ish>"
```

If Git reports that a branch is already checked out, locate and reuse that
worktree. Do not bypass the check with force flags.
