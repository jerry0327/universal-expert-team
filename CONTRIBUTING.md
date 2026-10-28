# Contributing

Contributions are welcome through GitHub issues and pull requests.

## What makes a useful change

Keep the core workflow useful across subjects and environments. Propose a change with a concrete task, the observed behavior, the expected outcome, and enough public or synthetic input to reproduce the problem. Explain any host or tool assumptions.

Do not include private conversations, credentials, personal account identifiers, confidential documents or another person's data. Replace them with a small synthetic example.

## Make a focused pull request

1. Edit the installable skill in `skills/universal-expert-team/` or the relevant repository documentation.
2. Keep `SKILL.md` concise; place conditional procedures in its directly linked references.
3. Update both README languages when user-visible behavior changes.
4. Run the validation and packaging commands in [the validation guide](docs/validation.md).
5. Describe what you actually checked. Distinguish real tool execution from a written scenario and from unsupported behavior.

Use a new, scoped worker for independent review when the host supports one. Record the artifact reviewed and the material findings. A second pass by the author is useful, but does not count as an independent review.

## Design boundaries

- Preserve the default single complete delivery mode. Iteration follows the user's requested scope and ends at observable acceptance.
- Prefer native collaboration when available; never invent workers, tools, model settings or access.
- Use the highest available capability tier and deepest supported reasoning unless the user's current instructions or host restrictions require otherwise.
- Keep external publication, messages, device access and costs inside the user's actual authorization.
- Resolve conflicting evidence on its merits, not by vote count.
- Avoid hard-coded rosters, agent counts, model versions, devices or fixed review rounds.

By submitting a contribution, you agree to license it under the project's [MIT License](LICENSE). Do not contribute material you do not have the right to share.
