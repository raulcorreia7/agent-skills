# Accessibility

- Prefer native semantic controls. Preserve the programmatic name, role,
  value, state, and relationships that users need.
- Support keyboard-only operation. Keep focus visible, ordered, and restored
  after dialogs, menus, or other temporary surfaces close.
- Provide text alternatives and applicable contrast, zoom, reflow, target, and
  pointer alternatives.
- Connect errors to their fields. Announce important status changes without
  moving focus unexpectedly.
- Check the complete user process, not only the changed component. Combine
  automated checks with keyboard use and representative assistive technology
  for material interactions.
- Claim WCAG conformance only for the applicable page or process and level.
  Scanner success alone is not conformance evidence.

Example—connect an invalid field to a new error message:

```html
<label for="email">Email</label>
<input id="email" name="email" aria-invalid="true" aria-describedby="email-error">
<p id="email-error" role="alert">Enter a valid email address.</p>
```

Keep the label visible. Insert the alert when validation fails, and move focus
only when the interaction contract requires it.

Source: [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/).
