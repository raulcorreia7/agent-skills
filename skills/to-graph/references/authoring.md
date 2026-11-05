# Authoring a graph

How to express a task in [graph.schema.json](graph.schema.json). The schema
owns field names and types; this file explains how to use them.

## Nodes

- Give each node one result that one check can confirm. Split a node that needs
  two checks or two owners.
- Write `outcome` as the result, not the action: "Tests pass", not "Run tests".
- Add `done_when` when the result needs a measurable test.

## Running a node

- `run: <command>` runs with bash. Use a `|` block for multi-line commands.
- `run: { uses: <executable>, with: {...} }` calls any program and passes
  `with` as JSON on stdin.
- `${NAME}` is an input. `${node-id.output}` is the last line that node
  printed; it is empty when that node did not run.
- Values reach a command as environment variables, never as code, so a value
  cannot run commands. Quote them as in bash: `"${PR}"` keeps spaces together.
- Put an agent harness in an input and call it unquoted, so bash splits it into
  words: `AGENT: { default: "claude --allowedTools Read --model haiku -p" }`
  and `${AGENT} "prompt"`. Changing the harness changes one value. End a
  list option such as `--allowedTools` with another option, or it swallows
  the prompt.
- When an agent's output is redirected to a file, end the prompt with "Print
  only the result; do not create or edit files." Otherwise the agent may try
  to write the file itself and print commentary instead.

## Outcomes and links

- Exit 0 is `succeeded`; any other exit is `failed`.
- For other branches, list names in `outcomes` and print one as the last line.
- `next` maps each outcome to the next node. A task must map at least one
  success outcome.
- A gate ends as `approved`, `rejected`, or `unavailable`. Map `approved` and
  `rejected`. An unmapped `unavailable` ends the run as blocked.

## Loops, waits, and joins

- Loop only with `retry`; it is always bounded. Polling is
  `retry: { when: pending, every: 5m, max: N, then: <terminal> }`.
- A node that several nodes link to waits for all of them. Without `run`, it
  succeeds only if every node that ran reached it and succeeded.

## Gates

Put every step that needs a person, credentials, money, production access, or
an irreversible change behind a `gate`. Name the `authority` and the `evidence`
nodes the decision rests on.

A scheduled run has nobody to answer a gate. Record a standing approval in
the graph's top-level `extensions.approvals`, one entry per approved action
with its `action` scope, `gate`, `approver`, and `recorded_on` date; the
scheduler passes `--decide <gate>=approved` only for those gates. Map every
other gate's `unavailable` to a node that prints the planned action as a dry
run. See the nightly CI health example.

## YAML traps

- `on`, `off`, `yes`, and `no` read as booleans. Use `when:` for keys, and
  quote such words as values or ids.
- A comma inside `{ }` splits a value, and `: ` inside plain text starts a
  mapping. Quote such text, or use a `|` block.

## Extensions

Put settings that only one runner understands, such as a model name or a
scheduler hint, in `extensions`.
