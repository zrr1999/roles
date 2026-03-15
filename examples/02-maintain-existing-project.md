# Example 02: Maintain An Existing Project

## User Ask

这个项目我之前做过一半，现在有点乱。帮我看看当前状态，挑一个最值得推进的点继续做，不要整个推倒重来。

## Expected Director

`directors/maintain-project`

## Likely Specialist Support

- run `specialists/analyst` on current structure and `specialists/tester` on the failing or confusing path in parallel when they are independent
- then use `specialists/coder` for the chosen change
- then use `specialists/tester` again for targeted regression checks

## Why

- the repo already exists
- the user wants continuation and narrowing, not a fresh design
- preserving momentum matters more than reopening every old decision
- analysis and repro can often proceed in parallel before the code change is chosen

## Good Output

- current state summary
- one chosen continuation path
- immediate next change
- risks and follow-ups
- explicit note about which specialist work ran in parallel and which had to stay serial

## Bad Output

- ignoring existing code reality
- proposing a full rewrite without strong evidence
- a long single-agent pass that never splits analysis from verification
