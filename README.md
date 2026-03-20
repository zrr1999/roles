# roles

Personal work-mode roles for three kinds of work: start new things, maintain existing things, and study other projects.

This repo only defines role responsibilities and routing. It does not own a memory system, transcript mining loop, or a separate framework layer.

## Role Boundary

- `roles/` decides what kind of work this is.
- The sibling `skills` repo provides reusable methods such as `work-mode-routing`, `tech-preferences`, `project-kickoff`, `maintenance-pass`, and `project-reading`.
- Outputs can stay in the conversation or in ad hoc notes; this repo does not require a fixed runtime memory file.

## Layout

- `roles/` canonical role prompts.
- `roles.toml` project metadata for `uvx role-forge`.
- `examples/` a few realistic routing examples.
- `install.sh` one-shot installer for `uvx role-forge` and this roles package.

## Hierarchy

- Load `work-mode-routing` when work mode is unclear; it routes to directors.
- `directors/` own one of the three core work modes and decompose non-trivial work.
- `specialists/` do narrow execution under a director's explicit brief.

## Role Map

- `work-mode-routing` (skill): choose the current work mode, keep the boundary explicit, and require explicit decomposition for non-trivial work.
- `directors/new-project`: start a new repo, prototype, or greenfield direction, then split discovery, proof, and validation work.
- `directors/maintain-project`: continue an existing repo, bugfix, refactor, or next slice of work, then split analysis, implementation, and verification work.
- `directors/learn-project`: study a strong project, then split reading and distillation work into bounded briefs.
- `specialists/*`: narrow execution helpers with merge-ready outputs.

## When To Route Where

- Route to `directors/new-project` when the user is opening a new repo, exploring a prototype, or asking for the first workable architecture.
- Route to `directors/maintain-project` when the user is continuing, fixing, refactoring, or shipping the next step in an existing repo.
- Route to `directors/learn-project` when the user is reading another project to mine ideas, patterns, or implementation techniques.
- Load `tech-preferences` before meaningful stack choices.
- Keep one primary mode active unless the user clearly wants a combined pass.

## Operating Rules

- Sequence across modes; parallelize inside a mode whenever the subproblems are independent.
- Directors should make decomposition explicit for non-trivial work: subproblems, dependencies, output floors, and merge plan.
- If two or more specialist briefs do not depend on each other, run them in parallel by default.
- Directors should do specialist-sized work directly only when the task is too small to justify delegation or tight synthesis makes delegation wasteful.
- Specialist briefs should name `goal`, `inputs`, `non-goals`, `expected output`, and whether the brief blocks other work.

## Use It

Install or update the roles package with `uvx role-forge`:

```bash
uvx role-forge add zrr1999/roles
```

Or use the helper script:

```bash
bash install.sh
```

If you maintain this repo and need to regenerate `.opencode` outputs locally:

```bash
uvx role-forge cast --project-dir . --target opencode
```

## Commit messages

Commits use a short summary line: optional leading token (for example an emoji), a [Conventional Commits](https://www.conventionalcommits.org/)–style type, optional scope and `!`, then a subject — for example `✨ feat: add more functionality`. Merge, revert, `fixup!`, and `squash!` lines are accepted as-is.

To enforce this locally with Git’s `commit-msg` hook (Python 3.10+):

```bash
git config core.hooksPath .githooks
```

The hook runs `python3 -m tools.hooks.commit_message_validator` on the message file Git passes in. You can run the same check manually:

```bash
python3 -m tools.hooks.commit_message_validator path/to/COMMIT_EDITMSG
```

## Expected Outputs

- `directors/new-project`: goal, constraints, initial shape, what to prove first, next 3 tasks
- `directors/maintain-project`: current state, chosen scope, concrete next change, risks, follow-ups
- `directors/learn-project`: project snapshot, patterns worth borrowing, patterns to avoid, suggested application
- `specialists/*`: merge-ready packet with concrete evidence, changes, or wording and any blockers

Use local notes only when they help. The roles should still work without any dedicated artifact file.

## Examples

- Start a fresh repo for a small internal tool and decide the smallest viable shape.
- Continue an older project, pick the next meaningful slice, and avoid reopening settled choices.
- Read an excellent external repo and extract patterns worth bringing back.

See `examples/README.md` for concrete packets and expected routing.
