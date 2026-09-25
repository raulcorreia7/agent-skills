# Efficient Tool Use for Agents

**Decision:** Use progressive discovery and select the most semantically aware
existing tool that can return sufficient, attributable evidence. Optimize task
success, coverage, context, latency, cost, and tool use together. Do not use
universal token, line, file, or operation limits.

This report was reviewed on 2026-08-07 for maintainers of this repository. It
covers repository exploration, code localization, command selection, tool
output, structured queries, and temporary programmatic analysis. It is a
targeted review of primary research, official specifications, maintainer
documentation, and labelled practitioner evidence. It is not a systematic
literature review.

## Evidence method

The review prioritizes peer-reviewed papers and official specifications. It
uses first-party engineering reports for product and interface practice.
Maintainer documentation establishes supported tool behavior. Community
material identifies operational patterns but does not establish general model
behavior.

The sources use different models, repositories, tasks, interfaces, and cost
measures. Their numeric results do not define portable thresholds. The runtime
contract derives conservative behavior from converging results and retains an
explicit path to broader evidence.

## What the evidence establishes

### Focused context can improve agent performance

SWE-agent directly tested coding-agent interface choices. In its SWE-bench Lite
ablation, a 100-line viewer resolved 18.0% of tasks, compared with 14.3% for a
30-line viewer and 12.7% for complete files. The last five observations
resolved 18.0%, compared with 15.0% for full history. Summarized search resolved
18.0%, compared with 12.0% for iterative result-by-result search. These results
support bounded, informative output and also show that an arbitrarily small
view can remove necessary context. [SWE-agent, NeurIPS
2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5a7c947568c1b1328ccc5230172e1e7c-Abstract-Conference.html)

Long-context studies supply a broader caution. Models can underuse evidence in
the middle of long inputs, and irrelevant context can reduce reasoning
accuracy. A later study reported performance degradation across math,
question-answering, and coding tasks as context grew, even when retrieval was
controlled. These studies do not show that short context is always sufficient.
They show that supported context length is not a reason to load unselected
content. [Lost in the Middle, TACL
2024](https://aclanthology.org/2024.tacl-1.9/), [Irrelevant Context, ICML
2023](https://proceedings.mlr.press/v202/shi23a.html), [Context Length Alone
Hurts LLM Performance, Findings of EMNLP
2025](https://aclanthology.org/2025.findings-emnlp.1264/)

### Retrieval must remain selective and expandable

Repoformer found that selective repository retrieval improved inference speed
without reducing quality in its evaluated code-completion settings. RepoCoder
found that targeted cross-file snippets improved over in-file-only context by
more than 10% across its reported settings. LocAgent used progressive detail
and dependency traversal; its results show that narrow localization can fail
when a task needs multi-hop repository evidence. Together, these results
support an adaptive sequence: retrieve on demand, preserve cross-file
discovery, and broaden for unresolved relationships. [Repoformer, ICML
2024](https://proceedings.mlr.press/v235/wu24a.html), [RepoCoder, EMNLP
2023](https://aclanthology.org/2023.emnlp-main.151/), [LocAgent, ACL
2025](https://aclanthology.org/2025.acl-long.426/)

Agentless and AutoCodeRover provide compatible system evidence. Agentless
localizes through repository structure, file-level information, and finer
locations. AutoCodeRover uses program structure and iterative search. Their
complete systems differ, so they support progressive localization as an
interface pattern, not one mandatory algorithm. [Agentless, FSE
2025](https://doi.org/10.1145/3715754), [AutoCodeRover, ISSTA
2024](https://doi.org/10.1145/3650212.3680384)

### Tool interfaces should control information before it enters context

The Model Context Protocol defines structured tool results, output schemas, and
cursor pagination. Its pagination guidance exists so list operations can yield
smaller chunks instead of complete large result sets. The protocol establishes
available mechanisms; it does not prove that every task should stop after one
page. [MCP schema](https://modelcontextprotocol.io/specification/2025-06-18/schema),
[MCP pagination](https://modelcontextprotocol.io/specification/draft/server/utilities/pagination)

Anthropic's tool-design guidance recommends pagination, range selection,
filtering, truncation, useful defaults, and response-detail controls. Its
programmatic tool guidance recommends processing large intermediates outside
model context. These are first-party engineering practices rather than
independent controlled evidence. They support tool interfaces that expose
enough detail for the next action without relaying every intermediate record.
[Writing effective tools for
agents](https://www.anthropic.com/engineering/writing-tools-for-agents), [Code
execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)

### Instruction and tool economy need quality checks

Yin et al. removed 60% of task-definition tokens while maintaining or
improving performance in their evaluated setting, but output information was
the most consequential content. Prompt-compression research also reports that
query-aware compression can help while warning that compression can discard
key details. These results support removing irrelevant or repeated content,
not shortening every instruction. [Yin et al., ACL
2023](https://aclanthology.org/2023.acl-long.172/), [LongLLMLingua, ACL
2024](https://aclanthology.org/2024.acl-long.91/), [Information Preservation in
Prompt Compression, Findings of EMNLP
2025](https://aclanthology.org/2025.findings-emnlp.949/)

## Tool-capability decision model

The evidence question selects the capability. Existing repository and stack
configuration takes precedence over the examples below.

| Evidence question | Prefer when available | Efficient operation shape | Main caution |
| --- | --- | --- | --- |
| What exists or changed? | Version-control indexes, repository maps, manifests, and task runners | Paths, names, statuses, counts, or summaries before content | Ignored, generated, vendored, or untracked paths can require deliberate expansion. |
| Where is an exact term, symbol, error, or key? | Fast lexical search with path, type, glob, count, and context controls | Candidate locations followed by bounded excerpts | Text matches do not establish semantic ownership or references. |
| What defines, calls, implements, or resolves this symbol? | Compiler, type checker, language server, AST query, symbol index, or repository graph | Semantic locations and relationships before full bodies | Index state, language coverage, and generated code can limit results. |
| Which tests provide evidence? | Repository task runner and test-runner discovery or selection | List or collect first; run the narrowest credible selection | Narrow selection can miss integration, ordering, or configuration behavior. |
| Which dependency, version, or package owns this behavior? | Package-manager metadata, dependency graphs, module resolvers, and lockfiles | Query ownership and reachability before reading full manifests or locks | Query, install, update, and audit operations can have different side effects. |
| What does the framework own? | Framework route, schema, migration, configuration, or generator introspection | Select the owned contract and its producer | Generated output remains evidence, not the edit owner. |
| What remote records are relevant? | Read-only API, GraphQL, or platform CLI with filters and field selection | Server-side filtering, stable IDs, structured output, deliberate pages | One page can be incomplete; exhaustive pagination can multiply cost and noise. |
| How do several structured sources relate? | Structured-data query tool or temporary program | Parse, join, deduplicate, rank, count, and return findings with provenance | Transformation logic can hide omissions or introduce a new bug. |
| Which documentation contract applies? | Documentation generator, navigation source, schema, link checker, or focused docs build | Inspect the source owner and run the relevant check | Rendered or generated pages can be stale derivatives. |

This model prefers the most semantically aware available capability, not the most
specialized tool by default. A direct lexical search can be better than a stale
semantic index. A repository-owned task can be better than reconstructing its
steps. A temporary program can be better than sending thousands of records to
the model, but it is worse than a direct query when it duplicates native
semantics.

## Concrete mechanisms

These tools illustrate capabilities. They are not baseline requirements.

- The ripgrep guide documents file discovery, directory and file-type scope,
  globs, and output controls. Its ignore behavior is useful but can hide
  expected evidence; broaden deliberately when a scoped search fails.
  [ripgrep guide](https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md)
- Git supplies tracked-file indexes, path-scoped history, name and status
  summaries, and diff statistics before full patches. Summary output locates
  change; it does not establish change semantics. [Git diff](https://git-scm.com/docs/git-diff.html),
  [git-ls-files](https://git-scm.com/docs/git-ls-files)
- Language Server Protocol definition, reference, and workspace-symbol
  operations can target semantic code locations. Capability support and index
  freshness vary by client and language server. [LSP
  3.17](https://microsoft.github.io/language-server-protocol/specifications/lsp/3.17/specification/)
- ast-grep provides structural matching and structured output when text search
  cannot represent the syntax relationship. [ast-grep core
  concepts](https://ast-grep.github.io/advanced/core-concepts.html)
- GitHub supports server-side code-search qualifiers, REST pagination, GraphQL
  field selection, and structured CLI projection. Client-side projection
  reduces model-visible output but might not reduce the server payload.
  [GitHub code search](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax),
  [REST pagination](https://docs.github.com/en/rest/using-the-rest-api/using-pagination-in-the-rest-api),
  [GraphQL API](https://docs.github.com/en/graphql/overview/about-the-graphql-api),
  [`gh api`](https://cli.github.com/manual/gh_api)
- jq can select, transform, and stream structured records before output enters
  model context. Slurping complete inputs can create the same scale problem in
  a different process. [jq manual](https://jqlang.org/manual/dev/)

Aider and Continue use compact repository maps and selected signatures before
adding detailed files. They are useful practitioner precedents, not controlled
proof that one map size or ranking method transfers to every agent. [Aider
repository map](https://aider.chat/docs/repomap.html), [Continue repository map
provider](https://docs.continue.dev/customize/deep-dives/custom-providers)

## Operation rules derived from the evidence

1. Define the question and evidence needed to stop.
2. Discover applicable instructions, configured workflows, stack metadata, and
   available capabilities.
3. Start with paths, symbols, summaries, selected fields, or other lightweight
   locators.
4. Inspect bounded, attributable evidence.
5. Escalate to semantic or structural tooling when lexical evidence is noisy or
   cannot express the relationship.
6. Broaden across files, history, relationships, or pages for a named gap.
7. Use temporary code when it can keep large parsed or correlated
   intermediates outside model context.
8. Verify the result through the source owner or a check that can falsify it.
9. Stop when the requested outcome has sufficient evidence and coverage limits
   are explicit.

Independent bounded queries can share one tool round trip or run concurrently
when their outputs remain attributable. Dependent queries remain sequential.
Parallelism is not an unconditional optimization: rate limits, shared state,
result volume, and a dependency on earlier evidence can make it slower or less
reliable.

## Evaluation and limits

Evaluate representative tasks with correctness and evidence coverage as hard
gates. Track context tokens, tool calls, latency, cost, repeated retrieval, and
avoidable raw output as separate secondary measures. Include exact-term,
unknown-owner, multi-hop relationship, a known multi-file set, large structured
result, full-file, programmatic aggregation, and broad-audit cases.

No reviewed source establishes a universal optimal excerpt size, repository-map
budget, result count, or tool-call limit. SWE-agent's interface ablation is the
most direct evidence for bounded file and search output, but its thresholds are
harness-specific. Retrieval and compression can omit decisive evidence.
Semantic indexes can be stale. Programmatic transformations can introduce
errors. Server-side filtering, client-side projection, and model-context
reduction are different optimizations and must not be conflated.

The implemented runtime contract is
[`baselines/guardrails/efficient-tool-use.md`](../../baselines/guardrails/efficient-tool-use.md).
It keeps the portable decision rules and evaluation cases. This report owns the
evidence, examples, and implementation rationale.
