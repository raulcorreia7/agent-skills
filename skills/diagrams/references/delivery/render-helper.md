# Bundled Render Helper

Resolve `<skill-root>` as the directory containing `SKILL.md`.

POSIX:

```text
python3 <skill-root>/scripts/render.py architecture.mmd
python3 <skill-root>/scripts/render.py one.mmd two.dot --format png
python3 <skill-root>/scripts/render.py diagrams/ --recursive --output-dir build/diagrams
```

Windows:

```text
py -3 <skill-root>\scripts\render.py architecture.mmd
py -3 <skill-root>\scripts\render.py diagrams\ --recursive --output-dir build\diagrams
```

The helper accepts Mermaid (`.mmd`, `.mermaid`), Graphviz (`.dot`, `.gv`), and
D2 (`.d2`). It creates SVG by default and selects `mmdc`, `dot`, or `d2` from
`PATH`. Use `--dry-run` to inspect a batch.

A successful render atomically replaces an existing implicit or explicit
regular output; no `--force` flag is required. The helper refuses symlinks,
directories, and special output files. A batch stops at the first failure and
retains outputs already completed earlier in that batch. The failed job does
not replace its destination. Inspect the dry-run plan and completed output
lines before retrying.

| Status | Meaning |
|---|---|
| `0` | Render or dry-run succeeded |
| `1` | Renderer or output operation failed |
| `2` | Command, plan, path boundary, or renderer availability is invalid |
| `130` | Operation was interrupted |
