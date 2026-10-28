"""Regression checks for publication boundaries, using disposable repositories."""

import hashlib
import os
from pathlib import Path
import tempfile
import unittest
import zipfile

from scripts.build_release import archive_bytes, build
from scripts.validate import ValidationError, validate


class ReleaseTests(unittest.TestCase):
    def fixture(self) -> Path:
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        repo = Path(temporary.name)
        package = repo / "skills/universal-expert-team"
        package.mkdir(parents=True)
        (repo / "VERSION").write_text("1.0.0\n", encoding="utf-8")
        (repo / "LICENSE").write_text(
            "MIT License\n\nCopyright (c) 2026 Test Author\n\n"
            "Permission is hereby granted, free of charge, to any person.\n",
            encoding="utf-8",
        )
        files = {
            "SKILL.md": (
                "---\nname: universal-expert-team\n"
                'description: "Coordinate useful expert work."\n---\n\n'
                "# Universal Expert Team\n\n"
                "[Work](references/work-packages.md)\n"
                "[Review](references/review-strategies.md)\n"
                "[Boundary](references/execution-boundaries.md)\n"
                "[Runtime](references/runtime-adapters.md)\n"
            ),
            "agents/openai.yaml": (
                'interface:\n  display_name: "Universal Expert Team"\n'
                '  icon_small: "./assets/icon.svg"\n'
            ),
            "assets/icon.svg": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"/>\n',
            "references/work-packages.md": "# Work\nDefine acceptance.\n",
            "references/review-strategies.md": "# Review\nAssess the evidence.\n",
            "references/execution-boundaries.md": "# Boundary\nRespect authorization.\n",
            "references/runtime-adapters.md": "# Runtime\nDiscover actual tools.\n",
        }
        for relative, content in files.items():
            path = package / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        return repo

    def test_release_has_only_public_files_and_matching_checksum(self):
        repo = self.fixture()
        (repo / "private-notes.txt").write_text("must never ship", encoding="utf-8")
        archive, digest = build(repo)
        expected = {
            "universal-expert-team/LICENSE",
            "universal-expert-team/SKILL.md",
            "universal-expert-team/agents/openai.yaml",
            "universal-expert-team/assets/icon.svg",
            "universal-expert-team/references/execution-boundaries.md",
            "universal-expert-team/references/review-strategies.md",
            "universal-expert-team/references/runtime-adapters.md",
            "universal-expert-team/references/work-packages.md",
        }
        with zipfile.ZipFile(archive) as release:
            self.assertEqual(set(release.namelist()), expected)
            self.assertEqual(len(release.namelist()), len(expected))
            self.assertEqual(release.read("universal-expert-team/LICENSE"), (repo / "LICENSE").read_bytes())
            self.assertIsNone(release.testzip())
        self.assertEqual(archive.name, "universal-expert-team-v1.0.0.zip")
        self.assertEqual(digest, hashlib.sha256(archive.read_bytes()).hexdigest())
        self.assertEqual((repo / "dist/SHA256SUMS").read_text(), f"{digest}  {archive.name}\n")

    def test_rebuild_is_identical_after_metadata_changes(self):
        repo = self.fixture()
        archive, first_digest = build(repo)
        first_bytes = archive.read_bytes()
        for path in (repo / "skills").rglob("*"):
            if path.is_file():
                os.utime(path, (1_700_000_000, 1_700_000_000))
                path.chmod(0o755)
        archive, second_digest = build(repo)
        self.assertEqual(first_bytes, archive.read_bytes())
        self.assertEqual(first_digest, second_digest)

    def test_source_symlinks_and_extra_files_are_rejected(self):
        for kind in ("file-link", "directory-link", "extra-file"):
            with self.subTest(kind=kind):
                repo = self.fixture()
                package = repo / "skills/universal-expert-team"
                if kind == "file-link":
                    path = package / "SKILL.md"
                    target = repo / "saved-skill.md"
                    path.rename(target)
                    path.symlink_to(target)
                elif kind == "directory-link":
                    path = package / "references"
                    target = repo / "saved-references"
                    path.rename(target)
                    path.symlink_to(target, target_is_directory=True)
                else:
                    (package / ".env").write_text("SECRET=not-for-release\n", encoding="utf-8")
                with self.assertRaises(ValidationError):
                    build(repo)
                self.assertFalse((repo / "dist").exists())

    def test_missing_and_escaping_local_links_are_rejected(self):
        targets = ("../LICENSE", "%2e%2e/LICENSE", "/absolute.md", "C:/absolute.md",
                   "references\\work-packages.md", "references/missing.md")
        for target in targets:
            with self.subTest(target=target):
                repo = self.fixture()
                skill = repo / "skills/universal-expert-team/SKILL.md"
                with skill.open("a", encoding="utf-8") as handle:
                    handle.write(f"\n[Invalid]({target})\n")
                with self.assertRaises(ValidationError):
                    validate(repo)

    def test_output_links_cannot_overwrite_other_files(self):
        for kind in ("directory-link", "file-link", "hard-link"):
            with self.subTest(kind=kind):
                repo = self.fixture()
                outside = repo / "unrelated"
                outside.mkdir()
                protected = outside / "keep.txt"
                protected.write_text("preserve me", encoding="utf-8")
                output = repo / "dist"
                if kind == "directory-link":
                    output.symlink_to(outside, target_is_directory=True)
                else:
                    output.mkdir()
                    destination = output / "universal-expert-team-v1.0.0.zip"
                    if kind == "file-link":
                        destination.symlink_to(protected)
                    else:
                        os.link(protected, destination)
                with self.assertRaises(ValidationError):
                    build(repo)
                self.assertEqual(protected.read_text(), "preserve me")
                self.assertEqual(sorted(p.name for p in outside.iterdir()), ["keep.txt"])

    def test_archive_entry_and_version_traversal_are_rejected(self):
        for name in ("../secret", "/secret", "C:/secret", "a\\secret", "a/../secret", "a\x00b"):
            with self.subTest(entry=name), self.assertRaises(ValidationError):
                archive_bytes({name: b"unsafe"})
        repo = self.fixture()
        for version in ("../../outside", "1.0.0/secret", "v1.0.0", "01.0.0"):
            with self.subTest(version=version):
                (repo / "VERSION").write_text(version, encoding="utf-8")
                with self.assertRaises(ValidationError):
                    build(repo)
        self.assertFalse((repo / "dist").exists())

    def test_invalid_metadata_and_private_markers_are_rejected(self):
        mutations = (
            lambda s: s.replace("name: universal-expert-team", "name: wrong-name"),
            lambda s: s.replace('description: "Coordinate useful expert work."', "description: ''"),
            lambda s: s + "\nLoad /home/example/private-skill/SKILL.md\n",
            lambda s: s + "\nTODO: write this section\n",
        )
        for index, mutate in enumerate(mutations):
            with self.subTest(mutation=index):
                repo = self.fixture()
                skill = repo / "skills/universal-expert-team/SKILL.md"
                skill.write_text(mutate(skill.read_text(encoding="utf-8")), encoding="utf-8")
                with self.assertRaises(ValidationError):
                    validate(repo)


if __name__ == "__main__":
    unittest.main()
