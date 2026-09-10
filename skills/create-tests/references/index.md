# Test Branch Index

Read only the leaves that match these conditions:

- Read [core-evidence.md](core-evidence.md) for every task. It defines the
  oracle, test-level, and evidence contract.
- Read [cases.md](cases.md) when choosing case shape, row names, or how many
  rows a behavior needs.
- Read [generative-and-fault-based.md](generative-and-fault-based.md) when the
  task has broad input spaces, weak oracles, parsers, transformations, or weak
  assertion risk.
- Read [flakiness.md](flakiness.md) when a test fails nondeterministically or a
  change adds retries, sleeps, quarantine, or timeout increases.
- Read [concurrency.md](concurrency.md) when behavior depends on shared state,
  asynchronous work, ordering, cancellation, retries, or idempotency.
- Read [migrations.md](migrations.md) when a change moves schemas, stored data,
  or compatibility between deployed versions.
- Read [security.md](security.md) when a claim crosses a trust boundary or fixes
  a vulnerability.
- Read [agent-generated-tests.md](agent-generated-tests.md) when an agent
  generates tests or repairs code from test feedback.
- Read [metrics.md](metrics.md) only when the user or repository uses coverage,
  mutation, pass, flake, runtime, test-count, or agent metrics.
