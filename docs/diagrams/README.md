# Diagram visual design gallery

Open [index.html](index.html) directly in a modern browser, or run
`uv run poe serve`, to review the repository's visual tokens, themes, and
diagram examples. The page loads its renderers from jsDelivr, so it needs a
network connection. It is not part of the distributable `diagrams` skill.

## Ownership

[`skills/diagrams/references/design/visual.md`](../../skills/diagrams/references/design/visual.md)
owns the shared visual behavior. The adjacent `*.DESIGN.md` files own theme
tokens, identity, and exceptions. The default tokens are in
[`carbon.DESIGN.md`](../../skills/diagrams/references/design/carbon.DESIGN.md).
This gallery mirrors the tokens and examples for local review. Update the
gallery in the same change whenever the main style or family guidance
changes.

The renderers are pinned to exact npm versions, and each classic script carries
a Subresource Integrity hash. Change a version only together with its hash.

| Package | Version | License |
| --- | --- | --- |
| `mermaid` | 11.16.0 | MIT |
| `@viz-js/viz` | 3.28.0 | MIT |
| `@terrastruct/d2` | 0.1.33 | MPL-2.0 |
| `@floating-ui/core` | 1.7.3 | MIT |
| `@floating-ui/dom` | 1.7.4 | MIT |
| `lucide` | 1.17.0 | ISC |
