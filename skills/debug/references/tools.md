# Debugging Tools

Pick the tool that answers the current question with the fewest runs. Each
section names when it fits.

## Minimal Reproduction

Use when the failure needs a large system, manual steps, or flaky timing to
appear.

- Write one script or test that triggers the failure from a known state and
  exits non-zero when it occurs. Put it in a scratch location, not the tree.
- Remove inputs, configuration, and steps one at a time; keep each removal
  that still fails. Stop when every remaining part is needed.
- Pin time, randomness, locale, and ordering so a rerun gives the same
  result. For an intermittent failure, loop the script and report the failure
  rate, not one run.

```text
repro.sh: setup known state → run the one failing call → assert the symptom → exit 1 on failure
```

## Git Bisect

Use when the failure is present at one commit and absent at an earlier one,
and the reproduction runs unattended.

```bash
git bisect start <bad> <good>
git bisect run /path/to/repro.sh   # exit 0 good, 125 skip, other 1-127 bad
git bisect reset
```

Make the script exit 125 for commits that can't build or run, so they're
skipped rather than blamed. Bisect checks out each commit, so start from a
clean tree or a separate worktree. The first bad commit is where the symptom
starts, which may expose an older cause rather than contain it.

## Debugger Or Tracer

Use when you need the state at a known point, or the order of calls across a
boundary.

- Break at the first place the state is known to be wrong, then walk back
  through the call stack to where it became wrong.
- Prefer a conditional breakpoint or a watchpoint to stepping through loops.
- For timing-sensitive or remote failures, use a tracer (system-call tracer,
  distributed trace, or a language's trace hooks) instead of pausing the
  process; pausing changes the timing.
- Record the exact command and settings used, so the observation can be
  repeated.

## Log Narrowing

Use when logs are the main evidence.

- Find the request, trace, or correlation ID of one failing operation and
  filter every log to it.
- Bound the time window to the first failure and the minute before it.
- Compare one failing and one passing operation side by side; the first line
  where they differ is the next place to look.
- When the user allows a temporary log line, add it only at a boundary that
  splits the remaining suspects in half, and remove it after the diagnosis.
