# Documentation Page Quality

Start page-level quality and correctness audits read-only.

## Page shape

- Check the title, one-line purpose, first useful action, heading outline,
  examples, source-backed contracts, and troubleshooting path.
- Lead with the outcome or quick path, then contracts, examples,
  troubleshooting, and deeper rationale.
- Put tables where facts repeat and diagrams beside the text they explain.
- Remove empty sections, ceremonial introductions, and background that delays
  the reader's task.

## Correctness

- Trace claims to code, config, tests, pipelines, schemas, contracts, owned
  docs, or user evidence.
- Mark unknown or inferred facts.
- Do not present illustrative commands as verified behavior.
- Record remaining unverifiable claims.

## Security

Remove secrets, credentials, customer data, connection strings, sensitive
hostnames, and unnecessary production detail. Use clearly marked placeholders.

## Example

Replace an opening history section with an actionable start:

```md
# Recover a failed deployment

Restore the last healthy release, verify service health, and record escalation
evidence.

## Prerequisites
```

Move history and rationale after the procedure when readers still need it.

Run the narrowest available Markdown, docs-build, example, and diagram checks.

Source: [Diátaxis](https://diataxis.fr/).
