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
risk ← cancellation races completion and emits two terminal events
invariant ← exactly one terminal event per job
schedules ← cancel → complete | complete → cancel | forced overlap
evidence ← controlled scheduler + race detector pass
not proved ← production timing
```

## Evidence Base

- [Musuvathi et al., CHESS schedule exploration](https://www.usenix.org/event/osdi08/tech/full_papers/musuvathi/musuvathi_html/index.html)
