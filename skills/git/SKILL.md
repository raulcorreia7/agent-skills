---
name: git
description: Inspects Git state, drafts Git text, and performs approved repository mutations. Use when commits, branches, pull requests, releases, or work-item links are primary.
---

# Git

## Job

Assist with human-owned Git state: inspect safely, draft clear Git text, and
mutate Git only after explicit approval for the exact operation and boundary.

## Branches

- **Inspect:** Read repository state and keep it unchanged.
- **Draft:** Prepare Git text and keep repository state unchanged.
- **Mutate:** Change only the Git state that the user explicitly approves.

## Steps

1. Select `inspect`, `draft`, or `mutate`. Treat an unclear mutation request as
   inspection or drafting.
2. Inspect applicable repository instructions, contribution policy, status,
   relevant diffs, templates, and local naming conventions. Finish when the
   repository evidence supports the requested action or draft.
3. If sensitive data appears, stop the exposure and identify only the affected
   file or field. Finish when the output contains no sensitive value.
4. Load only the reference for the requested Git artifact:
   - Read `references/commits.md` for commit messages and breaking-change markers.
   - Read `references/branch-names.md` for branch naming.
   - Read `references/work-item-links.md` for issue and work-item references.
   - Read `references/pull-requests.md` for PR titles, bodies, templates, and
     create or update evidence.
   - Read `references/releases.md` for generated version, changelog, and tag flow.
5. For a mutation, confirm the exact action, paths or refs, and intended
   boundary.
6. Stage explicit paths. Use broad staging only when status proves every change
   is in the approved scope.
7. Recheck the staged diff before a commit. Recheck destination refs before an
   amend, tag, push, rebase, reset, squash, or force-push.
   Finish when the checked state matches the approved boundary.

## Guardrails

- Preserve repository conventions and generated release workflows. Prefer
  `commitlint` or an equivalent hook in consuming repositories for header
  grammar; this skill owns inspect, draft, mutate approval, and blast radius.
- Keep unrelated files outside staging and mutations.
- Obtain explicit approval before each external or destructive mutation.
- When the user explicitly requests correctness or risk review, compose with
  the manual `$review` skill.

## Output

- Drafted text or changed Git state
- Included scope and intentionally untouched files
- Commands and results when the branch ran them
- Approval-gated mutations
