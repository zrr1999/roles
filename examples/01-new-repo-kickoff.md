# Example 01: New repo kickoff

## User ask

我想做一个新的小工具仓库，先给我一个最小可行方向，最好能顺手做出第一版原型。

## Expected routing (experts only)

- No coordinator role: call experts with explicit briefs.
- If feasibility splits into separate questions, run `researcher` and `analyst` **in parallel**.
- Then `coder` for the first proof or minimal implementation.
- Then `tester` for whatever claim the proof is meant to validate.

Optional: load `project-kickoff` / `tech-preferences` from skills when stack or shape decisions matter.

## Why

- Greenfield: discovery and proof before polish.
- Independent feasibility threads should not be collapsed into one long single pass.

## Good output

- Goal and constraints from the briefs, synthesized by the orchestrator
- Smallest viable repo shape and what to prove first
- Next 3 tasks
- Clear note of which expert briefs ran in parallel vs serial

## Bad output

- Overdesigned architecture before a first proof
- A huge option list with no recommendation
- One expert doing discovery, implementation, and validation end-to-end without a reason
