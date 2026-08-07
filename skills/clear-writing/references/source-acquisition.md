# Source Acquisition

The optional downloader retrieves the official source only when the user asks.
Resolve `<skill-root>` as the directory that contains `SKILL.md`. Specify
explicit output paths. The command refuses to replace a file unless you add
`--overwrite`.

On POSIX, download the official PDF and validate its PDF format:

```text
"<skill-root>/scripts/download.py" pdf --pdf-output <pdf-path>
```

Download the PDF and create attributed Markdown:

```text
"<skill-root>/scripts/download.py" pdf-and-markdown \
  --pdf-output <pdf-path> --output <markdown-path>
```

Use `python3 <skill-root>/scripts/download.py ...` when direct execution is not
available. On Windows, use `py -3` instead. The PDF command uses only the Python
standard library. Markdown conversion requires Poppler `pdftotext`. The
PDF-only command does not verify Issue 9 identity. The Markdown command checks
the issue markers and gives one source-page marker for each of the 434 pages.

WARNING: The official source has copyright and distribution conditions. Keep
downloaded or converted files outside a distributable skill package unless an
authorized use permits distribution.
