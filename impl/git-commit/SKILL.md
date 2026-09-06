---
name: git-commit
description: Prepare one coherent conventional commit by reviewing changes, staging its files, and suggesting its message. Do not create a commit.
---

Review the diff, identify one coherent commit, stage only its files, and suggest its message. Do not create a commit.

# Conventional Commit Format

```
<gitmoji> (<scope>): <description> (<ticket or issue, if applicable>)
```

Omit scope and ticket when they add no value. Keep description specific, imperative, and under 72 characters.

# Gitmoji

ref: https://github.com/carloscuesta/gitmoji

```
✨ feat(scope): description
```

## Common Gitmoji

| Emoji | intent |
| ----- | ------------- |
| ✨ | `feat` new feature or feature update |
| 🐛 | `fix` bug fix |
| 📝 | `docs` documentation |
| 💄 | `style` formatting or style |
| ♻️ | `refactor` code refactor |
| ⚡️ | `perf` performance improvement |
| ✅ | `test` tests |
| 🏗️ | `build` build or dependency changes |
| 👷 | `ci` CI or configuration changes |
| 🔧 | `chore` tool or configuration maintenance |
| ⏪ | `revert` revert commit |

Use most appropriate emoji; table is a guide.

```text
🐳 build(email): update email job Dockerfile
```

## Workflow
1. Review the changes and identify one coherent commit.
2. Stage only files that belong to it.
3. Suggest a commit message; do not commit.

## Safety

- Never stage unrelated or unreviewed changes.
- Never stage secrets: `.env`, credentials, or private keys.
- Never commit, amend, push, change Git configuration, skip hooks, or run destructive Git commands unless explicitly requested.
