# Diagram Toolchain Readiness

A binary on one engineer's machine is not team support. Record four layers:

1. **Authoring:** editor support is optional; source stays plain text.
2. **Validation and rendering:** exact CLI, runtime, version, fonts, and engine.
3. **Assets:** icon packs, local images, includes, themes, and licenses.
4. **Delivery:** native renderer, approved plugin or build, or reviewed image.

Classify each dependency as `native`, `team-managed`, `author-local`, or
`unavailable`. Do not recommend source-only delivery when readers cannot render
it. Do not add repository packages, CI jobs, extensions, public renderers, or
installation side effects without approval.

Use common team fonts or package approved fonts. Substitution can move nodes,
clip labels, and invalidate review. Record every icon pack and license and keep
labeled shape fallbacks when a host cannot register icons.
