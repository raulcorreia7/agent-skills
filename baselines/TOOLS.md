# Tools

Check the section for a tool before using it.

## Generically available

Assume present: shell, coreutils, grep, sed, git, curl, ssh, python3.

## Widely adopted

Common but not guaranteed — verify with `command -v`. Examples: rg, jq, gh, fd, docker, just.

## Optionally available

Never assume — check first.

### tgrep

Name shared by treegrep (tree-result UI) and microsoft/tgrep (trigram-indexed search). Check `tgrep --version` first. Default to ripgrep; use indexed tgrep only when ripgrep takes seconds per query.

### ast-grep

Structure-aware search and rewrite, not text search: patterns never match comments or strings, and fail where no code structure fits. Use only for structure-aware queries; use ripgrep for text.

### yq

YAML counterpart to jq: query and edit YAML from shell pipelines. Use for reading or patching YAML in scripts; prefer python for multi-step transforms.

### hyperfine

Statistical command benchmarking with warmups and repeated runs. Use when comparing timings; plain `time` suffices for one-off measurements.
