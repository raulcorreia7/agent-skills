#!/usr/bin/env python3
"""Run quick, preliminary ASD-STE100 checks on UTF-8 plain text."""

from __future__ import annotations

import argparse
import bisect
import json
import re
import signal
import sys
from collections.abc import Iterable, Sequence
from pathlib import Path
from typing import NamedTuple


class Finding(NamedTuple):
    offset: int
    end: int
    severity: str
    category: str
    code: str
    rule: str | None
    source: str | None
    explanation: str
    hint: str


SOURCES = {
    "Rule 1.1": "Official PDF pages 45–46 and 145–146",
    "Rule 3.4": "Official PDF pages 67 and 69",
    "Rule 3.5": "Official PDF pages 67 and 70–71",
    "Rule 3.6": "Official PDF pages 67 and 71–75",
    "Rule 3.7": "Official PDF pages 67 and 75",
    "Rule 4.2": "Official PDF pages 77 and 79–80",
    "Rule 5.1": "Official PDF pages 87–88",
    "Rule 6.3": "Official PDF pages 95 and 98–99",
    "Rule 6.6": "Official PDF pages 95 and 101",
    "Rule 8.1": "Official PDF pages 107–108",
    "Rule 9.3": "Official PDF pages 115 and 121",
    "GR-3": "Official PDF page 125",
    "GR-4": "Official PDF page 125",
    "GR-6": "Official PDF page 126",
    "GR-7": "Official PDF pages 126–127",
}

CONTRACTIONS = re.compile(
    r"\b(?:"
    r"(?:are|can|could|did|do|does|had|has|have|is|might|must|need|should|was|were|will|would)n['’]t"
    r"|(?:here|how|it|that|there|this|what|when|where|who|why)['’]s"
    r"|(?:I|you|we|they|he|she|it)['’](?:d|ll|m|re|ve)"
    r"|let['’]s"
    r")\b",
    re.IGNORECASE,
)
ING_WORD = re.compile(r"\b[A-Za-z][A-Za-z-]*ing\b", re.IGNORECASE)
PASSIVE = re.compile(
    r"\b(?:am|is|are|was|were|be|been|being|become|becomes|became|stay|stays|stayed)"
    r"(?:\s+[A-Za-z]+ly)?\s+[A-Za-z]+(?:ed|en)\b",
    re.IGNORECASE,
)
STACKED_AUXILIARY = re.compile(
    r"\b(?:(?:have|has|had)\s+(?:been\s+)?[A-Za-z]+(?:ed|en)"
    r"|(?:can|could|may|might|must|shall|should|will|would)\s+(?:have\s+)?be(?:en|ing)?\s+[A-Za-z]+(?:ed|en))\b",
    re.IGNORECASE,
)
NOMINALIZATION = re.compile(
    r"\b(?:adjustment|application|completion|connection|installation|inspection|measurement|operation|removal|replacement|selection|verification)\s+of\b",
    re.IGNORECASE,
)
PHRASAL_VERB = re.compile(
    r"\b(?:carry\s+out|check\s+out|look\s+at|set\s+up|shut\s+down|switch\s+(?:on|off)|turn\s+(?:on|off))\b",
    re.IGNORECASE,
)
RECURRING_ERROR = re.compile(
    r"\b(?:acceptable|alternate|any|avoid|both|check|complete|cover|damage|ensure|fit|follow|further|have\s+to|however|insert|main|may|need|required|now|old|over|people|perform|portion|press|reach|repeat|rotate|secure|shall|should|since|test|therefore|under|using)\b",
    re.IGNORECASE,
)
LATIN_ABBREVIATION = re.compile(r"(?<!\w)(?:e\.g\.|i\.e\.|etc\.)(?!\w)", re.IGNORECASE)
GENDERED_PRONOUN = re.compile(r"\b(?:he|she|him|her|his|hers)\b", re.IGNORECASE)
BARE_THIS = re.compile(
    r"\bthis\b(?=\s+(?:can|cannot|does|has|is|may|must|was|will)\b|\s*[.,:;!?]|$)",
    re.IGNORECASE,
)
ANTI_SLOP = re.compile(
    r"\b(?:delve|game[- ]changer|in\s+order\s+to|it\s+is\s+(?:important|worth)\s+noting|leverage|seamlessly)\b",
    re.IGNORECASE,
)
ABBREVIATION_AT_END = re.compile(
    r"\b(?P<abbreviation>e\.g\.|i\.e\.|etc\.|fig\.|no\.|mr\.|mrs\.|ms\.|dr\.|prof\.)$",
    re.IGNORECASE,
)
TITLE_ABBREVIATIONS = {"dr.", "mr.", "mrs.", "ms.", "prof."}

APPROVED_ING_WORDS = {
    "during",
    "lighting",
    "mating",
    "missing",
    "opening",
    "remaining",
    "routing",
    "servicing",
    "something",
}


def parser() -> argparse.ArgumentParser:
    examples = """Examples:
  analyze_text.py --type procedure maintenance.txt
  analyze_text.py --type description --format json < overview.txt

Exit status:
  0  No violations. Review findings can still be present.
  1  One or more violations.
  2  Invalid arguments or unreadable input.
"""
    result = argparse.ArgumentParser(
        description="Run quick, non-certifying ASD-STE100 checks on a UTF-8 file or standard input.",
        epilog=examples,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    result.add_argument("--type", choices=("procedure", "description"), required=True, dest="text_type")
    result.add_argument("--format", choices=("text", "json"), default="text", dest="output_format")
    result.add_argument("file", nargs="?", help="UTF-8 text file or -; omit to read standard input")
    return result


def read_input(filename: str | None) -> tuple[str, str]:
    if filename is None or filename == "-":
        return sys.stdin.buffer.read().decode("utf-8"), "<stdin>"
    path = Path(filename)
    return path.read_text(encoding="utf-8"), str(path)


def abbreviation_continues_sentence(text: str, start: int, end: int) -> bool:
    match = ABBREVIATION_AT_END.search(text[start:end])
    if match is None:
        return False

    following = re.match(r"(?P<spacing>\s+)(?P<token>\S+)", text[end:])
    if following is None or "\n\n" in following.group("spacing"):
        return False

    abbreviation = match.group("abbreviation").casefold()
    token = following.group("token")
    if abbreviation == "etc.":
        return token[0].islower()
    if abbreviation == "no.":
        return bool(re.match(r"(?:\d|[A-Za-z]*\d)", token))
    if abbreviation == "fig.":
        return token[0].isalnum()
    if abbreviation in TITLE_ABBREVIATIONS:
        return token[0].isalpha()
    return True


def sentence_spans(text: str) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    start = 0
    for match in re.finditer(r"[.!?]+(?=\s|$)", text):
        end = match.end()
        if match.group() == "." and abbreviation_continues_sentence(text, start, end):
            continue
        if text[start:end].strip():
            leading = len(text[start:end]) - len(text[start:end].lstrip())
            spans.append((start + leading, end))
        start = end
    if text[start:].strip():
        leading = len(text[start:]) - len(text[start:].lstrip())
        spans.append((start + leading, len(text)))
    return spans


def mask_atomic_text(sentence: str) -> str:
    result: list[str] = []
    depth = 0
    emitted = False
    for character in sentence:
        if character == "(":
            if depth == 0:
                result.append(" PARENTHETICAL ")
                emitted = True
            depth += 1
        elif character == ")" and depth:
            depth -= 1
        elif depth == 0:
            result.append(character)
    masked = "".join(result) if emitted else sentence
    masked = re.sub(r'"[^"\n]*"|“[^”\n]*”', " QUOTED_TEXT ", masked)
    return re.sub(r"\b(?:[A-Z][A-Za-z]+\s+){1,}[A-Z][A-Za-z]+\b", " PROPER_NAME ", masked)


def word_count(sentence: str) -> int:
    masked = mask_atomic_text(sentence)
    tokens = re.findall(
        r"(?:\d+(?:[.,]\d+)?(?:\s*[°%]|\s*(?:degrees|degree|MHz|kPa|cm|deg|ft|Hz|kg|km|lb|mg|min|mL|mm|ohm|A|g|h|in|L|m|N|s|V|W)\b)?)"
        r"|(?:[A-Za-z]+(?:['’][A-Za-z]+)?(?:-[A-Za-z0-9]+)*)",
        masked,
    )
    return len(tokens)


def finding_for_match(
    match: re.Match[str],
    *,
    severity: str,
    category: str,
    code: str,
    rule: str | None,
    explanation: str,
    hint: str,
) -> Finding:
    return Finding(
        match.start(),
        match.end(),
        severity,
        category,
        code,
        rule,
        SOURCES.get(rule) if rule else None,
        explanation,
        hint,
    )


def regex_findings(
    text: str,
    pattern: re.Pattern[str],
    *,
    severity: str,
    category: str,
    code: str,
    rule: str | None,
    explanation: str,
    hint: str,
) -> Iterable[Finding]:
    for match in pattern.finditer(text):
        yield finding_for_match(
            match,
            severity=severity,
            category=category,
            code=code,
            rule=rule,
            explanation=explanation,
            hint=hint,
        )


def delimiter_findings(text: str) -> Iterable[Finding]:
    pairs = {"(": ")", "[": "]", "{": "}"}
    closing = {value: key for key, value in pairs.items()}
    stack: list[tuple[str, int]] = []
    for offset, character in enumerate(text):
        if character in pairs:
            stack.append((character, offset))
        elif character in closing:
            if stack and stack[-1][0] == closing[character]:
                stack.pop()
            else:
                yield Finding(
                    offset,
                    offset + 1,
                    "Violation",
                    "normative",
                    "unbalanced-delimiter",
                    "Rule 8.1",
                    SOURCES["Rule 8.1"],
                    "The closing delimiter has no matching opening delimiter.",
                    "Add the matching opening delimiter or remove this delimiter.",
                )
    for _character, offset in stack:
        yield Finding(
            offset,
            offset + 1,
            "Violation",
            "normative",
            "unbalanced-delimiter",
            "Rule 8.1",
            SOURCES["Rule 8.1"],
            "The opening delimiter has no matching closing delimiter.",
            "Add the matching closing delimiter or remove this delimiter.",
        )

    for opening, closing_character in (("“", "”"),):
        opens = [match.start() for match in re.finditer(re.escape(opening), text)]
        closes = [match.start() for match in re.finditer(re.escape(closing_character), text)]
        if len(opens) != len(closes):
            offsets = opens[len(closes) :] if len(opens) > len(closes) else closes[len(opens) :]
            for offset in offsets:
                yield Finding(
                    offset,
                    offset + 1,
                    "Violation",
                    "normative",
                    "unbalanced-quotation",
                    "Rule 8.1",
                    SOURCES["Rule 8.1"],
                    "The quotation mark has no matching pair.",
                    "Add the matching quotation mark or remove this mark.",
                )

    single_quote_stack: list[int] = []
    for offset, character in enumerate(text):
        if character == "‘":
            single_quote_stack.append(offset)
        elif character == "’":
            embedded = (
                offset > 0 and offset + 1 < len(text) and text[offset - 1].isalnum() and text[offset + 1].isalnum()
            )
            if embedded:
                continue
            if single_quote_stack:
                single_quote_stack.pop()
            elif offset == 0 or not text[offset - 1].isalnum():
                yield Finding(
                    offset,
                    offset + 1,
                    "Violation",
                    "normative",
                    "unbalanced-quotation",
                    "Rule 8.1",
                    SOURCES["Rule 8.1"],
                    "The quotation mark has no matching pair.",
                    "Add the matching quotation mark or remove this mark.",
                )
    for offset in single_quote_stack:
        yield Finding(
            offset,
            offset + 1,
            "Violation",
            "normative",
            "unbalanced-quotation",
            "Rule 8.1",
            SOURCES["Rule 8.1"],
            "The quotation mark has no matching pair.",
            "Add the matching quotation mark or remove this mark.",
        )

    straight_quotes = [match.start() for match in re.finditer('"', text)]
    if len(straight_quotes) % 2:
        offset = straight_quotes[-1]
        yield Finding(
            offset,
            offset + 1,
            "Violation",
            "normative",
            "unbalanced-quotation",
            "Rule 8.1",
            SOURCES["Rule 8.1"],
            "The quotation mark has no matching pair.",
            "Add the matching quotation mark or remove this mark.",
        )


def paragraph_findings(text: str, text_type: str) -> Iterable[Finding]:
    if text_type != "description":
        return
    for match in re.finditer(r"(?:^|\n\s*\n)([^\n](?:(?!\n\s*\n)[\s\S])*)", text):
        paragraph = match.group(1)
        paragraph_offset = match.start(1)
        count = len(sentence_spans(paragraph))
        if count > 6:
            yield Finding(
                paragraph_offset,
                paragraph_offset + len(paragraph),
                "Violation",
                "normative",
                "description-paragraph-limit",
                "Rule 6.6",
                SOURCES["Rule 6.6"],
                f"The description paragraph has {count} sentences. The maximum is 6.",
                "Divide the paragraph by topic.",
            )


def analyze(text: str, text_type: str) -> list[Finding]:
    findings: list[Finding] = []
    limit = 20 if text_type == "procedure" else 25
    limit_rule = "Rule 5.1" if text_type == "procedure" else "Rule 6.3"
    for start, end in sentence_spans(text):
        sentence = text[start:end]
        count = word_count(sentence)
        if count > limit:
            findings.append(
                Finding(
                    start,
                    end,
                    "Violation",
                    "normative",
                    "sentence-limit",
                    limit_rule,
                    SOURCES[limit_rule],
                    f"The sentence has {count} counted words. The maximum for a {text_type} is {limit}.",
                    "Divide the sentence without changing the technical meaning.",
                )
            )

    findings.extend(
        regex_findings(
            text,
            re.compile(r";"),
            severity="Violation",
            category="normative",
            code="semicolon",
            rule="Rule 8.1",
            explanation="ASD-STE100 does not permit semicolons.",
            hint="Divide the clauses into separate sentences.",
        )
    )
    findings.extend(
        regex_findings(
            text,
            CONTRACTIONS,
            severity="Violation",
            category="normative",
            code="contraction",
            rule="Rule 4.2",
            explanation="ASD-STE100 does not permit contractions.",
            hint="Write the contraction in full.",
        )
    )
    findings.extend(delimiter_findings(text))
    findings.extend(paragraph_findings(text, text_type))

    for match in ING_WORD.finditer(text):
        if match.group(0).casefold() not in APPROVED_ING_WORDS:
            findings.append(
                finding_for_match(
                    match,
                    severity="Review",
                    category="asd-review",
                    code="ing-form",
                    rule="Rule 3.5",
                    explanation=(
                        "This can be an unapproved -ing verb form. Technical nouns and some listed words are permitted."
                    ),
                    hint="Confirm the part of speech and dictionary or technical-noun route.",
                )
            )

    review_specs = (
        (
            PASSIVE,
            "passive-voice",
            "Rule 3.6",
            "This can be passive voice.",
            "Identify the real agent. Keep passive voice in a description only when the agent is unknown.",
        ),
        (
            STACKED_AUXILIARY,
            "stacked-auxiliary",
            "Rule 3.4",
            "This can be a complex auxiliary construction.",
            "Use a permitted simple tense or an imperative when the meaning permits it.",
        ),
        (
            NOMINALIZATION,
            "nominalization",
            "Rule 3.7",
            "This noun-based construction can hide the action.",
            "Check whether an approved direct verb states the action accurately.",
        ),
        (
            PHRASAL_VERB,
            "phrasal-verb",
            "Rule 9.3",
            "This can be a phrasal verb.",
            "Confirm that the complete phrasal verb is approved with this meaning.",
        ),
        (
            RECURRING_ERROR,
            "recurring-error-term",
            "Rule 1.1",
            "This term appears in the official recurring-errors list and is context-sensitive.",
            "Inspect the complete dictionary entry and reconstruct the sentence when necessary.",
        ),
    )
    for pattern, code, rule, explanation, hint in review_specs:
        findings.extend(
            regex_findings(
                text,
                pattern,
                severity="Review",
                category="asd-review",
                code=code,
                rule=rule,
                explanation=explanation,
                hint=hint,
            )
        )

    recommendation_specs = (
        (
            LATIN_ABBREVIATION,
            "latin-abbreviation",
            "GR-6",
            "Issue 9 recommends that technical text not use Latin abbreviations.",
            "Use an English phrase or omit the abbreviation.",
        ),
        (
            GENDERED_PRONOUN,
            "gendered-pronoun",
            "GR-3",
            "This pronoun can be ambiguous; Issue 9 recommends an exact noun and does not recommend he or she.",
            "Use the exact role or noun and confirm inclusive language under GR-7.",
        ),
        (
            GENDERED_PRONOUN,
            "inclusive-language",
            "GR-7",
            "This gendered pronoun can be unnecessary or non-inclusive.",
            "Use the exact gender-neutral role or noun unless the distinction is necessary.",
        ),
        (
            BARE_THIS,
            "bare-this",
            "GR-4",
            "The referent of this can be ambiguous.",
            "Add the applicable noun unless there is only one unmistakable referent.",
        ),
    )
    for pattern, code, rule, explanation, hint in recommendation_specs:
        findings.extend(
            regex_findings(
                text,
                pattern,
                severity="Review",
                category="recommendation",
                code=code,
                rule=rule,
                explanation=explanation,
                hint=hint,
            )
        )

    findings.extend(
        regex_findings(
            text,
            ANTI_SLOP,
            severity="Review",
            category="non-normative-review",
            code="non-normative-style",
            rule=None,
            explanation="This phrase can make technical prose vague or promotional. This is not an ASD-STE100 rule.",
            hint="Remove it or replace it with a precise technical statement when appropriate.",
        )
    )
    return sorted(findings, key=lambda item: (item.offset, item.end, item.code, item.rule or ""))


def line_starts(text: str) -> list[int]:
    return [0] + [match.end() for match in re.finditer(r"\n", text)]


def serialize(text: str, findings: Sequence[Finding]) -> list[dict[str, object]]:
    starts = line_starts(text)
    result: list[dict[str, object]] = []
    for finding in findings:
        line_index = bisect.bisect_right(starts, finding.offset) - 1
        result.append(
            {
                "line": line_index + 1,
                "column": finding.offset - starts[line_index] + 1,
                "severity": finding.severity,
                "category": finding.category,
                "code": finding.code,
                "rule": finding.rule,
                "source": finding.source,
                "matched_text": text[finding.offset : finding.end],
                "explanation": finding.explanation,
                "hint": finding.hint,
            }
        )
    return result


def print_text(filename: str, items: Sequence[dict[str, object]]) -> None:
    if not items:
        print("No findings.")
        return
    for item in items:
        rule = " [{}]".format(item["rule"]) if item["rule"] else ""
        print(
            "{}:{}:{}: {} {}/{}{}: {!r}".format(
                filename,
                item["line"],
                item["column"],
                item["severity"],
                item["category"],
                item["code"],
                rule,
                item["matched_text"],
            )
        )
        print("  {} Hint: {} Source: {}".format(item["explanation"], item["hint"], item["source"] or "n/a"))
    violations = sum(item["severity"] == "Violation" for item in items)
    reviews = len(items) - violations
    print(f"{violations} violation(s), {reviews} review item(s).")


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        text, filename = read_input(args.file)
    except (OSError, UnicodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    findings = analyze(text, args.text_type)
    items = serialize(text, findings)
    if args.output_format == "json":
        document = {
            "schema_version": 1,
            "input": filename,
            "text_type": args.text_type,
            "status": "violations" if any(item["severity"] == "Violation" for item in items) else "no-violations",
            "counts": {
                "violations": sum(item["severity"] == "Violation" for item in items),
                "reviews": sum(item["severity"] == "Review" for item in items),
            },
            "findings": items,
        }
        print(json.dumps(document, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print_text(filename, items)
    return 1 if any(item["severity"] == "Violation" for item in items) else 0


def configure_posix_pipeline() -> None:
    """Use normal POSIX termination when a downstream command closes the pipe."""
    if hasattr(signal, "SIGPIPE"):
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)


if __name__ == "__main__":
    configure_posix_pipeline()
    raise SystemExit(main())
