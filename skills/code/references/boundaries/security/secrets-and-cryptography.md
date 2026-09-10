# Secrets And Cryptography

- Use a purpose-built secret store and scoped workload identity when the
  platform provides them. Do not put secrets in source, ordinary configuration,
  build output, errors, telemetry, comments, or user responses.
- Own the complete secret lifecycle: creation, distribution, access, rotation,
  revocation, expiry, audit, detection, and exposure response.
- Define the protection goal and threat before selecting cryptography. Use a
  maintained platform implementation and the current organization standard.
  Do not invent algorithms, protocols, padding, or token formats.
- Use a cryptographically secure random source for keys, nonces, tokens, and
  other unpredictable values. Never reuse a nonce where the algorithm forbids
  reuse.
- Keep keys separate from protected data. Give each key one purpose and minimum
  access. Preserve a key identifier and a safe rotation path.
- Prefer authenticated encryption when data needs confidentiality and
  integrity. Bind important context as authenticated data when the protocol
  requires it.

Example—encrypt an owned record without exposing raw key material:

```text
workload identity → key handle from secret store
record + context + secure random nonce → authenticated encryption
stored envelope = key_id + nonce + ciphertext + authentication tag
```

Rotation changes the key identifier. Diagnostics contain neither plaintext nor
key material.

Sources: pinned OWASP [Secrets Management Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Secrets_Management_Cheat_Sheet.md),
[Cryptographic Storage Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Cryptographic_Storage_Cheat_Sheet.md),
and [Key Management Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Key_Management_Cheat_Sheet.md).
