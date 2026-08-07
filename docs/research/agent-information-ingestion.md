# Safe Information Ingestion for LLMs and Agents

**Decision:** Use the implicit `ingest-sources` skill for material acquisition,
conversion, or corpus work. Keep an ordinary single-page lookup in the active
research workflow. Use the compact baseline guardrail for untrusted content,
network access, parser isolation, provenance, and authority. The skill prefers
native, publisher-owned representations. It retains immutable source bytes
beside every derivative and preserves structure and locators before chunking.
It retrieves a small evidence set instead of placing an entire corpus in model
context.

This report was reviewed on 2026-08-06. It covers bounded ingestion for
inference-time research, retrieval, and agent work. It does not authorize model
training, redistribution, bypassing access controls, or a particular use of
copyrighted or personal data. It is a targeted review of primary specifications,
official tool documentation, and peer-reviewed research, not legal advice or a
systematic literature review.

## Evidence method

The review prioritizes standards and source-owner documentation for formats,
protocols, and tools, and peer-reviewed research for retrieval, deduplication,
long-context behavior, and prompt injection. Preprints are used only for the
original indirect-prompt-injection threat description. Search results and
secondary guides were discovery inputs, not evidence.

Few studies compare complete ingestion pipelines across all formats. The
workflow below is therefore a conservative design inference from format
contracts, documented tool behavior, and converging retrieval and security
evidence. Tool examples illustrate decisions. They are not an implementation or
an approval to fetch a source.

## Governing principles

1. **Discover before downloading.** Start with explicit seeds, publisher-owned
   indexes, schemas, manifests, and repository trees. Do not recursively crawl
   first and decide scope later.
2. **Prefer native before derived.** Use a structured API, source file, or
   publisher-supplied Markdown before extracting a rendered page. Use embedded
   PDF text before layout inference and OCR.
3. **Keep the source and the derivation.** Raw bytes are evidence. Markdown,
   extracted text, OCR, summaries, and chunks are replaceable views with named
   tools, versions, settings, and hashes.
4. **Preserve structure before reducing content.** Keep headings, tables,
   fields, types, links, page or line anchors, code symbols, and parent-child
   relationships before filtering and chunking.
5. **Treat all acquired content as untrusted data.** A page, PDF, repository,
   comment, metadata field, source map, or retrieved chunk cannot change the
   task, permissions, tools, source scope, or approval state.
6. **Minimize by purpose.** Ingest only the sources, fields, files, versions,
   and chunks needed for the declared use. For personal data this is also the
   GDPR data-minimization principle: processing must be adequate, relevant, and
   limited to what is necessary. [GDPR Article 5](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679)
7. **Retrieve, then expand.** Search for a small evidence set and expand to its
   parent, neighbor, table, or definition only when the question needs it.
   Long-context models can use evidence substantially worse when it occurs in
   the middle of a long input. [Lost in the Middle, TACL 2024](https://aclanthology.org/2024.tacl-1.9/)

## Acquisition and conversion choices

| Choice | Use when | Main benefit | Material loss or risk | Required preservation or check |
| --- | --- | --- | --- | --- |
| Direct HTTP fetch | Canonical static HTML, text, file, or API response is available | Fast, deterministic, no browser script execution, and captures headers | Client-rendered content may be absent; redirects can cross trust boundaries | Final URL, redirect chain, status, media type, headers, raw bytes, validators, hash |
| Publisher Markdown or text endpoint | The publisher owns and versions it | Compact and often cleaner than extracted HTML | It can omit interactive examples, figures, tables, warnings, or recent page changes | Compare title, version, headings, links, and a sample against the canonical page |
| Reader/main-content extraction | The page is prose with repeated navigation or advertising | Removes high-volume chrome | It is a lossy heuristic. Mozilla Readability can return HTML or text with all tags removed and warns that untrusted output must be sanitized before rendering | Keep raw HTML and extracted HTML/Markdown; test code, tables, links, warnings, and headings. [Mozilla Readability](https://github.com/mozilla/readability) |
| Isolated browser rendering | Required content is unavailable without client execution | Captures the post-render DOM | Non-determinism, extra requests, credential leakage, script execution, and a larger attack surface | Use a disposable profile without ambient credentials; bound hosts, requests, time, and bytes; retain final DOM and network provenance |
| Plain PDF text | A born-digital, simple-layout PDF has usable embedded text | Cheapest searchable representation | Columns, tables, reading order, figures, equations, and coordinates can collapse | Retain page breaks; compare sample pages; escalate on structure-sensitive content |
| Layout-aware PDF document model | Tables, multi-column text, forms, formulas, figures, or precise citation matter | Can retain hierarchy, reading order, tables, pages, and bounding boxes | Model inference can still misclassify elements or order | Keep structured JSON plus page coordinates and Markdown; visually spot-check difficult pages |
| OCR | Pages are image-only or have unusable text | Makes scans searchable | Recognition errors, language dependence, lost typography, and changed document signatures | OCR only affected pages, record engine/language/settings/confidence, keep page images and original PDF |
| Native JSON/XML/CSV/other structured parse | The source has meaningful types, fields, rows, identifiers, or schema | Preserves machine semantics and supports exact filtering | Flattening to prose loses types and relationships; unsafe parsers can load external resources | Keep native records and schema; validate first; create a separate text projection with field paths |
| Repository raw/API access | Only a few known files or metadata fields are needed | Minimum transfer and no history | Provider limits, truncation, pagination, and many round trips at scale | Capture API version, response metadata, ref and resolved commit; detect truncation |
| Commit-pinned archive | A reproducible source snapshot is needed without Git history | Smaller and simpler than a clone | No history; submodule and Git LFS content may be absent or represented by pointers | Pin a commit, inventory archive members, record submodules/LFS policy, hash the download and extracted files |
| Partial, sparse, or shallow clone | Broad source analysis needs repository semantics but not all history or blobs | Preserves Git paths and a commit identity with lower transfer | Missing history, tags, blobs, submodule content, or older definitions can affect analysis | Record clone options and commit; fetch omitted material only for an explicit need |
| Full clone | History, blame, tags, renamed files, or complete object reachability is required | Highest repository fidelity | Highest transfer, storage, and secret/history exposure | Bound repository and refs; scan scope and retention; capture commit and submodule states |

No single converted representation should replace the source. Pandoc documents
HTML-to-Markdown conversion, while MarkItDown explicitly describes its Markdown
as optimized for text analysis rather than high-fidelity human conversion.
These tools are useful derivatives, not evidence that conversion is lossless.
[Pandoc manual](https://pandoc.org/MANUAL.html),
[Microsoft MarkItDown](https://github.com/microsoft/markitdown)

## Web pages and documentation sites

### Progressive web acquisition

1. Resolve the canonical publisher, product version, locale, and intended page
   set. Prefer a supplied URL list over open-ended traversal.
2. Read `/robots.txt` for crawler rules and Sitemap pointers, then use
   `sitemap.xml`, a sitemap index, documentation navigation, an API inventory,
   or a publisher search index to build candidates. Sitemaps require URL
   locations and may carry `lastmod`, but `lastmod` is optional and separate
   from HTTP validators. It is a discovery hint, not proof that a page is
   complete or current. [Sitemaps protocol](https://www.sitemaps.org/protocol.html)
3. Use a direct, bounded fetch. Accept only expected schemes, hosts, media
   types, and sizes. Validate every redirect and resolved address against the
   network policy; an HTTPS-only command does not by itself prevent a redirect
   or hostname from reaching a private service. OWASP recommends allowlists
   where possible and explicit protection for localhost, link-local, private,
   and metadata endpoints. [OWASP SSRF prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
4. Parse HTML without running page scripts or loading remote resources. Prefer
   semantic `main`, `article`, headings, tables, lists, code, and link targets;
   fall back to a reader heuristic only for main-content selection. The HTML
   Standard defines structural semantics that a plain-text projection cannot
   retain. [WHATWG HTML Standard](https://html.spec.whatwg.org/)
5. Render in a browser only when a comparison proves that direct HTML lacks
   required content. The browser worker must be isolated from secrets,
   privileged sessions, local network access, and mutation tools.
6. Deduplicate canonical, print, mobile, locale, query-string, and version
   variants only after their content and provenance have been compared.

`/llms.txt` can be a useful curated pointer when a publisher supplies it, but it
remains a proposal for inference-time orientation. Treat it as advisory and
neither exhaustive nor an access or reuse policy. Verify linked resources
against the canonical site and normal freshness metadata.
[/llms.txt proposal](https://llmstxt.org/)

### Site indexes, source maps, and generated documentation

- A site map, documentation table of contents, or search index is for
  discovery. It does not establish authority, completeness, license, or
  freshness.
- An OpenAPI/schema document or documentation source repository is often a
  better structural source than rendered reference pages. Record the deployed
  product version and source commit; generated pages may not match the default
  branch.
- An ECMA-426 source map maps generated JavaScript, WebAssembly, or CSS back to
  original sources for debugging. Use one only when deployed bundle analysis
  is in scope, bind it to the exact generated artifact, and treat embedded
  `sourcesContent` as separately licensed source material. It is not a general
  site index. [ECMA-426](https://ecma-international.org/publications-and-standards/standards/ecma-426/)
- A language or code-navigation index such as LSIF can expose definitions and
  references without a local source copy, but it is derived data and must be
  tied to the exact commit and indexer version. LSP and LSIF standardize these
  navigation relationships. [Language Server Protocol and LSIF](https://microsoft.github.io/language-server-protocol/)

## PDFs and OCR

Classify a PDF before choosing a converter:

- **Born digital, simple layout:** extract embedded text first and preserve
  page separators. Poppler's `pdftotext` defaults to inferred reading order;
  `-layout` attempts to retain physical layout, while raw content-stream order
  is explicitly not recommended. This choice must be tested on the document.
  [Poppler `pdftotext` manual](https://manpages.debian.org/bookworm/poppler-utils/pdftotext.1.en.html)
- **Born digital, complex layout:** use a document model that retains tables,
  hierarchy, reading order, page numbers, and bounding boxes. Docling can emit
  Markdown and JSON; its provenance item is a pointer back to a page bounding
  box. Keep the JSON even if Markdown is the retrieval projection.
  [Docling document model](https://docling-project.github.io/docling/reference/docling_document/)
- **Image-only scan:** add an OCR layer or create a sidecar extract. Record the
  OCR language, version, preprocessing, affected pages, and confidence. OCRmyPDF
  normally grafts an OCR layer back onto a PDF and documents why manual
  rasterize/reassemble workflows can lose vector art, text, image quality,
  cropping, rotation, and scaling. [OCRmyPDF introduction](https://ocrmypdf.readthedocs.io/en/stable/introduction.html)
- **Mixed PDF:** preserve existing digital text and OCR only image regions or
  pages. Forcing OCR can rasterize vector content. A changed PDF cannot retain
  its original digital signature; keep the signed original and make the OCR
  output an explicitly derived artifact. [OCRmyPDF errors](https://ocrmypdf.readthedocs.io/en/stable/errors.html),
  [OCRmyPDF signed-PDF guidance](https://ocrmypdf.readthedocs.io/en/latest/cookbook.html#digitally-signed-pdfs)

Markdown or plain text materially loses structure when meaning depends on
absolute position, column flow, merged cells, repeated table headers, forms,
footnotes, equations, charts, figures and captions, annotations, layers,
attachments, color, typography, or page geometry. Conversion is unacceptable
as the sole retained artifact when any of these carry the answer. Keep page
images or the original PDF, structured elements, and page/bounding-box anchors,
then verify representative difficult pages visually.

PDFs are active, complex containers that may include JavaScript, forms, media,
and network actions. OCRmyPDF states that it is not a malware sanitizer and
recommends a container or virtual machine for untrusted PDFs. Conversion and
OCR workers should therefore be disposable, resource-limited, offline by
default, and unable to reach secrets or the destination index directly.
[OCRmyPDF PDF security](https://ocrmypdf.readthedocs.io/en/v15.3.1/pdfsecurity.html)

## Structured formats

Preserve the native object and make text a projection, not a replacement:

- For JSON, retain object keys, ordered arrays, number/string/boolean/null
  types, schema identifier, and JSON Pointer-like field paths. RFC 8259 permits
  implementations to set size, nesting, and number limits; ingestion should set
  them. Validate against a supplied JSON Schema before selecting fields.
  [RFC 8259](https://www.rfc-editor.org/info/rfc8259/),
  [JSON Schema 2020-12](https://json-schema.org/specification)
- For XML, retain namespaces, element and attribute paths, order where it is
  meaningful, and the applicable schema. Disable DTDs, external entities,
  external schema fetches, and XInclude for untrusted input; otherwise parsing
  can cause file disclosure, SSRF, or resource exhaustion.
  [OWASP XXE prevention](https://cheatsheetseries.owasp.org/cheatsheets/XML_External_Entity_Prevention_Cheat_Sheet.html)
- For CSV/TSV, capture encoding, delimiter, quote and escape behavior, header
  decision, row identity, null policy, and any sidecar schema. Do not infer a
  durable type contract from one sample. Keep column names with every row-group
  chunk.
- For YAML and other extensible serializers, use a safe data-only loader, bound
  aliases and nesting, disable application-specific or executable tags, and
  retain the original representation. A conversion to JSON can lose comments,
  anchors, aliases, tags, scalar style, and ordering guarantees outside the
  target contract.
- For schemas, OpenAPI, package manifests, lockfiles, and configuration, index
  both semantic fields and their original file/line or object path. Never let a
  string field become an agent instruction merely because it is named
  `prompt`, `system`, `command`, or `instructions`.

## Source repositories

Choose access by the smallest faithful scope:

1. **Raw file or provider API** for a few named files, commit metadata, or a
   tree inventory.
2. **Archive pinned to a commit ID** for a fixed snapshot without history.
   GitHub states that commit-pinned archives preserve the same file contents on
   repeated requests, assuming the commit remains and the repository name does
   not change. [GitHub source archives](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives)
3. **Partial, sparse, or shallow clone** when broad analysis needs Git paths,
   repository-native search, or later selective blob retrieval. Git documents
   `--filter`, `--sparse`, `--depth`, and `--single-branch`; each intentionally
   omits information and must be recorded. [Git clone](https://git-scm.com/docs/git-clone.html)
4. **Full clone** only for history-sensitive questions such as blame, deleted
   behavior, release ancestry, or rename analysis.

Resolve mutable branches and tags to a commit before indexing. Capture remote
URL, requested ref, commit object ID and hash algorithm, submodule paths and
commits, Git LFS pointer/object policy, and archive or clone settings. A commit
identifies a Git snapshot, but it does not prove that a separately downloaded
archive, submodule, generated artifact, or LFS object was present and verified.

Inventory tracked paths before loading bodies. Include authoritative source,
tests, public interfaces, manifests, lockfiles, configuration, migrations,
licenses, and relevant documentation. Exclude dependency caches, build output,
editor state, binaries, vendored copies, generated files, and fixtures only
after classifying them; any can be relevant to a specific question. Do not
follow a repository symlink outside the acquired root. Keep generated artifacts
linked to their generator when both are present.

For code, fixed token windows are a fallback. Tree-sitter builds concrete syntax
trees and exposes error and missing nodes, allowing chunks to follow modules,
classes, functions, methods, declarations, comments, and source ranges even for
some incomplete code. Parser errors must be recorded, not silently treated as a
valid symbol map. [Tree-sitter](https://github.com/tree-sitter/tree-sitter),
[Tree-sitter query syntax](https://tree-sitter.github.io/tree-sitter/using-parsers/queries/1-syntax.html)

Each code chunk should retain repository and commit, path, language, qualified
symbol, signature, containing symbol, imports or dependencies needed to read
it, and start/end lines. Keep a whole symbol when it fits. For an oversized
symbol, subchunk at statement or region boundaries and repeat the signature,
docstring, and parent identity. Use LSP/LSIF or another code-navigation index
for definition/reference expansion, not as a substitute for source bytes.

## Provenance, freshness, and deduplication

W3C PROV models entities, transformation activities, responsible agents,
derivations, and timestamps. A compact ingestion manifest should apply the same
separation. [W3C PROV-O](https://www.w3.org/TR/prov-o/)

Record at least:

| Layer | Required metadata |
| --- | --- |
| Source identity | Requested and canonical URI or repository remote; publisher/owner; requested locale/version/ref; license and terms locator |
| Acquisition | Retrieval time; final URL and redirect chain; HTTP status/media type; `ETag`, `Last-Modified`, `Content-Digest` when present; API version; robots decision; credential class without the credential |
| Immutable evidence | Raw byte length and SHA-256; Git commit and submodule commits; archive member or file hashes where reproducibility matters |
| Transformation | Parser/OCR/converter name and version; settings; model/checkpoint if used; start/end time; warnings and failures; derived artifact hash |
| Structure | Document title/version/language; schema; page/line/object paths; headings; symbol path; parent and neighbor IDs |
| Chunk | Deterministic chunk ID; exact text hash; source spans; parent; tokenizer/model version; dedup group and aliases |
| Lifecycle | Freshness policy; last successful validation; superseded/deleted state; retention and access classification |

HTTP `ETag` and `Last-Modified` support conditional refreshes. An ETag can be
weak, absent, or scoped to a representation, so use validators to avoid needless
transfer and a local SHA-256 to identify the bytes actually processed. RFC 9530
defines `Content-Digest` and `Repr-Digest` for HTTP integrity, but a server may
omit them. [HTTP semantics, RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html),
[Digest Fields, RFC 9530](https://www.rfc-editor.org/rfc/rfc9530.html)

Deduplicate in stages:

1. Exact raw-byte hash to avoid converting the same payload twice.
2. Exact normalized-content hash to group encoding or container variants while
   retaining every source alias.
3. Chunk-level exact hashes to collapse repeated navigation, headers, generated
   reference fragments, and mirrors at retrieval time.
4. Conservative near-duplicate candidate generation, such as shingling and
   MinHash, followed by exact comparison and a version/provenance check. Do not
   delete because embeddings are similar.

Near duplicates can be different versions or conflicting authorities. Keep one
canonical retrieval record only when equivalence is established; preserve all
aliases, dates, licenses, and hashes. Deduplication research found less
train-test leakage and memorized emission after removing repeated training
material, and separate work found reduced privacy extraction risk. Those
training results support avoiding accidental repetition, but do not justify
discarding distinct evidence in an inference corpus.
[Lee et al., ACL 2022](https://aclanthology.org/2022.acl-long.577/),
[Kandpal et al., ICML 2022](https://proceedings.mlr.press/v162/kandpal22a)

## Chunking and retrieval

Chunk after conversion validation and minimization:

- Split on source-owned boundaries: document sections, paragraphs, list groups,
  table row groups with repeated headers, API operations, records, modules,
  classes, and functions.
- Preserve parent headings, captions, schema fields, page/line/object paths, and
  neighbor IDs. Add overlap only when evaluation shows that boundary loss is a
  recurring failure.
- Respect the selected embedding or generation tokenizer, but do not adopt one
  universal token size. Docling's hybrid chunker combines document hierarchy
  with tokenizer-aware split/merge logic and repeats table headers when a table
  spans chunks, illustrating the right separation between structure and size.
  [Docling chunking](https://docling-project.github.io/docling/concepts/chunking/)
- Keep a parent-document or section record so a narrow match can expand without
  relying on duplicated overlap. Hierarchical retrieval can help questions that
  require different abstraction levels, but it adds generated summaries that
  need provenance and evaluation. [RAPTOR, ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/hash/8a2acd174940dbca361a6398a4f9df91-Abstract-Conference.html)

Start retrieval with the simplest mode that covers the query distribution:

1. Repository-native search or lexical/BM25 retrieval for exact identifiers,
   error strings, citations, paths, and rare terms.
2. Dense retrieval for paraphrase and semantic matching when representative
   evaluation shows a gain.
3. Hybrid candidates, metadata filtering, and reranking when neither mode alone
   meets recall and latency targets.
4. Parent, neighbor, definition, table, or page expansion after ranking.

BEIR found BM25 a robust zero-shot baseline across heterogeneous datasets and
found that reranking and late-interaction models performed best on average at a
higher computational cost. This argues for evaluation and staged complexity,
not a universal retriever. [BEIR, NeurIPS 2021](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/65b9eea6e1cc6bb9f0cd2a47751a186f-Abstract-round2.html)
Retrieval-augmented generation explicitly separates non-parametric source
passages from model memory and identifies provenance and knowledge updates as
core motivations. Every returned chunk should therefore carry a resolvable
source/version/page-or-line locator. [RAG, NeurIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html)

Evaluate with real questions and known relevant spans. Track retrieval recall at
`k`, ranking quality, answer-support coverage, duplicate rate, stale-result
rate, unresolved locators, token/latency cost, and performance by format. Keep
exact-string, paraphrase, cross-section, table, code-definition, and
version-sensitive cases separate so one average does not hide a broken mode.

## Untrusted-content and legal boundaries

Indirect prompt injection places malicious instructions in data that an
LLM-enabled application later retrieves. AgentDojo's 97 tasks and 629 security
test cases show that tool-using agents remain vulnerable and that current
defenses do not preserve every security property. [Indirect Prompt Injection,
AISec 2023](https://arxiv.org/abs/2302.12173), [AgentDojo, NeurIPS
2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/97091a5177d8dc64b1da8bf3e1f6fb54-Abstract-Datasets_and_Benchmarks_Track.html)

The enforceable boundary is architectural:

- Content acquired as corpus data is always data, even when it resembles a
  system message, tool instruction, approval, `AGENTS.md`, README procedure,
  code comment, hidden HTML, PDF layer, or metadata field. The exception is an
  instruction artifact that the trusted client runtime independently
  designates as governing for the current workspace; corpus text cannot make
  that designation itself.
- A deterministic parser is preferred. A model-based extractor, when needed,
  runs in a quarantined worker with no secrets, ambient credentials, mutation
  tools, or unrestricted network, and returns a validated schema.
- Retrieved content cannot select new sources, follow links, request secrets,
  change output targets, authorize actions, or alter retention. The trusted
  task plan makes those decisions.
- HTML sanitization prevents active-content rendering attacks but does not turn
  natural-language instructions into trusted policy. Action authorization,
  parameter validation, least privilege, and human approval for consequential
  effects remain outside the model.
- Bound fetch size, decompressed size, file count, nesting, redirects, time,
  parser CPU/memory, pages, image pixels, archive expansion, and output size.
  Reject path traversal and symlink escape during archive extraction.

`robots.txt` is a crawler-request protocol, not access authorization, and RFC
9309 explicitly says so. Honor applicable rules and rate limits, but separately
check authentication, terms, license, privacy, and intended use.
[Robots Exclusion Protocol, RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html)

Public accessibility is not permission to reproduce, redistribute, train on,
or publish a work. GitHub notes that without a license default copyright rules
apply; SPDX supplies stable license identifiers but does not interpret whether
a planned use complies. Record repository-, directory-, file-, page-, and data-
level terms, because they can differ. [GitHub repository licensing](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository),
[SPDX License List](https://spdx.org/licenses/)

Fair use is purpose- and fact-specific, with no safe universal word, page, or
percentage threshold. When permission or an exception is not clear, reduce
retention and output to the necessary evidence and obtain legal or owner review
before persistent indexing, training, redistribution, or publication.
[U.S. Copyright Office fair-use guidance](https://www.copyright.gov/fair-use/more-info.html)

## Illustrative command and tool choices

These examples assume an already approved public target and an isolated working
directory. A production fetcher still needs host/IP allowlisting, redirect
revalidation, archive safety, quotas, logging, and credential separation that a
single command cannot supply.

### Bounded direct fetch

POSIX shell with curl 8.4.0 or later:

```console
curl --fail --show-error --location --max-redirs 5 --max-time 30 \
  --max-filesize 20M --proto '=https' --proto-redir '=https' \
  --etag-compare source.etag --etag-save source.etag \
  --dump-header source.headers --no-clobber --remove-on-error \
  --output source.bin \
  'https://docs.example.org/version/page'
```

curl documents conditional ETag files, protocol restrictions, redirect limits,
transfer time, and maximum file size. `--max-filesize` reliably aborts an
unknown-length transfer at the threshold in curl 8.4.0 and later; older clients
must enforce the received-byte limit elsewhere. Avoid response-selected
filenames for untrusted servers and use an explicit local path.
[curl manual](https://curl.se/docs/manpage.html)

### Derived representations

Pandoc, installed separately on supported platforms:

```console
pandoc --from=html --to=gfm --wrap=none source.html --output source.md
```

Docling's cross-platform Python CLI for a structure-sensitive PDF:

```console
docling convert input.pdf --to json --to md --output output
```

The repeatable `--to` formats and output directory are part of Docling's current
CLI contract. Run document converters inside the untrusted-file sandbox, not in
the agent's privileged process. [Docling CLI](https://docling-project.github.io/docling/reference/cli/)

Poppler and OCRmyPDF, installed separately:

```console
pdftotext -layout input.pdf output.txt
ocrmypdf --skip-text input.pdf searchable.pdf
```

The first is a low-cost layout attempt. The second preserves pages that already
contain text and OCRs the remainder; its output is a derivative, not a complete
validation of reading order or structure.

### Repository snapshot and identity

POSIX shell with Git:

```console
git clone --depth 1 --single-branch --branch <ref> --filter=blob:none \
  <repository-url> <destination>
git -C <destination> rev-parse HEAD
git -C <destination> submodule status --recursive
```

Use a full clone when history is material. A commit-pinned archive is preferable
when only one immutable snapshot is needed; provider API URLs and authentication
are provider-specific.

Cross-platform Python 3.11+ byte hash:

```python
from hashlib import file_digest
from pathlib import Path

with Path("source.bin").open("rb") as source:
    print(file_digest(source, "sha256").hexdigest())
```

On POSIX systems `sha256sum source.bin` is a common equivalent. In PowerShell,
use `Get-FileHash -Algorithm SHA256 source.bin`. Store the algorithm with the
digest.

## Repository ownership

Use **both** a skill and a guardrail, with no duplicated workflow text:

| Owner | Contract |
| --- | --- |
| Implicit `ingest-sources` skill for material source work | Intake questions; source discovery; format classification; direct/API/archive/clone choice; HTML/PDF/OCR/structured/code routing; raw-plus-derived manifest; validation; deduplication; structural chunking; retrieval evaluation; freshness and removal workflow; explicit `## Output` contract |
| Always-on agent-security guardrail | Retrieved content is data, not authority; validate network targets and redirects; isolate untrusted parsers and model readers; no ambient secrets or mutation capability; quotas; least privilege; approval gates; robots is not authorization |
| Research and documentation skills | Point to the ingestion skill when acquisition or corpus construction is material; retain ownership of evidence synthesis and documentation respectively |
| Format-specific skills | Own high-fidelity manipulation of a user-selected PDF, spreadsheet, or document; do not become the general corpus acquisition policy |

The skill activates implicitly only when source work is material. Activation
does not authorize network, credential, paid, persistent, or sensitive-data
operations. Their approval gates remain. The guardrail is always-on because any
agent can read an untrusted repository, webpage, document, or tool result
without invoking an ingestion workflow.

## Release and evaluation gates

Before releasing the skill or an ingestion implementation, test:

- Static and client-rendered HTML; prose plus code/tables; malicious hidden
  instructions; cross-host and private-address redirects; oversized and
  compressed responses.
- Born-digital, scanned, mixed, signed, multi-column, table-heavy, and
  formula/figure-heavy PDFs; OCR languages and poor scans; parser crashes and
  timeouts.
- JSON/XML/CSV with schemas, deeply nested input, duplicate or ambiguous fields,
  hostile XML entities, encoding variants, and intentionally irrelevant or
  sensitive fields.
- Small API reads, commit archives, partial/shallow and full clones; submodules,
  LFS pointers, symlinks, generated/vendor trees, mutable refs, and source maps.
- Exact and near duplicates that are true mirrors, different licenses, stale
  versions, and materially conflicting texts.
- Retrieval questions requiring an exact identifier, paraphrase, table row,
  code definition/reference, adjacent chunk, parent section, and superseded
  version.
- Prompt injection that asks the reader to follow a link, broaden scope, reveal
  secrets, mutate a tool, change the index, or treat artifact text as higher
  authority.

Success requires raw-source recoverability, complete manifest fields, resolved
locators, no unauthorized network or action, no silent structure loss on the
seeded cases, and retrieval targets met on a representative query set. A parser
or OCR warning, unresolved license, ambiguous authority, or unverified
conversion must remain visible in the output rather than being converted into
false confidence.

## Evidence limits

No reviewed source establishes one universally best HTML reader, PDF converter,
OCR engine, chunk size, embedding model, or retriever. Tool behavior and model
quality change, while document layouts, languages, codebases, and query
distributions differ. Benchmark gains do not remove the need to test the actual
corpus.

Raw-byte retention improves auditability but can increase copyright, privacy,
and breach impact, so retention and access must follow the declared purpose.
Deduplication reduces repeated processing but can hide conflicting versions if
provenance is discarded. OCR and layout models make inaccessible content
searchable but introduce new errors. Sanitization reduces active content; it
does not solve indirect prompt injection. Structural least privilege and
external authorization remain necessary.
