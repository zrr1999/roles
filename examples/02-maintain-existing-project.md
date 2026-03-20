# Example 02: Maintain an existing project

## User ask

这个项目我之前做过一半，现在有点乱。帮我看看当前状态，挑一个最值得推进的点继续做，不要整个推倒重来。

## Expected routing (experts only)

- Run `analyst` on current structure and `tester` on the failing or confusing path **in parallel** when those tracks are independent.
- Then `coder` for the chosen change once scope is clear.
- Then `tester` again for targeted regression.

Optional: load `maintenance-pass` from skills when it helps the briefs.

## Why

- Repo already exists; narrow continuation beats full redesign.
- Analysis and repro often proceed in parallel before implementation.

## Good output

- Current state summary (from `analyst` / synthesis)
- One chosen continuation path and immediate next change
- Risks and follow-ups
- Explicit note of parallel vs serial expert runs

## Bad output

- Ignoring existing code
- Full rewrite without evidence
- One long pass that never separates analysis from verification
