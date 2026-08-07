# Vendored gallery runtimes

These browser distributions make the repository-only diagram gallery available
offline. Replace them only as a pinned set after validating the gallery without
network access.

| File | Package | Version | License |
| --- | --- | --- | --- |
| `mermaid.min.js` | `mermaid` | 11.16.0 | MIT |
| `viz-global.min.js` | `@viz-js/viz` | 3.28.0 | MIT |
| `d2.global.min.js` | `@terrastruct/d2` | 0.1.33 | MPL-2.0 |
| `floating-ui.core.umd.min.js` | `@floating-ui/core` | 1.7.3 | MIT |
| `floating-ui.dom.umd.min.js` | `@floating-ui/dom` | 1.7.4 | MIT |
| `lucide.min.js` | `lucide` | 1.17.0 | ISC |

The pinned package archives come from npm. Their distribution headers and
package licenses remain the authoritative license material.

Viz.js and D2 publish production browser builds instead of separate minified
files. Their pinned distributions use `.min.js` names. The D2 export uses a
classic global so that the gallery works directly from disk.
