# Guided Intake

Start with repository evidence, then ask only questions that change the
boundary or intended state. Establish:

- system or project purpose.
- included and excluded business flows.
- repository, delivery, cloud, platform, data, and SaaS seeds.
- environment and data boundaries.
- existing documentation to migrate.
- authorized live-discovery scope.
- target repository, branch, documentation destination, and mapped folder.

## Destination

When repository evidence doesn't
settle the destination, ask for it only if the answer changes paths,
navigation metadata, link syntax, or renderer constraints. Otherwise use
portable Markdown links and add no destination-specific navigation files or
metadata. Preserve existing destination-specific path and filename casing
unless an approved migration changes it.

## Missing intent

Preserve the human knowledge and open questions already in the context page.
When answers are unavailable, record the missing intent on the gaps page and
continue only with observed-state claims the evidence supports.

## Page needs

During intake, record the smallest likely set of technical-page needs. Revisit
the selection after discovery. Add a page only when it has evidence-backed
content to own, and drop a selected page whose evidence doesn't support it.

## Example

Repository evidence points to `docs/`, but the request also mentions a hosted
wiki. Ask: "Should the bundle remain in `docs/`, or map to the hosted wiki?"
The answer changes navigation metadata and renderer constraints. Select the
destination adapter only after confirmation.
