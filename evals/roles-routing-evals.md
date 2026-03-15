# Roles Routing Smoke Tests

Use these prompts to sanity-check whether the top-level routing still picks the right director.

## 1. `directors/new-project`

Prompt:

> 我想开一个新的工具仓库，先做第一版原型，帮我定一个最小可行起点。

Expected:

- `orchestrator` chooses `directors/new-project`
- likely flow includes `leaders/scout`, `leaders/shaper`, and possibly `leaders/builder`

## 2. `directors/maintain-project`

Prompt:

> 这个老项目我做到一半停住了，帮我基于当前代码挑一个最值得继续做的点，不要全推翻。

Expected:

- `orchestrator` chooses `directors/maintain-project`
- likely flow includes `leaders/scout`, `leaders/shaper`, `leaders/builder`

## 3. `directors/learn-project`

Prompt:

> 帮我读一下这个优秀项目，提炼下有哪些模式值得借到我自己的 repo 里。

Expected:

- `orchestrator` chooses `directors/learn-project`
- likely flow includes `leaders/scout` and `leaders/distiller`

## 4. mixed request

Prompt:

> 我想先看看这个优秀项目有哪些设计值得借鉴，然后顺手把我自己的老项目下一步怎么改也一起想一下。

Expected:

- `orchestrator` keeps the modes explicit instead of blurring them
- likely sequence: `directors/learn-project` then `directors/maintain-project`
