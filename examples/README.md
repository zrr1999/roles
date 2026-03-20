# Example flows

These examples are realistic packets for the `roles` system: **direct expert calls** only.

Each example shows:

- the user ask
- which expert(s) to invoke first and how to parallelize
- what good and bad outcomes look like

## Example index

- `01-new-repo-kickoff.md`: greenfield / prototype
- `02-maintain-existing-project.md`: continue an existing codebase
- `03-study-good-project.md`: learn from a strong external project

Separation of concerns:

- **This repo** defines experts and tight boundaries.
- **Skills** (other repo) supply reusable working methods when useful.
- **Orchestration** stays outside the role files: you or the main agent merges briefs and ordering.
