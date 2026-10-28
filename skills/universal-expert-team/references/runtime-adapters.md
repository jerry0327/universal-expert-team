# Runtime adapters

Use this reference before first dispatch and when capabilities, ownership or live
task state change. It is a portable execution contract, not a tool API. Do not
invent function names or assume a particular product exposes subagents.

Contents: [Discovery](#discover-the-current-runtime), [Dispatch](#dispatch-and-schedule),
[Lifecycle](#manage-lifecycle-and-ownership), [Recovery](#cancel-and-resume),
[Adapters](#use-optional-host-adapters).

## Discover the current runtime

1. Read directly exposed host-native collaboration interfaces and their live
   documentation. Inspect native creation separately from MCP/plugin inventories:
   an empty MCP registry does not establish native absence, and an MCP connector
   does not establish native worker support.
2. Determine actual creation, messaging, status, result retrieval, interruption
   and resume capabilities. Use only documented operations. Distinguish a missing
   interface from an interface whose request is denied, temporarily full, or whose
   result has not yet arrived.
3. Determine the concurrency convention: whether the coordinator, descendants,
   idle workers and pending operations count. Inspect current occupancy when
   supported. Do not guess a numeric limit or treat each parent as having a new
   independent quota.
4. Read offered model and reasoning controls plus inheritance/fork restrictions.
   Select the highest capability tier and deepest reasoning actually supported
   within current authorization and user/host constraints. Use host capability
   descriptions rather than comparing version strings. If rankings are unclear,
   follow the documented host recommendation and state the uncertainty. If no
   override exists, use documented inheritance/defaults and do not claim to set it.
5. Record the supported route, relevant limits, requested settings, observed
   settings and unavailable controls in the task record. A creation receipt proves
   a worker exists; it does not verify hidden backend reasoning or model identity.

If native delegation is absent, use an alternative only if its real interface and
prerequisites are present, the user explicitly authorized that route for this
task, and host rules permit it. Verify its ability to maintain distinct worker
contexts, retrieve results and control outstanding work. A browser, prior login
or installed plugin alone is not evidence of such a route. Do not install new
orchestration software, log into accounts, switch devices, or open external
sessions merely to imitate a missing native tool.

If no permitted route exists, complete feasible work directly. Say that actual
delegation and independent review are unavailable; do not present role-played
perspectives as separate agents. Leave a required independent gate unverified.

## Dispatch and schedule

- Maintain a lightweight dependency queue: ready, running, awaiting input/review,
  accepted, blocked, or cancelled. Record actual worker identity and task attempt
  once creation succeeds; a planned role is not a live worker.
- Use all useful available capacity. Keep enough coordination ability to integrate
  results, but do not reserve idle seats for work that cannot yet begin. Queue
  additional specialties when the host is full; do not create filler assignments
  or use another route to bypass the limit.
- Give a new substantive topic or independent assessment a fresh task scope and,
  where supported, a fresh context. Explicitly control whether history is forked;
  supply minimum task-local context. A new label on the author's old context does
  not make independent review. If isolation cannot be established, disclose that
  limitation rather than asserting a blind assessment.
- Continue the original owner for corrections to its own deliverable when its
  context remains usable. Give acceptance reviewers current raw artifacts and
  criteria without the author's preferred conclusion or private rationale.
- Assign an explicit descendant allowance and exclusive resource scope. A worker
  without allocated capacity must return a proposal instead of spawning a tree.
  Include descendants in the same capacity accounting when the host does.
- Verify each worker's required tool and destination access from that worker's
  actual observations. Do not infer its capabilities from Root's success.

Delegate goals, inputs, acceptance and authority using
[work packages](work-packages.md). Permit routine independent decisions and direct
peer coordination when supported. Route consequential changes in scope, sources,
interfaces, ownership and blockers to Root. Workers may produce and save final
artifacts directly within their authorized scope; Root remains accountable for
complete coverage and integration.

## Manage lifecycle and ownership

Treat shared files, tabs and external records as shared even when workers have
distinct contexts. Give each mutable resource one active writer, or use genuinely
isolated candidate copies with a named integration owner. Readers must know which
artifact revision they assessed.

For asynchronous work, retain the real operation/worker identifiers and check
status or await documented notifications. Use nonblocking progress mechanisms
where available, avoid busy polling, and keep the user informed during sustained
work. Do not assume that a timeout, lost connection, interruption request or
missing response means an operation failed or stopped.

When a creation or write outcome is ambiguous:

1. Reconcile the actual operation using supported status, identity and destination
   observations before retrying it. An unconfirmed request can still complete.
2. Retain ownership while late mutations remain possible. Do not launch a second
   writer against the same target. An instruction saying "stop" is not proof
   that the existing writer is fenced from the resource.
3. Continue unaffected work or use a separate candidate destination. Reconcile
   completed effects and preserve user changes before integration.
4. If state cannot be resolved, mark the affected action uncertain and report the
   concrete next requirement. Do not claim success, failure or safe release of
   ownership without evidence.

Release occupied capacity according to the host's documented lifecycle. A finished
response may still leave an addressable worker that counts toward the limit.
Use only actual supported close/release controls; do not invent a way to reclaim
a seat. Preserve necessary artifacts and receipts before releasing a context.

## Cancel and resume

Apply a user stop or narrowed scope promptly to the affected tree. Issue supported
interrupt/cancel controls, notify dependent workers and reconcile outstanding
operations. Cancellation is not rollback. Do not delete useful work or reverse
completed external effects unless authorized; report material effects and any
operation whose termination remains uncertain.

Before a long handoff or context loss, retain a concise checkpoint in an authorized
task location: current goal and quality mode, acceptance, valid outputs and
versions, open defects, workers and operation identifiers, capacity allocations,
write ownership, uncertain actions and next dependencies. Include only necessary
context and no credentials. Do not claim the checkpoint provides scheduling.

On resume, reread the user's current intent and constraints, recover the record,
and reconcile live workers, available tools and destination state. Historical
identities may no longer be addressable. Verify accepted outputs still exist and
remain current. Reuse valid results; isolate stale or late results. Do not retry
an uncertain external mutation or inherit a cancelled authorization from the
summary alone.

## Use optional host adapters

Use a host-specific adapter when the current environment actually supplies it
and its documented scope matches the task. Apply it to concrete API syntax,
transport and lifecycle details. It remains subject to current user instructions,
host policy and the boundaries above; it cannot add missing tools or permissions.

Do not require a privately installed companion skill, account-specific path,
device name or plugin identifier. Keep host-specific configuration outside the
portable core. When an adapter is unavailable, use verified native tools and this
reference; if the missing part prevents correct execution, expose the limitation.
