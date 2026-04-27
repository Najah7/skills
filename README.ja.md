# Agent Skills

AI コーディングエージェント向けの個人用スキル集です。主に Codex 向けに調整していますが、多くのスキルは Markdown なので、少し直せば他のエージェントでも使えます。

[English README](README)

## 対応 AI エージェント

- Codex（主対象）: 普段の開発で Codex を使っているため、多くのスキルは Codex 向けに調整しています。

## 含まれるスキル

| Skill | Purpose |
| --- | --- |
| `swe` | Todo List から実装を進めるための汎用ワークフロー |
| `todo-planner` | 要件を概要ドキュメントと Todo List に分解 |
| `git-commit` | 現在の変更から Conventional Commit を作成 |
| `caveman` | 短く圧縮した会話モード |
| `compress` | メモリ/スキルファイルを caveman 形式に圧縮 |

## 構成

各スキルは専用ディレクトリにあり、中心ファイルは `SKILL.md` です。スキルによっては以下も含みます。

- `references/` - 詳細なガイド
- `agents/` - エージェント別の設定
- `scripts/` - 補助 CLI
- `assets/` - 画像などの静的ファイル

## セットアップ

### 新規インストール

```sh
mkdir -p ~/.agents
git clone git@github.com:Najah7/skills.git ~/.agents/skills
```

### 既存の `~/.agents` に追加

```sh
git clone --depth 1 git@github.com:Najah7/skills.git .tmp
find .tmp -mindepth 1 -maxdepth 1 -type d -exec rsync -a {} ~/.agents/skills/ \;
rm -rf .tmp
```

## 使い方

エージェントのプロンプトで、スキル名またはパスを参照します。

```md
Use ~/.agents/skills/frontend-swe/SKILL.md
```

Codex では、このリポジトリを `~/.agents/skills` に置くと、そこからスキルを見つけられます。

## 謝辞

このプロジェクトの一部スキルは、以下のリポジトリを参考にしています。

- https://github.com/github/awesome-copilot
- https://github.com/JuliusBrussee/caveman
