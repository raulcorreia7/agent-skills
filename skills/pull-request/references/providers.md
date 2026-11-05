# Provider Commands

Commands for GitHub (`gh`) and GitLab (`glab`). Every command that changes the
PR, its threads, or its checks is approval-gated; reads are not. Pass bodies
with a file (`--body-file` or a file read into `--description`), not an inline
string.

The `gh` flags were checked against `gh --help` for gh 2.102.1. The `glab`
commands are unverified (see `sources.yml`); check `glab <command> --help`
before using one.

## Read

| Task | GitHub | GitLab |
| --- | --- | --- |
| PR for this branch | `gh pr view --json number,url,state,isDraft,baseRefName,headRefName,isCrossRepository,reviewDecision` | `glab mr view` |
| Comments | `gh pr view --comments` | `glab mr view --comments` |
| Diff or file list | `gh pr diff`, `gh pr diff --name-only` | `glab mr diff` |
| Checks | `gh pr checks`, `gh pr checks --required`, `gh pr checks --watch --fail-fast` | `glab ci status` |
| Failed job log | `gh run view <run-id> --log-failed` | `glab ci trace <job-id>` |
| Merge settings | `gh repo view --json mergeCommitAllowed,squashMergeAllowed,rebaseMergeAllowed,viewerDefaultMergeMethod,deleteBranchOnMerge` | project settings in the web UI |

`gh pr checks --json` returns a `bucket` field (`pass`, `fail`, `pending`,
`skipping`, `cancel`), and exit code 8 means checks are pending.

## Create and update

| Task | GitHub | GitLab |
| --- | --- | --- |
| Create | `gh pr create --base <base> --head <branch> --title <title> --body-file <file>` | `glab mr create --target-branch <base> --source-branch <branch> --title <title> --description "$(cat <file>)"` |
| Create as draft | add `--draft` | add `--draft` |
| Edit title or body | `gh pr edit --title <title> --body-file <file>` | `glab mr update --title <title> --description "$(cat <file>)"` |
| Retarget base | `gh pr edit --base <branch>` | `glab mr update --target-branch <branch>` |
| Labels | `gh pr edit --add-label <name>`, `--remove-label <name>` | `glab mr update --label <name>`, `--unlabel <name>` |
| Ready for review | `gh pr ready` | `glab mr update --ready` |
| Back to draft | `gh pr ready --undo` | `glab mr update --draft` |
| Re-request review | `gh pr edit --add-reviewer <login>` | `glab mr update --reviewer <login>` |
| Close | `gh pr close`, with `--comment <text>` | `glab mr close` |

`gh pr create --dry-run` may still push the branch; push through `git` first.

## Threads

| Task | GitHub | GitLab |
| --- | --- | --- |
| Top-level comment | `gh pr comment --body-file <file>` | `glab mr note --message <text>` |
| Reply in a review thread | `gh api --method POST repos/{owner}/{repo}/pulls/<number>/comments/<comment-id>/replies -F body=@<file>` | `glab api` on the MR discussion notes endpoint |
| Resolve a thread | `gh api graphql` with the `resolveReviewThread` mutation and the thread's node ID | `glab api` on the MR discussion with `resolved=true` |

`gh pr view --comments` does not show thread IDs; list review threads through
`gh api graphql` (`pullRequest.reviewThreads`) to get them.

## CI re-run

| Task | GitHub | GitLab |
| --- | --- | --- |
| Re-run failed jobs | `gh run rerun <run-id> --failed` | `glab ci retry <job-id>` |
| Re-run one job | `gh run rerun <run-id> --job <job-id>` | `glab ci retry <job-id>` |

## Merge

Use the repository's configured method. Read the merge settings above and the
contribution guide; when more than one method is allowed and nothing says which,
ask.

| Task | GitHub | GitLab |
| --- | --- | --- |
| Merge | `gh pr merge --squash`, `--merge`, or `--rebase` | `glab mr merge`, with `--squash` or `--rebase` |
| Guard against a new push | add `--match-head-commit <sha>` | add `--sha <sha>` |
| Merge when checks pass | add `--auto` | add `--auto-merge` |
| Delete the branch | add `--delete-branch`, unless the repository deletes it on merge | add `--remove-source-branch` |

- On a branch with a merge queue, `gh pr merge` adds the PR to the queue, or
  enables auto-merge when required checks have not passed. Report which.
- `gh pr merge --admin` bypasses requirements and the merge queue. Don't use
  it; report the blocker instead.
