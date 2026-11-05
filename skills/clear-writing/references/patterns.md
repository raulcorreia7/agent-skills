# Patterns

Three tiers. Fix the first tier wherever it appears. Fix the second tier when
it clusters: one instance is ordinary writing, several in a paragraph or the
same one in every paragraph is a tell. Never remove the third tier to make text
shorter or plainer.

Evidence key: S is peer-reviewed and quantified, M is one study, a preprint,
or an expert taxonomy, and W is practitioner consensus. The IDs point to
[sources](sources.yml).

## Always fix

These add nothing a reader needs, in any register.

| Pattern | Example | Safe fix | Evidence |
| --- | --- | --- | --- |
| Preamble or restating the question | "Great question! Let's dive in." | Start with the answer. | M (A10, C6) |
| Validation and flattery | "You're absolutely right to ask." | Delete it. Agree only when the evidence supports it, and give the reason. | S for the behaviour (A14); the phrase link is inferred |
| Closing offers | "Let me know if you'd like me to expand on any of this!" | Delete it. If the reader has a real next decision, name it. | W |
| Summary that repeats the body | "In summary, the migration improves speed, safety, and cost." after a paragraph saying so | Delete it. A long document may open with a short summary instead. | M (B1, 18% of expert edits) |
| Padding | "It is worth noting that the cache is cleared on restart." | "The cache clears on restart." Cut any sentence with no new claim, step, or reason. | S (A17, A18) |
| Filler phrases | "please note", "at this time", "simply", "easy" in instructions | Delete, or use "now". | W (C5) |
| Stacked or empty hedges | "It may potentially be possible that the job fails." | "The job can fail." Keep one hedge that matches the evidence. | M (D5) |
| False certainty | "This fixes the leak." when it was tested once | "This fixed the leak in one test run." | S (A15) |
| Generic claims and clichés | "plays a crucial role in today's fast-paced world" | A concrete example, number, or name, or cut it. | S (B1) |
| Mannered prose | "a rich tapestry of interlocking services" | Say it literally: "twelve services that call each other". | S (B1); P1 |
| Promotional register outside marketing | "a powerful, game-changing API" | State the capability: "an API that batches up to 500 writes". | M (C10) |
| Nested clauses | "The value that the function that parses the header returns is cached." | Main clause first: "The header parser's return value is cached." | S (C12) |
| Over-length for the question | Three paragraphs answering a yes-or-no question | Answer at the length the question needs. On an ambiguous request, answer the likely reading or ask, rather than covering every reading. | M (N4) |

## Fix when clustered

Each of these is legitimate on its own. Fix the cluster, keep the instance
that does real work.

| Pattern | Example | Safe fix | Evidence |
| --- | --- | --- | --- |
| Style verbs | delve, underscore, showcase, foster, leverage, navigate (figurative) | The plain verb for the actual action: shows, uses, improves. Keep literal uses, such as navigating a menu. | S (A1, A5) |
| Inflated adjectives and intensifiers | crucial, comprehensive, robust, seamless, pivotal, notably | The specific property: "handles 10,000 requests a second". If there isn't one, delete. | S (A1) |
| Ornate nouns | tapestry, landscape, realm, testament, journey | The literal noun. | S (A6) |
| Additive openers | "Additionally, … Moreover, … Furthermore, …" | Use "also", or merge the sentences. | S for "additionally" (A1); additive links can lower comprehension (D6) |
| Trailing participle clauses | "The script runs nightly, ensuring that backups stay fresh." | "The script runs nightly so backups stay fresh." Keep one that describes a truly simultaneous action. | S (A6, 2–5 times the human rate) |
| Nominalization stacks | "the implementation of the validation of input" | A verb with an actor: "the parser validates input". | S (A6, about twice the human rate) |
| Reflexive triplets | "clear, concise, and comprehensive" | Keep the items that carry distinct content. Two or four is fine when that's the true count. | S for coordination (A6); W for triplets |
| "Not X, but Y" | "It's not just a tool, it's a platform." | State Y. Keep the contrast only when the reader actually believes X. | M (A9, up to 6.3 times the human rate) |
| Uniform openings and rhythm | Every paragraph opens with a topic sentence, adds three supports, and closes on a wrap-up line | Vary shape where the content allows. Keep terms consistent. | S (A8); M (N2, N8) |
| Em dashes in density | Four em dashes in one paragraph | Swap most for commas, colons, parentheses, or a full stop. Keep the ones that work. | Contested (N9, N11); standard punctuation in C6 |
| Markdown inflation | Headings and bullets on a four-sentence answer; bold scattered through prose | Prose for reasoning and short answers; lists for parallel items or steps. | W–M (N9, A10) |
| Creative clichés | "her voice barely a whisper", "his heart hammered", "light flickered" | A concrete image of your own, or drop it. | S (A9) |

## Never strip

Removing these makes text shorter and worse.

| Keep | Example | Why | Evidence |
| --- | --- | --- | --- |
| Causal and contrastive connectives | because, so, therefore, however, unless | Readers use them to link ideas, and readers without background or reading in a second language rely on them most. | S (D3, D4, D6) |
| Hedges that carry real uncertainty | "likely", "in our tests on Linux", "we haven't measured this" | They mark scope and evidence strength. Models already under-hedge. | S (D5, A15) |
| The why | "Retry once, because the first call warms the cache." | Rationale is what change records, comments, and design text exist to carry. | Practice (C8, C9) |
| Passives where the actor is unknown or irrelevant | "The file was deleted at 03:00." | Inventing an actor adds a false claim. Models already use fewer actorless passives than people do. | S (A6, C13) |
| Terms of art | idempotent, tort, p-value, mise en place | The exact term is clearer to its readers than a plain paraphrase. Define it once if the reader may not know it. | Practice (C5) |
| Author voice in creative and personal work | dialect, rhythm, a deliberate fragment | Naturalness means fit to the author and audience, not one house style. | S (B4, A19) |
| Specifics that add length | numbers, names, conditions, error causes | Length that carries information isn't padding. | S (B1, A10) |
| Explicit links for newcomers | "First…, then…, which means…" in a tutorial | Readers with little background learn more from text that spells out the links. | S (D1, D2) |

## Word list

Signals, not proof. Each word is ordinary English; the signal is density
across a passage, and the fix is a more precise word, never a ban. The list is
English only and drifts with each model generation, so treat it as dated to
the review in [sources](sources.yml). The structural patterns above apply in
any language.

- Verbs: delve, underscore, showcase, foster, leverage, enhance, emphasize,
  navigate (figurative), exhibit.
- Adjectives and adverbs: crucial, pivotal, comprehensive, robust, seamless,
  palpable, notably, particularly.
- Nouns: tapestry, landscape, realm, testament, camaraderie, insights.
- Connectives: additionally, moreover, furthermore.
- Fiction: shimmered, flickered, "voice barely a whisper", the name Elara.

Sources: A1, A5, A6, A9, N6.

## Notes

- Don't ban the em dash. It's standard punctuation, and the evidence that it
  marks model text comes from preprints, with rates that vary widely by model.
- Don't chase readability scores or sentence-length targets. Formulas miss
  content, structure, and audience (C11); about 25 words is a heuristic for
  general readers, not a limit.
- Don't rely on a model, including yourself, to judge whether text is slop.
  Model judges fail at it (A10, B2). Work from the named patterns and the
  source facts; prompting only "avoid slop" led to reward hacking (N3).
