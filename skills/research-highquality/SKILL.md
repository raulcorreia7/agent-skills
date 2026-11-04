---
name: research-highquality
description: Manual invocation only. High-quality research for broad or contested external questions with traceable claims, source appraisal, conflict analysis, and explicit coverage.
---

# High-quality research

## Job

Answer a broad or contested external research question with a concise synthesis.
Make each material claim traceable to a current source.

## Steps

1. Define the question, audience, as-of date, exclusions, source boundary, and
   output. Divide the question into core, background, and follow-up questions.
   Define sufficient evidence before the search; let sufficiency, not a fixed
   source or word count, set the stopping point. When the user requests
   delegated research and independent parallel passes offer a clear coverage or
   time benefit, read [delegated-research.md](references/delegated-research.md);
   otherwise process the questions sequentially. Complete when each core
   question has a sufficiency criterion.
2. Search with varied terms. Before choosing or appraising a decisive source,
   read [appraisal.md](references/appraisal.md) to match the source type to the
   claim. For a question about practice or tool maturity, also read
   [practice-maturity.md](references/practice-maturity.md) and keep consensus
   separate from evidence of effectiveness or operational maturity. Open each
   source and cite the opened source, never a search snippet. For each material
   atomic claim, note the canonical locator, exact support, date, source status,
   support state, limits, and conflicting evidence, in proportion to the task.
   Treat copied or syndicated pages as one provenance root. Complete when every
   material claim has a note from an opened source.
3. For conflicting evidence, compare definitions, dates, scope, population,
   method, directness, reliability, and provenance. Resolve a conflict only on
   that comparison, never by repetition, order, source count, or user
   preference. Complete when each material conflict is resolved on stated
   grounds or preserved as open.
4. Synthesize only from the verified evidence notes. Lead with the finding that
   affects the decision. Put each citation beside the claim that it supports.
   Separate facts, source-reported results, inferences, and unknown information.
   Identify a preprint, workshop paper, vendor study, or other source status
   when the status affects confidence. Make the report proportional to the
   decision. Complete when every material claim in the draft carries a citation
   or an evidence-state label.
5. Verify the report. Divide each material external statement into atomic
   claims. Confirm that each link opens the inspected source. Check full
   support, citation completeness, time validity, source ownership, and
   conflicts. Revise, divide, qualify, or remove an unsupported claim. Use an
   automated judge only for triage; manually inspect each decisive or disputed
   claim. Claim an exhaustive or systematic review only with a reproducible
   search and screening method. Complete when the core questions meet their
   sufficiency criteria and every remaining gap is explicit.

## Flow

```text
question ← scope, boundary, sufficient evidence
per question → search → open → note(locator, date, status, limits)
conflict ← compare; keep material ones open
synthesis ← notes only, citation per claim
verify claims and links
stop: core questions sufficient, gaps explicit
```

## Guardrails

- Relevance does not establish reliability. Multiple URLs do not establish
  independent corroboration.
- Source status is metadata, not a verdict. Official material can be stale.
  Papers can have weak methods, books can be outdated, and community practice
  can precede formal guidance.
- Citation presence does not establish citation correctness or completeness.
- Fill evidence gaps only from inspected sources, never from model memory.
  State confidence in words tied to the evidence, not uncalibrated numbers.
- Narrow, qualify, ask, or leave a claim unresolved when evidence is
  insufficient.
- Measure research depth by evidence sufficiency, not source count, delegation
  count, or report length.
- Protect credentials, private content, paywalled content, and personal data.

## Composition

- Use `docs` when the primary output is a guide, specification, runbook, or
  other document beyond a research report.
- Use `audit` for repository or system-state inspection.
- Apply `adversarial-review` only after the report and evidence packet are
  stable. Its reviewers do not browse. Include inspected source text or local
  source artifacts when source verification is a criterion.
- Acquire, convert, or curate sources through `ingest-sources`; this report
  keeps appraisal and citation ownership.

## Output

Return:

- The research question, audience, as-of date, boundary, and material exclusions.
- Concise findings with a canonical citation for each material claim.
- Evidence and publication status, conflicts, limits, and coverage gaps.
- The next verification step only for a material unresolved claim.
- A self-contained response by default. Write or update a Markdown file only when the user explicitly requests persistence and names or approves the destination.
