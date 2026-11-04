# Acquisition safety

Read before any network fetch, archive extraction, or parser run.

## Network

- Allow only approved schemes and hosts. Validate each redirect and resolved
  address. Block loopback, link-local, private, and metadata endpoints unless
  the task explicitly authorizes them.
- Treat `robots.txt`, a site map, and `/llms.txt` as discovery data. They do not
  grant access, reuse, or redistribution rights.

## Workers

- Run browsers, parsers, converters, OCR, and model extractors in disposable,
  resource-limited workers. Remove ambient secrets and mutation tools. Disable
  network access unless an approved step requires it.

## Limits

- Set limits for hosts, redirects, requests, bytes, files, nesting, parser
  resources, and derived output before acquisition.
- Bound transfer size, decompressed size, archive expansion, file count,
  nesting, pages, pixels, CPU, memory, time, and output size.

## Archives

- Inventory members before extraction. Reject archive path traversal.
- Do not follow a symlink outside the acquired root; record it as skipped.
