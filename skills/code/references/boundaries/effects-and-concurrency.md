# Effects And Concurrency

- Make database writes, network calls, file changes, messages, time,
  randomness, and logging visible near the boundary that owns them.
- Review multiple side effects for partial failure. Use a transaction, outbox,
  idempotency key, retry, or compensation only when the consistency contract
  requires it.
- Define duplicate behavior for retryable mutating operations. Make the check
  and mutation atomic when concurrent duplicates are possible.
- Make task ownership, completion, cancellation, shutdown, and failure
  propagation explicit. Bound concurrency and define partial-failure behavior
  for batches and streams.
- Keep synchronized state and its lock together. Keep critical sections narrow
  and explain a non-obvious protected invariant.

Example—one accepted batch item has one owner and one terminal result:

```text
admit item -> register ownership -> process with batch cancellation
           -> record success | failure | cancellation
shutdown   -> stop admission -> wait for admitted senders -> drain workers
```

The shutdown path closes shared work only after admitted senders finish, so it
cannot race a send against channel or queue closure.
