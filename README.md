# roles

Personal **expert** roles: route work straight to `coder`, `analyst`, `researcher`, `tester`, or `writer` with explicit briefs. There is no intermediate director or work-mode role in this package.

This repo only defines role responsibilities and routing hints. It does not own a memory system, transcript mining loop, or a separate framework layer.

## Role Boundary

- `roles/` lists callable experts and what each one owns.
- The sibling `skills` repo can still provide reusable methods (`tech-preferences`, `project-kickoff`, `maintenance-pass`, `project-reading`, etc.); load them when they help, independent of which expert is active.
- Outputs can stay in the conversation or in ad hoc notes; this repo does not require a fixed runtime memory file.

## Layout

- `roles/` one `.md` per expert.
- `roles.toml` project metadata for `uvx role-forge`.
- `examples/` realistic routing examples (direct expert calls).
- `install.sh` one-shot installer for `uvx role-forge` and this roles package.

## Expert roles

| Role | Use for |
|------|--------|
| `researcher` | Framed questions, prior art, bounded reading of code or docs |
| `analyst` | Evidence about structure, diffs, logs, or scoping the next change |
| `coder` | Well-scoped implementation, refactors, prototypes, proofs |
| `tester` | Targeted repro, diagnostics, regression checks for a named claim |
| `writer` | Packaging approved findings without changing substance |

## When to route where

- **Greenfield or “smallest first step”** — often `researcher` and/or `analyst` in parallel when feasibility splits; then `coder`; then `tester` when something must be validated.
- **Existing repo, continue or fix** — often `analyst` and `tester` in parallel when tracks are independent; then `coder`; then `tester` again for regression.
- **Study another project** — parallel `researcher` briefs per question or subsystem; then `analyst` for pattern/tradeoff synthesis; `writer` only to polish the final packet.
- Load `tech-preferences` before meaningful stack choices (via skills, not a role here).

## Operating rules

- The orchestrator (main agent or you) splits work into **explicit briefs**: `goal`, `inputs`, `non-goals`, `expected output`, and whether the brief blocks other work.
- If two or more expert briefs do not depend on each other, run them **in parallel** by default.
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

Each expert returns a **merge-ready packet**: concrete evidence, changes, commands/results, or wording, plus blockers. No role invents a second layer of delegation.

## Examples

See `examples/README.md` for concrete user asks and expected expert routing.
