# PR Description

## Title

Use the repository's title rule or PR template. When neither exists, write a
concise Conventional Commit-style title that could serve as the squash or merge
commit subject:

```text
type: subject
type(scope): subject
```

The branch name may be less formal, but the title should still be
recognizable from it. For commit types and breaking-change markers, follow the
commit conventions in `git`.

## Content

Write for a reviewer who has not seen the work. Give each part only when it
applies, in this order:

| Part | What it says |
| --- | --- |
| Why | The problem or goal, and the linked work item. |
| What | The change in a few sentences, by behaviour rather than by file. |
| How tested | The exact commands that ran and their result; manual steps with what you saw. |
| Risk | What could break, for whom, and how a reviewer can check it. |
| Rollout and rollback | Flags, migrations, ordering, and how to undo the change. |
| Screenshots | Before and after for a visible UI change. |
| Breaking changes | What consumers must change, matching the commit's breaking marker. |
| Improvements | Adjacent improvements committed separately, one line each, or suggested ones not made. |
| Follow-ups | Larger opportunities and known gaps left for later work. |

- Record a check only when it ran, with the command as you ran it. Explain a
  missing check only when its absence leaves a real risk.
- Don't claim generated files or release steps were checked when they were
  not.
- For work-item links and closing keywords, use the syntax in `git`; use a
  closing keyword only when merging should close the item.

## Templates

When the repository has a PR template:

- Keep its headings and fill every section that applies.
- Mark a section that does not apply with `Not provided`, `Not stacked`,
  `Not a release PR`, or `None`. Keep every required section, even when empty.
- Put the parts above under the template's closest headings, and add an
  `Improvements` heading when the template has none and there is something to
  list.
- For a template's release section, follow the release PR conventions in
  `git`.

## Check before posting

- The base and destination branches are correct.
- The pushed commits match the intended scope, with nothing unrelated.
- Generated release files are present or absent on purpose.
- The title follows the local convention.
- The body keeps the template.
- Every validation command comes from an actual run.

## Example

```markdown
fix(auth): reject expired refresh tokens

## Why

Expired refresh tokens still returned new access tokens, so a leaked token
stayed useful after expiry. Refs: #482

## What

The token service now checks `expires_at` before issuing an access token and
returns 401 with `token_expired`. Clients already handle 401 by sending the
user to sign in.

## How tested

- `uv run pytest tests/auth -q`: 64 passed, including two new expiry cases.
- Manual: signed in, moved the clock past expiry, refreshed; got 401.

## Risk

Clients whose clocks run fast could see early sign-outs. The check uses the
server clock only, so client time does not matter.

## Rollout and rollback

No migration. Revert the commit to roll back.

## Improvements

- `refactor(auth): rename TokenStore.get to find` (separate commit; the old
  name hid that it returns None).

## Follow-ups

- Rotate refresh tokens on use (#490).
```
