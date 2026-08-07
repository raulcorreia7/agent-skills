# LLM-Readable Documentation And llms.txt

Agent-readable surfaces include `llms.txt`, Markdown mirrors, service and SDK
docs, portals, and agent-facing maps.

## Position

- `llms.txt` is a proposed curated Markdown index for inference-time use.
- It is not access control, crawler enforcement, `robots.txt`, a sitemap, or a
  second source of truth.
- Put it at `/llms.txt` for a website or at the root of an intentionally scoped,
  trusted documentation surface.
- Point to canonical docs. Prefer clean Markdown variants when the publisher
  exposes them.
- Use `llms.txt` as a curated publishing boundary, not a second source of
  truth.

## Add It When

- the docs surface is stable and large enough to need a curated route.
- the intended agent and trust boundary are explicit.
- important concepts, setup, APIs, examples, errors, limits, and support paths
  have canonical pages.
- someone or some build process will keep the index current.

Skip or defer when docs are stale, contradictory, too small, sensitive for the
target context, or expected to enforce crawling, training, or licensing rules.

## Shape

1. One H1 naming the site, product, service, or project.
2. A blockquote with scope and audience.
3. Optional brief notes that prevent common wrong assumptions.
4. H2 sections with curated Markdown links.
5. An optional `Optional` section for material outside a small context.

Each entry needs a descriptive title, stable URL, and short explanation of the
question it answers.

```markdown
# Example API

> Public developer documentation for Example API.

Important: sandbox credentials do not work in production.

## Start here

- [Quickstart](https://docs.example.com/quickstart.md): Authentication and a
  first successful request.
- [Concepts](https://docs.example.com/concepts.md): Resources and lifecycle.

## Reference

- [REST API](https://docs.example.com/api/rest.md): Endpoints, pagination, and
  errors.

## Optional

- [Changelog](https://docs.example.com/changelog.md): Versioned changes.
```

## Curation

- Curate. Do not mirror the whole site.
- Separate quickstart, concepts, API/reference, auth, examples, errors,
  changelog, and troubleshooting when those pages exist.
- Use short descriptions that help an agent select the right source.
- Avoid unexplained internal jargon. Link a glossary when needed.
- Exclude secrets, credentials, customer data, private hostnames, and
  privileged operational detail unless the surface is explicitly private and
  trusted.
- Generate from canonical navigation when it is clean and stable. Curate
  manually when generated navigation is noisy.

## Validation

When practical, verify the published path and links. Check important Markdown
mirrors and test realistic and near-miss questions against the expanded
context. Compare answers with canonical docs. A stale index can be worse than
none.

Sources: [llms.txt proposal](https://llmstxt.org/) and [llms-txt repository](https://github.com/AnswerDotAI/llms-txt).
