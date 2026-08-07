# Worktree Configuration

- `worktree.guessRemote=true` can infer a unique matching remote branch.
- `worktree.useRelativePaths=true` can help when the main repository and all
  worktrees move together, provided every Git version in use supports it.

Do not change Git configuration without explicit user intent.

After approval, inspect the current repository-local value before changing it:

```bash
git config --local --get worktree.guessRemote
git config --local worktree.guessRemote true
```
