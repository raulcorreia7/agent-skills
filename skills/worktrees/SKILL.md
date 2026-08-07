---
name: worktrees
description: Manual invocation only. Safe Git worktree management and provider review checkout.
---

# Worktrees

## Job

Run predictable Git worktree workflows with explicit paths, provider selection,
preflight checks, and cleanup guardrails.

## Steps

1. Resolve the requested action, repository root, branch or ref, base ref,
   target path, provider, and approval boundary.
2. Run the common preflight: resolve the repository root, inspect
   `git status --short --branch` and `git worktree list --porcelain`, and check
   whether the requested branch, ref, or path already exists.
3. Select the provider. Use Worktrunk unless the request explicitly requires
   copy-on-write. For that branch, use simgit after its pilot passes. Use native
   Git only when the selected provider is unsuitable. Read
   `references/providers.md` for provider selection or a copy-on-write request.
4. Load only the reference for the selected operation:
   - For Worktrunk or simgit, use the provider commands in
     `references/providers.md`. Read the native operation references for their
     guardrails and verification only.
   - Read `references/add.md` to create, adopt, track, or detach a worktree.
   - Read `references/maintain.md` to inspect, move, repair, lock, or unlock one.
   - Read `references/remove.md` to remove a worktree.
   - Read `references/prune.md` to inspect or prune stale administrative records.
   - Read `references/configuration.md` only when the user explicitly requests
     worktree configuration.
   - For a provider review checkout, read `references/provider-checkout.md` and
     exactly one of `references/github.md` or `references/gitlab.md`.
   - Read `references/sources.yml` only to audit or re-verify worktree
     provenance.
5. Run only the selected operation and its necessary preflight. Finish when the
   final path, branch or detached state, tracking state, and cleanup state are
   known.

## Guardrails

- Use Worktrunk unless the request requires copy-on-write. Use simgit only with
  `--require-cow`. Use native Git as the compatibility fallback.
- Do not silently downgrade a requested copy-on-write workflow.
- Do not assume that Worktrunk's ignored-file copies use copy-on-write.
- Do not use broad ignored-file cleanup such as `git clean -ffdx` while managed
  worktrees exist. Remove the selected worktree through Git instead.
- Default native Git and simgit paths to
  `../<repo-name>-worktrees/<branch-slug>`.
- Inspect Worktrunk's path configuration and ensure its destination is outside
  the source repository.
- Lowercase branch slugs, replace separators and unsafe path characters with
  `-`, collapse repeated `-`, and trim edges. Reject an empty slug, `.`, or
  `..`.
- Treat branch deletion as a separate explicit action.
- Preserve Git configuration unless the user explicitly requests a change.
- Keep worktrees outside `/tmp`, `.tmp`, and the source repository.
- Obtain explicit approval for `--clobber`, `--force`, `-B`, `-D`, real prune,
  branch deletion, process reaping, and network fetches.
- Prefer porcelain output for machine parsing.

## Composition

- Compose with the `git` skill only when drafting branch, PR, release, or
  work-item text is an independent deliverable. This skill retains ownership of
  worktree operations and resolves existing refs directly.
- Remain usable without the `git` skill. Use local repository naming
  conventions and do not read another skill's files.

## Output

- Action and final worktree state
- Repository, branch or ref, and absolute path
- Commands and verification results
- Selected provider and fallback state
- Approval-gated operations and cleanup state
