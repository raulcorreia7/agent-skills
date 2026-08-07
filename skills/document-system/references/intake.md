# Guided Intake

Start with repository evidence, then ask only questions that materially change
the boundary or intended state. Establish:

- system or project purpose.
- included and excluded business flows.
- repository, delivery, cloud, platform, data, and SaaS seeds.
- environment and data boundaries.
- existing documentation to migrate.
- authorized live-discovery scope.
- target repository, branch, documentation destination, and mapped folder.

If repository evidence does not settle the destination, identify the affected
output. Ask for the destination when it changes paths, navigation metadata,
link syntax, or renderer constraints. Otherwise, use portable Markdown links
and do not add platform-specific navigation files.

Keep `context.md` human-owned. Propose changes for confirmation, preserve human
knowledge and open questions, and never use the file for agent scratch notes.
If answers are unavailable, record the missing intent in `gaps.md` and continue
only with observed-state claims that evidence supports.

During intake, record the smallest likely set of technical-page needs. Revisit
the selection after discovery. Add a page only when it has evidence-backed
material to own. Remove a selected page whose evidence does not support it.

## Example

Repository evidence points to `docs/`, but the request also mentions a hosted
wiki. Ask: "Should the bundle remain in `docs/`, or map to the hosted wiki?"
The answer changes navigation metadata and renderer constraints. Select the
destination adapter only after confirmation. Do not ask about a destination
detail that leaves the output unchanged.
