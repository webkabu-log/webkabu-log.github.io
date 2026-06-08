# プロジェクト仕様書 ＆ 変更履歴

この仕様書は、「Web収益だけで株を買う日記」プロジェクトの目的、構成、技術仕様、およびこれまでの変更履歴と今後の改善候補を記録するマスタードキュメントです。

---

## 1. プロジェクト概要
* **サイト名**: Web収益だけで株を買う日記
* **コンセプト**: 「Webで生まれたお金だけで、株を買えるのか。」
* **ターゲット**: 大学生・投資初心者
* **サイトの目的**:
  * 読者にとって再現可能な「大学生がAIとWebで0円から収益を作り、そのお金だけで株投資を学ぶ実験ログ」として学習過程を公開する。
  * 投資助言ではなく、個人の学習記録であることを明確にする。
  * 将来的にAIツール紹介、就活サービス紹介、アフィリエイト、広告収益化につなげる。

---

## 2. 守るべきルール
* **生活費・貯金は使わない**: 投資資金はすべて当サイトおよびWeb運営から発生した収益のみとする。
* **借金はしない**: クレジットカードの分割や無理な借り入れは行わない。
* **信用取引はしない**: 現物株の少額取引のみを検討する。
* **投資助言は行わない**: 「この株を買うべき」といった推奨や利益保証の表現は一切使わず、自己責任での判断を促す。
* **結果の全公開**: 成功談だけでなく、迷ったことや失敗もすべて記録する。

---

## 3. サイト構成（ファイルマップ）

| ファイル名 | 役割・ページ内容 | 備考 |
| :--- | :--- | :--- |
| [index.html](file:///c:/trader/index.html) | トップページ | ヒーロー、現在地、3つの柱、進捗メーター、記事一覧レーン |
| [hajimari.html](file:///c:/trader/hajimari.html) | Day 0: 挑戦のはじまり | なぜこの挑戦を始めるのかの対話記録 |
| [day1.html](file:///c:/trader/day1.html) | Day 1: 読まれる流れを考える | ブログ集客設計とX運用の基本方針 |
| [day2.html](file:///c:/trader/day2.html) | Day 2: 読まれる入口を作る | Google Analytics, Search Console, AdSense設定 |
| [job-log-01.html](file:///c:/trader/job-log-01.html) | AI就活 01: 就活で最初に整理すること | 就活で最初に整理すべき5大要素と文理の具体例 |
| [job-log-02.html](file:///c:/trader/job-log-02.html) | AI就活 02: 理系学生の経験を整理する | 理系向けに「課題・行動・学び」に分けるアプローチ |
| [job-log-03.html](file:///c:/trader/job-log-03.html) | AI就活 03: チーム開発で学ぶこと | 進捗共有・認識合わせなどのプロセス管理の重要性 |
| [study-ai-jobhunting-01.html](file:///c:/trader/study-ai-jobhunting-01.html) | AI就活 04: ChatGPTで自己PRを磨く | 生成AIをESに二人三脚で活用するガイドライン |
| [roadmap.html](file:///c:/trader/roadmap.html) | 投資学習ロードマップ | 口座や市場区分などを学ぶ順序と用語集 |
| [study-investing-01.html](file:///c:/trader/study-investing-01.html) | Study 01: 投資とは何か | 貯金と投資の違い、リスクの基本 |
| [study-investing-02.html](file:///c:/trader/study-investing-02.html) | Study 02: 株価が動く理由 | 需要と供給のバランス |
| [study-investing-03.html](file:///c:/trader/study-investing-03.html) | Study 03: 株・市場・口座の整理 | 金融市場と口座、市場区分の基本 |
| [tools.html](file:///c:/trader/tools.html) | 使っているツール・サービス | 開発、AI、就活、投資学習で使うツールの紹介ページ |
| [monthly-report-2026-06.html](file:///c:/trader/monthly-report-2026-06.html) | 2026年6月度 運営レポート | 記事数、PV、収益、当月学んだこと、来月のアクション |
| [contact.html](file:///c:/trader/contact.html) | お問い合わせ | Googleフォーム連携用のプレースホルダー（メールアドレスなし） |
| [profile.html](file:///c:/trader/profile.html) | プロフィール | 運営者（大学生）について、基本匿名での学習姿勢 |
| [privacy.html](file:///c:/trader/privacy.html) | プライバシーポリシー | 個人情報保護方針、Analytics・広告に関する記述 |
| [monetization.html](file:///c:/trader/monetization.html) | 広告・運営方針 | 広告掲載時のPR表記などに関するポリシー表明 |
| [sitemap.xml](file:///c:/trader/sitemap.xml) | 検索エンジン用サイトマップ | Google Search Consoleに送信済み |
| [robots.txt](file:///c:/trader/robots.txt) | クローラー巡回設定 | sitemap.xmlへのパスを記述 |

---

## 4. デザイン・UI技術仕様
* **配色システム**:
  * メイン背景（Paper）: `#f5f2e9` / 文字色（Ink）: `#1c2521`
  * テーマアクセント色: 緑（`#1b7a5b`）、青（`#2d5f9a`）、金/ゴールド（`#bd7b2b`）
* **横スクロールコンテナ (`.journey`, `.lane-grid`)**:
  * `overflow-x: auto;` および `overflow-y: hidden;` を適用。
  * カードがホバーされた際の浮き上がり（`translateY(-4px)`）や影（`box-shadow`）がカットされないよう、コンテナには十分な上下パディング（`padding: 12px 4px 24px;`）と、カード高さを揃える `align-items: stretch;` を指定しています。
* **マウスホイールスクロールの横スクロール連動**:
  * JavaScript (`script.js`) にて、縦のマウスホイール入力を横スクロールに変換。
  * サブピクセル描画によるズレでスクロールがロックされるのを防ぐため、`2.5px` の判定許容値（tolerance）を設け、端まで到達した場合は即座にページ全体の縦スクロールに戻るよう制御されています。
* **将来のアフィリエイト/PR構造**:
  * 広告・ツール関連ページの上部には必ず `※本ページはプロモーションを含みます。` 等のPR表記領域（`.article-note`）を配置しています。

---

## 5. 変更履歴（チェンジログ）

### 第2期：AI就活ログ新カテゴリ追加（2026年6月8日実施）
* **新規記事の作成**:
  * [job-log-01.html](file:///c:/trader/job-log-01.html)（AI就活 01）：就活で最初に整理すべき5大要素と文理別アプローチの整理。
  * [job-log-02.html](file:///c:/trader/job-log-02.html)（AI就活 02）：理系学生向けの「課題・行動・学び」に着目した経験整理法。
  * [job-log-03.html](file:///c:/trader/job-log-03.html)（AI就活 03）：チーム開発におけるプロセス管理と手戻り対策の学習。
* **トップページの更新**:
  * 公開記事数を `9本` から `12本` に更新。
  * 「AI就活ログ」レーンの説明文を更新し、新規3カードを追加。既存の `study-ai-jobhunting-01.html` を `AI就活 04` としてスライド統合。
* **ロードマップ・サイトマップの同期**:
  * `roadmap.html` の「AI・就活のロードマップ」を全4記事の公開済み状態に更新し、リンクを設定。
  * `sitemap.xml` に新規3ページのURLを追加。

### 第1期：機能・レイアウト拡張（2026年6月8日実施）
* **ファーストビュー改善**: コピーを「大学生がAIとWebで0円から〜」の形式にリニューアル。
* **「現在地」セクション追加**: `index.html` に「公開記事数（9本）」「Web収益（0円）」「投資金額（0円）」「次の目標（Webで1円を作る）」を並べた現代的な進捗ダッシュボードを追加。
* **「3つの柱」セクション追加**: Web収益化、AI・就活、投資学習の3つを表現する導入カードを追加。
* **記事カードフォーマット改善**: 全ての記事カードを「ラベル」「タイトル」「得られること」「投稿日」「読むボタン」で統一。
* **AI就活ログカテゴリ新設**:
  * 新カテゴリ用記事 [study-ai-jobhunting-01.html](file:///c:/trader/study-ai-jobhunting-01.html) (ChatGPTでの自己PRブラッシュアップ) を作成。
  * トップページに専用の横スクロールレーンを追加。
* **新規ページ追加**:
  * ツール紹介ページ [tools.html](file:///c:/trader/tools.html)
  * 月次運営レポート [monthly-report-2026-06.html](file:///c:/trader/monthly-report-2026-06.html)
  * お問い合わせページ [contact.html](file:///c:/trader/contact.html)
* **スクロールバー・クリッピング修正**: 横スクロールレーンの縦バーを非表示にし、カードの内容や影が欠けないように調整。
* **表記の統一**: 全ページから「大学3年」等の学年表記を除去し、汎用的な「大学生」へ統一。
* **コンプライアンス対応**: 投資関連ページと全フッターに統一された投資自己責任免責の警告文を配置。

---

## 6. 今後の改善候補
1. **お問い合わせフォームの実装**:
   * `contact.html` 内のプレースホルダー部分に、Googleフォーム等の埋め込みコード（`iframe`）またはリンクボタンを設置する。
2. **Google AdSenseの審査完了対応**:
   * 審査通過後、`monetization.html` の記載に沿って過度でない配置で広告ユニットを表示させる。
3. **新規学習記事（Study 04以降）の追加**:
   * 「一般口座・特定口座・NISA口座の違いを整理する」の対話作成。
   * 以降、NISAの基本、東証市場区分の深掘り等、ロードマップに従った記事の公開。
