# Roles routing smoke tests

Use these prompts to check that routing goes **straight to experts** with sensible parallelization.

## 1. Greenfield prototype

Prompt:

> 我想开一个新的工具仓库，先做第一版原型，帮我定一个最小可行起点。

Expected:

- Invoke `researcher` / `analyst` in parallel when multiple independent feasibility questions exist; otherwise start with the single best-fit expert.
- After decisions, `coder` then `tester` as needed.
- Kickoff shape and “what to prove first” appear before heavy build-out.

## 2. Stalled existing project

Prompt:

> 这个老项目我做到一半停住了，帮我基于当前代码挑一个最值得继续做的点，不要全推翻。

Expected:

- Prefer `analyst` plus `tester` in parallel when structure review and repro are independent.
- Then `coder`, then targeted `tester`.
- One clear continuation path, not a generic rewrite pitch.

## 3. Learn from another repo

Prompt:

> 帮我读一下这个优秀项目，提炼下有哪些模式值得借到我自己的 repo 里。

Expected:

- Parallel `researcher` briefs per question or subsystem when broad.
- `analyst` for synthesis; `writer` only for packaging.
- Learning questions explicit before unfocused browsing.

## 4. Mixed ask (learn + own repo)

Prompt:

> 我想先看看这个优秀项目有哪些设计值得借鉴，然后顺手把我自己的老项目下一步怎么改也一起想一下。

Expected:

- Treat as two concerns: keep expert briefs separate instead of one blended pass.
- Typical order: experts for external learning first, then experts for the user’s repo (not a single mega-role).

## 5. Two independent slow paths

Prompt:

> 帮我看看这个老项目里接口变慢和测试变慢分别卡在哪，最后给我一个优先级建议，但不要先入为主只盯一个问题。

Expected:

- Two explicit investigation briefs (often `analyst` / `tester` combinations per track) **in parallel** when independent.
- Merged priority recommendation after both return evidence.
