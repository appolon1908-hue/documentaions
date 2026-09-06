#!/usr/bin/env python3
"""Fail-closed validation for the Codestra documentation repository."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

EXCLUDED = {".git", ".venv", ".venv-ci", "__pycache__", "node_modules", "dist", "build"}
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


class ValidationError(RuntimeError):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def iter_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if any(part in EXCLUDED for part in path.parts):
            continue
        if path.is_file():
            yield path


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def validate_paths(root: Path) -> None:
    for path in root.rglob("*"):
        if any(part in EXCLUDED for part in path.parts):
            continue
        if path.is_symlink():
            target = path.resolve(strict=False)
            try:
                target.relative_to(root)
            except ValueError:
                fail(f"symlink escapes repository: {rel(path, root)} -> {target}")
        if path.is_file() and path.stat().st_size > 50 * 1024 * 1024:
            fail(f"documentation file exceeds 50 MiB: {rel(path, root)}")


def validate_json(root: Path) -> int:
    checked = 0
    for path in iter_files(root):
        if path.suffix.lower() != ".json" or path.stat().st_size > 5 * 1024 * 1024:
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
            fail(f"invalid JSON in {rel(path, root)}: {exc}")
        checked += 1
    return checked


def validate_yaml(root: Path) -> int:
    try:
        import yaml  # type: ignore
    except ImportError as exc:
        fail(f"PyYAML is required: {exc}")
    checked = 0
    for path in iter_files(root):
        if path.suffix.lower() not in {".yaml", ".yml"} or path.stat().st_size > 5 * 1024 * 1024:
            continue
        try:
            list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
        except (OSError, UnicodeDecodeError, yaml.YAMLError) as exc:
            fail(f"invalid YAML in {rel(path, root)}: {exc}")
        checked += 1
    return checked


def validate_markdown(root: Path) -> tuple[int, int]:
    documents = 0
    links = 0
    for path in iter_files(root):
        if path.suffix.lower() not in {".md", ".mdx"} or path.stat().st_size > 5 * 1024 * 1024:
            continue
        documents += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        for raw in MARKDOWN_LINK.findall(text):
            target = raw.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "/", "http://", "https://", "mailto:", "tel:", "data:")) or any(marker in target for marker in ("${", "{{", "}}")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            destination = (path.parent / target).resolve(strict=False)
            try:
                destination.relative_to(root)
            except ValueError:
                fail(f"Markdown link escapes repository in {rel(path, root)}: {raw}")
            if not destination.exists():
                fail(f"broken local Markdown link in {rel(path, root)}: {raw}")
            links += 1
    return documents, links


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--mode", choices=("audit", "ci", "release"), default="ci")
    parser.add_argument("--branch", default=os.environ.get("GITHUB_REF_NAME", "unknown"))
    parser.add_argument("--repository-class", default="documentation")
    parser.add_argument("--evidence", type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    if not root.is_dir():
        fail(f"repository root does not exist: {root}")
    validate_paths(root)
    json_count = validate_json(root)
    yaml_count = validate_yaml(root)
    document_count, link_count = validate_markdown(root)
    if document_count == 0:
        fail("documentation repository contains no Markdown documents")

    payload = {
        "schema_version": 1,
        "repository": os.environ.get("GITHUB_REPOSITORY"),
        "source_sha": os.environ.get("GITHUB_SHA"),
        "source_tree": subprocess.run(["git", "rev-parse", "HEAD^{tree}"], cwd=root, check=False, capture_output=True, text=True).stdout.strip(),
        "branch": args.branch,
        "mode": args.mode,
        "repository_class": "documentation",
        "markdown_documents": document_count,
        "validated_local_markdown_links": link_count,
        "validated_json_files": json_count,
        "validated_yaml_files": yaml_count,
        "runtime_deployment_authorized": False,
        "external_effects_authorized": False,
    }
    if args.evidence is not None:
        args.evidence.parent.mkdir(parents=True, exist_ok=True)
        args.evidence.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(f"MARKDOWN_DOCUMENTS={document_count}")
    print(f"LOCAL_LINKS_VALIDATED={link_count}")
    print("RUNTIME_DEPLOYMENT_AUTHORIZED=NO")
    print("EXTERNAL_EFFECTS_AUTHORIZED=NO")
    print("DOCUMENTATION_VALIDATION=PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ValidationError as exc:
        print(f"DOCUMENTATION_VALIDATION_ERROR={exc}", file=sys.stderr)
        raise SystemExit(1)
