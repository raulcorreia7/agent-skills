# Tools

Use the Assumed row directly; check the others with `command -v` and keep a
fallback for Optional tools. The installer creates this file once and never
overwrites it, so edit it to match your machine.

| Availability | Rule                         | Tools                                                                                                        |
| ------------ | ---------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Assumed      | Use directly                 | shell, coreutils, grep, sed, git, curl, ssh, python3                                                         |
| Common       | Verify with `command -v`     | rg, jq, gh, fd, docker, just                                                                                 |
| Optional     | Check, keep a fallback       | tgrep (indexed grep for very large codebases), ast-grep (syntax shapes), yq (YAML; python for multi-step), hyperfine (timings; `time` for one-offs) |

## Yours

<!-- Override or extend the table: what you always have, what to check, quirks. -->
