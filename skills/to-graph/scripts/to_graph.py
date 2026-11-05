# /// script
# requires-python = ">=3.11"
# dependencies = ["jsonschema>=4.18", "pyyaml>=6"]
# ///
"""Check, render, and run to-graph workflow files.

A graph's shape is defined only by references/graph.schema.json; this tool
validates against it and adds the checks a schema cannot express.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from collections.abc import Iterator, Sequence
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

Node = dict[str, Any]
Graph = dict[str, Any]

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "references" / "graph.schema.json"
BUILTIN_OUTCOMES = {"task": {"succeeded", "failed"}, "gate": {"approved", "rejected", "unavailable"}, "terminal": set()}
REF = re.compile(r"\$\{([A-Za-z_][A-Za-z0-9_-]*)(\.output)?\}")
UNIT_SECONDS = {"s": 1, "m": 60, "h": 3600}

EXIT_OK, EXIT_FAILURE, EXIT_USAGE, EXIT_BLOCKED, EXIT_INTERRUPTED = 0, 1, 2, 3, 130
EXIT_BY_STATUS = {"success": EXIT_OK, "failure": EXIT_FAILURE, "blocked": EXIT_BLOCKED}

EPILOG = """\
exit codes: 0 success, 1 failure, 2 usage or invalid graph, 3 blocked, 130 interrupted

examples:
  to_graph.py check graphs/*.yaml
  to_graph.py render graphs/release.yaml > release.mmd
  to_graph.py render --format dot graphs/release.yaml | dot -Tsvg -o release.svg
  to_graph.py run --dry-run graphs/release.yaml VERSION=1.4.0
  to_graph.py run graphs/release.yaml VERSION=1.4.0 --decide approve=approved
"""


# --- graph model -------------------------------------------------------------


def kind(node: Node) -> str:
    return node.get("kind", "task")


def outcomes(node: Node) -> set[str]:
    return BUILTIN_OUTCOMES[kind(node)] | set(node.get("outcomes", []))


def exits(node: Node) -> set[str]:
    """Every node this node can route to."""
    retry_then = {node["retry"]["then"]} if "retry" in node else set()
    return set(node.get("next", {}).values()) | retry_then


def env_name(nid: str) -> str:
    """Environment variable that carries a node's output into later commands."""
    return "TG_OUTPUT_" + re.sub(r"\W", "_", nid)


def strings(value: Any) -> Iterator[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for item in value.values():
            yield from strings(item)
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)


def load(path: Path) -> Graph:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


# --- check -------------------------------------------------------------------


def node_errors(nid: str, node: Node, graph: Graph) -> list[str]:
    nodes, inputs = graph["nodes"], graph.get("inputs", {})
    nxt, allowed = node.get("next", {}), outcomes(node)
    errors: list[str] = []

    targets = [(f"next.{o}", t) for o, t in nxt.items()]
    targets += [("retry.then", node["retry"]["then"])] if "retry" in node else []
    targets += [("gate.evidence", e) for e in node.get("gate", {}).get("evidence", [])]
    errors += [f"{nid}.{where}: unknown node '{t}'" for where, t in targets if t not in nodes]
    errors += [
        f"{nid}.next.{o}: not an outcome of this {kind(node)}; declare it in outcomes" for o in nxt if o not in allowed
    ]

    if "retry" in node and node["retry"]["when"] not in allowed:
        errors.append(f"{nid}.retry.when: '{node['retry']['when']}' is not an outcome of this node")
    if kind(node) == "task" and not ({"succeeded"} | set(node.get("outcomes", []))) & set(nxt):
        errors.append(f"{nid}: next maps no success outcome")
    if kind(node) == "terminal":
        errors += [f"{nid}: a terminal ends the graph; remove {f}" for f in ("next", "run", "retry") if f in node]
    if kind(node) == "gate":
        errors += [f"{nid}: gate needs next.{need}" for need in ("approved", "rejected") if need not in nxt]

    for text in strings(node):
        for name, is_output in REF.findall(text):
            if is_output and name not in nodes:
                errors.append(f"{nid}: ${{{name}.output}} names no node")
            elif name not in inputs and name not in nodes:
                errors.append(f"{nid}: ${{{name}}} is not a declared input or node")
    return errors


def id_errors(nodes: dict[str, Node]) -> list[str]:
    seen: dict[str, str] = {}
    errors = []
    for nid in nodes:
        other = seen.setdefault(env_name(nid), nid)
        if other != nid:
            errors.append(f"{nid}: collides with {other}; ids must differ by more than - and _")
    return errors


def cycle_errors(nodes: dict[str, Node]) -> list[str]:
    links = {nid: exits(n) & set(nodes) for nid, n in nodes.items()}
    state: dict[str, str] = {}
    errors: list[str] = []

    def visit(u: str) -> None:
        state[u] = "open"
        for v in sorted(links[u]):
            if state.get(v) == "open":
                errors.append(f"cycle {u} -> {v}; only a node's own retry may repeat it")
            elif v not in state:
                visit(v)
        state[u] = "done"

    for nid in nodes:
        if nid not in state:
            visit(nid)
    return errors


def reach_errors(nodes: dict[str, Node]) -> list[str]:
    terminals = {nid for nid, n in nodes.items() if kind(n) == "terminal"}
    if not terminals:
        return ["graph has no terminal node"]
    reach, grew = set(terminals), True
    while grew:
        grew = False
        for nid, node in nodes.items():
            if nid not in reach and exits(node) & reach:
                reach.add(nid)
                grew = True
    return [f"{nid}: cannot reach a terminal" for nid in nodes if nid not in reach]


def check(path: Path) -> list[str]:
    """Return every problem in the graph file; empty means valid."""
    try:
        graph = load(path)
    except (OSError, yaml.YAMLError) as exc:
        return [f"cannot read: {exc}"]
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors = [
        f"schema: {'/'.join(map(str, e.absolute_path)) or '<root>'}: {e.message}"
        for e in Draft202012Validator(schema).iter_errors(graph)
    ]
    if errors:
        return errors
    nodes = graph["nodes"]
    errors = [e for nid, node in nodes.items() for e in node_errors(nid, node, graph)]
    errors += [
        f"criteria.{cid}: unknown node '{v}'"
        for cid, c in graph.get("criteria", {}).items()
        for v in c["verified_by"]
        if v not in nodes
    ]
    return errors + id_errors(nodes) + cycle_errors(nodes) + reach_errors(nodes)


# --- render ------------------------------------------------------------------

MERMAID_SHAPE = {"task": ('["', '"]'), "gate": ('{"', '"}'), "terminal": ('(["', '"])')}
DOT_SHAPE = {"task": "box", "gate": "diamond", "terminal": "doublecircle"}
STATUS_FILL = {"success": "#d3f9d8", "failure": "#ffe3e3", "blocked": "#fff3bf"}


def runner_label(node: Node) -> str:
    run = node.get("run")
    if isinstance(run, str):
        return run.split()[0] if run.split() else ""
    return run["uses"] if run else ""


def links(nid: str, node: Node) -> Iterator[tuple[str, str, bool]]:
    """Yield (target, label, dashed) for every way out of a node."""
    for outcome, target in node.get("next", {}).items():
        yield target, ("" if outcome == "succeeded" else outcome), False
    if "retry" in node:
        r = node["retry"]
        every = f" every {r['every']}" if "every" in r else ""
        yield nid, f"{r['when']} ≤{r['max']}{every}", True
        yield r["then"], "retries exhausted", True


def mermaid(graph: Graph) -> str:
    key = {nid: f"n{i}" for i, nid in enumerate(graph["nodes"])}  # ids can be Mermaid keywords such as end

    def text(value: str) -> str:
        return value.replace('"', "#quot;")

    lines = ["flowchart TD"]
    for nid, node in graph["nodes"].items():
        open_, close = MERMAID_SHAPE[kind(node)]
        sub = f"<br/><small>{text(runner_label(node))}</small>" if runner_label(node) else ""
        lines.append(f"  {key[nid]}{open_}{text(nid)}{sub}{close}")
        if kind(node) == "terminal":
            lines.append(f"  style {key[nid]} fill:{STATUS_FILL[node['status']]},color:#111")
    for nid, node in graph["nodes"].items():
        for target, label, dashed in links(nid, node):
            arrow = ("-.->" if dashed else "-->") + (f'|"{text(label)}"|' if label else "")
            lines.append(f"  {key[nid]} {arrow} {key[target]}")
    return "\n".join(lines)


def dot_text(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def dot(graph: Graph) -> str:
    lines = ["digraph G {", "  rankdir=TB; node [fontname=Helvetica];"]
    for nid, node in graph["nodes"].items():
        fill = f', style=filled, fillcolor="{STATUS_FILL[node["status"]]}"' if kind(node) == "terminal" else ""
        lines.append(f'  "{dot_text(nid)}" [shape={DOT_SHAPE[kind(node)]}{fill}];')
    for nid, node in graph["nodes"].items():
        for target, label, dashed in links(nid, node):
            attrs = ([f'label="{dot_text(label)}"'] if label else []) + (["style=dashed"] if dashed else [])
            suffix = f" [{', '.join(attrs)}]" if attrs else ""
            lines.append(f'  "{dot_text(nid)}" -> "{dot_text(target)}"{suffix};')
    return "\n".join([*lines, "}"])


# --- run ---------------------------------------------------------------------


def log(message: str) -> None:
    print(f"[to-graph] {message}", file=sys.stderr, flush=True)


def seconds(every: str) -> int:
    return int(every[:-1]) * UNIT_SECONDS[every[-1]]


class Runner:
    """Walk the graph one node at a time.

    A node is ready once every node that links to it has finished. A link that
    was not taken is pruned along with the path behind it, so branches never
    deadlock a join.
    """

    def __init__(self, graph: Graph, values: dict[str, str], decisions: dict[str, str], dry_run: bool):
        self.nodes: dict[str, Node] = graph["nodes"]
        self.values, self.decisions, self.dry_run = values, decisions, dry_run
        self.outputs: dict[str, str] = {}
        self.preds = {nid: {p for p, n in self.nodes.items() if nid in exits(n)} for nid in self.nodes}
        self.finished: dict[str, set[str]] = {nid: set() for nid in self.nodes}
        self.arrivals: dict[str, list[str]] = {nid: [] for nid in self.nodes}

    def value(self, name: str, is_output: bool, nid: str) -> str:
        if not (is_output or name in self.nodes):
            return self.values[name]
        if name not in self.outputs:
            if not self.dry_run:
                log(f"{nid}: ${{{name}.output}} is empty because {name} did not run")
            return f"<{name}.output>" if self.dry_run else ""
        return self.outputs[name]

    def substitute(self, value: Any, nid: str) -> Any:
        """Insert values as text; used for `with` data and log lines, never for shell code."""
        if isinstance(value, dict):
            return {k: self.substitute(v, nid) for k, v in value.items()}
        if isinstance(value, list):
            return [self.substitute(v, nid) for v in value]
        if not isinstance(value, str):
            return value
        return REF.sub(lambda m: self.value(m.group(1), bool(m.group(2)), nid), value)

    def shell(self, script: str, nid: str) -> tuple[str, dict[str, str]]:
        """Turn a string run into bash code plus environment.

        Values reach bash as environment variables, so bash expands them as data
        and never parses them as code. `${node.output}` becomes `${TG_OUTPUT_node}`.
        """
        env = {**os.environ, **self.values}
        for name in {m.group(1) for m in REF.finditer(script) if m.group(2) or m.group(1) in self.nodes}:
            env[env_name(name)] = self.value(name, True, nid)

        def rename(match: re.Match[str]) -> str:
            name, is_output = match.group(1), match.group(2)
            return f"${{{env_name(name)}}}" if is_output or name in self.nodes else match.group(0)

        return REF.sub(rename, script), env

    def execute(self, nid: str, node: Node) -> str:
        """Run a node's command once and return its outcome."""
        run, env = node["run"], None
        if isinstance(run, str):
            command, stdin = ["bash", "-c", run], None
        else:
            command, stdin = [run["uses"]], json.dumps(self.substitute(run.get("with", {}), nid))
        if self.dry_run:
            shown = self.substitute(run, nid) if isinstance(run, str) else f"{command[0]} <<< {stdin}"
            log(f"{nid}: would run: {shown}")
            named = [o for o in node.get("outcomes", []) if o in node.get("next", {})]
            return "succeeded" if "succeeded" in node.get("next", {}) else named[0]
        if isinstance(run, str):
            script, env = self.shell(run, nid)
            command = ["bash", "-c", script]

        with subprocess.Popen(
            command, stdin=subprocess.PIPE if stdin else None, stdout=subprocess.PIPE, text=True, env=env
        ) as proc:
            if stdin is not None and proc.stdin:
                proc.stdin.write(stdin)
                proc.stdin.close()
            last = ""
            for line in proc.stdout or ():
                sys.stdout.write(line)
                last = line.strip() or last
            code = proc.wait()
        self.outputs[nid] = last
        if last in node.get("outcomes", []):
            return last
        return "succeeded" if code == 0 else "failed"

    def decide(self, nid: str, node: Node) -> str:
        if nid in self.decisions:
            return self.decisions[nid]
        if self.dry_run:
            return "approved"
        if sys.stdin.isatty():
            who = node["gate"]["authority"]
            evidence = ", ".join(node["gate"].get("evidence", [])) or "none"
            answer = input(f"[to-graph] gate {nid}: {node['outcome']} ({who}; evidence: {evidence}) approve? [y/n] ")
            return "approved" if answer.strip().lower().startswith("y") else "rejected"
        return "unavailable"

    def step(self, nid: str) -> tuple[str, str | None]:
        """Run one node; return its outcome and the node it routes to (None if unmapped)."""
        node = self.nodes[nid]
        if kind(node) == "gate":
            outcome = self.decide(nid, node)
        elif "run" not in node:
            outcome = "failed" if {"failed", "missing"} & set(self.arrivals[nid]) else "succeeded"
        else:
            retry, attempt = node.get("retry"), 1
            outcome = self.execute(nid, node)
            while retry and outcome == retry["when"] and not self.dry_run:
                if attempt > retry["max"]:
                    log(f"{nid}: {outcome} after {attempt} attempts; retries exhausted")
                    return outcome, retry["then"]
                log(f"{nid}: {outcome}; retry {attempt}/{retry['max']}")
                attempt += 1
                time.sleep(seconds(retry.get("every", "0s")))
                outcome = self.execute(nid, node)
        log(f"{nid}: {outcome}")
        return outcome, node.get("next", {}).get(outcome)

    def finish(self, src: str, chosen: str | None, outcome: str, ready: list[str], ran: bool = True) -> None:
        """Record that src is done; queue each target whose predecessors are all done.

        A predecessor that ran but went elsewhere arrives as "missing", so a join
        without `run` fails. A predecessor on a pruned path does not count.
        """
        for target in exits(self.nodes[src]):
            self.finished[target].add(src)
            if target == chosen:
                self.arrivals[target].append("failed" if outcome == "failed" else "ok")
            elif ran:
                self.arrivals[target].append("missing")
            if self.finished[target] == self.preds[target]:
                if {"ok", "failed"} & set(self.arrivals[target]):
                    ready.append(target)
                else:
                    self.finish(target, None, "", ready, ran=False)

    def run(self) -> int:
        ready = [nid for nid in self.nodes if not self.preds[nid]]
        if not ready:
            log("no node can start: every node has a predecessor")
            return EXIT_USAGE
        ends: list[str] = []
        while ready:
            nid = ready.pop(0)
            node = self.nodes[nid]
            if kind(node) == "terminal":
                log(f"end: {nid} ({node['status']}) - {self.substitute(node['outcome'], nid)}")
                ends.append(node["status"])
                continue
            outcome, chosen = self.step(nid)
            if chosen is None:
                end = "blocked" if outcome == "unavailable" else "failure"
                log(f"{nid}: no next for {outcome}; this branch ends {end}")
                ends.append(end)
            self.finish(nid, chosen, outcome, ready)
        status = "failure" if "failure" in ends else "blocked" if "blocked" in ends or not ends else "success"
        log(f"result: {status}")
        return EXIT_BY_STATUS[status]


def resolve_inputs(graph: Graph, given: dict[str, str], dry_run: bool) -> tuple[dict[str, str], list[str]]:
    """Inputs come from NAME=VALUE, then the environment, then the default."""
    values: dict[str, str] = {}
    missing: list[str] = []
    for name, spec in graph.get("inputs", {}).items():
        value = given.get(name, os.environ.get(name, spec.get("default")))
        if value is None:
            if spec.get("required", True):
                missing.append(name)
            value = f"<{name}>" if dry_run else ""
        values[name] = str(value)
    return values, missing


# --- command line ------------------------------------------------------------


def pairs(items: Sequence[str], what: str) -> dict[str, str]:
    result = {}
    for item in items:
        name, sep, value = item.partition("=")
        if not sep or not name:
            raise argparse.ArgumentTypeError(f"{what} must be NAME=VALUE: {item!r}")
        result[name] = value
    return result


def report(path: Path, errors: list[str]) -> None:
    for error in errors:
        print(f"{path}: {error}", file=sys.stderr)


def cmd_check(args: argparse.Namespace) -> int:
    failed = False
    for path in args.graphs:
        errors = check(path)
        report(path, errors)
        if not errors:
            print(f"{path}: ok")
        failed = failed or bool(errors)
    return EXIT_USAGE if failed else EXIT_OK


def cmd_render(args: argparse.Namespace) -> int:
    errors = check(args.graph)
    if errors:
        report(args.graph, errors)
        return EXIT_USAGE
    graph = load(args.graph)
    print(mermaid(graph) if args.format == "mermaid" else dot(graph))
    return EXIT_OK


def cmd_run(args: argparse.Namespace) -> int:
    errors = check(args.graph)
    if errors:
        report(args.graph, errors)
        return EXIT_USAGE
    graph = load(args.graph)
    given, decisions = pairs(args.inputs, "input"), pairs(args.decide, "--decide")
    declared = graph.get("inputs", {})
    problems = [f"unknown input {n} (declared: {', '.join(declared) or 'none'})" for n in given if n not in declared]
    problems += [f"--decide: {g} is not a gate" for g in decisions if kind(graph["nodes"].get(g, {})) != "gate"]
    problems += [
        f"--decide: {g}={o} must be approved, rejected, or unavailable"
        for g, o in decisions.items()
        if o not in BUILTIN_OUTCOMES["gate"]
    ]
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return EXIT_USAGE
    values, missing = resolve_inputs(graph, given, args.dry_run)
    if missing and not args.dry_run:
        print(f"missing inputs: {', '.join(missing)} (pass NAME=VALUE)", file=sys.stderr)
        return EXIT_USAGE
    return Runner(graph, values, decisions, args.dry_run).run()


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(
        prog="to_graph.py",
        description=__doc__.splitlines()[0],
        epilog=EPILOG,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = root.add_subparsers(dest="command", required=True, metavar="COMMAND")

    p = sub.add_parser("check", help="validate graph files; print ok per valid file")
    p.add_argument("graphs", nargs="+", type=Path, metavar="GRAPH")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("render", help="print a Mermaid or Graphviz DOT diagram")
    p.add_argument("graph", type=Path, metavar="GRAPH")
    p.add_argument("--format", choices=("mermaid", "dot"), default="mermaid", help="diagram format (default: mermaid)")
    p.set_defaults(func=cmd_render)

    p = sub.add_parser(
        "run",
        help="run a graph",
        description=(
            "Run a graph. A string run executes with bash; {uses, with} executes `uses` with `with` as JSON on "
            "stdin. A node's outcome is its last printed line when that line is a declared outcome; otherwise "
            "exit 0 is succeeded and anything else failed. Gates use --decide, else ask on a terminal, else end "
            "as unavailable. Command output goes to stdout; progress goes to stderr."
        ),
    )
    p.add_argument("graph", type=Path, metavar="GRAPH")
    p.add_argument("inputs", nargs="*", metavar="NAME=VALUE", help="input values; override env and defaults")
    p.add_argument("--decide", action="append", default=[], metavar="GATE=OUTCOME", help="pre-answer a gate")
    p.add_argument("-n", "--dry-run", action="store_true", help="print the success path and commands; run nothing")
    p.set_defaults(func=cmd_run)
    return root


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    try:
        return args.func(args)
    except argparse.ArgumentTypeError as exc:
        print(f"to_graph.py: {exc}", file=sys.stderr)
        return EXIT_USAGE
    except KeyboardInterrupt:
        log("interrupted")
        return EXIT_INTERRUPTED


if __name__ == "__main__":
    raise SystemExit(main())
