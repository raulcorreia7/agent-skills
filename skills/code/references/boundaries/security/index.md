# Security Boundaries

Read [trust and resource boundaries](trust-and-resource-boundaries.md) for
every security-sensitive change. Then read only the leaves that match the
affected boundary:

- [Authorization](authorization.md) for permissions, tenant isolation,
  protected objects, or disclosure of their existence.
- [Authentication and sessions](authentication-and-sessions.md) for identity,
  credentials, account recovery, tokens, cookies, or session state.
- [Secrets and cryptography](secrets-and-cryptography.md) for secret material,
  encryption, hashing, signing, random values, or keys.
- [Outbound requests](outbound-requests.md) when untrusted data can affect a
  destination, redirect, proxy, callback, webhook, or fetched resource.
- [Untrusted files](untrusted-files.md) for uploads, imports, archives,
  documents, media, or user-controlled filesystem names.
- [Unsafe deserialization](unsafe-deserialization.md) for native object
  graphs, dynamic types, or untrusted serialized objects.

Several leaves can apply to one change. Stop after the common contract and the
selected leaves.

Use the [structured-data router](../structured-data/index.md) for format and
protocol behavior. Use the [quality router](../../quality/index.md) for
dependency or observability changes. Use `create-tests` when security tests are
the primary artifact.
