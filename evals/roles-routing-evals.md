# Roles Routing Smoke Tests

Use these prompts to sanity-check whether the top-level routing still picks the right director.

## 1. `directors/new-project`

Prompt:

> 我想开一个新的工具仓库，先做第一版原型，帮我定一个最小可行起点。

Expected:

- route to `directors/new-project`
- the director makes the kickoff packet explicit before building
- if feasibility splits into separate questions, likely flow includes parallel `specialists/researcher` and `specialists/analyst`, followed by `specialists/coder` and `specialists/tester`

## 2. `directors/maintain-project`

Prompt:

> 这个老项目我做到一半停住了，帮我基于当前代码挑一个最值得继续做的点，不要全推翻。

Expected:

- route to `directors/maintain-project`
- the director narrows the work to one continuation path
- likely flow includes parallel `specialists/analyst` and `specialists/tester` when current behavior can be inspected independently, followed by `specialists/coder` and targeted retest

## 3. `directors/learn-project`

Prompt:

> 帮我读一下这个优秀项目，提炼下有哪些模式值得借到我自己的 repo 里。

Expected:

- route to `directors/learn-project`
- the director defines the learning questions before broad reading
- likely flow includes parallel question-focused `specialists/researcher` briefs or a split between `specialists/researcher` and `specialists/analyst`, followed by `specialists/writer`

## 4. mixed request

Prompt:

> 我想先看看这个优秀项目有哪些设计值得借鉴，然后顺手把我自己的老项目下一步怎么改也一起想一下。

Expected:

- keep the modes explicit instead of blurring them
- likely sequence: `directors/learn-project` then `directors/maintain-project`
- within each mode, independent specialist briefs are parallelized instead of serialized into one long director pass

## 5. same-mode parallelization

Prompt:

> 帮我看看这个老项目里接口变慢和测试变慢分别卡在哪，最后给我一个优先级建议，但不要先入为主只盯一个问题。

Expected:

- route to `directors/maintain-project`
- the director makes the two investigation tracks explicit instead of collapsing them into one generic scan
- likely flow includes parallel specialist briefs for the two slow paths, followed by a merged continuation packet with priority recommendation
