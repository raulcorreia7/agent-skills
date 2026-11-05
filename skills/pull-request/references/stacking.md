# Splitting and Stacking

Use this when a branch holds more than one intent, or one intent too large to
review in one sitting. All commands are plain Git and run through `git`; each
branch creation, rebase, and push is approval-gated.

## Split or stack

- Split into independent PRs when the parts don't depend on each other. Each
  one targets the main branch and can merge in any order.
- Stack when a later part needs an earlier one. Each PR in the stack holds one
  intent and targets the branch of the PR below it.
- Order the stack so each PR builds and passes its checks on its own:
  refactors and groundwork first, behaviour changes after, cleanup last.

## Base chaining

```text
main ← part-1 ← part-2 ← part-3
```

- `part-1` targets `main`; `part-2` targets `part-1`; `part-3` targets
  `part-2`. Each PR's diff then shows only its own commits.
- Say in each description that it is stacked, which PR it depends on, and
  which PR depends on it. A template section for stacks uses `Not stacked`
  when the PR stands alone.
- Open the lower PRs as ready and the upper ones as drafts when the team
  reviews bottom-up.

## After a parent merges

1. Update the local main branch.
2. Rebase the next branch onto main, dropping the commits that already merged:

   ```bash
   git rebase --onto main part-1 part-2
   ```

   With a squash merge, `part-1`'s original commits are not on main, so
   `--onto` is what drops them.
3. Retarget the child PR's base to main with the provider's edit command
   (`providers.md`).
4. Push the rebased branch with `--force-with-lease`.
5. Repeat for each branch higher in the stack, rebasing each onto its new
   parent in order from the bottom up.

## Changes lower in the stack

When review asks for a change in `part-1`, commit it there, then rebase each
higher branch onto its updated parent, bottom up, and push each with
`--force-with-lease`. Recheck each PR's diff afterwards; a conflict resolved
during a rebase is new code the reviewer has not seen.
