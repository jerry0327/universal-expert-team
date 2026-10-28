<div align="center">

<img src="skills/universal-expert-team/assets/icon.svg" alt="Universal Expert Team" width="88" height="88">

# Universal Expert Team

**Build the team around the task. Verify with evidence. Deliver usable work.**

A reusable coordination skill for research, writing, software, analysis, and work across disciplines.

[![License: MIT](https://img.shields.io/badge/License-MIT-2563eb.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/jerry0327/universal-expert-team?color=2563eb)](https://github.com/jerry0327/universal-expert-team/releases/latest)
[![Language](https://img.shields.io/badge/English-繁體中文-475569)](README.md)

[Download](https://github.com/jerry0327/universal-expert-team/releases/latest) · [Installation](docs/installation.md#english) · [Usage](docs/usage.md#english) · [Skill source](skills/universal-expert-team/SKILL.md)

</div>

---

Universal Expert Team guides an AI assistant through designing a team, delegating useful work, integrating results, and arranging independent review and repair when needed. Specialties emerge from the task: a research comparison needs different work packages from a software fix, a data analysis, or a publication draft.

This repository provides a complete, readable skill and its references. **The host supplies the actual agents, search, files, browser access, and model controls.** When a capability is missing, the workflow requires the assistant to explain the limit, complete unaffected work, and identify what remains unverified.

## What it helps you do

| Need | Approach |
| --- | --- |
| Combine different kinds of expertise | Design work packages around outcomes, dependencies, and risk, without a fixed roster or agent count. |
| Get a finished result | Research, create, edit, check, and integrate within the user's authorization; use a single complete delivery by default. |
| Check consequential work | Choose source verification, independent review, counterexample search, or hands-on validation for the actual failure risk. |
| Keep revisions focused | Define observable acceptance criteria, repair concrete defects, and stop at acceptance or a specific blocker. |
| Work across different hosts | Inspect the tools, permissions, and capacity available in the current session before choosing an execution route. |

Use it when a task benefits from separable work or different judgments. For a small task with no useful independent split, the assistant may finish directly. Naming several roles does not establish that several agents ran.

## Three ways to work

| Mode | Choose it when | Result |
| --- | --- | --- |
| **Single complete delivery** | Default; “finish this in one delivery” | Complete the work, perform necessary checks, repair known material problems, and deliver. |
| **Iterative review and repair** | “Keep verifying and fixing until these criteria hold” | Obtain a non-author's assessment when available, repair concrete defects, and recheck affected evidence. No fixed round count. |
| **Mixed scope** | Different components need different scrutiny | Apply iterative review to one component and single delivery to another. This combines the first two modes by scope. |

“Thorough,” “professional,” or “high quality” alone does not request an endless loop. Every mode must address known material errors. Iteration does not authorize unrelated scope expansion.

## Download and get started

1. Open [Releases](https://github.com/jerry0327/universal-expert-team/releases/latest) and choose `universal-expert-team-v1.0.0.zip`. Alternatively, obtain the complete `skills/universal-expert-team/` directory and copy the repository-root `LICENSE` into the installed skill folder, as shown in the [installation guide](docs/installation.md#english).
2. **ChatGPT environments that support skill uploads:** upload the complete ZIP, request installation, and verify that the skill was loaded. Availability depends on your account and interface; attaching a file is not proof of installation.
3. **Local Codex:** place the complete skill directory at `.agents/skills/universal-expert-team/` in your project and verify discovery. See the [installation guide](docs/installation.md#english) for commands and other scopes, based on [official OpenAI documentation](https://learn.chatgpt.com/docs/build-skills).
4. Once installed, ask the assistant to use the skill and provide the outcome, inputs, boundaries, and acceptance criteria.

```text
Use universal-expert-team to design the division of work for this task
and finish it in one complete delivery.

Outcome: [what I need]
Inputs: [files, links, data, or working directory]
Boundaries: [time, format, editable scope, excluded actions]
Acceptance: [observable completion criteria]

Check the agents and tools actually available in this session.
Delegate useful independent work. Deliver the result, relevant verification
evidence, and anything that could not be established.
```

After installation, supported ChatGPT interfaces can select a skill with `@`; Codex can use `$universal-expert-team`. **Typing `@universal-expert-team` alone does not download or install anything.** Pasted instructions do not create an agent runtime. See the [official invocation guide](https://learn.chatgpt.com/docs/build-skills).

## Copyable examples

**Research and a decision**

```text
Use universal-expert-team to compare [options A, B, and C] for [use case].
Choose the needed specialties from the questions, then deliver a comparison,
a recommendation, and sources in one complete response.
Separate sourced facts, inference, and missing evidence.
If search or original sources are unavailable, deliver the supported analysis
and identify the resulting limits.
```

**Software repair with iterative acceptance**

```text
Use universal-expert-team to fix [reproducible problem] in this repository.
Arrange implementation and independent review where available.
Keep repairing until the reproducer and relevant existing checks pass,
with no unresolved material defect.
You may change necessary code and tests. Do not deploy or message anyone.
Deliver the changes, verification results, and remaining risks.
```

**Writing with mixed scope**

```text
Use universal-expert-team to turn these materials into a report for [audience].
Iteratively verify data and citations until each main claim has a traceable
source. Complete prose and layout in a single delivery.
Do not invent facts absent from the inputs.
Deliver the report with the necessary sources and limitations.
```

Find more examples and acceptance guidance in the [usage guide](docs/usage.md#english).

## Review philosophy

- **Distinguish roles, workers, and outputs.** Claims about delegation must match the work that actually ran.
- **Give review a chance to find a problem.** Provide the artifact, authoritative inputs, and acceptance criteria. An author's second pass is not independent review.
- **Resolve disagreement through evidence.** Several agents repeating one source do not create independent evidence. A majority vote does not establish correctness.
- **Recheck the affected version.** Evidence for an earlier artifact does not certify a material revision; accepted, unaffected work need not be repeated.
- **Make stopping meaningful.** Deliver when the agreed outcome and checks are satisfied. Report an essential missing source or capability as a blocker instead of declaring success.

See [review strategies](skills/universal-expert-team/references/review-strategies.md) and [work packages](skills/universal-expert-team/references/work-packages.md) for the full process.

## Capabilities and limits

The skill prefers the host's native agent interface. Where selection is available, it calls for the highest available capability tier and deepest supported reasoning, subject to the host and the user's constraints. Requested settings must be distinguished from observed settings. No particular model, concurrency level, or background execution is guaranteed.

| What the host actually provides | Expected behavior |
| --- | --- |
| Skill loading and real subagent tools | Delegate within available capacity, gather outputs, arrange review, and integrate. |
| Skill loading without subagent tools | Use the workflow with a single assistant; do not claim multiple agents or independent review. |
| Text prompts only | Apply the readable guidance; do not claim installation, loading of all references, or new capabilities. |
| Missing search, data, write access, or validation tools | Complete unaffected work and mark the affected scope blocked or unverified. |

The public edition includes its own references and requires no private workspace skills. Host permissions, user authorization, and execution restrictions remain in force. Instructions cannot create missing APIs, access, or permission. See [execution boundaries](skills/universal-expert-team/references/execution-boundaries.md) and [runtime adapters](skills/universal-expert-team/references/runtime-adapters.md).

## Repository guide

| Path | Purpose |
| --- | --- |
| [`skills/universal-expert-team/`](skills/universal-expert-team/) | Complete installable unit: instructions, metadata, icon, and references. |
| [`docs/installation.md`](docs/installation.md#english) | Download, ChatGPT and Codex setup, loading checks, and updates. |
| [`docs/usage.md`](docs/usage.md#english) | Chinese and English prompts, mode selection, acceptance, and missing capabilities. |
| [`README.md`](README.md) | 繁體中文專案首頁。 |

## License and contributions

Released under the [MIT License](LICENSE). You may use, modify, and redistribute it with the license notice preserved. Report reproducible problems through [Issues](https://github.com/jerry0327/universal-expert-team/issues), or propose improvements through a pull request. Include the host, expected behavior, and observed result; remove private information first.

This is an independent open-source skill. It does not claim official certification by OpenAI or another platform.
