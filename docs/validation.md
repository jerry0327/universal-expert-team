# Validation and release construction

Run these commands from the repository root with Python 3.10 or newer. They use
only the Python standard library and do not require an API key, account, network
connection, npm, or a particular agent host.

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
python3 scripts/build_release.py
```

Both scripts also accept `--repo PATH` for an explicit repository root. The build
always writes inside that repository's `dist` directory; there is no independent
output-path option. Build from a checkout that is not being modified concurrently.

## Automated structural checks

`validate.py` checks the following release contract:

- `VERSION` is a numeric `major.minor.patch` value, and the root `LICENSE` contains
  an MIT heading, a copyright notice, and the permission grant.
- The skill contains exactly the seven declared files: `SKILL.md`,
  `agents/openai.yaml`, `assets/icon.svg`, and the four reference documents.
- `SKILL.md` starts with simple YAML frontmatter containing the expected name and
  a nonempty description. This intentionally supports one-line scalar values,
  not the complete YAML language.
- All four reference documents are linked from `SKILL.md`. Simple inline
  Markdown file links and declared agent icon paths resolve within the package.
  Parent traversal, absolute file paths, missing targets, and symlinks fail.
- The icon is parseable SVG without script, foreign objects, event handlers, or
  linked resources.
- Known private filesystem prefixes, private skill identifiers, private runtime
  dependencies, and common unfinished-copy markers are absent from skill files.

This is a focused release check, not a general Markdown/YAML parser, exhaustive
secret scanner, legal opinion, or proof that all instructions are correct.
Reference-style Markdown links and headings are not resolved. Human review must
still assess the actual wording, licensing and attribution, permissions, privacy,
and whether the skill works as intended.

## Archive guarantees and regression tests

The builder runs validation first, then snapshots the allowlisted skill files and
root license. It writes `dist/universal-expert-team-v1.0.0.zip` when `VERSION` is
`1.0.0`, with exactly one top-level `universal-expert-team/` directory. The ZIP
contains the seven skill files and `LICENSE`; repository documentation, tests,
Git history, and environment files are excluded.

Entries are sorted, their timestamp is fixed to the ZIP epoch, and their stored
permissions are ordinary read/write text-file permissions. Entries are stored
without compression to avoid differences between compression-library versions.
Text is UTF-8 with normalized newlines. The same validated text and version
produce the same archive bytes regardless of source file modification times and
permissions. `dist/SHA256SUMS` records the archive's SHA-256 digest and filename.

The regression suite builds disposable repositories to check exact archive
membership and checksum, repeated-build equality after metadata changes,
symlink and extra-file rejection, local-link escape and missing-target rejection,
output symlink/hard-link protection, unsafe archive names and version values,
and invalid metadata/private-marker rejection. These tests exercise the Python
tooling. They do not run an LLM or simulate successful agent execution.

To verify a downloaded release on a system with `sha256sum`, keep the checksum
file beside the ZIP and run:

```sh
sha256sum -c SHA256SUMS
```

## Behavioral scenarios and host compatibility

Before claiming that the skill works on a particular host, evaluate actual
behavior with the host's available tools. Useful scenarios include:

| Scenario | Evidence to seek |
| --- | --- |
| Single complete delivery | Complete accepted work; no invented ongoing review loop. |
| Explicit iterative review | Concrete acceptance criteria, independent assessment when available, repair, and affected rechecks. |
| No delegation interface | Truthful direct work and a clear account of the unavailable independent check. |
| More work than available workers | Queued work respects actual capacity; roles are not reported as created agents. |
| Denied or excluded execution route | Unaffected authorized work continues; no fallback bypasses the denial. |
| Shared files and late results | One active owner per shared resource; stale evidence is not treated as current acceptance. |

This table is an evaluation plan, not a claim that those scenarios have passed.
Record the host, tool availability, skill version, actual actions, observed
result, and any limitation when running them. A written scenario review is
different from a live execution test. Structural validation alone does not
establish behavior on Codex, Claude Code, ChatGPT, or any other host, and it does
not establish model configuration, permissions, or cross-device availability.

## Continuous integration

The GitHub workflow runs validation, regression tests, and archive construction
for pushes, pull requests, and manual runs. Its token has only `contents: read`,
and checkout does not persist credentials. It does not publish a release.

The checkout action is pinned to commit
`11d5960a326750d5838078e36cf38b85af677262`, verified against the official
[actions/checkout v4.4.0 release](https://github.com/actions/checkout/releases/tag/v4.4.0)
and its [commit](https://github.com/actions/checkout/commit/11d5960a326750d5838078e36cf38b85af677262).
The workflow uses Python supplied by the `ubuntu-24.04` runner. Passing local
commands is not evidence of a completed GitHub Actions run; inspect the actual
run before claiming remote CI success.
