# Vocabulary and Dictionary Decisions

These compact rules support formal audits and vocabulary verification. They do
not replace the official Issue 9 dictionary.

## Dictionary Decision Path

Apply this path to each unique word in formal vocabulary verification:

1. Find the exact headword and part of speech in an authorized official source.
2. For an approved uppercase entry, match the intended part of speech, approved
   meaning, and listed form. Apply every help note and context restriction.
3. For an unapproved lowercase entry, evaluate each proposed alternative. Use
   direct substitution only when its part of speech and meaning agree. Otherwise,
   reconstruct the sentence.
4. If the dictionary does not authorize the use, apply Rules 1.5–1.11. Determine
   whether the word is a valid technical noun. Then, apply Rules 1.12–1.13 and
   determine whether it is a valid technical verb. This decision also applies
   to an unapproved dictionary entry.
5. If no route applies, do not use the word.

The dictionary has four columns. They contain the word and part of speech, the
approved meaning or alternatives, an STE example, and a non-STE example. It
recognizes noun, verb, adjective, adverb, pronoun, article, preposition, and
conjunction. Nouns appear in singular form. Use normal countable plurals unless
help restricts them. Verbs list only permitted regular,
irregular, auxiliary, or defective modal forms.

Adjectives list permitted comparative and superlative forms when needed.

Adverbs can have form restrictions. An example illustrates one valid
construction. It does not authorize a different meaning or form.

Dictionary help has four mechanics:

1. Usage advice for an approved word.
2. Alternatives for meanings outside an approved word's restricted meaning.
3. A context restriction, such as safety instructions only.
4. Other mandatory information about an approved or unapproved entry, such as
   prohibited forms or when no replacement is necessary.

Source: dictionary introduction, official PDF pages 131–144.

## Rules 1.1–1.14

| Rule | Operational check | Official PDF pages |
|---|---|---|
| 1.1 | Use an approved dictionary word, a valid technical noun, or a valid technical verb. | 45–46 |
| 1.2 | Use an approved word only as its listed part of speech. | 45–47 |
| 1.3 | Use an approved word only with its listed meaning. | 45, 48 |
| 1.4 | Use only the listed forms of verbs and adjectives. | 45, 48 |
| 1.5 | Use a technical noun only when it names a subject-field concept in at least one of the 22 categories below. | 45, 49–53 |
| 1.6 | Use an unapproved word only in the context where it qualifies as a technical noun or part of one. | 45, 53–54 |
| 1.7 | Do not use a technical noun as a verb. | 45, 55 |
| 1.8 | Use terminology approved by the applicable company, industry, or subject field. | 45, 55 |
| 1.9 | If no official source gives a term, select a short, familiar, precise technical noun, normally no more than three words. | 45, 56 |
| 1.10 | Do not select regional, slang, or jargon terms. | 45, 56 |
| 1.11 | Use one technical noun consistently for one item or concept. | 45, 57 |
| 1.12 | Use a necessary technical verb only in a listed category and its specified context. Prefer an accurate approved verb. | 45, 57–60 |
| 1.13 | Do not use a technical verb as a noun. A permitted past participle can be an adjective. | 45, 60 |
| 1.14 | Use the dictionary's American English spelling unless an applicable official directive requires another spelling. Preserve immutable quotations. | 45, 61 |

## Technical-Noun Categories

A project term can use more than one category. The categories are exhaustive.
Their examples in the standard are not exhaustive.

1. Official parts information.
2. Vehicles or machines, and locations on them.
3. Tools and support equipment, their parts, and locations on them.
4. Materials, consumables, and unwanted material.
5. Facilities, infrastructure, and logistic procedures.
6. Systems, components and circuits, their functions, configurations, and parts.
7. Mathematical, scientific, and engineering terms and formulas.
8. Navigation and geographic terms.
9. Numbers, units of measurement, time, and their symbols.
10. Quoted text that cannot change, such as labels, signs, and display text.
11. Professional roles, individuals, groups, organizations, and geopolitical entities.
12. Parts of the body.
13. Common personal effects, food, and beverages.
14. Medical terms.
15. Official documents, parts of documentation, standards, and guidelines.
16. Environmental and operational conditions.
17. Colors. STE treats colors as technical nouns. Do not use comparative or
    superlative color forms.
18. Damage terms.
19. Computer science, information, and communication technology.
20. Civil and military operations.
21. Law and regulations.
22. Animals, plants, and other life forms.

Source: Rule 1.5, official PDF pages 49–53.

## Technical-Verb Categories and Restrictions

Use a technical verb only for the precise process and subject-field context.
It must obey the permitted verb forms and tenses in Section 3.

1. Manufacturing processes:
   - Remove material.
   - Add material.
   - Attach material.
   - Change mechanical strength, structure, or physical properties.
   - Change a surface finish.
   - Change a material's shape.
2. Computer processes and applications:
   - Input and output processes.
   - User-interface and application processes.
   - System operations.
3. Instructions and information for applicable subject fields:
   - Engineering, mathematics, and science.
   - Medicine.
   - Civil and military operations.
   - Navigation.
   - Automotive and railway work.
   - Energy, oil, and gas.
4. Law and regulations. Use these verbs only in legal and regulatory texts such
   as contracts, warranties, certificates, standards, specifications, and
   legal papers.

Prefer an approved verb whenever it gives the meaning accurately. Do not use a
general technical verb when a more precise process verb is necessary. A verb
can qualify in one category and fail in another context. Do not turn a
technical noun into a verb merely because standard English permits it.

Source: Rules 1.12–1.13, official PDF pages 57–60.

## Project-Term Record

Create this table only when domain terms occur:

| Term | Class | Controlled meaning | Category | Approving source | Permitted forms |
|---|---|---|---|---|---|
| `hydraulic pump` | technical noun | Project definition | 1 or 6 | Glossary locator | Singular, plural |
| `ream` | technical verb | Project definition | 1a | Process specification | Listed project forms |

## Recurring-Error Lookup Prompts

These are context-sensitive review prompts, not unconditional replacements:

| Source | Candidate route |
|---|---|
| `acceptable` | `PERMITTED` |
| `alternate` | `ALTERNATIVE` |
| `any` | Omit or reconstruct. |
| `avoid` | `PREVENT` |
| `both` | `THE TWO` as a technical noun. |
| `check`, `cover`, `damage`, `test` as verbs | Use the applicable noun construction. |
| `complete` | `COMPLETED` when the adjective meaning fits. |
| `ensure` | `MAKE SURE` |
| `fit` | `INSTALL` |
| `follow` | `OBEY` only when that meaning fits. |
| `further` | `MORE` |
| `have to` | Use an imperative action verb. |
| `however` | `BUT` |
| `insert` | `PUT` |
| `main` | `PRIMARY` |
| `may` | `CAN` |
| `need`, `required` | Use `NECESSARY` and reconstruct the sentence. |
| `now` | `AT THIS TIME` |
| `old` | `REMAINING`, `USED`, or `EXPIRED`, by meaning. |
| `over` | `ABOVE`, `ON`, or `ALONG`, by meaning. |
| `people` | `PERSON` or `PERSONNEL` |
| `perform` | `DO` |
| `portion` | `PART` |
| `press` | `PUSH` |
| `reach` | `GET` |
| `repeat` | `DO ... AGAIN` |
| `rotate` | `TURN` |
| `secure` | `ATTACH` or `SAFETY`, by meaning. |
| `shall`, `should` | `MUST` when the requirement meaning fits. |
| `since` | `BECAUSE` when causal. |
| `therefore` | `THUS` or `AS A RESULT` |
| `under` | `BELOW`, `IN`, or `LESS THAN`, by meaning. |
| `using` | Use `USE` or `WITH` and reconstruct the sentence. |

Source: recurring errors, official PDF pages 145–146.

## Automation Boundary

Software can find candidate spellings and forms. It cannot determine the
intended part of speech, meaning, technical category, domain approval, agent,
or help restriction reliably. Only an authorized official dictionary lookup
and human technical judgment can finish a formal vocabulary route.
