# learn-git

这是一个用于练习真实 Git/GitHub 团队协作流程的仓库。

## 练习项目

仓库使用一个最小 Python 任务管理 CLI 产生真实的代码差异、提交、冲突和 Review 场景。
运行时生成的 `tasks.json` 属于业务数据，不允许提交到仓库。

## 分支入口

- `main`：稳定分支，只接受 `release/*` 和 `hotfix/*`
- `dev`：日常集成分支
- `feature/*`：从 `dev` 创建并通过 PR 合并回 `dev`
- `release/*`：从 `dev` 创建并合并到 `main` 和 `dev`

详细规则见 [design/GIT_WORKFLOW.md](design/GIT_WORKFLOW.md)。
