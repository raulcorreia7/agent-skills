# Curate And Retrieve

Preserve source aliases and provenance through every reduction step.

## Minimize And Deduplicate

1. Remove sources, records, fields, and sections that do not support the
   approved questions or required context.
2. Group exact raw-byte matches by SHA-256. Convert one payload, but retain all
   source aliases, dates, licenses, and validators.
3. Group exact normalized-content matches only when normalization rules are
   recorded and the original bytes remain available.
4. Collapse exact repeated chunks at retrieval time. Keep source spans and
   aliases for each chunk.
5. Use near-duplicate methods only to propose candidates. Compare candidates
   directly before consolidation.
6. Keep versions or sources separate when authority, license, date, or meaning
   differs. Use embedding similarity only to propose comparisons.

## Chunk

Split on source-owned boundaries:

- Document sections, paragraphs, list groups, and table row groups.
- API operations, schema objects, records, and field groups.
- Repository modules, classes, functions, methods, and declarations.

Preserve parent headings, table headers, captions, schema fields, page or line
spans, object paths, symbol identity, and neighbor IDs. Keep parent records so
a result can expand without duplicated overlap.

Use the selected embedding or generation tokenizer. Set chunk size from the
source and retrieval evaluation. Add overlap only when evaluation shows
recurring boundary loss.

## Retrieve And Expand

1. Start with repository-native or lexical search for identifiers, paths,
   error text, citations, and rare terms.
2. Add dense retrieval only when paraphrase tests show a material gain.
3. Add hybrid candidates, metadata filters, or reranking only when simpler
   retrieval misses the target quality.
4. Return a small evidence set. Expand a parent, neighbor, table, definition,
   or page only when the question requires it.
5. Attach a resolvable source, version, page, line, object, or symbol locator to
   every result.

## Evaluate And Refresh

Use representative questions with known relevant spans. Measure retrieval
recall, ranking quality, answer support, duplicates, stale results, unresolved
locators, latency, and token cost. Separate exact, paraphrase, table, code,
cross-section, and version-sensitive cases.

Use HTTP validators or repository refs to detect change. Hash acquired bytes to
identify the processed representation. Reprocess changed sources and mark old
derivatives as superseded. Propagate access revocation and source deletion
through raw artifacts, derivatives, chunks, indexes, and caches.

## Example

A version-migration query first retrieves the exact API operation name and
version. It then expands to the operation's parent section and referenced
schema. The result keeps the page, object path, source version, and raw artifact
hash. It does not load unrelated chapters or another product version.

## Sources

- [HTTP Semantics, RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html)
- [W3C PROV-O](https://www.w3.org/TR/prov-o/)
- [Lost in the Middle, TACL 2024](https://aclanthology.org/2024.tacl-1.9/)
- [BEIR, NeurIPS 2021](https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/65b9eea6e1cc6bb9f0cd2a47751a186f-Abstract-round2.html)
- [Retrieval-Augmented Generation, NeurIPS 2020](https://proceedings.neurips.cc/paper/2020/hash/6b493230205f780e1bc26945df7481e5-Abstract.html)
