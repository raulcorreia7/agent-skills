# Authentication And Sessions

- Use a maintained identity and session implementation. Do not invent password
  storage, token formats, credential recovery, or authentication protocols.
- Use generic external failure responses where account discovery is a risk.
  Apply the maintained verifier and bounded abuse controls to credential and
  recovery attempts.
- Require stronger or repeated authentication before a sensitive operation
  when the risk and product contract require it.
- Renew the session identifier after authentication or a privilege change.
  Invalidate server-side session state on logout, expiry, compromise, or
  administrative revocation.
- Enforce server-side idle and absolute expiry. Restrict cookie `Secure`,
  `HttpOnly`, `SameSite`, `Path`, and `Domain` attributes to the owned contract.
- Protect cookie-authenticated state changes with the framework's maintained
  cross-site request control.

Example—create an owned server session after verification:

```text
credentials -> maintained verifier -> abuse policy -> new session identifier
session -> server-side idle and absolute expiry -> restrictive cookie
```

A privilege change rotates the identifier. Logout revokes the server record.

Sources: pinned OWASP [Authentication Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Authentication_Cheat_Sheet.md),
[Session Management Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Session_Management_Cheat_Sheet.md),
and [Cross-Site Request Forgery Prevention Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.md).
