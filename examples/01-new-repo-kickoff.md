# Example 01: New Repo Kickoff

## User Ask

我想做一个新的小工具仓库，先给我一个最小可行方向，最好能顺手做出第一版原型。

## Expected Director

`directors/new-project`

## Likely Specialist Support

- if feasibility splits into separate questions, run `specialists/researcher` and `specialists/analyst` in parallel
- then use `specialists/coder` for the first proof
- then use `specialists/tester` for the claim that the proof is meant to validate

## Why

- this is greenfield work
- the main need is initial shape, not ongoing maintenance
- stack choices may appear, so `tech-preferences` may need to load
- separate feasibility questions should be parallelized instead of collapsed into one long director pass

## Good Output

- goal and constraints
- smallest viable repo shape
- what should be proved first
- next 3 tasks
- explicit delegation plan when more than one independent risk exists

## Bad Output

- overdesigned architecture before the first proof exists
- a huge option list with no recommendation
- the director doing all discovery, implementation, and validation alone without a good reason
