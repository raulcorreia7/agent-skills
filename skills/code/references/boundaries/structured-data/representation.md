# Data Representation

- Use domain-correct numeric types, units, precision, and rounding. Reuse the
  codebase convention before introducing a new representation.
- Use structured filesystem and resource-path APIs. Make encoding,
  normalization, traversal, and platform behavior explicit at the boundary.
- Make time zone, calendar, precision, clock source, date meaning, and
  serialized format explicit when they affect behavior.
- Stream large or unbounded data. Materialize bounded data when repeated
  traversal, ordering, or atomic validation requires a snapshot.
- For a streamed data source, propagate cancellation, close the cursor or
  iterator, check its terminal error, and define whether an interrupted stream
  is discardable, resumable, or a valid partial result.
- Bound memory, bytes, records, recursion, and processing time. Verify edge
  values and round trips with the production representation libraries.

Example—make units and stream framing explicit:

```json
{"id":"ord_123","occurredAt":"2026-08-06T10:15:30Z","totalCents":1250}
{"id":"ord_124","occurredAt":"2026-08-06T10:15:31Z","totalCents":499}
```

This NDJSON contract defines UTC timestamps and integer cents. The reader caps
line bytes and record count, closes its source on cancellation, and reports the
last complete record when partial delivery is a valid outcome.
