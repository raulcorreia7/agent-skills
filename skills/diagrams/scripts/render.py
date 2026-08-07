#!/usr/bin/env python3
"""Render Mermaid, Graphviz DOT, or D2 source files."""

from __future__ import annotations

import argparse
import os
import shlex
import shutil
import stat
import subprocess
import sys
import tempfile
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path

SOURCE_KINDS = {
    ".d2": "d2",
    ".dot": "graphviz",
    ".gv": "graphviz",
    ".mermaid": "mermaid",
    ".mmd": "mermaid",
}
OUTPUT_FORMATS = ("pdf", "png", "svg")
GRAPHVIZ_ENGINES = ("circo", "dot", "fdp", "neato", "osage", "patchwork", "sfdp", "twopi")
EXAMPLES = r"""Resolve <skill-root> as the directory containing SKILL.md.

POSIX examples:
  python3 <skill-root>/scripts/render.py architecture.mmd
  python3 <skill-root>/scripts/render.py one.dot two.d2 --format png
  python3 <skill-root>/scripts/render.py diagrams/ --recursive --output-dir build/diagrams

Windows examples:
  py -3 <skill-root>\scripts\render.py architecture.mmd
  py -3 <skill-root>\scripts\render.py one.dot two.d2 --format png
  py -3 <skill-root>\scripts\render.py diagrams\ --dry-run

Behavior:
  Source renderers must be available on PATH.
  The default output is a sibling SVG; --output or --format changes it.
  Successful implicit and explicit outputs replace existing regular files atomically.
  No --force or --overwrite flag is required for ordinary replacement.
  A batch stops at the first failure and retains earlier successful outputs.

Exit status:
  0    Success or dry-run success.
  1    A renderer or output operation failed.
  2    The command, render plan, or renderer availability is invalid.
  130  The operation was interrupted.
"""


class UsageError(ValueError):
    """Report an invalid render plan without a traceback."""


@dataclass(frozen=True)
class Job:
    source: Path
    output: Path
    kind: str


def lexical_absolute(path: Path) -> Path:
    """Return an absolute path without following its final symlink."""

    return Path(os.path.abspath(path.expanduser()))


def symlink_component(path: Path) -> Path | None:
    """Return the first existing symlink in an absolute lexical path."""

    current = Path(path.anchor)
    for part in path.parts[1:]:
        current /= part
        if current.is_symlink():
            return current
        if not current.exists():
            break
    return None


def reject_symlink_components(path: Path, *, label: str) -> None:
    """Reject a path that is or traverses a symlink."""

    if component := symlink_component(path):
        raise UsageError(f"{label} cannot traverse a symlink: {component}")


def reject_non_regular_output(path: Path) -> None:
    """Reject an existing output that is not a regular file."""

    try:
        mode = path.lstat().st_mode
    except FileNotFoundError:
        return
    if not stat.S_ISREG(mode):
        raise UsageError(f"existing output is not a regular file: {path}")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=__doc__,
        epilog=EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("paths", nargs="+", type=Path, help="Source files or directories.")
    parser.add_argument(
        "-f",
        "--format",
        choices=OUTPUT_FORMATS,
        help="Output format. The default is SVG or the --output suffix.",
    )
    output = parser.add_mutually_exclusive_group()
    output.add_argument("-o", "--output", type=Path, help="Output path for one source file.")
    output.add_argument("--output-dir", type=Path, help="Write all results to this directory.")
    parser.add_argument("-r", "--recursive", action="store_true", help="Search input directories recursively.")
    parser.add_argument("-n", "--dry-run", action="store_true", help="Print the render plan without writing files.")
    parser.add_argument(
        "--graphviz-engine",
        choices=GRAPHVIZ_ENGINES,
        default="dot",
        help="Graphviz layout engine. The default is dot.",
    )
    return parser.parse_args(argv)


def collect_sources(paths: Sequence[Path], *, recursive: bool) -> list[Path]:
    sources: set[Path] = set()
    for raw_path in paths:
        path = lexical_absolute(raw_path)
        reject_symlink_components(path, label="input")
        if not path.exists():
            raise UsageError(f"input does not exist: {raw_path}")
        if path.is_file():
            if path.suffix.lower() not in SOURCE_KINDS:
                raise UsageError(f"unsupported source extension: {raw_path}")
            sources.add(path)
            continue
        if not path.is_dir():
            raise UsageError(f"input is not a file or directory: {raw_path}")
        if path == Path(path.anchor):
            raise UsageError(f"input directory cannot be a filesystem root: {raw_path}")
        candidates = path.rglob("*") if recursive else path.iterdir()
        for candidate in candidates:
            if candidate.suffix.lower() not in SOURCE_KINDS:
                continue
            reject_symlink_components(lexical_absolute(candidate), label="input")
            if candidate.is_file():
                sources.add(lexical_absolute(candidate))
    if not sources:
        extensions = ", ".join(sorted(SOURCE_KINDS))
        raise UsageError(f"no diagram sources found; supported extensions: {extensions}")
    return sorted(sources)


def select_format(args: argparse.Namespace) -> str:
    if args.output is None:
        return args.format or "svg"
    suffix = args.output.suffix.lower().removeprefix(".")
    if suffix not in OUTPUT_FORMATS:
        supported = ", ".join(OUTPUT_FORMATS)
        raise UsageError(f"--output must use one of these extensions: {supported}")
    if args.format is not None and args.format != suffix:
        raise UsageError("--format must match the --output extension")
    return args.format or suffix


def build_jobs(args: argparse.Namespace) -> tuple[list[Job], str]:
    sources = collect_sources(args.paths, recursive=args.recursive)
    output_format = select_format(args)
    if args.output is not None and len(sources) != 1:
        raise UsageError("--output requires exactly one source file")

    output_dir = lexical_absolute(args.output_dir) if args.output_dir is not None else None
    if output_dir is not None and output_dir == Path(output_dir.anchor):
        raise UsageError("--output-dir cannot be a filesystem root")
    if output_dir is not None:
        reject_symlink_components(output_dir, label="--output-dir")
    if output_dir is not None and output_dir.exists() and not output_dir.is_dir():
        raise UsageError(f"--output-dir is not a directory: {output_dir}")

    jobs: list[Job] = []
    outputs: dict[Path, Path] = {}
    for source in sources:
        if args.output is not None:
            output = lexical_absolute(args.output)
        elif output_dir is not None:
            output = output_dir / f"{source.stem}.{output_format}"
        else:
            output = source.with_suffix(f".{output_format}")
        reject_symlink_components(output, label="output")
        if output == source:
            raise UsageError(f"output would replace its source: {source}")
        reject_non_regular_output(output)
        ancestor = output.parent
        while not ancestor.exists() and ancestor != ancestor.parent:
            ancestor = ancestor.parent
        if not ancestor.is_dir():
            raise UsageError(f"output parent is not a directory: {ancestor}")
        if previous := outputs.get(output):
            raise UsageError(f"sources map to the same output: {previous} and {source} -> {output}")
        outputs[output] = source
        jobs.append(Job(source=source, output=output, kind=SOURCE_KINDS[source.suffix.lower()]))

    return jobs, output_format


def renderer_names(jobs: Sequence[Job]) -> set[str]:
    names: set[str] = set()
    for job in jobs:
        names.add({"mermaid": "mmdc", "graphviz": "dot", "d2": "d2"}[job.kind])
    return names


def require_renderers(jobs: Sequence[Job]) -> None:
    missing = sorted(name for name in renderer_names(jobs) if shutil.which(name) is None)
    if missing:
        raise UsageError(f"required renderer not found on PATH: {', '.join(missing)}")


def command_for(job: Job, output: Path, *, graphviz_engine: str) -> list[str]:
    output_format = output.suffix.lower().removeprefix(".")
    if job.kind == "mermaid":
        return ["mmdc", "-i", str(job.source), "-o", str(output)]
    if job.kind == "graphviz":
        return ["dot", f"-K{graphviz_engine}", f"-T{output_format}", str(job.source), "-o", str(output)]
    return ["d2", str(job.source), str(output)]


def print_plan(jobs: Sequence[Job], *, graphviz_engine: str) -> None:
    for job in jobs:
        command = command_for(job, job.output, graphviz_engine=graphviz_engine)
        print(shlex.join(command))


def render(job: Job, *, graphviz_engine: str) -> bool:
    try:
        reject_symlink_components(job.source, label="input")
        reject_symlink_components(job.output, label="output")
        job.output.parent.mkdir(parents=True, exist_ok=True)
        reject_symlink_components(job.output, label="output")
        with tempfile.TemporaryDirectory(prefix=f".{job.output.stem}.", dir=job.output.parent) as temporary_dir:
            temporary = Path(temporary_dir) / job.output.name
            command = command_for(job, temporary, graphviz_engine=graphviz_engine)
            completed = subprocess.run(command, check=False)
            if completed.returncode != 0:
                print(f"render failed ({completed.returncode}): {job.source}", file=sys.stderr)
                return False
            if not temporary.is_file() or temporary.stat().st_size == 0:
                print(f"renderer produced no output: {job.source}", file=sys.stderr)
                return False
            reject_symlink_components(job.output, label="output")
            reject_non_regular_output(job.output)
            os.replace(temporary, job.output)
        print(f"{job.source} -> {job.output}")
        return True
    except UsageError as exc:
        print(f"render refused: {exc}", file=sys.stderr)
        return False
    except OSError as exc:
        print(f"output error: {job.output}: {exc}", file=sys.stderr)
        return False


def run(args: argparse.Namespace) -> int:
    try:
        jobs, _ = build_jobs(args)
        if args.dry_run:
            print_plan(jobs, graphviz_engine=args.graphviz_engine)
            return 0
        require_renderers(jobs)
    except UsageError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    for job in jobs:
        if not render(job, graphviz_engine=args.graphviz_engine):
            return 1
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    try:
        return run(parse_args(argv))
    except KeyboardInterrupt:
        print("interrupted", file=sys.stderr)
        return 130
    except BrokenPipeError:
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
