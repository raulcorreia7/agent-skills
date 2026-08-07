# Outbound Requests And SSRF

- Select a configured destination by an owned identifier instead of accepting
  a complete user-controlled URL when possible.
- When the contract requires a dynamic destination, allow only required schemes,
  ports, hosts, and paths. Parse with the maintained URL API.
- Resolve and validate every destination address before each connection. Reject
  loopback, private, link-local, metadata, and other prohibited networks for
  both IPv4 and IPv6.
- Disable redirects by default. If the contract permits redirects, apply the
  same destination policy to every hop. Do not forward credentials across an
  untrusted boundary.
- Enforce the destination policy with network egress controls. Application
  validation alone does not contain alternate encodings, DNS rebinding, or a
  compromised dependency.
- Use the [structured-data router](../structured-data/index.md) to apply the
  HTTP contract and shared resource limits.

Example—map a caller choice to an owned origin:

```text
provider = allowed_providers[request.provider_id]
path = url_api.encode_path_segment(request.document_id)
request = http_client.get(provider.fixed_origin, path, redirects=false)
```

The client can reach only the provider network through the egress policy.

Source: pinned OWASP [Server-Side Request Forgery Prevention Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.md).
