# Git 协作规范

## 分支流向

```text
main -> dev -> feature/* -> dev -> release/* -> main
                                      \------> dev
main -> hotfix/* -> main
               \-> dev
```

- 不直接修改 `main`。
- 功能分支必须从最新 `dev` 创建。
- 临时分支合并后删除。
- PR 的版本号由 Reviewer 分配。

## 命名

- Feature：`feature/<short-name>/#SHOU-XXX`
- Release：`release/<version>/#SHOU-XXX`
- Hotfix：`hotfix/<short-name>/#SHOU-XXX`

Commit message：

```text
<type>(<scope>): #SHOU-XXX <subject>
```

示例：

```text
feat(task): #SHOU-102 add task creation
```

## Review

- PR 需要经过 AI Review 和 Reviewer Review。
- 作者回复 Review Comment，但不自行标记 resolved。
- 提出 Comment 的 Reviewer 验证修改后再解决线程。
