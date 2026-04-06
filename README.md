# roles

Personal **agent-first** roles: route work to `inspector`, `executor`, or `verifier` with explicit briefs. Roles describe **responsibility contracts**, not human job titles. There is no intermediate director or work-mode role in this package.

This repo only defines role responsibilities and routing hints. It does not own a memory system, transcript mining loop, or a separate framework layer.

## Role boundary

- `roles/` lists callable roles and what each one owns.
- The sibling `skills` repo can still provide reusable methods (`tech-preferences`, `project-workflows`, etc.); load them when they help, independent of which role is active.
- Outputs can stay in the conversation or in ad hoc notes; this repo does not require a fixed runtime memory file.

## Brief contract

Every brief should make clear:

- **goal** — what to produce or decide
- **inputs** — repos, paths, commits, logs, links
- **non_goals** — what is out of scope
- **expected_output** — shape of the deliverable
- **blocking** — whether other work waits on this brief
- **lens** (optional) — for `verifier` only: `security`, `performance`, and/or `architecture` (see [`roles/verifier.md`](roles/verifier.md))

## Core roles

| Role | Use for |
|------|--------|
| `inspector` | Bounded reading, evidence, structure, diffs, logs, prior art, tradeoffs, scoping the next change |
| `executor` | Well-scoped implementation, narrow refactors, prototypes, proofs—merge-ready diff + checks |
| `verifier` | Repro, diagnostics, regression checks, and review against a named claim; add `lens` for security/perf/architecture depth |

Packaging or polishing prose is a normal agent output; there is no separate `writer` role unless you split that work explicitly in orchestration.

## When to route where

- **Greenfield or “smallest first step”** — often two `inspector` briefs in parallel when feasibility splits into independent questions; then `executor`; then `verifier` when something must be validated.
- **Existing repo, continue or fix** — often `inspector` and `verifier` in parallel when structure review and repro are independent; then `executor`; then `verifier` again for regression.
- **Study another project** — parallel `inspector` briefs per question or subsystem when broad; then one `inspector` pass for synthesis if needed. Final user-facing packaging can be done by the orchestrator or a dedicated brief—no separate role required.
- Load `tech-preferences` before meaningful stack choices (via skills, not a role here).

## Specialized review

Do **not** use separate top-level roles for security, performance, or architecture review. Use **`verifier` with `lens: security`**, **`lens: performance`**, or **`lens: architecture`** (see [`roles/verifier.md`](roles/verifier.md)).

## Operating rules

- The orchestrator (main agent or you) splits work into **explicit briefs** as above.
- If two or more briefs do not depend on each other, run them **in parallel** by default.
- Stay serial when one result materially changes the next brief.
- Do not chain through a fake “coordinator” role; merge and sequence at the orchestration layer.

## Use it

```bash
uvx role-forge add zrr1999/roles
```

Or:

```bash
bash install.sh
```

If you maintain this repo and regenerate tool outputs, use whatever `role-forge` currently documents for your version (subcommands differ by release).

## Expected outputs

Each role returns a **merge-ready packet**: concrete evidence, changes, commands/results, or review findings, plus blockers. No role invents a second layer of delegation.

## Examples

See [`examples/README.md`](examples/README.md) for concrete user asks and expected routing.

## Migration from older role names

If you used the previous five-role model or separate reviewer roles, see [`MIGRATION.md`](MIGRATION.md).
