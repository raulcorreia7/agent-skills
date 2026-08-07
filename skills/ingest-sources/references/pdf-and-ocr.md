# PDF And OCR

Keep the original PDF because conversion and OCR are lossy.

## Classify

Inspect a representative sample. Then use the applicable path:

- For a born-digital PDF with simple layout, extract embedded text and retain
  page separators.
- For a complex layout, use a document model that retains hierarchy, reading
  order, tables, pages, and bounding boxes.
- For an image-only scan, OCR only the necessary pages or regions.
- For a mixed PDF, preserve existing text and OCR only image pages or regions.

## Process

1. Hash and retain the original PDF before processing.
2. Run the selected parser or OCR engine in an offline, disposable, resource-limited
   worker. PDF files can contain active content.
3. Preserve page numbers and coordinates when layout can affect meaning.
4. Keep structured JSON or another document model beside the text projection
   when tables, forms, equations, figures, or columns matter.
5. Record the tool, version, settings, language, affected pages, confidence,
   warnings, and output hashes.
6. Keep a signed original unchanged. Mark each OCR or rewritten PDF as a
   derivative because the original signature does not cover it.
7. Compare representative difficult pages visually. Check reading order,
   repeated headers, tables, captions, footnotes, equations, and warnings.

Keep the original or a structured model when page geometry, annotations,
attachments, or figures carry meaning.

## Example

For a mixed 40-page PDF, keep the signed original. Extract embedded text from
digital pages and OCR only pages 12–14. Record those page numbers, the OCR
language, warnings, output hashes, and the visual checks for tables and reading
order.

## Sources

- [Poppler `pdftotext` manual](https://manpages.debian.org/bookworm/poppler-utils/pdftotext.1.en.html)
- [Docling document model](https://docling-project.github.io/docling/reference/docling_document/)
- [OCRmyPDF introduction](https://ocrmypdf.readthedocs.io/en/stable/introduction.html)
- [OCRmyPDF PDF security](https://ocrmypdf.readthedocs.io/en/v15.3.1/pdfsecurity.html)
