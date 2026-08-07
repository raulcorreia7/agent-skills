# Documentation Deduplication And Freshness

Start duplicate-content cleanup and stale-documentation review read-only.
Apply removals or moves only within the approved write boundary.

Look for repeated setup steps, commands, configuration tables, architecture
descriptions, glossary terms, diagrams, warnings, and runbook procedures.
Choose one source of truth, replace copies with links, and remove stale or
speculative material when safe.

Keep current contracts separate from prospective adoption, deployment, or
promotion requirements. Consolidate duplicated quick-start instructions,
command descriptions, and delivery claims behind one canonical page or source.
Nearby repositories can establish presentation conventions, but never become a
source for facts about the current repository.

## Example

If the root README and two runbooks repeat the same validation command, keep the
verified command and its expected result in the development guide. Replace the
runbook copies with a descriptive link, while keeping runbook-specific recovery
steps local.

Validate retained source links, navigation, and references to removed content.
