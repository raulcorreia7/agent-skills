# Web And HTML

Prefer a native API, schema, source repository, or publisher text endpoint
when it contains the required evidence.

## Acquire

1. Confirm the publisher, product version, locale, and exact page set.
2. Use explicit URLs first. Use site maps, navigation, API inventories, and
   publisher search indexes only to discover candidates.
3. Fetch static content directly. Do not run scripts or load remote resources
   during parsing.
4. Apply the network rules and limits in `safety.md`, and accept only
   approved media types.
5. Preserve the request URL, final URL, redirect chain, response headers, raw
   bytes, retrieval time, and byte hash.
6. Use an approved HTML parser or converter on the retained file. Select
   semantic `main` or `article` content. Preserve headings, tables,
   lists, code blocks, warnings, and link targets.
7. Use a main-content heuristic only when page chrome obscures the evidence.
8. Use a browser, in a worker as defined in `safety.md`, only when a static
   comparison proves that required content is absent.
9. Compare the derived output with difficult source sections. Check code,
   tables, warnings, links, and headings.

Do not deduplicate canonical, print, mobile, locale, query, or version variants
until their content and source record establish equivalence.

## Example

For one documentation page, retain `source.html` and derive `source.md`. Record
the requested URL, final URL, response validators, byte hash, converter version,
and the headings checked against the rendered page.

## Sources

- [WHATWG HTML Standard](https://html.spec.whatwg.org/)
- [Robots Exclusion Protocol, RFC 9309](https://www.rfc-editor.org/rfc/rfc9309.html)
- [Sitemaps protocol](https://www.sitemaps.org/protocol.html)
- [OWASP SSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
- [curl manual](https://curl.se/docs/manpage.html)
- [Pandoc manual](https://pandoc.org/MANUAL.html)
