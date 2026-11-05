---
name: worktrees
description: Manual invocation only. Safe Git worktree management and provider review checkout.
---

# Worktrees

## Job

Run predictable Git worktree workflows with explicit paths, provider selection,
preflight checks, and cleanup guardrails. This skill resolves existing refs
directly.
Not for commits, pushes, or branch, PR, release, or work-item text; use `git`.

## Steps

1. Resolve the requested action, repository root, branch or ref, base ref,
   target path, provider, and approval boundary. Run the common preflight:
   inspect `git status --short --branch` and `git worktree list --porcelain`,
   and check whether the requested branch, ref, or path already exists.
   Complete when each of those inputs is known or stated as an assumption.
2. Select the provider: Worktrunk unless the request explicitly requires
   copy-on-write; simgit for copy-on-write after its pilot passes; native Git
   only when the selected provider is unsuitable. Then load only the references
   for the selected operation:
   - Read `references/providers.md` for Worktrunk, simgit, or a copy-on-write
     request, and use its provider commands. Read the native operation
     references for their guardrails and verification only.
   - Read `references/add.md` to create, adopt, track, or detach a worktree.
   - Read `references/maintain.md` to inspect, move, repair, lock, or unlock one.
   - Read `references/remove.md` to remove a worktree.
   - Read `references/prune.md` to inspect or prune stale administrative records.
   - Read `references/configuration.md` only when the user explicitly requests
     worktree configuration.
   - For a provider review checkout, read `references/provider-checkout.md` and
     exactly one of `references/github.md` or `references/gitlab.md`.
   - Read `references/sources.yml` only to audit or re-verify this
     skill's sources.

   Complete when one provider is selected and its fallback state is known.
3. List the gated actions the selected operation needs (see Guardrails),
   including branch creation and running Worktrunk project hooks, and get
   approval for each exact operation before running it. Without approval, use
   the ungated form (`--detach`, `--no-hooks`) or stop with the planned
   commands. Complete when every gated action is approved or replaced.
4. Run only the selected operation and its necessary preflight. Complete when
   the final path, branch or detached state, tracking state, and cleanup state
   are known.

## Flow

```text
input ← action, repository, ref, path, provider, approval boundary
preflight → select provider → load operation references
gated flag or action? yes → approved? yes → continue | no → ungated form or stop
run operation → verify
stop: final path, ref state, tracking, and cleanup state are known
```

## Guardrails

- Report a fallback from a requested copy-on-write workflow before you create
  the worktree, and treat Worktrunk's ignored-file copies as full copies unless
  the filesystem is verified to share blocks.
- Do not use broad ignored-file cleanup such as `git clean -ffdx` while managed
  worktrees exist. Remove the selected worktree through Git instead.
- Keep worktrees outside `/tmp`, `.tmp`, and the source repository.
- Preserve Git configuration unless the user explicitly requests a change.
- Obtain explicit approval for `--clobber`, `--force`, `-B`, `-D`, real prune,
  branch deletion, process reaping, and network fetches. Branch deletion is
  always a separate action.
- Branch creation is approval-gated like any Git mutation:
  `git worktree add -b`, `wt switch --create`, and a provider checkout that
  creates a local branch (`wt switch pr:N`, `gh pr checkout`,
  `glab mr checkout`).
- Worktrunk project hooks are executable repository content. Pass
  `--no-hooks` for an untrusted checkout, including any pull or merge request,
  and run hooks only after approval. Never pass `-y`/`--yes` without approval,
  because it approves hook commands and other prompts in one step.
- Prefer porcelain output for machine parsing.

## Output

- Action and final worktree state
- Repository, branch or ref, and absolute path
- Commands and verification results
- Selected provider and fallback state
- Approval-gated operations and cleanup state
