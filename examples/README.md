# Example Flows

These examples are designed to be used as realistic starting packets for the `roles` system.

Each example shows:

- the user ask
- which director the orchestrator should choose
- which leader flow is likely to be used underneath
- what the chosen role should produce next

## Example Index

- `01-new-repo-kickoff.md`: open a fresh repo or prototype
- `02-maintain-existing-project.md`: continue and narrow an older codebase
- `03-study-good-project.md`: learn from a strong project and bring lessons back

The examples intentionally show the separation of concerns:

- roles choose the work mode
- skills provide reusable working methods
- `tech-preferences` only gets involved when real choices need it

They also show the layering:

- orchestrator chooses the director
- directors use leaders for common sub-work
- leaders may use specialists for narrow execution
