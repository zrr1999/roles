# roles

Personal work-mode roles for three kinds of work: start new things, maintain existing things, and study other projects.

This repo only defines role responsibilities and routing. It does not own a memory system, transcript mining loop, or a separate framework layer.

## Role Boundary

- `roles/` decides what kind of work this is.
- The sibling `skills` repo provides reusable methods such as `tech-preferences`, `project-kickoff`, `maintenance-pass`, and `project-reading`.
- Outputs can stay in the conversation or in ad hoc notes; this repo does not require a fixed runtime memory file.

## Layout

- `roles/` canonical role prompts.
- `roles.toml` casting metadata for `uvx role-forge`.
- `examples/` a few realistic routing examples.
- `justfile` a tiny local command wrapper.
- `install.sh` one-shot installer for `uvx role-forge` and repo casting.

## Hierarchy

- `orchestrator` routes the work.
- `directors/` own one of the three core work modes.
- `specialists/` do narrow execution.

## Role Map

- `orchestrator`: choose the current work mode and keep the boundary explicit.
- `directors/new-project`: start a new repo, prototype, or greenfield direction.
- `directors/maintain-project`: continue an existing repo, bugfix, refactor, or next slice of work.
- `directors/learn-project`: study a strong project and extract what is worth borrowing.
- `specialists/*`: narrow execution helpers.

## When To Route Where

- Route to `directors/new-project` when the user is opening a new repo, exploring a prototype, or asking for the first workable architecture.
- Route to `directors/maintain-project` when the user is continuing, fixing, refactoring, or shipping the next step in an existing repo.
- Route to `directors/learn-project` when the user is reading another project to mine ideas, patterns, or implementation techniques.
- Load `tech-preferences` before meaningful stack choices.
- Keep one primary mode active unless the user clearly wants a combined pass.

## Use It

Render the roles with `uvx role-forge`:

```bash
uvx role-forge cast --config roles.toml
```

Or install and cast in one shot:

```bash
bash install.sh
```

Or use the tiny helper:

```bash
just cast
```

## Expected Outputs

- `directors/new-project`: goal, constraints, initial shape, what to prove first, next 3 tasks
- `directors/maintain-project`: current state, chosen scope, concrete next change, risks, follow-ups
- `directors/learn-project`: project snapshot, patterns worth borrowing, patterns to avoid, suggested application

Use local notes only when they help. The roles should still work without any dedicated artifact file.

## Examples

- Start a fresh repo for a small internal tool and decide the smallest viable shape.
- Continue an older project, pick the next meaningful slice, and avoid reopening settled choices.
- Read an excellent external repo and extract patterns worth bringing back.

See `examples/README.md` for concrete packets and expected routing.
