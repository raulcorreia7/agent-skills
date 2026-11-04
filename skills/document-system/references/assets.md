# Page Templates

Paths are relative to the skill root. Use the mandatory templates:
`assets/baseline/home.md`, `assets/baseline/system.md`,
`assets/baseline/context.md`, `assets/baseline/evidence.md`, and
`assets/baseline/gaps.md`.

After page selection, load only each chosen technical template:

- `modules.md`: `assets/technical-pages/modules.md`
- `schema.md`: `assets/technical-pages/schema.md`
- `interfaces.md`: `assets/technical-pages/interfaces.md`
- `integrations.md`: `assets/technical-pages/integrations.md`
- `infrastructure.md`: `assets/technical-pages/infrastructure.md`
- `delivery.md`: `assets/technical-pages/delivery.md`

After diagram selection, load only each chosen diagram template:

- `architecture.md`: `assets/diagram-pages/architecture.md`
- `context.md`: `assets/diagram-pages/context.md`
- `deployment.md`: `assets/diagram-pages/deployment.md`
- `logical.md`: `assets/diagram-pages/logical.md`
- `schema.md`: `assets/diagram-pages/schema.md`

## Filling templates

- A minimal bundle has no empty optional pages.
- Load a diagram template only when its evidence contract is met. Create the
  logical diagram only when it materially improves clarity.
- Replace placeholders and remove inapplicable links. Replace every `{{...}}`
  token in a selected asset, including Mermaid node and relationship labels, so
  every published label and relationship comes from the evidence.
- Keep portable Markdown links as the default navigation. Add
  destination-specific navigation metadata only for a confirmed destination.
