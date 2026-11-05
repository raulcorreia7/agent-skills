# Mermaid Core Authoring

This file covers syntax shared across families. Family-specific references own
their grammar and examples.

## Source Shape

A diagram starts with one declaration. Use `%%` for a line comment. Unknown
keywords break parsing. Misspelled configuration keys can fail silently.

```mermaid
---
title: Checkout request
config:
  look: classic
  flowchart:
    curve: linear
---
flowchart LR
    accTitle: Checkout request path
    accDescr: A shopper submits a cart to the checkout API, which writes an order.
    shopper([Shopper]) -->|submits cart| api[Checkout API]
    api -->|writes order| store[(Order store)]
```

Use quoted labels for punctuation, Markdown strings, and parser-sensitive words.
The lowercase word `end` can break flowchart and sequence parsing when used as
an unquoted identifier or label. Keep stable short IDs separate from display
labels.

## Frontmatter And Configuration

YAML frontmatter must begin on the first line and uses case-sensitive keys.
Prefer frontmatter over deprecated initialization directives. Important shared
controls include:

- `theme`: built-in themes include `default`, `neutral`, `dark`, `forest`, and
  `base`. Only `base` is intended for custom `themeVariables`.
- Omit `theme` from portable source when the host or build selects light, dark,
  high-contrast, or print output. A source-level theme overrides CLI theme
  selection and can make text or fills unreadable on another background. Fix a
  theme only for a rendered asset with an explicit matching background.
- `look`: `classic` or `handDrawn` where supported. Use hand-drawn style for
  workshops or provisional concepts, not as a default architecture aesthetic.
- `layout`: `dagre`, `elk`, `tidy-tree`, or `cose-bilkent` when the family and
  host bundle support them. ELK is not automatically present in every embed.
- family keys such as `flowchart`, `sequence`, `gantt`, or `radar` for local
  options.
- `securityLevel`: host-owned in most Markdown integrations. Do not weaken it
  merely to enable links or HTML.

Directives in `%%{init: ...}%%` are less portable. Use them only for a verified legacy renderer.

For a fixed-background PNG, the renderer-owned profile lives in
`../delivery/mermaid.md`; load it only when rendering a fixed asset.

## Labels, Styling, And Links

| Need | Practical fragment | Portability note |
|---|---|---|
| Stable ID and quoted label | `api["Checkout API (v2)"]` | Keep the ID short. Quote punctuation and parser-sensitive words |
| Literal special character | `cost["Priority #35;1"]` | Mermaid entity codes such as `#35;` are safer than raw parser delimiters. Verify the family |
| Reusable class | `classDef external stroke-width:2px,stroke-dasharray:5 3` then `class payments external` | Prefer structural, theme-adaptive properties. Fixed colors need theme review |
| Edge styling | `linkStyle 0 stroke-width:2px` | Indexes are source-order sensitive. Use sparingly |
| Link | `click docs "https://example.com/docs" "Open documentation"` | Host security policy can disable links. Keep the URL visible nearby when essential |

Do not backslash-escape Mermaid blindly: escaping rules differ between YAML,
Markdown fences, Mermaid grammars, HTML/entity processing, and host Markdown.
Prefer stable IDs, quoted labels, and supported entity codes. Render the exact
final fence after any documentation templating.

- Use Markdown strings only when ordinary quoted labels are insufficient.
- Prefer structure, labels, and a small number of semantic classes. Inline
  `style` statements are harder to reuse and audit than `classDef`.
- Keep fills vivid but purposeful, borders visible, and text contrast strong.
  Avoid fixed colors in native Markdown when the host controls the theme.
- Use `linkStyle` sparingly and keep edge meaning in labels or line patterns.
- `click` links, HTML labels, images, and custom CSS depend on the host security
  policy and are not portable.
- Math rendering uses KaTeX, which requires host support. Use plain Unicode or
  text when it communicates as well as mathematics.

## Icons

Flowchart and architecture icon syntax relies on registered packs; load
`../design/icons.md` when a diagram uses icons.

## Accessibility

Use `accTitle` and `accDescr` inside the diagram where supported. The title
identifies the view. The description states its essential meaning rather than
listing every visual coordinate. Complex diagrams also need a nearby structured
description. Keep node and relationship labels meaningful without color.

## Validation

```text
mmdc -i diagram.mmd -o diagram.png -b white -s 2
```

Inspect the PNG at its intended display size. Confirm that it has the right
content and that labels, icons, edges, and contrast are readable. Check the
embedded Mermaid version only when the destination rejects otherwise valid
source.

Sources: [syntax structure](https://mermaid.js.org/intro/syntax-reference.html),
[configuration](https://mermaid.js.org/config/configuration.html),
[theming](https://mermaid.js.org/config/theming),
[layouts](https://mermaid.js.org/config/layouts),
[icons](https://mermaid.js.org/config/icons.html),
[math](https://mermaid.js.org/config/math.html), and
[accessibility](https://mermaid.js.org/config/accessibility.html).
