# HTTP

- Use HTTP and URL APIs that preserve the distinction between origin, path,
  query, headers, and body. Encode each component with its own rules.
- Treat methods, header names, media types, status codes, and redirect policy
  as protocol structure. Allowlist client-controlled structure and serialize
  values through the owning API.
- Define authentication, timeout, cancellation, retry, redirect, proxy,
  decompression, body-size, and connection-reuse behavior at the client
  boundary. Retry only operations whose semantics and idempotency allow it.
- Check the final destination when redirects or dynamic paths can cross a trust
  boundary. Keep credentials and sensitive query values out of diagnostics.
- Translate remote status, headers, and bodies into owned domain outcomes.
  Bound response reads and preserve actionable internal failure evidence.
- At a server boundary, define request-size and parsing limits, disconnect and
  cancellation behavior, response content type, header-commit point,
  backpressure, and what a failure means after response bytes are committed.
- Choose a response framing contract that matches failure semantics. Buffer a
  bounded atomic JSON response, or use a framed format such as NDJSON when
  partial delivery must be observable and recoverable.
- Verify request construction and response handling with a protocol-aware test
  server or transport. Cover cancellation or disconnects, malformed messages,
  partial writes, limits, and relevant cache or conditional-request behavior.

Example—one bounded request contract:

```http
GET /v1/orders?cursor=eyJpZCI6IjEyMyJ9 HTTP/1.1
Host: api.example.test
Accept: application/json
If-None-Match: "orders-v7"
```

The server validates the cursor as data, caps the page size, propagates client
disconnect cancellation, and returns an owned JSON response. If it streams
independent records, it uses an explicit framed media type such as NDJSON.
