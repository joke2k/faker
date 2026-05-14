"""
Verify a consistent order for top-level test helper classes in ``tests/``.

* Top-level classes whose names start with ``_`` come **before** any top-level
  class whose name starts with ``Test``.
* Among ``_…`` classes only: if one subclasses another defined in the same file,
  enforce base before subclass; otherwise require ASCII order by class name.
* Among ``Test…`` classes only: same as above (local ``Test*`` → ``Test*``
  inheritance vs strict ASCII).

Run from repo root: python scripts/check_test_class_order.py
"""

from __future__ import annotations

import ast
import sys

from collections import defaultdict
from pathlib import Path


def _local_bases(node: ast.ClassDef, defined: set[str]) -> list[str]:
    out: list[str] = []
    for base in node.bases:
        if isinstance(base, ast.Name) and base.id in defined:
            out.append(base.id)
    return out


def _check_group(
    path: Path,
    names: list[str],
    graph: dict[str, list[str]],
    label: str,
) -> list[str]:
    errors: list[str] = []
    if len(names) < 2:
        return errors

    idx = {n: i for i, n in enumerate(names)}
    for parent, children in graph.items():
        for child in children:
            if idx[parent] >= idx[child]:
                errors.append(f"{path}:{child}: subclass must appear after base `{parent}` in this file " f"({label}).")

    if graph:
        return errors

    n = len(names)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = names[i], names[j]
            if a > b:
                errors.append(
                    f"{path}: {label} classes out of order: `{a}` before `{b}` "
                    f"(ASCII order requires `{min(a, b)}` first)."
                )
    return errors


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    src = path.read_text(encoding="utf-8")
    try:
        tree = ast.parse(src, filename=str(path))
    except SyntaxError as e:
        return [f"{path}: syntax error: {e}"]

    underscore_names: list[str] = []
    test_names: list[str] = []
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        if node.name.startswith("_"):
            underscore_names.append(node.name)
        elif node.name.startswith("Test"):
            test_names.append(node.name)

    if underscore_names and test_names:
        u_max = max(
            i for i, node in enumerate(tree.body) if isinstance(node, ast.ClassDef) and node.name in underscore_names
        )
        t_min = min(i for i, node in enumerate(tree.body) if isinstance(node, ast.ClassDef) and node.name in test_names)
        if u_max > t_min:
            errors.append(
                f"{path}: top-level classes named with leading `_` must appear " f"before any top-level `Test*` class."
            )

    u_set = set(underscore_names)
    if len(underscore_names) >= 2:
        u_graph: dict[str, list[str]] = defaultdict(list)
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and node.name.startswith("_"):
                for parent in _local_bases(node, u_set):
                    if parent.startswith("_"):
                        u_graph[parent].append(node.name)
        errors.extend(_check_group(path, underscore_names, u_graph, "`_…`"))

    t_set = set(test_names)
    if len(test_names) >= 2:
        t_graph: dict[str, list[str]] = defaultdict(list)
        for node in tree.body:
            if isinstance(node, ast.ClassDef) and node.name.startswith("Test"):
                for parent in _local_bases(node, t_set):
                    if parent.startswith("Test"):
                        t_graph[parent].append(node.name)
        errors.extend(_check_group(path, test_names, t_graph, "`Test*`"))

    return errors


def main() -> int:
    tests_root = Path(__file__).resolve().parent.parent / "tests"
    all_errors: list[str] = []
    for path in sorted(tests_root.rglob("*.py")):
        all_errors.extend(check_file(path))

    if all_errors:
        print("\n".join(all_errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
