# Codex Agent Skills

Codex を主対象にした個人用スキル集です。Codex の `SKILL.md` による検出と `$skill-name` 呼び出しを前提として設計・運用しています。他のコーディングエージェントにも転用できますが、互換性の主対象は Codex です。

[English README](README.md)

## Codex 前提

- Codexの`$skill-installer`で、必要なskillをインストールします。
- Codexのプロンプトから`$skill-name`で直接呼び出します。
- `SKILL.md`にはエージェント向け指示を、存在する`agents/openai.yaml`にはCodex向けUIメタデータを記載します。

# レイアウト

トップレベルは、skillが扱う作業domainで分類しています。

- `plan/`はPlan作成、Planレビュー、PlanからIssueへの変換を扱います。
- `impl/`は実装、実装レビュー、commit準備を扱います。
- `chat/`は対話とコミュニケーションスタイルを扱います。

`templates/`は呼び出すskillではなく、再利用するsource templateを置く特殊なフォルダです。`deprecated/`は参照用に置く廃止済みskillであり、通常のworkflowには含めません。

# スキル

## Plan

| Skill | Purpose |
| --- | --- |
| `plan-with-doc` | 構造化された設計インタビューと委譲調査を通じて、実装用 Plan を作成・更新 |
| `plan2issue` | Plan を人間向けに要約して GitHub Issue を作成 |
| `review-plan` | Plan レビューを個別に実行し、read-only の結果を統合 |
| `review-edge-cases` | Plan の異常系、失敗時の振る舞い、境界値をレビュー |
| `review-test-coverage` | E2E、Integration、Unit テストへの配分と検証漏れをレビュー |
| `review-parallel-test` | Plan のテストが並列安全に実行できるかをレビュー |

## Impl

| Skill | Purpose |
| --- | --- |
| `git-commit` | 変更を確認し、1 つの論理的なコミットになるファイルをステージして、コミットせずに Gitmoji 付き Conventional Commit メッセージを提案 |
| `plan2impl` | Plan が実装可能かを確認し、テスト済みの完了まで実装 |
| `review-impl` | 未コミットの実装変更に対する個別レビューを実行・統合 |
| `review-comment` | 未コミット変更のコメントについて、意図不足・古さ・不要さをレビュー |
| `review-consistency` | 未コミット変更が既存パターンと意味のある不整合を起こしていないかをレビュー |
| `review-depndency` | 未コミット変更の import、依存、interface、DI をレビュー |
| `review-kiss` | 未コミット変更の不要な複雑さ、抽象化、YAGNI 違反をレビュー |
| `review-srp` | 未コミット変更がファイル・module の責務を混在させていないかをレビュー |
| `review-ssot` | 未コミット変更のロジック、データ、設定の重複と単一情報源の問題をレビュー |
| `review-with-plan` | 未コミット実装が指定Planに適合しているかをレビュー |

## Chat

| Skill | Purpose |
| --- | --- |
| `caveman` | 技術的な正確さを保ったまま応答を圧縮。lite、full、ultra モードに対応 |
| `grill-me` | Plan や設計を、重要な判断が解決するまで 1 問ずつ確認 |

# 推奨Codexワークフロー

```text
$plan-with-doc → $review-plan → $plan2issue
                               └→ $plan2impl → $review-impl → $git-commit
```

設計判断を明確にしたいときは`grill-me`を使います。1つの観点だけで十分な場合は個別の`review-*`を使います。

# セットアップ

## Codex向けインストール

必要なskillだけを、このリポジトリからCodexにインストールするよう依頼してください。例:

```text
$skill-installer Install plan-with-doc from Najah7/skills at plan/plan-with-doc
```

複数のskillをまとめて導入することもできます:

```text
$skill-installer Install these skills from Najah7/skills:
- plan/plan-with-doc
- plan/plan2issue
- impl/plan2impl
- chat/grill-me
```

インストールしたskillは、新しいCodexターンから利用できます。

# 使い方

Codexのプロンプトからskillを呼び出します。

```md
$git-commit
$plan-with-doc Add password reset
$review-plan plans/add-password-reset.md
$plan2issue plans/add-password-reset.md
$plan2impl plans/add-password-reset.md
$review-impl
```

`plan2issue`は対象GitHub repositoryを最初に確認してから、Planを人間向けIssueとして作成します。`review-plan`と`review-impl`は複数観点の結果を統合し、個別の`review-*`は1観点だけを確認します。

# 謝辞

このプロジェクトの一部スキルは、以下のリポジトリを参考にしています。

- https://github.com/github/awesome-copilot
- https://github.com/JuliusBrussee/caveman
- https://github.com/mattpocock/skills
