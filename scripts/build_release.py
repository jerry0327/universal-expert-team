#!/usr/bin/env python3
"""Build a deterministic, allowlisted skill ZIP and its SHA-256 checksum."""

from __future__ import annotations

import argparse
import hashlib
import io
from pathlib import Path
import re
import stat
import sys
import zipfile

try:
    from .validate import SKILL_NAME, ValidationError, require, validate
except ImportError:
    from validate import SKILL_NAME, ValidationError, require, validate


def archive_bytes(payload: dict[str, bytes]) -> bytes:
    """Use stored entries so output is independent of the installed zlib version."""
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_STORED) as archive:
        for relative, content in sorted(payload.items()):
            require(relative and not relative.startswith("/")
                    and not re.search(r"[\\:\x00-\x1f]", relative)
                    and all(part not in ("", ".", "..") for part in relative.split("/")),
                    f"Unsafe archive entry: {relative!r}")
            entry = zipfile.ZipInfo(f"{SKILL_NAME}/{relative}", date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = (stat.S_IFREG | 0o644) << 16
            archive.writestr(entry, content)
    return output.getvalue()


def build(repo: Path) -> tuple[Path, str]:
    # Validation snapshots only approved text files. No recursive packaging occurs.
    repo = repo.absolute()
    version, payload = validate(repo)
    data = archive_bytes(payload)
    digest = hashlib.sha256(data).hexdigest()
    output = repo / "dist"
    require(not output.is_symlink(), "dist must not be a symlink")
    require(not output.exists() or output.is_dir(), "dist must be a directory")
    output.mkdir(exist_ok=True)
    archive = output / f"{SKILL_NAME}-v{version}.zip"
    checksums = output / "SHA256SUMS"
    for path in (archive, checksums):
        require(not path.is_symlink(), f"Output must not be a symlink: {path.name}")
        require(not path.exists() or path.is_file(), f"Output must be a regular file: {path.name}")
        require(not path.exists() or path.stat().st_nlink == 1,
                f"Output must not be a hard link: {path.name}")
    archive.write_bytes(data)
    checksums.write_text(f"{digest}  {archive.name}\n", encoding="ascii", newline="\n")
    return archive, digest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1],
                        help="repository root; output is always its dist directory")
    args = parser.parse_args()
    try:
        archive, digest = build(args.repo)
    except (ValidationError, OSError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1
    print(f"Built {archive}\nSHA256 {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
