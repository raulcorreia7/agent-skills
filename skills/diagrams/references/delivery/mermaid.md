# Mermaid Rendering

Use a native target renderer or pinned `@mermaid-js/mermaid-cli` and its browser
dependency. Native host rendering and local validation are separate contracts.

```text
mmdc --version
mmdc -i checkout.mmd -o checkout.png -b white -s 2
mmdc -i wide.mmd -o wide.png -b white -w 1600 -s 1
```

`--scale` changes capture density; `--width` changes the browser viewport. For
wide families, increase width before scale. A local CLI can accept a family an
embedded host rejects. When native rendering is unavailable, retain `.mmd` and
publish a reviewed PNG.

## Fixed PNG Profile

Keep native Markdown theme-adaptive. For a fixed light-background PNG, put a
profile in one renderer-owned `mermaid-png.json` and pass it with `-c` (or the
helper's `--mermaid-config`). Do not copy theme frontmatter into every diagram.
A hosted Mermaid destination will not load this local file.

A selected bundled theme (`../design/*.DESIGN.md`) or a project `DESIGN.md`
owns the color tokens; map them onto these `themeVariables`. The values below
are a neutral fallback for when no theme is selected. The quadrant colors are
semantic categories for the prioritization example, not a license to assign a
different color to every node.

```json
{
  "theme": "base",
  "look": "classic",
  "themeVariables": {
    "fontFamily": "Inter, Segoe UI, sans-serif",
    "background": "#FFFFFF",
    "primaryColor": "#F8FAFC",
    "primaryBorderColor": "#64748B",
    "primaryTextColor": "#0F172A",
    "secondaryColor": "#D8E3FB",
    "secondaryBorderColor": "#2563EB",
    "secondaryTextColor": "#102A63",
    "tertiaryColor": "#F8E7D2",
    "tertiaryBorderColor": "#D97706",
    "tertiaryTextColor": "#5B3203",
    "lineColor": "#475569",
    "textColor": "#0F172A",
    "quadrant1Fill": "#F8E7D2",
    "quadrant1TextFill": "#5B3203",
    "quadrant2Fill": "#D5E8DC",
    "quadrant2TextFill": "#09361A",
    "quadrant3Fill": "#F8FAFC",
    "quadrant3TextFill": "#0F172A",
    "quadrant4Fill": "#E7DCFC",
    "quadrant4TextFill": "#341864",
    "quadrantPointFill": "#2563EB",
    "quadrantPointTextFill": "#0F172A",
    "quadrantInternalBorderStrokeFill": "#94A3B8",
    "quadrantExternalBorderStrokeFill": "#64748B"
  },
  "flowchart": {
    "curve": "linear",
    "nodeSpacing": 48,
    "rankSpacing": 56,
    "padding": 16,
    "wrappingWidth": 180
  }
}
```

```text
mmdc -i diagram.mmd -o diagram.png -c mermaid-png.json -b white -s 2
```

Inspect the natural aspect ratio. Treat the profile as a starting point, not
source-level policy: remove unused semantic accents, keep ordinary edges
quiet, and change one spacing value at a time only when labels or boundaries
collide. Create a separate reviewed dark profile when the destination needs
one.

Source: [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli).
