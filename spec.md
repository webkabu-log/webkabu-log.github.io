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
| [day3.html](file:///c:/trader/day3.html) | Day 3: 広告審査・アクセス解析・収益0円の現状整理 | 収益0円の現状分析とAdSense広告審査、Analytics、Search Console、X運用の進捗状況、今後の改善項目の整理 |
| [day4.html](file:///c:/trader/day4.html) | Day 4: Web収益0円のまま、自分でも読みにくいところを直した日 | サイトを読み返して、導線や読みにくさを改善した運営記録 |
| [day5.html](file:///c:/trader/day5.html) | Day 5: GA4とSearch Consoleを見たら、ほぼ誰にも読まれていなかった日 | AnalyticsとSearch Consoleで初期の読まれ方を確認した記録 |
| [day6.html](file:///c:/trader/day6.html) | Day 6: サイト全体のナビとツールページを見直した日 | ナビゲーション、関連リンク、ツールページの見直し記録 |
| [day7.html](file:///c:/trader/day7.html) | Day 7: 記事を増やす前に次に読む流れを決めた日 | 記事追加前にサイト内導線と次に読む流れを整理した記録 |
| [job-log-01.html](file:///c:/trader/job-log-01.html) | AI就活 01: 就活で最初に整理すること | 就活で最初に整理すべき5大要素と文理の具体例 |
| [job-log-02.html](file:///c:/trader/job-log-02.html) | AI就活 02: 理系学生の経験を整理する | 理系向けに「課題・行動・学び」に分けるアプローチ |
| [job-log-03.html](file:///c:/trader/job-log-03.html) | AI就活 03: チーム開発で学ぶこと | 進捗共有・認識合わせなどのプロセス管理の重要性 |
| [job-log-04.html](file:///c:/trader/job-log-04.html) | AI就活 04: STAR法で経験を整理する | 自己分析・ESで必須のSTAR法と文理別の具体的な整理例 |
| [study-ai-jobhunting-01.html](file:///c:/trader/study-ai-jobhunting-01.html) | AI就活 05: ChatGPTで自己PRを磨く | 生成AIをESに二人三脚で活用するガイドライン |
| [job-log-05.html](file:///c:/trader/job-log-05.html) | AI就活 06: ガクチカの作り方 | 自己PRとの違いや、STAR構造に沿ったAI壁打ちプロンプト |
| [job-log-06.html](file:///c:/trader/job-log-06.html) | AI就活 07: チーム開発経験の伝え方 | 調整役・課題解決をESで言語化する方法 |
| [job-log-07.html](file:///c:/trader/job-log-07.html) | AI就活 08: 自己PRを盛りすぎないためにAIに確認してもらったこと | AIで文章を盛るのではなく、説明できる経験か確認する記録 |
| [job-log-08.html](file:///c:/trader/job-log-08.html) | AI就活 09: 面接練習にChatGPTを使う方法 | ChatGPTを面接官役にして深掘り質問を受ける練習記録 |
| [roadmap.html](file:///c:/trader/roadmap.html) | 投資学習ロードマップ | 口座や市場区分などを学ぶ順序と用語集 |
| [study-investing-01.html](file:///c:/trader/study-investing-01.html) | Study 01: 投資とは何か | 貯金と投資の違い、リスクの基本 |
| [study-investing-02.html](file:///c:/trader/study-investing-02.html) | Study 02: 株価が動く理由 | 需要と供給のバランス |
| [study-investing-03.html](file:///c:/trader/study-investing-03.html) | Study 03: 株・市場・口座の整理 | 金融市場と口座、市場区分の基本 |
| [study-investing-04.html](file:///c:/trader/study-investing-04.html) | Study 04: 口座の種類と税金の違い | 一般口座・特定口座・NISA口座の違いと税金の仕組みの整理 |
| [study-investing-05.html](file:///c:/trader/study-investing-05.html) | Study 05: NISAの基本と注意点 | つみたて投資枠と成長投資枠の併用、非課税枠、生涯投資枠の再利用ルールと注意点の整理 |
| [study-investing-06.html](file:///c:/trader/study-investing-06.html) | Study 06: 市場区分の役割と違い | 東証のプライム・スタンダード・グロース市場の役割と特徴、注意点の整理 |
| [study-investing-07.html](file:///c:/trader/study-investing-07.html) | Study 07: リスクとは何か | 投資におけるリスク（値動きの振れ幅）の定義とリスク許容度の考え方の整理 |
| [study-investing-08.html](file:///c:/trader/study-investing-08.html) | Study 08: 少額投資を考える前の確認 | 投資を始める前に確認すべき生活防衛資金や安全ルール、チェックリストの整理 |
| [study-investing-09.html](file:///c:/trader/study-investing-09.html) | Study 09: 銘柄を選ばず、企業を観察する練習 | 企業の事業内容（ビジネスモデル）、売上と利益の違い、株価以外の価値、公式IRの重要性の整理 |
| [study-investing-10.html](file:///c:/trader/study-investing-10.html) | Study 10: SBI証券の口座開設を大学生がやってみた | 初心者向けの口座開設手順と注意点の整理 |
| [study-investing-11.html](file:///c:/trader/study-investing-11.html) | Study 11: 口座開設後すぐ買わないための初期設定チェック | 口座開設後にすぐ買わず、安全設定と確認事項を整理する記録 |
| [ai-tips-01.html](file:///c:/trader/ai-tips-01.html) | AI Tips 01: 大学生向けChatGPT活用術10選 | 学習、就活、ブログ作成の補助として使うAI活用メモ |
| [ai-tips-02.html](file:///c:/trader/ai-tips-02.html) | AI Tips 02: AIっぽい文章を自分の文章に戻す方法 | 生成AIで整えた文章を本人の記録として自然に見直す方法 |
| [tools.html](file:///c:/trader/tools.html) | 使っているツール・サービス | 開発、AI、就活、投資学習で使うツールの紹介ページ |
| [monthly-report-2026-06.html](file:///c:/trader/monthly-report-2026-06.html) | 2026年6月度 運営レポート | （準備中）6月末公開予定。記事数、PV、収益、振り返り等 |
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

### 第16期：AI活用メモとAI就活ログの導線分離（2026年6月17日実施）
* **トップページのカテゴリ分離**:
  - `index.html` の記録一覧で、`AI活用メモ` と `AI就活ログ` を別レーン化。
  - `AI活用メモ` には `ai-tips-01.html`, `ai-tips-02.html` を配置し、`AI就活ログ` には就活準備に絞った記事を配置。
* **グローバルナビの整理**:
  - 全HTMLの共通ナビに `AI活用` と `AI就活` を分けて表示し、`index.html#ai-tips` と `index.html#ai-records` へ誘導。
* **ロードマップの整理**:
  - `roadmap.html` に `AI活用メモ` セクションを追加し、従来の「AI・就活のロードマップ」を `AI就活のロードマップ` に変更。
* **AI活用記事の関連記事整理**:
  - `ai-tips-01.html`, `ai-tips-02.html` の戻り先と関連記事見出しをAI活用寄りに調整し、就活記事は関連するAI就活ログとして橋渡し。

### 第15期：サイト全体の品質監査と修正（2026年6月17日実施）
* **セキュリティ・プライバシー修正**:
  - `blog/operations.md` の個人名を匿名化。GitHub Pagesの公開成果物に `blog/` が含まれないことも確認。
* **ナビゲーション修正**:
  - AI就活シリーズの前後リンクを `job-log-04.html` → `study-ai-jobhunting-01.html` → `job-log-05.html` の順に修正。
  - `hajimari.html` と `day1.html` の article-nav を補完。`day7.html` のシリーズ外 next を削除。
* **SEOメタタグ追加・修正**:
  - `tools.html`, `contact.html`, `profile.html`, `privacy.html`, `monetization.html`, `roadmap.html`, `monthly-report-2026-06.html` に OGP/Twitter メタタグを追加。
  - `day3.html`, `study-investing-09.html` の `og:title` から重複したサイト名を削除。
  - `monthly-report-2026-06.html` の noindex/canonical 併存を解消し、最新の運営ログリンクを `day7.html` に修正。
* **アクセシビリティ改善**:
  - 古い記事16ページに skip-link を追加し、`<main id="article-main">` へ統一。
* **CSS品質改善**:
  - `styles.css` の重複ルール（`prefers-reduced-motion`, `.pillars-grid`, `.status-grid`）を整理。
  - 未使用CSS（`.live-panel`, `.card-meta`, 単独 `.journey`）と無効指定（`.lane-grid` の `grid-template-columns`）を削除。
  - `contact.html` のインラインCSSを `styles.css` に移動。
* **仕様書・引き継ぎ文書の同期**:
  - 実在する追加ページをファイルマップと作成済みリストへ反映し、最新コミット欄と次回作業を更新。

### 第14期：新規学習記事（Study 09）の追加と関連情報の同期（2026年6月12日実施）
* **新規記事「銘柄を選ばず、企業を観察する練習」（Study 09）の追加**:
  - 特定の銘柄を推奨せず、企業の事業内容、売上と利益の違い、株価の数字以外の価値、企業公式IR情報を見る姿勢などを対話とクイズ形式で解説した記事 [study-investing-09.html](file:///c:/trader/study-investing-09.html) を作成。
* **既存ページとの同期およびリンク接続**:
  - [index.html](file:///c:/trader/index.html) の「公開記事数」を **20本** にインクリメント。投資学習ログのレーンへ Study 09 のカードを追加。
  - [roadmap.html](file:///c:/trader/roadmap.html) の Study 09 を公開済みにし、リンクを付与。
  - [study-investing-08.html](file:///c:/trader/study-investing-08.html) のナビゲーションを、ロードマップ戻りから新規記事への「Study 09へ進む」へ変更。
  - [sitemap.xml](file:///c:/trader/sitemap.xml) へ新規記事URLおよびその他の最終更新日を同期（自動更新スクリプトを実行）。
* **仕様書のアップデート**:
  - `spec.md` に `study-investing-09.html` を追加し、本チェンジログを記録。

### 第13期：新規作業・運営ログ（Day 3）の追加と関連情報の同期（2026年6月12日実施）
* **新規記事「広告審査・アクセス解析・収益0円の現状整理」（Day 3）の追加**:
  - Web収益と投資額がともに「0円」である現状、AdSense審査待ち状況、今後の改善計画（記事数、読みやすさ、内部リンク、Xからの導線）を整理した日記調の記事 [day3.html](file:///c:/trader/day3.html) を作成。
* **既存ページとの同期およびリンク接続**:
  - [index.html](file:///c:/trader/index.html) の「公開記事数」を **19本** にインクリメント。作業・運営ログのレーンへ Day 3 のカードを追加。
  - [day2.html](file:///c:/trader/day2.html) のナビゲーションを、ロードマップ戻りから新規記事への「Day 3へ進む」へ変更。
  - [sitemap.xml](file:///c:/trader/sitemap.xml) へ新規記事URLおよびその他の最終更新日を同期（自動更新スクリプトを実行）。
* **仕様書のアップデート**:
  - `spec.md` に `day3.html` を追加し、本チェンジログを記録。

### 第12期：新規学習記事（Study 08）の追加と関連情報の同期（2026年6月12日実施）
* **新規記事「少額投資を考える前の確認」（Study 08）の追加**:
  - 投資を始める前に確認すべき「生活防衛資金」の確保、Web収益の原則、少額投資のリスク、事前ルール策定、および公式情報の確認を対話とチェックリスト、クイズで解説した記事 [study-investing-08.html](file:///c:/trader/study-investing-08.html) を作成。
* **既存ページとの同期およびリンク接続**:
  - [index.html](file:///c:/trader/index.html) の「公開記事数」を **18本** にインクリメント。Study 08 のカードから準備中表示を除去し、新規記事へリンク。
  - [roadmap.html](file:///c:/trader/roadmap.html) の Study 08 を公開済みにし、リンクを付与。
  - [study-investing-07.html](file:///c:/trader/study-investing-07.html) のナビゲーションを、ロードマップ戻りから新規記事への「Study 08へ進む」へ変更。
  - [sitemap.xml](file:///c:/trader/sitemap.xml) へ新規記事URLを同期。
* **仕様書のアップデート**:
  - `spec.md` に Study 08 を追加し、本チェンジログを記録。

### 第11期：新規学習記事（Study 07）の追加と関連情報の同期（2026年6月10日実施）
* **新規記事「リスクとは何か」（Study 07）の追加**:
  - 投資における「リスク＝値動きの振れ幅」としての定義や、リスク許容度の説明、余剰資金運用の原則を対話とクイズ形式で解説した記事 [study-investing-07.html](file:///c:/trader/study-investing-07.html) を作成。
* **既存ページとの同期およびリンク接続**:
  - [index.html](file:///c:/trader/index.html) の「公開記事数」を **17本** にインクリメント。Study 07 のカードから準備中表示を除去し、新規記事へリンク。
  - [roadmap.html](file:///c:/trader/roadmap.html) の Study 07 を公開済みにし、リンクを付与。Study 08 を「次に学ぶ（準備中）」にアップデート。
  - [study-investing-06.html](file:///c:/trader/study-investing-06.html) のナビゲーションを、ロードマップ戻りから新規記事への「Study 07へ進む」へ変更。
  - [sitemap.xml](file:///c:/trader/sitemap.xml) へ新規記事URLを同期。
* **仕様書のアップデート**:
  - `spec.md` に Study 07 を追加し、本チェンジログを記録。

### 第10期：新規就活記事（AI就活 06）の追加と関連情報の同期（2026年6月10日実施）
* **新規記事「ガクチカの作り方」（AI就活 06）の追加**:
  - 自己PRとガクチカの違い、AI対話手順、STARプロンプト、ミニクイズを含む記事 [job-log-05.html](file:///c:/trader/job-log-05.html) を作成。
  - レビュー指摘に基づき、会話内の表現「矛盾が生じる」を「回答のつじつまが合わなくなる」へと修正し、客観性と親しみやすさを両立。
* **既存ページとの同期およびリンク接続**:
  - [index.html](file:///c:/trader/index.html) の「公開記事数」を **16本** にインクリメント。AI就活 06 のカードから準備中表示を除去し、新規記事へリンク。
  - [roadmap.html](file:///c:/trader/roadmap.html) の AI就活 06 を公開済みにし、リンクを付与。07 を「次に学ぶ（準備中）」、08・09を予定としてアップデート。
  - [study-ai-jobhunting-01.html](file:///c:/trader/study-ai-jobhunting-01.html) のナビゲーションを、ロードマップ戻りから新規記事への「AI就活 06へ進む」へ変更。
  - [sitemap.xml](file:///c:/trader/sitemap.xml) へ新規記事URLを同期。
* **技術的負債の記録**:
  - ファイル名が一部混在している（`study-ai-jobhunting-01.html`と`job-log-xx.html`）状況について、リンク安定性を重視してそのまま維持し、`spec.md`の今後の改善候補にリファクタリング課題として記録。

### 第9期：新規学習記事（Study 06）の追加と関連情報の同期（2026年6月10日実施）
* **新規記事「市場区分の役割と違い」（Study 06）の追加**:
  - 東証の新しい3つの市場区分（プライム・スタンダード・グロース）について、役割や時価総額等の基準イメージを整理した記事 [study-investing-06.html](file:///c:/trader/study-investing-06.html) を作成。
  - 「プライム市場＝絶対安全ではない」という本質的なリスク情報を対話とクイズ形式で分かりやすく整理。
* **既存ページとの同期およびリンク接続**:
  - [index.html](file:///c:/trader/index.html) の「公開記事数」を **15本** にインクリメント。Study 06 のカードから準備中表示を除去し、新規記事へリンク。
  - [roadmap.html](file:///c:/trader/roadmap.html) の Study 06 を公開済みにし、リンクを付与。Study 07（リスクとは何か）を「次に学ぶ（準備中）」にアップデート。
  - [study-investing-05.html](file:///c:/trader/study-investing-05.html) のナビゲーションを、ロードマップ戻りから新規記事への「Study 06へ進む」へ変更。
  - `tools/update_sitemap.py` を実行し、[sitemap.xml](file:///c:/trader/sitemap.xml) へ新規記事URLを同期。

### 第8期：新規学習記事（Study 05）の追加と関連情報の同期（2026年6月10日実施）
* **新規記事「NISAの基本と注意点」（Study 05）の追加**:
  - 新NISA制度における「つみたて投資枠」「成長投資枠」の基本、併用ルール、生涯非課税限度額（1800万円）、枠の再利用について解説した記事 [study-investing-05.html](file:///c:/trader/study-investing-05.html) を作成。
  - 元本保証がない点や、他口座の利益と相殺できない（損益通算不可）点などの初心者が知っておくべきリスク・注意点も分かりやすく整理。
* **既存ページとの同期およびリンク接続**:
  - [index.html](file:///c:/trader/index.html) の「公開記事数」を **14本** にインクリメント。Study 05 のカードから準備中表示を除去し、新規記事へリンク。
  - [roadmap.html](file:///c:/trader/roadmap.html) の Study 05 を公開済みにし、リンクを付与。Study 06 を「次に学ぶ（準備中）」にアップデート。
  - [study-investing-04.html](file:///c:/trader/study-investing-04.html) のナビゲーションを、ロードマップ戻りから新規記事への「Study 05へ進む」へ変更。
  - [sitemap.xml](file:///c:/trader/sitemap.xml) へ新規記事URLを自動同期。

### 第7期：新規学習記事（Study 04）の追加と関連情報の同期（2026年6月8日実施）
* **新規記事「一般口座・特定口座・NISA口座の違いを整理する」（Study 04）の追加**:
  - 証券口座開設時に選択する、一般口座、特定口座（源泉徴収あり/なし）、NISA口座の違いを解説した記事 [study-investing-04.html](file:///c:/trader/study-investing-04.html) を作成。
  - 通常税率（20.315%）とNISAの非課税優遇、確定申告の手間の違いを初心者向けに整理。またNISAの元本保証なしや損益通算不可などの注意点を解説。
* **既存ページとの同期およびリンク接続**:
  - [index.html](file:///c:/trader/index.html) の「公開記事数」を **13本** にインクリメント。Study 04のカードから準備中表示を除去し、新規記事へリンク。
  - [roadmap.html](file:///c:/trader/roadmap.html) のStudy 04を公開済みにし、リンクを付与。Study 05を「次に学ぶ（準備中）」にアップデート。
  - [study-investing-03.html](file:///c:/trader/study-investing-03.html) のナビゲーションを、ロードマップ戻りから新規記事への「Study 04へ進む」へ変更。
  - [sitemap.xml](file:///c:/trader/sitemap.xml) へ新規記事URLを自動同期。

### 第6期：成長方向性の強化とAI就活フローの洗練（2026年6月8日実施）
* **「3つの柱」の並び順とストーリー連携の強化**:
  - トップページにおける「3つの柱」セクションを、就活と投資・収益化の関連性が自然に伝わる説明文へアップデート。
  - プロセスの順序に従って「AI就活 ➔ Web収益 ➔ 投資学習」の順にカード配置を入れ替え。
* **準備中（Coming Soon）カードの追加**:
  - 今後追加予定の新規記事候補について、リンク切れを防ぎつつ全体のロードマップを見せるため、合計9枚の準備中カードをAI就活ログおよび投資学習ログの末尾に挿入。
  - スタイルシートに `.pending-card` および `.pending-button` を追加し、ホバー動作の無効化や破線ボーダー、不透明度調整によって、準備中であることを直感的に伝える minimal なデザインを適用。

### 第5期：STAR法による経験整理記事の追加と順序整理（2026年6月8日実施）
* **新規記事「STAR法で経験を整理する」（AI就活 04）の追加**:
  - 自己分析やガクチカで必須となる「S・T・A・R」のフレームワーク解説記事 [job-log-04.html](file:///c:/trader/job-log-04.html) を新規に執筆。文系・理系・チーム開発別の具体的な当てはめ例を網羅。
* **記事順序の再構築（ChatGPT記事のシフト）**:
  - 既存の「ChatGPTで自己PRを磨き上げる」を `AI就活 05` に更新し、前後のリンク（`03 ➔ 04 ➔ 05`）を正しく再接続。
  - トップページのカードレーン、学習ロードマップ、およびサイトマップの記述を完全に同期。
* **運営レポートの非公開化と公開記事数の整理**:
  - 開設間もない時期（6月上旬）の運営レポート公開は時系列として不自然なため、トップページおよびサイトマップから `monthly-report-2026-06.html` を非表示（6月末公開の準備中）に変更。
  - これに伴い、トップページの「公開記事数」メーターを **12本** に修正。

### 第4期：情報設計の整理と見出し・カード説明文の最適化（2026年6月8日実施）
* **ヒーローエリアの統合とセンタリング**:
  * ヒーローエリア右側にあった「現在の状況」（`.live-panel`）を完全に削除し、実績メーター機能を「現在地」セクション（5カラムカード構成）に一本化。
  * これに伴い、デスクトップでのヒーローレイアウトを中央揃えの1カラム（最大 `800px`）へ変更し、視線がメインコピーとボタンに集中する美しい landing page に改善。
* **「現在の進め方」の簡略化**:
  * 従来のカード型横スクロールレーンだった `.journey` を廃止し、シンプルで場所を取らない4ステップの「コンパクト・タイムライン」に変更（PCでは横一列、スマホでは縦方向へ自動レスポンシブ配置）。他のカード型レイアウトと視覚的に競合しない補助的役割に整理。
* **見出しのシンプル化**:
  * 長くて雑多になっていたメインセクションの見出し `作業・運営ログ・AI就活・投資学習ログ` を、すっきりとした `記録一覧` へ短縮。
* **記事カード説明文の削減**:
  * トップページにある全12枚の記事カード内の「この記事で得られること」（`.benefits-text`）を1〜2行（40文字〜50文字程度）へ大幅に短縮。文字の圧迫感を減らし、グリッド全体の高さを引き締めてクリーンな印象に向上。

### 第3期：UI/UX改善・情報設計の最適化（2026年6月8日実施）
* **タイムラインの統合**: 記事カードから不要な「投稿日」メタ情報を削除し、「Day/Study/AI就活」ラベルを唯一の進行指標に統合。
* **プレミアムホバーアニメーションの導入**:
  * カード表面の光のスイープ（斜めラインの反射）を廃止し、滑らかな浮上（`translateY(-6px)`）と微小スケールアップ（`scale(1.01)`）、より滑らかで深みのある陰影表現に変更。
  * 進行度バッジ（`.record-date`）に220msの transition を設定し、ホバー拡大を滑らかに。
  * カード本体のホバーと「読む」ボタンの背景色反転（各テーマ色）、浮上、および右矢印（` →`）が右へスライドするマイクロアニメーションを連動。
* **「現在地」セクションの拡張**: 「現在の状況：学習中」カードを追加して計5カラムに拡張し、列幅を最適化。
* **横スクロールの端部余白の確保**: `.lane-grid` および `.journey` の末尾に擬似要素で `flex: 0 0 16px;` のスペーサーを差し込み、右端スクロール時の表示切れを解消。
* **情報階層の整理**: ヒーローエリアのボタン群を「挑戦のはじまり（Day 0）を読む」（Primary）と「現在の実績と記録を見る」（Secondary）の2つに厳選。
* **セクション名の統一（Option A適用）**:
  * 「作業の記録」 ➔ 「作業・運営ログ」
  * 「投資前の学習」 ➔ 「投資学習ログ」
  * これに伴い、トップページおよび月次レポート内の参照文字列を一括更新。

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
   * 審査通過後, `monetization.html` の記載に沿って過度でない配置で広告ユニットを表示させる。
3. **新規学習記事（Study 12以降）の追加**:
   * Study 11までは公開済み。次はロードマップに従って、口座開設後の安全確認、制度・用語の深掘り、実取引前の確認項目を増やす。
   * 証券会社、証券口座、NISA、市場区分、リスク管理などの制度・用語・定義は、公開前に公式情報で確認する。
4. **ファイル命名規則の統一（技術的負債）**:
   * AI就活関連の記事において、`job-log-01.html`〜`job-log-04.html` と `study-ai-jobhunting-01.html`（AI就活 05）および `job-log-05.html`（AI就活 06）が混在している。
   * GitHub Pagesでのリンク切れやSEOへの影響を避けるため、リリース優先で現状維持としているが、将来的に一貫性のある命名規則（例：`job-log-xx.html`）へのリダイレクト設定を含めた統一リファクタリングを検討する。
