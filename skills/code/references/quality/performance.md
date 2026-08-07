# Measured Performance

- State the user-visible performance requirement and the workload that produces
  it. Do not substitute a local microbenchmark for an end-to-end contract.
- Measure before optimization. Keep the environment, input distribution,
  concurrency, warmup, and sample method stable enough for comparison.
- Record distributions and errors. Include tail latency, throughput, resource
  use, and cost when they can change the decision.
- Profile or trace the representative workload. Optimize the demonstrated
  bottleneck instead of the most visible code.
- Measure after the change with the same method. Keep a regression check only
  when the requirement is durable and the environment is controlled.
- Report noise, scope, and transfer limits. Do not invent a universal target.

Example—retain one comparable benchmark record:

```text
{revision, environment, workload, concurrency, warmup, samples,
 p50, p95, p99, throughput, errors, peak_memory, cost}
```

Compare candidate and baseline records from the same setup. Investigate a
changed distribution before attributing it to the code change.

Amdahl's law limits total speedup to the improved fraction. Tail latency grows
in importance when one request depends on many components. Neither result
supplies a transferable numeric target.

Sources: [Amdahl, 1967](https://doi.org/10.1145/1465482.1465560) and
[Dean and Barroso, 2013](https://doi.org/10.1145/2408776.2408794).
