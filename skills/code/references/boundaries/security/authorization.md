# Authorization

- Define the permitted operation, protected object, principal, relationship,
  and relevant context. Authentication alone does not grant access.
- Enforce authorization at the server-side owner of every protected operation
  and object. Do not rely on route visibility or client checks.
- Deny by default. Grant the minimum capability and data scope required for
  the current operation.
- Derive tenant and ownership scope from trusted identity state when possible.
  Do not accept a caller-supplied scope as authority.
- Keep policy in one maintained enforcement mechanism. Keep the resource query
  and authorization decision consistent when concurrent change matters.
- Return only information the caller can receive. Use equivalent external
  outcomes when object existence is itself protected.

Example—authorize the protected operation at its owner:

```text
principal + order_id → tenant-scoped lookup → authorize CancelOrder
                     → cancel order → owned result
```

The external response does not distinguish a missing order from an order in a
different protected tenant.

Source: pinned OWASP [Authorization Cheat Sheet](https://github.com/OWASP/CheatSheetSeries/blob/da4c967e9de854727f72bb2748dd98f76c888b06/cheatsheets/Authorization_Cheat_Sheet.md).
