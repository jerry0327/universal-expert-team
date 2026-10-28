#!/usr/bin/env python3
"""Validate the deliberately small public skill package using only the stdlib."""

from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


SKILL_NAME = "universal-expert-team"
SKILL_DIR = Path("skills") / SKILL_NAME
PACKAGE_FILES = (
    "SKILL.md",
    "agents/openai.yaml",
    "assets/icon.svg",
    "references/execution-boundaries.md",
    "references/review-strategies.md",
    "references/runtime-adapters.md",
    "references/work-packages.md",
)
REFERENCE_FILES = frozenset(p for p in PACKAGE_FILES if p.startswith("references/"))
PRIVATE_MARKERS = re.compile(
    r"/(?:root|home|Users|workspace|mnt/data|tmp)/"
    r"|[A-Za-z]:[\\/]Users[\\/]"
    r"|(?:skill|plugin|libfile)-[a-f0-9]{24,}"
    r"|(?:skill|oai-library|mcp-resource)://"
    r"|devspace-session-capabilities|devspace-task-scoped-collaboration",
    re.IGNORECASE,
)
PLACEHOLDERS = re.compile(r"\b(?:TODO|TBD|FIXME|CHANGEME)\b|<YOUR[_ -]", re.IGNORECASE)
MARKDOWN_LINK = re.compile(r"\[[^\]\n]*\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)")


class ValidationError(ValueError):
    """A package is unsafe or does not satisfy its declared public layout."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def checked_file(root: Path, relative: str) -> Path:
    """Return a regular file under root, rejecting ambiguous paths and symlinks."""
    parts = relative.split("/")
    require(bool(relative) and not PurePosixPath(relative).is_absolute(),
            f"Expected a relative path: {relative!r}")
    require(not re.search(r"[\\:\x00-\x1f]", relative)
            and not any(p in ("", "..") for p in parts),
            f"Unsafe relative path: {relative!r}")
    candidate = root
    for part in parts:
        candidate = candidate / part
        require(not candidate.is_symlink(), f"Symlinks are not allowed: {relative}")
    require(candidate.resolve().is_relative_to(root.resolve()),
            f"Path leaves package: {relative}")
    require(candidate.is_file(), f"Missing regular file: {relative}")
    return candidate


def read_text(root: Path, relative: str) -> str:
    path = checked_file(root, relative)
    require(path.stat().st_size <= 256_000, f"Unexpectedly large text file: {relative}")
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeError as exc:
        raise ValidationError(f"Not UTF-8 text: {relative}") from exc
    require("\x00" not in text, f"NUL byte in text: {relative}")
    return text


def scalar(value: str) -> str:
    """Read the one-line scalar subset used by this package, not general YAML."""
    value = value.strip()
    if value.startswith(('"', "'")):
        require(len(value) >= 2 and value[-1] == value[0], "Unclosed quoted scalar")
        value = value[1:-1]
    require(bool(value) and value not in ("|", ">", "null", "~"),
            "Expected a nonempty one-line scalar")
    return value


def frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    require(bool(lines) and lines[0] == "---", "SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValidationError("Unclosed SKILL.md frontmatter") from exc
    fields: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r"([a-z][a-z_-]*):\s*(.+)", line)
        require(match is not None, "Frontmatter must use one-line key: value fields")
        assert match is not None
        key, value = match.groups()
        require(key not in fields, f"Duplicate frontmatter key: {key}")
        fields[key] = scalar(value)
    require(fields.get("name") == SKILL_NAME, f"Frontmatter name must be {SKILL_NAME}")
    require(bool(fields.get("description")), "Frontmatter description is required")
    return fields


def local_target(package: Path, source: str, raw: str) -> str | None:
    """Resolve a simple inline Markdown target or skill-relative icon target."""
    target = unquote(raw.strip("<>"))
    parsed = urlsplit(target)
    if parsed.scheme:
        require(parsed.scheme in ("https", "http", "mailto"),
                f"Unsupported link scheme in {source}: {raw}")
        return None
    require(not parsed.netloc, f"Network path in {source}: {raw}")
    if not parsed.path:
        return None
    require(not parsed.query, f"Local file link has a query in {source}: {raw}")
    relative = str(PurePosixPath(source).parent / parsed.path)
    checked_file(package, relative)
    return PurePosixPath(relative).as_posix()


def validate(repo: Path) -> tuple[str, dict[str, bytes]]:
    """Return the version and validated archive payload, without writing anything."""
    repo = repo.absolute()
    require(repo.is_dir() and not repo.is_symlink(), "Repository must be a real directory")
    version = read_text(repo, "VERSION").strip()
    require(re.fullmatch(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)", version) is not None,
            "VERSION must be a plain numeric version such as 1.0.0")
    license_text = read_text(repo, "LICENSE")
    require(license_text.startswith("MIT License\n") and "Copyright" in license_text
            and "Permission is hereby granted" in license_text,
            "Root LICENSE must contain the MIT license and copyright notice")

    # Inspect every component, even though the archive has an explicit allowlist.
    for relative in PACKAGE_FILES:
        checked_file(repo, (SKILL_DIR / relative).as_posix())
    package = repo / SKILL_DIR
    expected_dirs = {str(PurePosixPath(p).parent) for p in PACKAGE_FILES} - {"."}
    for path in package.rglob("*"):
        relative = path.relative_to(package).as_posix()
        require(not path.is_symlink(), f"Symlinks are not allowed: {relative}")
        if path.is_dir():
            require(relative in expected_dirs, f"Unexpected package directory: {relative}")
        else:
            require(relative in PACKAGE_FILES, f"Unexpected package file: {relative}")

    texts = {relative: read_text(package, relative) for relative in PACKAGE_FILES}
    for relative, text in texts.items():
        require(not PRIVATE_MARKERS.search(text), f"Private path, ID or dependency in {relative}")
        require(not PLACEHOLDERS.search(text), f"Unresolved placeholder in {relative}")
    frontmatter(texts["SKILL.md"])
    skill_targets = set()
    for relative, text in texts.items():
        if relative.endswith(".md"):
            for raw in MARKDOWN_LINK.findall(text):
                target = local_target(package, relative, raw)
                if relative == "SKILL.md" and target is not None:
                    skill_targets.add(target)
    require(REFERENCE_FILES <= skill_targets, "SKILL.md must link all four bundled references")
    icons = re.findall(r"^\s+icon_(?:small|large):\s*(.+)$", texts["agents/openai.yaml"], re.MULTILINE)
    require(bool(icons), "agents/openai.yaml must declare a bundled icon")
    for icon in icons:
        target = local_target(package, "SKILL.md", scalar(icon))
        require(target == "assets/icon.svg", "Agent icons must use ./assets/icon.svg")
    try:
        svg = ET.fromstring(texts["assets/icon.svg"])
    except ET.ParseError as exc:
        raise ValidationError("assets/icon.svg is not valid XML") from exc
    require(svg.tag == "{http://www.w3.org/2000/svg}svg", "Icon must be an SVG image")
    for element in svg.iter():
        require(element.tag.rsplit("}", 1)[-1] not in ("script", "foreignObject"),
                "Icon must not contain active content")
        require(not any(key.lower().startswith("on") or key.rsplit("}", 1)[-1] == "href"
                        for key in element.attrib), "Icon must be self-contained and static")
    payload = {relative: text.encode("utf-8") for relative, text in texts.items()}
    payload["LICENSE"] = license_text.encode("utf-8")
    return version, payload


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1],
                        help="repository root (defaults to this script's repository)")
    args = parser.parse_args()
    try:
        version, payload = validate(args.repo)
    except (ValidationError, OSError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    print(f"Validated {SKILL_NAME} v{version}: {len(payload)} release files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
