# Formal ASD-STE100 workflow

Resolve `<skill-root>` as the directory that contains this `SKILL.md`. All
skill files and commands below are relative to that directory.

1. Classify each block as a `procedure` or `description`. Apply the safety
overlay to text that controls a risk.
2. Read [core rules](core-rules.md), then read each applicable branch:
   - Read [procedures](procedures.md) for procedures.
   - Read [descriptions](descriptions.md) for descriptions.
   - For safety text, read both [procedures](procedures.md) and the [safety
overlay](safety.md).
3. Read [word count](word-count.md) or [punctuation](punctuation.md) only when
that decision is material. Read [directive precedence](directive-precedence.md)
when an applicable directive affects the result.
4. For every formal compliance or verification claim, read [official source and
evidence](official-source.md) and inspect an authorized official source. Read
[vocabulary and dictionary decisions](vocabulary.md) when word choice is in
scope. Read [general recommendations](general-recommendations.md) only when the
request includes advisory Issue 9 guidance; report recommendations separately
from normative compliance.
5. Apply the applicable rules to every new or changed in-scope sentence.

For user-requested source acquisition, read [source
acquisition](source-acquisition.md), then use
`<skill-root>/scripts/download.py`. Keep acquisition approval-gated.

Use `<skill-root>/scripts/analyze_text.py` only for a requested or useful
preliminary formal ASD-STE100 check of plain UTF-8 text. The analyzer cannot
verify vocabulary or compliance. Treat `Review` findings as prompts for human
judgment. Run `<skill-root>/scripts/analyze_text.py --help` for its interface.

- Use an authorized official dictionary and every applicable entry field for a
  formal vocabulary-verification claim.
- Treat the official ASD-STE100 Issue 9 PDF as authoritative for formal
  ASD-STE100 work. Local references are operational guidance, not the complete
  standard or dictionary.

Finish when every sentence has a result and every formal compliance or
verification claim has authoritative evidence or an explicit unresolved item.
