# Concurrency Tests

Model the shared state and assert ordering, cancellation, retry, idempotency,
and cleanup invariants that apply.

Use controlled schedules or systematic schedule exploration when the platform
supports them. Use race or sanitizer tools as separate evidence. Random stress
repetition samples schedules. It does not prove systematic coverage.

Record the selected schedules, seed, worker count, platform, and tool settings.
Preserve a reproducible schedule for each failure.

## Example

```text
Risk: cancellation races with completion and emits two terminal events.
Invariant: each job emits exactly one terminal event.
Schedules: cancel-before-complete, complete-before-cancel, and forced overlap.
Evidence: controlled scheduler and race detector pass. Production timing remains unproved.
```

## Evidence Base

- [Musuvathi et al., CHESS schedule exploration](https://www.usenix.org/event/osdi08/tech/full_papers/musuvathi/musuvathi_html/index.html)
