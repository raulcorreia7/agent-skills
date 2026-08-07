# Platform Delivery

Use the destination's actual capabilities instead of an assumption that a Mermaid
or another language fence renders everywhere.

## Profiles

| Destination | Default | Verify |
|---|---|---|
| GitHub | Fenced Mermaid. Otherwise PNG | Render the exact required family and feature in the target |
| GitLab | Native Mermaid where enabled. Otherwise repository-rendered PNG | Instance version, feature configuration, and sanitization |
| Obsidian | Fenced Mermaid | App Mermaid version, theme contrast, internal-link behavior |
| Codex | Mermaid in conversation. Source or image for durable files | Host renderer can lag Mermaid. Beta families can report “No diagram type detected” even when current CLI accepts them |
| Generic Markdown | Assume code display only | Site generator or renderer integration |
| Static docs site | Build plugin or pre-rendered PNG | Pinned plugin/Mermaid version, CSP, icon registration, dark mode |
| Office/PDF | PNG | Font embedding, clipping, transparency, and print contrast |
| Image-only system | PNG | Size limits and alt-text support |
| Terminal/plain text | Prose, table, or a validated ASCII export | Unicode support and whether topology remains understandable |

Sources: [Mermaid integrations](https://mermaid.js.org/ecosystem/integrations-community.html),
[GitHub diagrams](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams),
and [Obsidian diagram syntax](https://obsidian.md/help/Editing%2Band%2Bformatting/Advanced%2Bformatting%2Bsyntax).
