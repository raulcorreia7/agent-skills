# Efficient Tool Use Guardrail

> Maximize relevant evidence per unit of context, time, and tool use.

The rules in [`AGENTS.md`](../AGENTS.md) are authoritative. Apply this
companion when repository exploration, multi-file evidence, large tool output,
or repeated tool use is material.

## Behavior contract

- Define the evidence question, required confidence, useful output shape, and
  stopping condition before broad discovery.
- Use progressive discovery: orient, locate, inspect, broaden, verify, and
  stop. Each operation supplies the evidence needed to select the next one.
- Discover applicable repository instructions, configured workflows, stack
  metadata, and available tool capabilities before inventing a command.
- Prefer an existing repository-owned or stack-aware tool that understands the
  target semantics and can return bounded evidence.
- Preserve provenance. Retain the paths, symbols, lines, identifiers, counts,
  query parameters, or commands needed to verify a result.
- Broaden when narrow evidence leaves ownership, dependencies, completeness,
  correctness, or risk unresolved. Do not use a small output as a substitute
  for sufficient coverage.
- Reuse unchanged observations and cached metadata. Retrieve evidence again
  when its source changed or the earlier result cannot support the new claim.
- Evaluate task success, evidence coverage, safety, latency, cost, context use,
  and tool calls together. Do not optimize one measure at the expense of the
  result.

## Progressive discovery

1. **Orient:** Inspect the applicable instructions and the smallest useful map
   of tracked or changed paths, manifests, task runners, configuration, and
   available capabilities.
2. **Locate:** Use names, symbols, exact terms, metadata, or indexed
   relationships to identify candidate owners and evidence.
3. **Inspect:** Request bounded excerpts, selected fields, summaries, counts,
   or structured records. Keep each result attributable to its source.
4. **Broaden:** Expand paths, result ranges, relationship depth, history, or
   pages only for a specific unresolved question.
5. **Verify:** Use the source owner, a repository-defined check, or a direct
   observation that can falsify the conclusion.
6. **Stop:** Stop when the evidence supports the requested outcome and material
   coverage limits are explicit.

## Tool selection

Use the most semantically aware available capability that answers the question with
acceptable scope, output, side effects, setup cost, and reliability. This is a
decision order, not a mandatory tool hierarchy:

Use an approved MCP or connector when it is the most semantically aware,
least-privilege interface for the task. Use its filters and structured fields.
Do not expand its approved scope.

1. Use repository-owned tasks, scripts, manifests, generators, and validators
   when they own the requested fact or check.
2. Use stack-aware capabilities such as compilers, type checkers, language
   servers, symbol indexes, test runners, package managers, framework
   introspection, schema tools, and read-only platform clients.
3. Use structured APIs or CLIs that support filters, field selection, stable
   identifiers, structured output, and pagination.
4. Use syntax, graph, or semantic search when lexical search cannot express the
   relationship or returns excessive noise.
5. Use generic filesystem, version-control, lexical-search, bounded-view, and
   structured-data tools when they are the simplest reliable interface.
6. Use a temporary programmatic operation when several inputs require parsing,
   correlation, joining, ranking, deduplication, aggregation, repeated
   pagination, or dependent transformations.

Do not install a tool or add a dependency only to reduce context. A new tool is
justified only when repeated use or a material correctness or safety risk
outweighs its setup, maintenance, and trust cost.

## Operation contract

- Prefer discovery and summary modes before detailed content modes.
- Filter at the source and select only required fields when the interface
  supports it. Client-side projection can reduce model-visible output even
  when it does not reduce the source payload.
- Paginate only when the required coverage needs another page. Do not assume
  that one page is complete or retrieve all pages by default.
- Run independent bounded operations together or concurrently when their
  outputs remain attributable. Keep dependent operations sequential when one
  result determines the next request.
- Request a set that one decision already selects — several files, references,
  excerpts, or records — in one operation: the interface's multi-target form, or
  the independent requests issued in one round trip. Keep each target's path,
  range, or identifier visible in the result.
- Filter, join, deduplicate, rank, count, or aggregate large intermediate data
  before it enters model context. Return compact findings with provenance and
  material exceptions.
- Use complete files, full history, or broad results when whole-file
  invariants, lifecycle, distant interactions, audit coverage, or edit safety
  require them.
- Make truncation visible. State the applied boundary and the next narrowing or
  continuation operation when omitted results can affect the answer.
- Keep one-off programmatic transformations temporary, inspectable, and
  dependency-free when practical. Do not replace a direct native query with
  custom code that adds more failure modes than it removes.

## Evaluation contract

Include these cases:

- A known symbol or exact error with a narrow evidence path.
- Unknown ownership that requires a repository or stack map before inspection.
- A relationship that requires syntax, language-server, compiler, or graph
  evidence instead of text matches.
- A small or central file whose complete content is necessary.
- A large structured or remote result that needs filtering and deliberate
  pagination.
- Independent questions that benefit from bounded grouped operations.
- A decision that selects several files, references, or records, which loads
  them as one operation rather than one call per target.
- Multi-source evidence that benefits from temporary programmatic aggregation.
- A broad audit whose completion criterion requires broad coverage.
- Truncated evidence with an explicit continuation path.

Measure task correctness and required evidence coverage first. Then compare
context volume, tool calls, latency, cost, repeated retrieval, and avoidable raw
output. Do not reward narrowness when it hides a material gap.
