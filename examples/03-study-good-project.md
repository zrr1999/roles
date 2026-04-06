# Example 03: Study a strong project

## User ask

帮我读一下这个优秀项目，看看它有哪些特别好的设计值得我借鉴，最好能顺手指出哪些不适合直接照搬。

## Expected routing (roles only)

- Separate `inspector` briefs **in parallel** for different subsystems or questions when the project is broad.
- `inspector` again once there is enough evidence to compare patterns and tradeoffs.
- Final user-facing packet can be assembled by the orchestrator from returned evidence—no separate packaging role required.

Optional: load `project-workflows` (learn-project lane) from skills to frame questions before broad browsing.

## Why

- Deliverable is transferable patterns, not implementation in the foreign repo.
- Broad reading should split into parallel question-focused briefs.

## Good output

- Concise project snapshot
- Patterns worth borrowing vs worth avoiding
- Suggested application to the user’s own work
- How reading was decomposed across briefs

## Bad output

- Vague praise with no transfer value
- Copying architecture without naming original constraints
- One undifferentiated reading pass
