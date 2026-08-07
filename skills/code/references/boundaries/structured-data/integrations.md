# Provider Integrations

- Isolate provider-specific authentication, serialization, validation, and
  error mapping in one adapter. Apply the shared HTTP lifecycle contract from
  the HTTP leaf and return domain-relevant types.
- Keep provider-specific names, status values, pagination tokens, rate-limit
  behavior, and compatibility shims at that boundary.
- Record provider pagination, rate limits, idempotency keys, delivery
  guarantees, and partial-success behavior where they affect the domain.
- Map provider errors without leaking credentials, sensitive payloads, or
  unstable upstream details into the public contract.
- Verify the adapter with a protocol-faithful test boundary and use a real
  sandbox or service check when wire behavior, authentication, or provider
  drift is material.

Example—map provider outcomes once at the adapter:

| Provider result | Domain result | Retry |
|---|---|---|
| `200` with valid payload | `OrderPage` | No |
| `429` with bounded delay | `TemporarilyUnavailable` | Policy-controlled |
| `404` for configured resource | `ConfigurationError` | No |
| Malformed success payload | `ProviderContractError` | No |

The domain does not receive provider response bodies, headers, or credentials.
