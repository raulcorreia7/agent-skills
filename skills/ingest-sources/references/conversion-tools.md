# Conversion Tools

Select a maintained tool that preserves the evidence needed for the approved
questions. Keep the original source and write each conversion as a derivative.

Use the tool for the mechanical transformation. Use the agent to select the
tool, set limits, inspect warnings, compare difficult sections, and decide
whether another representation is necessary. Do not ask the model to recreate
Markdown from raw HTML, PDF extraction noise, XML, JSON, or an office document
when an approved parser or converter can perform that step.

| Need | Prefer | Main limit |
| --- | --- | --- |
| Convert HTML or another supported markup format to explicit Markdown | Pandoc | The conversion can lose browser state, layout, or unsupported elements |
| Make a compact Markdown projection of a local PDF, office file, HTML file, or structured file for text analysis | MarkItDown | The output favors text analysis, not high-fidelity publication |
| Extract simple embedded PDF text | `pdftotext` | Columns, tables, and reading order can collapse |
| Preserve PDF hierarchy, pages, tables, and layout in a document model | Docling | Model extraction can still misclassify content |
| Add a searchable text layer to scanned or mixed PDFs | OCRmyPDF | OCR can be wrong and creates a derivative outside the original signature |

Use the narrowest installed format extra or converter. Do not install every
optional parser when the approved corpus needs one format.

## Local Conversion Examples

Convert retained static HTML to GitHub-Flavored Markdown:

```console
pandoc --from=html --to=gfm --wrap=none source.html --output derived/source.md
```

Create a text-analysis projection from a local supported file:

```console
markitdown source.pdf -o derived/source.md
```

Compare ordinary and layout-preserving PDF text before selecting one:

```console
pdftotext source.pdf derived/source.txt
pdftotext -layout source.pdf derived/source-layout.txt
```

Keep both Markdown and a structured document model for a layout-sensitive PDF:

```console
docling convert source.pdf --to md --to json --output derived/
```

Add OCR only where an existing text layer is absent:

```console
ocrmypdf --skip-text source.pdf derived/searchable.pdf
```

Run converters in the isolated worker defined by the parent skill. Use local
retained inputs instead of converter URL features. Record the tool version,
command, warnings, and output hashes. Compare representative difficult content
with the source before retrieval uses the derivative.

## Sources

- [Pandoc User's Guide](https://pandoc.org/MANUAL.html)
- [Microsoft MarkItDown](https://github.com/microsoft/markitdown)
- [Docling CLI reference](https://docling-project.github.io/docling/reference/cli/)
- [Poppler `pdftotext` manual](https://manpages.debian.org/bookworm/poppler-utils/pdftotext.1.en.html)
- [OCRmyPDF introduction](https://ocrmypdf.readthedocs.io/en/stable/introduction.html)
