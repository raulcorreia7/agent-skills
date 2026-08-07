# Word Count

## Counting Rules

| Rule | Operational check | Official PDF pages |
|---|---|---|
| 8.4 | Treat a colon before a vertical list as the end of the lead sentence. Count each list item as a separate sentence. | 107, 110–111 |
| 8.5 | Count parenthetical text as one word in the sentence that contains it. Examine the parenthetical text separately. | 107, 111 |
| 8.6 | Count each specified atomic element as one word. | 107, 111–114 |
| 8.7 | Count a no-space hyphenated term as one word. | 107, 114 |


## Atomic Counts

Count each of these as one word:

- A number.
- A number plus its unit, also when the unit has more than one word.
- An approved abbreviation.
- An identifier.
- Immutable quoted text, formula, referenced title, heading, placard, or label.
- A full proper name.
- A no-space hyphenated term.

Do not count structural document, paragraph, or work-step numbering. Do count
inline step references. A reliable count needs document structure and explicit
annotations or project lists for units, abbreviations, identifiers, names, and
immutable spans. Do not infer an immutable quotation from uppercase text alone.

Example token trace:

```text
Tighten | bolt | B7 | to | 10 N m
```

The sentence `Tighten bolt B7 to 10 N m.` has five counted words when `B7` is
an identifier and `N m` is the applicable unit.

Source: Rules 8.6–8.7, official PDF pages 111–114.

## Automation Boundary

Deterministic checks include structured list boundaries, structural-number
exclusions, and explicitly annotated atomic spans. Units, abbreviations,
composite identifiers, titles, and names require project data. Unknown
proper-name boundaries require review.

NOTE: Three printed example totals on official PDF pages 113–114 appear to be
one word too high. Use the Rule 8.6 method. Preserve an auditable token trace.
Identify the discrepancy if one of those examples is material.
