# Icons

Icons help recognition only when their source, meaning, and renderer are known.
They never replace a nearby product or service label.

## Selection Order

1. Use the vendor's current official icon for a named vendor service.
2. Use Material Design Icons for generic infrastructure and interface concepts.
3. Use Iconify Logos for a recognizable third-party product.
4. Use Font Awesome Free only when the renderer supports it natively and the
   icon's license and meaning fit.
5. Fall back to a labeled built-in shape.

For vendor-branded products, use the official published icon; do not crop, flip,
rotate, recolor, or distort it. Do not use a product icon to represent a
different product.
Put the official service name nearby. Review the current terms before you
vendor icon files into a reusable skill or project.

## Terrastruct Catalog

Terrastruct publishes a free hosted catalog of icons commonly used in software
architecture diagrams. D2 accepts a copied catalog URL as an `icon` value.
Treat the catalog as a discovery option, not as proof of redistribution rights
for every underlying logo or trademark.

- Keep the product/resource name visible beside the icon.
- Verify remote loading in the pinned renderer and final PNG.
- For offline, private, or reproducible builds, use an approved local copy after
  license review. Otherwise fall back to a labeled built-in shape.

## Mermaid Registration

Mermaid architecture diagrams include `cloud`, `database`, `disk`, `internet`,
and `server`. The embedding application must register other Iconify packs.
Registration is not portable to arbitrary Markdown renderers.

```text
mermaid.registerIconPacks([
  {
    name: "mdi",
    loader: () => import("@iconify-json/mdi").then((m) => m.icons),
  },
  {
    name: "logos",
    loader: () => import("@iconify-json/logos").then((m) => m.icons),
  },
]);
```

Use icon syntax only after registration confirmation, for example
`logos:github-icon` or `mdi:database`. When the target cannot register the pack,
render locally or replace the icon with a labeled built-in shape.

## Review

- Verify the pack, icon name, license, and target registration.
- Keep icon size and visual weight consistent. Do not mix unrelated icon styles
  casually.
- Confirm light, dark, high-contrast, and print legibility.
- Preserve a text label and accessible description.
- Avoid remote runtime loading for private, offline, or reproducible builds.

Renderer sources: [Mermaid icon registration](https://mermaid.js.org/config/icons.html),
[Mermaid architecture icons](https://mermaid.js.org/syntax/architecture.html),
[Terrastruct icon catalog](https://icons.terrastruct.com/),
[D2 icon guidance](https://d2lang.com/tour/icons/).
Icon sources: [Iconify collections](https://icon-sets.iconify.design/),
[Material Design Icons](https://pictogrammers.com/library/mdi/), and
[Font Awesome Free license](https://fontawesome.com/license/free).
