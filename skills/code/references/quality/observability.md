# Observability

- Start with an operator question or user-visible outcome. Instrument the
  smallest event or measure that answers it.
- Use stable event names and semantic fields. Correlate work across boundaries
  and record result, latency, and reason when useful.
- Keep metric labels bounded. Put high-cardinality identifiers in protected
  logs or traces only when investigation needs them.
- Keep telemetry within the repository's data classification and logging
  contracts.
- Make telemetry failure independent from the main operation. Test disabled,
  delayed, full, or unavailable telemetry when it can affect behavior.
- Alert on actionable symptoms and user impact. Use internal causes for
  diagnosis unless they require direct action.

Example—emit one stable outcome event:

```json
{"event":"order.submit","trace_id":"01J...","result":"rejected","reason":"inventory_conflict","duration_ms":42}
```

Keep `reason` in a bounded vocabulary. Do not attach the order payload or use
`trace_id` as a metric label.

Sources: [OpenTelemetry semantic conventions](https://opentelemetry.io/docs/specs/semconv/general/),
[Google SRE monitoring guidance](https://sre.google/sre-book/monitoring-distributed-systems/),
and the [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).
