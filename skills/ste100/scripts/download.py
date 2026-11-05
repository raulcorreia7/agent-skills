#!/usr/bin/env python3
"""Download the official ASD-STE100 PDF and optionally create Markdown."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from collections.abc import Sequence
from pathlib import Path

OFFICIAL_URL = "https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf"
TITLE = "ASD-STE100 Simplified Technical English — Issue 9"
EXPECTED_PAGES = 434
CONVERTER = "pdftotext"


class DownloadError(Exception):
    """Report a source download or conversion failure."""


def sha256(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def download_pdf(destination: Path) -> None:
    request = urllib.request.Request(
        OFFICIAL_URL,
        headers={"User-Agent": "portable-asd-ste100-downloader/1"},
    )
    try:
        with urllib.request.urlopen(request, timeout=120) as response, destination.open("wb") as output:
            shutil.copyfileobj(response, output)
    except (OSError, urllib.error.URLError) as error:
        raise DownloadError(f"could not download the official PDF: {error}") from error


def validate_pdf(path: Path) -> None:
    try:
        with path.open("rb") as source:
            marker = source.read(5)
    except OSError as error:
        raise DownloadError(f"could not read the downloaded file: {error}") from error
    if marker != b"%PDF-":
        raise DownloadError("the downloaded file is not a PDF")


def converter_version() -> str:
    command = [CONVERTER, "-v"]
    try:
        result = subprocess.run(command, check=False, capture_output=True, text=True)
    except OSError as error:
        raise DownloadError(f"could not run {CONVERTER}: {error}") from error
    version = result.stdout.strip() or result.stderr.strip() or "unknown"
    return version.splitlines()[0]


def convert_pdf(source: Path, destination: Path) -> str:
    if shutil.which(CONVERTER) is None:
        raise DownloadError("install Poppler pdftotext to create Markdown")
    command = [CONVERTER, "-layout", "-enc", "UTF-8", str(source), str(destination)]
    try:
        result = subprocess.run(command, check=False, capture_output=True, text=True)
    except OSError as error:
        raise DownloadError(f"could not run {CONVERTER}: {error}") from error
    if result.returncode:
        detail = result.stderr.strip() or result.stdout.strip() or "unknown converter error"
        raise DownloadError(f"{CONVERTER} failed: {detail}")
    try:
        text = destination.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise DownloadError(f"could not read UTF-8 converter output: {error}") from error
    pages = text.split("\f")
    while pages and not pages[-1].strip():
        pages.pop()
    return "\n\n".join(f"<!-- source-pdf-page: {number} -->\n\n{page.strip()}" for number, page in enumerate(pages, 1))


def validate_conversion(text: str) -> None:
    required = ("ASD-STE100", "Issue 9", "2025-01-15")
    missing = [value for value in required if value.casefold() not in text.casefold()]
    if missing:
        raise DownloadError(f"the conversion does not identify Issue 9: {', '.join(missing)}")
    pages = [int(value) for value in re.findall(r"<!-- source-pdf-page: (\d+) -->", text)]
    if pages != list(range(1, EXPECTED_PAGES + 1)):
        raise DownloadError(f"the conversion does not contain {EXPECTED_PAGES} ordered PDF page markers")


def markdown_content(source: Path, converted: str) -> str:
    return (
        "<!--\n"
        f"title: {TITLE}\n"
        "date: 2025-01-15\n"
        "publisher: Aerospace, Security and Defence Industries Association of Europe (ASD)\n"
        f"official-source: {OFFICIAL_URL}\n"
        f"source-sha256: {sha256(source)}\n"
        f"converter: {converter_version()}\n"
        "notice: Derived Markdown. The official PDF is authoritative. Obey its distribution conditions.\n"
        "-->\n\n"
        f"{converted}\n"
    )


def validate_output(path: Path, suffix: str, label: str) -> Path:
    output = path.expanduser().resolve()
    if output.suffix.casefold() != suffix:
        raise DownloadError(f"{label} must have a {suffix} extension: {output}")
    if output.parent == output:
        raise DownloadError(f"{label} cannot be a filesystem root")
    return output


def refuse_existing(paths: Sequence[Path], overwrite: bool) -> None:
    if overwrite:
        return
    existing = [str(path) for path in paths if path.exists()]
    if existing:
        raise DownloadError(f"output exists; select another path or pass --overwrite: {', '.join(existing)}")


def stage_bytes(source: Path, destination: Path) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            dir=destination.parent,
            prefix=f".{destination.name}.",
            suffix=".tmp",
            delete=False,
        ) as staged:
            with source.open("rb") as input_file:
                shutil.copyfileobj(input_file, staged)
            staged.flush()
            os.fsync(staged.fileno())
            return Path(staged.name)
    except OSError as error:
        raise DownloadError(f"could not stage {destination}: {error}") from error


def stage_text(content: str, destination: Path) -> Path:
    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            dir=destination.parent,
            prefix=f".{destination.name}.",
            suffix=".tmp",
            delete=False,
        ) as staged:
            staged.write(content)
            staged.flush()
            os.fsync(staged.fileno())
            return Path(staged.name)
    except OSError as error:
        raise DownloadError(f"could not stage {destination}: {error}") from error


def replace(staged: Path, destination: Path) -> None:
    try:
        staged.replace(destination)
    except OSError as error:
        staged.unlink(missing_ok=True)
        raise DownloadError(f"could not write {destination}: {error}") from error


def replace_outputs(outputs: Sequence[tuple[Path, Path]]) -> None:
    backups: dict[Path, Path] = {}
    replaced: list[Path] = []
    try:
        for _staged, destination in outputs:
            if destination.exists():
                backups[destination] = stage_bytes(destination, destination)
        for staged, destination in outputs:
            replace(staged, destination)
            replaced.append(destination)
    except DownloadError as error:
        rollback_errors: list[str] = []
        for destination in reversed(replaced):
            backup = backups.get(destination)
            try:
                if backup is None:
                    destination.unlink(missing_ok=True)
                else:
                    backup.replace(destination)
            except OSError as rollback_error:
                rollback_errors.append(f"{destination}: {rollback_error}")
        if rollback_errors:
            details = "; ".join(rollback_errors)
            raise DownloadError(f"{error}; rollback failed for {details}") from error
        raise
    finally:
        for backup in backups.values():
            backup.unlink(missing_ok=True)


def add_common_options(command: argparse.ArgumentParser) -> None:
    command.add_argument("--pdf-output", type=Path, required=True, help="destination for the official PDF")
    command.add_argument("--overwrite", action="store_true", help="replace existing output files")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    examples = """Examples:
  download.py pdf --pdf-output ASD-STE100_ISSUE9.pdf
  download.py pdf-and-markdown --pdf-output ASD-STE100_ISSUE9.pdf --output asd-ste100-issue-9.md

Exit status:
  0  The requested outputs were created.
  2  Arguments, download, validation, conversion, or output replacement failed.
"""
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog=examples,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    commands = parser.add_subparsers(dest="command", required=True)

    pdf = commands.add_parser("pdf", help="download the official PDF and validate its PDF format")
    add_common_options(pdf)

    markdown = commands.add_parser("pdf-and-markdown", help="download the PDF and create attributed Markdown")
    add_common_options(markdown)
    markdown.add_argument("--output", type=Path, required=True, help="destination for attributed Markdown")
    return parser.parse_args(argv)


def run(args: argparse.Namespace) -> tuple[Path, Path | None]:
    pdf_output = validate_output(args.pdf_output, ".pdf", "PDF output")
    markdown_output: Path | None = None
    if args.command == "pdf-and-markdown":
        markdown_output = validate_output(args.output, ".md", "Markdown output")
        if markdown_output == pdf_output:
            raise DownloadError("PDF and Markdown outputs must be different files")
    outputs = [pdf_output, *([markdown_output] if markdown_output else [])]
    refuse_existing(outputs, args.overwrite)

    with tempfile.TemporaryDirectory(prefix="asd-ste100-download-") as temporary:
        temporary_root = Path(temporary)
        source = temporary_root / "ASD-STE100_ISSUE9.pdf"
        print(f"Downloading {OFFICIAL_URL}", file=sys.stderr)
        download_pdf(source)
        validate_pdf(source)

        staged_outputs: list[Path] = []
        try:
            markdown_staged: Path | None = None
            if markdown_output is not None:
                print(f"Creating Markdown with {CONVERTER}", file=sys.stderr)
                converted = convert_pdf(source, temporary_root / "converted.md")
                validate_conversion(converted)
                markdown_staged = stage_text(markdown_content(source, converted), markdown_output)
                staged_outputs.append(markdown_staged)

            pdf_staged = stage_bytes(source, pdf_output)
            staged_outputs.append(pdf_staged)
            replacements = [(pdf_staged, pdf_output)]
            if markdown_staged is not None and markdown_output is not None:
                replacements.append((markdown_staged, markdown_output))
            replace_outputs(replacements)
        finally:
            for staged_output in staged_outputs:
                staged_output.unlink(missing_ok=True)
    return pdf_output, markdown_output


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        pdf_output, markdown_output = run(args)
    except DownloadError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(f"PDF: {pdf_output}")
    if markdown_output is not None:
        print(f"Markdown ({CONVERTER}): {markdown_output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
