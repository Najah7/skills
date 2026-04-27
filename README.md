# Agent Skills

Personal skill library for AI coding agents. These are mainly tuned for Codex, with small `agents/openai.yaml` files where useful. Most skills are plain Markdown and can be adapted for other agents too.

[日本語 README](README.ja.md)

## Supported AI agents:
- Codex (main focus): I personally use Codex for the daily work so most skills are tuned for it.

## Included

| Skill | Purpose |
| --- | --- |
| `swe` | General implementation workflow from a Todo List |
| `todo-planner` | Turn requirements into overview docs and Todo Lists |
| `git-commit` | Create conventional commits from current changes |
| `caveman` | Terse communication mode |
| `compress` | Compress memory/skill files into caveman format |

## Structure

Each skill lives in its own directory with a `SKILL.md`. Some skills also include:

- `references/` - deeper guidance for the skill
- `agents/` - agent-specific config
- `scripts/` - helper CLI code
- `assets/` - images or other static files

## Setup

### Fresh install

```sh
mkdir -p ~/.agents
git clone git@github.com:Najah7/skills.git ~/.agents/skills
```

### Add to existing `~/.agents`

```sh
git clone --depth 1 git@github.com:Najah7/skills.git .tmp
find .tmp -mindepth 1 -maxdepth 1 -type d -exec rsync -a {} ~/.agents/skills/ \;
rm -rf .tmp
```

## Usage

Reference a skill by path or name from your agent prompt, for example:

```md
Use ~/.agents/skills/frontend-swe/SKILL.md
```

For Codex, install this repo at `~/.agents/skills` and let skills be discovered from there.

## Acknowledgements

Some skills in this project are based on or inspired by the following repositories:

- https://github.com/github/awesome-copilot
- https://github.com/JuliusBrussee/caveman
