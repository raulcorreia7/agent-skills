---
name: git
description: "Inspects Git state, drafts Git text, and performs approved repository mutations. Use when a commit, branch, pull request, release, or work-item link is the primary deliverable. Not for worktree management; use `worktrees`."
---

# Git

## Job

Assist with human-owned Git state: inspect safely, draft clear Git text, and
mutate Git only after explicit approval for the exact operation and boundary.

## Modes

| Mode | Use when | Repository state |
| --- | --- | --- |
| `inspect` | The user needs Git facts | Unchanged |
| `draft` | The user needs Git text | Unchanged |
| `mutate` | The user explicitly asks to change Git state | Only the approved change |

## Steps

1. Select the mode; treat an unclear mutation request as `inspect` or `draft`.
   Inspect applicable repository instructions, contribution policy, status,
   relevant diffs, templates, and local naming conventions. Complete when one
   mode is selected and the repository evidence supports the requested action
   or draft.
2. Load only the references for the requested Git artifact, then inspect or
   draft:
   - Read `references/commits.md` for commit messages and breaking-change markers.
   - Read `references/branch-names.md` for branch naming.
   - Read `references/work-item-links.md` for issue and work-item references.
   - Read `references/pull-requests.md` for PR titles, bodies, templates, and
     create or update evidence.
   - Read `references/releases.md` for generated version, changelog, and tag flow.

   Complete when each requested fact or draft is backed by repository evidence
   and follows the loaded reference or the local convention.
3. For a mutation, state the exact action, paths or refs, and intended
   boundary, and obtain approval for that operation. Complete when the user has
   approved this exact operation.
4. Stage explicit paths; use broad staging only when status proves every change
   is in the approved scope. Recheck the staged diff before a commit. Recheck
   destination refs before an amend, tag, push, rebase, reset, squash, or
   force-push. Complete when the checked state matches the approved boundary.

## Flow

```text
input ← request, repository instructions, status, diffs, conventions
select mode → inspect evidence → load artifact reference → inspect or draft
mutate? no → stop with the facts or draft
approved for this exact operation? yes → continue | no → ask, or stop with the draft
stage explicit paths → recheck staged diff or destination refs → run
stop: checked state matches the approved boundary
```

## Guardrails

- Every Git mutation is approval-gated, including local ones such as branch
  creation, staging, and commits. Approval covers one exact operation; get it
  again for each further mutation.
- Keep unrelated files outside staging and mutations.
- Preserve generated release workflows.
- If sensitive data appears, stop the exposure and identify only the affected
  file or field; the output contains no sensitive value.

## Composition

- Create, remove, or clean up worktrees through `worktrees`. This skill keeps
  commit, branch, and remote operations.
- When the user explicitly requests correctness or risk review, compose with
  the manual `review` skill.

## Output

- Drafted text or changed Git state
- Included scope and intentionally untouched files
- Commands and results when the mode ran them
- Approval-gated mutations
