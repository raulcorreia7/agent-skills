# Acquisition Safety

Read before any network fetch, archive extraction, or parser run. The format
references point here for these rules.

## Network

- Allow only approved schemes and hosts. Validate each redirect and resolved
  address. Block loopback, link-local, private, and metadata endpoints unless
  the task explicitly authorizes them.
- Treat `robots.txt`, a site map, and `/llms.txt` as discovery data. They
  don't grant access, reuse, or redistribution rights.

## Workers

- Run browsers, parsers, converters, OCR, model extractors, provider clients,
  archive tools, and Git in disposable, resource-limited workers.
- Remove ambient secrets, credentials, and mutation tools. For Git, also
  disable hooks and executable filters. A browser uses a disposable profile
  without credentials.
- Keep network access off unless an approved step requires it.

## Limits

- Before acquisition, set bounds on hosts, redirects, requests, transfer and
  decompressed size, archive expansion, file count, nesting, pages, pixels,
  CPU, memory, time, and derived output size.

## Archives

- Inventory members before extraction. Reject absolute paths, parent
  traversal, device entries, and expansion beyond the limits.
- Don't follow a symlink outside the acquired root; record it as skipped.
