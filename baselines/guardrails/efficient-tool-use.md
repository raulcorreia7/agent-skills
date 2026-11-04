# Efficient Tool Use

> Get the most relevant evidence per unit of context, time, and tool calls.

Load when exploring a repository, gathering multi-file evidence, handling large
output, or repeating tool calls.

## Loop

```text
question ← evidence needed, confidence, output shape, stop condition
orient → locate → inspect → broaden? → verify → stop
orient:  instructions, tracked/changed paths, manifests, task runners, config, tools
locate:  names, symbols, exact terms, metadata, indexed relationships
inspect: bounded excerpts, selected fields, counts, structured records, with their source
broaden: only for a named unresolved question (ownership, dependencies, completeness, risk)
verify:  the source owner, a repository check, or an observation that could falsify the claim
stop:    evidence supports the outcome and coverage limits are stated
```

- Keep provenance: the paths, symbols, lines, identifiers, queries, or commands
  that let someone re-check a result.
- Reuse unchanged observations; fetch again when the source changed or the old
  result cannot support the new claim.
- Judge success, coverage, safety, latency, cost, context, and tool calls
  together; a smaller output never substitutes for sufficient coverage.

## Tool choice

Pick the most semantically aware tool that answers the question with
acceptable scope, side effects, setup cost, and reliability. Check
`~/.agents/TOOLS.md` for what is installed. In order of preference:

1. Repository-owned tasks, scripts, generators, and validators that own the
   fact or check.
2. An approved MCP server or connector, within its approved scope, using its
   filters and structured fields.
3. Stack-aware tools: compilers, type checkers, language servers, symbol
   indexes, test runners, package managers, schema tools, read-only platform
   clients.
4. Structured APIs and CLIs with filters, field selection, stable identifiers,
   and pagination.
5. Syntax, graph, or semantic search when text search is too noisy or cannot
   express the relationship.
6. Generic file, version-control, text-search, and bounded-view tools.
7. A temporary script when several inputs need parsing, joining, ranking,
   deduplication, aggregation, or repeated pagination.

Install a new tool only when repeated use or a material correctness or safety
risk outweighs its setup, maintenance, and trust cost.

## Operations

- Start with discovery and summary modes; fetch detailed content after.
- Filter at the source and select only the fields you need.
- Fetch another page only when the coverage needs it, and treat one page as
  possibly incomplete.
- Batch what one decision selects (several files, references, or records) into
  one operation or one round of parallel calls, keeping each target's path or
  identifier visible. Keep dependent calls sequential.
- Reduce large intermediate data (filter, join, deduplicate, rank, count)
  before it enters context; return compact findings with provenance.
- Read whole files, full history, or broad results when whole-file invariants,
  lifecycle, distant interactions, audit coverage, or edit safety need them.
- Make truncation visible: state the boundary and the next narrowing or
  continuation step.
- Keep one-off scripts temporary, inspectable, and dependency-free; prefer a
  direct native query when it has fewer failure modes.
