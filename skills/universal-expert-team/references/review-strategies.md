# Review strategies

Select methods by a concrete failure risk and the user's requested quality mode.
Combine only methods that add distinct evidence.

## Strategy menu

| Method | Use when | Conduct |
| --- | --- | --- |
| Necessary source/integrity checks | Any material claim or deliverable needs basic trust | Verify critical sources, calculations, requested coverage, destination and actual output as applicable. |
| Independent review | A material error could survive author self-check, or iterative acceptance needs a non-author | Assign a fresh non-author current sources, artifact and criteria; request evidence-backed findings. |
| Blind initial assessments | Anchoring, disputed classification or interpretive bias matters | Obtain initial judgments before revealing peers' conclusions; then compare specific differences. |
| Counterexample/adversarial assessment | Assumptions or exceptional conditions could invalidate success | Seek plausible failure cases and contrary evidence; do not demand invented objections. |
| Cross-specialty review | Correctness in one specialty can break another requirement | Review the same deliverable through distinct relevant expertise and reconcile tradeoffs. |
| Integration review | Independently correct packages may conflict | Check interfaces, versions, definitions, totals, terminology, design and whole-output usability. |
| End-to-end validation | The intended use depends on execution, rendering or delivery | Exercise the final artifact in the actual or justified representative environment; disclose environment limits. |

Independent context reduces anchoring; it does not ensure different models have
independent knowledge, error-free judgment or independent source provenance.
Do not count agreement as validation.

## Reviewer brief and findings

Provide raw current artifacts, requirements and source access. Avoid passing the
author's persuasive rationale, suspected diagnosis or desired answer unless the
specific review requires it. Relevant prior confirmed defects may be supplied
for a targeted regression check; label that as informed revalidation.

Ask for:

- The requirement evaluated and artifact/source version.
- Evidence or a reproduction, with impact and proposed acceptance condition.
- A distinction between confirmed defect, unsupported concern, blocked check,
  preference and acceptable tradeoff.
- A clear result for that scope: passes, needs repair, or remains unverified.

Do not ask for private reasoning traces. Keep reviewer role independent from
production when required. An author can self-test, but those results cannot be
relabeled as independent acceptance.

## Disagreement resolution

Compare the exact claims, context, definitions, timeframe and underlying sources.
Resolve a demonstrable error directly. Obtain additional evidence only when it
can materially change the decision. Use another adjudicator when the issue needs
unrepresented expertise or prior participation compromises required independence;
do not automatically create a third voter.

When evidence cannot resolve the dispute, explain competing interpretations,
confidence and practical impact. Never fabricate consensus or merge incompatible
data to complete a desired conclusion.

## Iterative closure

Define materiality by the user's acceptance and effect on correctness, usability
or intended use, not how easy the defect is to fix. Assign repairs to the owner
and revalidate affected properties after the actual change.

Keep the accepted artifact revision and review target aligned. A reviewer who
implements a substantive correction cannot certify their own changed scope as
independent. Reuse valid unaffected review results; do not restart all checks
because one component changed.

Stop after the criteria pass. Do not add fresh stylistic requirements, arbitrary
round counts or unrelated checks to prolong the task. If a recurring failure
reveals a wrong approach, change the approach; if an essential gate is impossible,
report it as blocked and deliver the useful qualified result.

For iterative searching, maintain open questions and coverage gaps. Broaden
sources, vary queries or inspect primary materials to close actual gaps. Source
saturation alone cannot establish a proposition is true or that no contrary
evidence exists.
