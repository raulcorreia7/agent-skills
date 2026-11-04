# Efficient Tool Use

> Settle each question with enough evidence and the least context, time, and
> tool calls.

Load when exploring a repository, gathering multi-file evidence, handling large
output, or repeating tool calls.

## Loop

```text
frame:   the question, the evidence that settles it, and the stop condition
orient:  instructions, changed paths, manifests, task runners, config, tools
locate:  names, symbols, exact terms, metadata, indexed relationships
inspect: bounded excerpts, selected fields, counts, structured records
broaden: only for a named open question (ownership, dependencies, completeness, risk)
verify:  the owning source, a repository check, or an observation that could falsify the claim
stop:    the evidence supports the outcome and its coverage limits are stated
```

- Record where each result came from: the path, symbol, line, identifier,
  query, or command that lets someone re-check it.
- Reuse an unchanged observation. Fetch again only when the source changed or
  the old result cannot support the new claim.
- Put coverage, correctness, and safety before context and call count. A
  smaller output never replaces sufficient coverage.

## Tool choice

Use the most semantically aware tool that answers the question with acceptable
scope, side effects, setup cost, and reliability. `~/.agents/TOOLS.md` lists
the installed tools. Prefer, in order:

1. Repository-owned tasks, scripts, generators, and validators that own the
   fact or check.
2. An approved MCP server or connector, within its approved scope, through its
   filters and structured fields.
3. Stack-aware tools: compilers, type checkers, language servers, symbol
   indexes, test runners, package managers, schema tools, and read-only
   platform clients.
4. Structured APIs and CLIs with filters, field selection, stable identifiers,
   and pagination.
5. Syntax, graph, or semantic search, when text search is too noisy or cannot
   express the relationship.
6. Generic file, version-control, text-search, and bounded-view tools.
7. A temporary script, when several inputs need parsing, joining, ranking,
   deduplication, aggregation, or repeated pagination.

Install a new tool only when repeated use, or a significant correctness or safety
risk, outweighs its setup, maintenance, and trust cost.

## Operations

- Discover and summarise first; then fetch detail for what the summary selects.
- Filter at the source and select only the fields you need.
- Fetch another page only when coverage needs it, and treat a single page as
  possibly incomplete.
- Batch what one decision selects into one operation or one round of parallel
  calls, and keep each target's path or identifier visible. Run dependent calls
  in sequence.
- Reduce large intermediate data (filter, join, deduplicate, rank, count)
  before it enters context, and return compact findings with their sources.
- Read whole files, full history, or broad results when whole-file invariants,
  lifecycle, distant interactions, audit coverage, or edit safety need them.
- Make truncation visible: state the boundary and the next narrowing or
  continuation step.

## Temporary code

Temporary code exists only to run through a tool call: inline shell commands,
one-off scripts, ad hoc queries, and scratch files.

- Keep it short and dependency-free. Prefer a direct native query when it has
  fewer failure modes than a script.
- Prefer a minified form to save tokens: no comments, docstrings, blank lines,
  or type hints; short local names; statements on one line where the language
  allows.
- Keep it readable enough to review when it changes state, needs approval, or
  produces output you will cite as evidence. Keep meaningful names where an
  error message would show them.
- Write durable code, and code the user receives as a deliverable, in the
  project's normal style.
