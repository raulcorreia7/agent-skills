# Checking, drawing, and running a graph

Run the commands from the user's working directory. `TO_GRAPH` stands for
`scripts/to_graph.py` inside this skill's directory, for example
`~/.agents/skills/to-graph/scripts/to_graph.py`. `uv run` installs the script's
dependencies on first use. `--help` on any command lists every option.

| Need | Command |
| --- | --- |
| Validate one or more graphs | `uv run $TO_GRAPH check GRAPH...` |
| Draw a Mermaid diagram | `uv run $TO_GRAPH render GRAPH` |
| Draw a Graphviz diagram | `uv run $TO_GRAPH render --format dot GRAPH \| dot -Tsvg -o graph.svg` |
| Preview the success path | `uv run $TO_GRAPH run --dry-run GRAPH` |
| Run | `uv run $TO_GRAPH run GRAPH NAME=VALUE --decide GATE=approved` |

## Run behaviour

- Inputs come from `NAME=VALUE`, then the environment, then the graph default.
  An undeclared `NAME` is an error.
- Command output goes to stdout; progress goes to stderr.
- A gate takes its answer from `--decide` (`approved`, `rejected`, or
  `unavailable`), asks on a terminal, or ends as `unavailable` when nobody can
  answer. Unmapped, `unavailable` ends the run as blocked (exit 3).
- Nodes run one at a time. The runner keeps no state between runs.
- Exit codes: 0 success, 1 failure, 2 invalid graph or usage, 3 blocked,
  130 interrupted.

## Diagrams

Use Mermaid by default; GitHub, Azure DevOps, Notion, and Obsidian display it
directly. Use Graphviz for large graphs. Tasks are boxes, gates are diamonds,
end states are rounded and coloured by status, and retries are dashed loops.

## Scheduling

A scheduler starts a run with the same command. For example:

```text
crontab:         0 6 * * *  cd ~/src/app && uv run ~/.agents/skills/to-graph/scripts/to_graph.py run ci-health.yaml
GitHub Actions:  on: { schedule: [{ cron: "0 6 * * *" }] }, then the same command in a step
```

To swap the agent harness for one run, pass the input:
`run ci-health.yaml AGENT="codex exec"`.
