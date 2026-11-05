# Optimization Scopes

Read the section for the scope that owns the target.

## Runtime

Inspect the critical path, wait time, CPU, memory, allocation, I/O, network,
serialization, database access, batching, concurrency, caching, retries, and
backpressure. Profile before rewriting an algorithm or adding a cache.

## Build and CI

Inspect task selection, dependency restore, cache keys, invalidation,
generated outputs, parallelism, test distribution, artifacts, environment
startup, and duplicated work. Preserve determinism and failure visibility.

## Size and dependencies

Measure bundles, images, binaries, transfers, storage, and dependency trees.
Check that the critical path uses a dependency before proposing its removal.

## Cost, capacity, and infrastructure

Inspect utilization, quotas, retention, idle resources, scaling, saturation,
headroom, request limits, throttling, queue depth, placement, egress, storage,
compute shape, startup cost, reservations, and high-availability overhead.
Compare provisioned, configured, requested, and observed capacity.

Low average utilization isn't waste when bursts, failover, maintenance,
recovery objectives, or commitments justify headroom. Recommend a SKU, region,
topology, or redundancy change only with current availability, quota, price,
compatibility, reliability, and migration evidence.

## Architecture

Trace the outcome across boundaries. Inspect fan-out, serialization, chatty
calls, data locality, consistency, caching, queues, contention, backpressure,
retry amplification, failure domains, scaling units, deployment coupling, and
observability gaps. Give each structural proposal a causal mechanism and a
measurable prediction. A named pattern is a hypothesis, not workload evidence.

## Process

Measure queue time, handoffs, rework, failure demand, review delay,
automation, recovery time, and lead time. Optimizing visible activity is a
loss when it makes the end-to-end outcome slower or less reliable.
