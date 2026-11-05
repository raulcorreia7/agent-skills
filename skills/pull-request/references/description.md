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

| Section | What it says |
| --- | --- |
| Summary | The problem and the outcome in 1–3 sentences, then the work item on its own line. |
| Changes | One fact per bullet, by behaviour rather than by file, with deliberate omissions and known limits. |
| Test plan | The exact commands that ran and their result, manual steps with what you saw, and what wasn't tested. |
| Risk and rollback | What could break, for whom, breaking changes, migrations, and how to undo the change; `None: <reason>` when low. |
| Screenshots | Before and after for a visible UI change; omit otherwise. |
| Review notes | Where you want scrutiny or a decision, or `None`. |
| Follow-ups | Adjacent improvements committed separately (one line each), suggested ones not made, and larger work left for later. |

- Record a check only when it ran, with the command as you ran it. Explain a
  missing check only when its absence leaves a real risk.
- Don't claim generated files or release steps were checked when they were
  not.
- For work-item links and closing keywords, use the syntax in `git`; use a
  closing keyword only when merging should close the item.

## Templates

When the repository has a PR template (on GitHub, `.github/pull_request_template.md`
or a file under `.github/PULL_REQUEST_TEMPLATE/`), use it:

- Keep its headings and fill every section that applies.
- Mark a section that does not apply with `Not provided`, `Not stacked`,
  `Not a release PR`, or `None`. Keep every required section, even when empty.
- Put the sections above under the template's closest headings, and add a
  `Follow-ups` heading when the template has none and there is something to
  list.
- For a template's release section, follow the release PR conventions in
  `git`.

## Disclosure footer

End everything an agent posts to the PR (the body, comments, and thread
replies) with one footer line, after a blank line:

```text
🤖 Agent (pull-request) · <model> effort: <effort>
```

Use the model's display name and the reasoning effort as the harness reports
them, and `unknown` for either one it does not report; never guess. Replace an
older footer line when editing the body. Commit messages carry no footer.

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

## Summary

Expired refresh tokens still returned new access tokens, so a leaked token
stayed useful after expiry. They now get a 401.

Refs: #482

## Changes

- The token service checks `expires_at` before issuing an access token.
- An expired token gets 401 with `token_expired`; clients already send the
  user to sign in on 401.

## Test plan

- `uv run pytest tests/auth -q`: 64 passed, including two new expiry cases.
- Manual: signed in, moved the clock past expiry, refreshed; got 401.

## Risk and rollback

Clients with fast clocks can't sign out early, because only the server clock
is checked. No migration; revert the commit to roll back.

## Review notes

The expiry comparison in `token_service.py`: is `>=` the boundary we want?

## Follow-ups

- `refactor(auth): rename TokenStore.get to find` (separate commit; the old
  name hid that it returns None).
- Rotate refresh tokens on use (#490).

```
