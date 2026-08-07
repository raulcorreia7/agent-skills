# Documentation Migration

When documentation already exists:

1. Inventory pages, canonical claims, links, navigation, and diagrams.
2. Map useful content to the page that owns its reader question.
3. Preserve source attribution and stable links where possible.
4. Update moved-page links and confirmed destination-specific navigation files
   in the same change.
5. Remove superseded pages only within the approved migration scope.

## Example

If `Architecture.md` mixes a system overview with deployment steps, move the
verified overview into `system.md` and the steps into `delivery.md`, then update
inbound links. Preserve the existing `Architecture` `.order` entry unless the
approved migration also authorizes its rename or removal.
