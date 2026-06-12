# 引き継ぎメモ

## 現在の状態

このプロジェクトは、「Web収益だけで株を買う」ことをテーマにしたWebサイトです。

公開URL:

https://webkabu-log.github.io/

GitHubリポジトリ:

https://github.com/webkabu-log/webkabu-log.github.io

ローカル作業場所:

```text
C:\trader
```

OneDrive内の古い作業フォルダは中身を削除済みです。フォルダ本体だけは、このCodexセッションまたはOneDriveに掴まれていて削除できませんでした。

## ここまでやったこと

- `C:\trader` に作業場所を移動
- GitHubリポジトリ `webkabu-log/webkabu-log.github.io` と連携
- GitHub Pagesでサイトを公開
- トップページを作成
- サイト名を「Web収益だけで株を買う日記」に設定
- ページ上の対話内表記を「私」に変更
- Agentsの見立てはサイト上に出さない方針に変更
- 「次に追うこと」「もし収益が出たら」は削除
- 流れる帯、収益メーター、背景の浮遊アニメーション、カードのホバー演出を追加
- 「はじまり」ページを作成
- Day 1「Webで1円を作る前に、まず読まれる流れを考える」を作成
- Day 2「読まれる入口と広告審査の準備を進める」を作成
- 学習ロードマップページを作成。証券会社、証券口座、NISA、東証Prime市場を混同しない順番で整理
- 学習記録「投資とは何かを1から確認する」を作成
- 学習記録「株価が動く理由を1から確認する」を作成
- 対話相手の表記は「先生」ではなく「AI」に変更
- トップの流れる帯は、投資を煽らず安全ルールと学習姿勢に寄せた
- トップの大きすぎる余白を調整
- プライバシーポリシーを作成
- 「このサイトの運営方針と広告について」ページを作成
- プロフィールページを作成
- 全ページのフッターに「プライバシーポリシー」「広告・運営方針」リンクを追加
- トップの公開記録を「作業の記録」と「投資前の学習」の2レーンに分割
- 「投資前の学習」ではロードマップをStudy 01より前の最初の項目に配置
- トップの見出しは「現在の進め方」「作業の記録」「投資前の学習」に変更済み
- 「現在の進め方」「作業の記録」「投資前の学習」はカード列を横スクロールで見せる
- 820px以下では共通ヘッダーをハンバーガーメニュー化する
- 横スクロール対象はマウスホイールの縦入力でも横へ移動できるようにする
- ロードマップには、実装済みのStudyページへのリンクを必ず全て付ける
- ヒーロー背景にチャート風の流れるライン、記録レーンに控えめなスキャン演出、カードにホバー時の光沢と矢印を追加
- プロフィールは基本匿名で運営する方針。個人が特定される情報や投資と関係のない詳しい属性は出しすぎない
- Google Analytics 4 を新URL用に作成し直し、Measurement ID を `G-FZVKWGP9SH` に変更
- GitHub PagesのURLを `https://webkabu-log.github.io/` に移行済み
- 旧URLでGoogle Search Consoleを登録済み。新URL `https://webkabu-log.github.io/` で登録し直す
- 新URLのGoogle Search Console確認用HTMLファイル `google84bdc80c78eef64d.html` を追加
- 新URLのGoogle Search Console確認用metaタグを `index.html` に追加
- 検索エンジン向けに `sitemap.xml` と `robots.txt` を追加
- 新URLの `https://webkabu-log.github.io/sitemap.xml` は公開URLでHTTP 200を確認済み
- Xプロフィール設定と初回投稿を実施済み
- Google AdSense サイト確認用コードを通常HTMLページの `<head>` に追加（publisher: `ca-pub-9424993744252378`）
- 全ページ共通フッターとプロフィールにXリンク `https://x.com/webkabu_log` を控えめに追加
- AdSense確認コード設置に合わせ、プライバシーポリシーと広告・運営方針の表記を更新

## サイトの基本方針

サイト上では、運営側の作業メニューを見せない。

見る人には、以下が自然に伝わるようにする。

- 運営者がWeb収益を作ろうとしている
- 生活費や貯金は使わない
- Webで生まれた収益だけを投資に使う
- 最初の目標は1円
- 投資助言ではなく、個人の学習記録である

## 投資まわりのルール

- 生活費は使わない
- 貯金は使わない
- 借金しない
- クレジットカードの分割や無理な支払いは使わない
- 信用取引はしない
- Web収益の範囲だけで投資を考える
- 勝っても負けても記録する
- 「この株を買うべき」のような投資助言にはしない

## 収益化まわりの考え方

いきなり広告を貼るより、まずはサイトの土台と記録を作る。

最初の目標:

```text
Webで1円を作る
```

その後に考えること:

- アクセス解析
- プライバシーポリシー（作成済み）
- お問い合わせページ
- 広告表記（広告掲載時にPR/広告表記を入れる方針）
- アフィリエイトの導入
- 初収益の記録

現在の判断:

- メインは「読まれる流れを作る」
- X運用を始め、サイトへの入口を作る。広告より先に、読まれる導線を育てる
- 広告やPRを使う場合は、読者にわかる場所へ明記する
- Google Analyticsでアクセス状況を確認する
- AdSense確認コードは設置済み。審査待ちの間は広告枠を増やさない
- Search Consoleは新URL `https://webkabu-log.github.io/` で登録済み
- Search Consoleのサイトマップには `sitemap.xml` を送信済み。公開URLではHTTP 200を確認済み
- 投資系アフィリエイトは、投資助言に見えやすいので急がない
- 収益が出るまでは株の実取引には進まない
- トップ上では「Day記録 / Study学習」とは書かず、「作業の記録 / 投資前の学習」として分ける
- DayラベルとStudyラベルはカード内の小さな分類として残す
- Studyページを追加したら、トップの投資前の学習、ロードマップ、サイトマップ、前後記事リンク、HANDOFFを更新する
- アニメーションは「煽るかっこよさ」ではなく「分析している感じ」に寄せる

作成済みページ:

```text
hajimari.html
day1.html
day2.html
job-log-01.html
job-log-02.html
job-log-03.html
job-log-04.html
job-log-05.html
study-ai-jobhunting-01.html
roadmap.html
study-investing-01.html
study-investing-02.html
study-investing-03.html
study-investing-04.html
study-investing-05.html
study-investing-06.html
study-investing-07.html
study-investing-08.html
tools.html
monthly-report-2026-06.html（準備中）
contact.html
profile.html
privacy.html
monetization.html
sitemap.xml
robots.txt
```

最新の主なコミット:

```text
5473171 Add monetization preparation pages
39b3e1d Refine study dialogue heading
7af3831 Use current wording in study headings
0351811 Use current content heading in records
afd7da2 Add first investing study record
e26075f Add day one revenue strategy record
```

## 次にやること

優先順は以下。

1. 公開サイトでDay 2の表示を確認する
2. Google AnalyticsのリアルタイムでXからのアクセスが見えるか確認する
3. Search Console のサイトマップは送信済み。`sitemap.xml` は公開URLで取得できるため、Search Console側の再処理を待つ
4. AdSenseは審査待ち。結果が出るまでは広告枠を増やさず、記事と学習記録を増やす
5. 学習記録「株・市場・証券会社・証券口座の違い」を `study-investing-03.html` として追加済み
6. 学習記録「一般口座・特定口座・NISA口座の違い」を `study-investing-04.html` として追加済み
7. 学習記録「NISAの基本と注意点」を `study-investing-05.html` として追加済み
8. 学習記録「東証の市場区分の役割と違い」を `study-investing-06.html` として追加済み
9. 学習記録「リスクとは何か」を `study-investing-07.html` として追加済み
10. 証券会社、証券口座、NISA、Prime市場、リスク管理などの制度・用語・定義は、公開前に公式情報で確認する
11. 学習記録「少額投資を考える前の確認」を `study-investing-08.html` として追加済み
12. 証券口座の開設状況や実取引の検討は、Web収益が実際に発生するまで保留する
13. お問い合わせページまたは連絡手段を検討する

## X運用方針

目的:

- サイトへの最初の読者導線を作る
- Web収益化と投資学習の過程を、投資助言ではなく学習記録として見せる
- 匿名方針を守り、個人が特定される情報を出さない

投稿方針:

- 断定的な投資判断、銘柄推奨、利益保証はしない
- 「学んだこと」「わからなかったこと」「次に確認すること」を短く出す
- サイトへのリンクは毎回貼らず、自然な区切りで貼る
- 反応を取りにいく煽りより、継続して読める記録を優先する

最初に作るもの:

- プロフィール文（設定済み。「挑戦中」表記）
- 固定ポスト
- 初回投稿 3本
- サイトへのリンク導線

## 次に作るページ案

### プロフィール

内容:

- 運営者について
- 基本匿名で運営する方針
- このサイトの目的
- 投資経験はこれから
- 収益化もこれから
- 失敗も含めて記録すること

### 記録

内容:

- ロードマップ: 学習順と混乱しやすい言葉の整理
- Study 01: 投資とは何かを1から確認する
- Study 02: 株価が動く理由を学ぶ
- Study 03: 株・市場・証券会社・証券口座の違いを整理する
- Study 04: 一般口座・特定口座・NISA口座の違いを整理する
- Study 05: NISAの基本と注意点を整理する
- Study 06: Prime・Standard・Growth市場を整理する
- Study 07: リスクとは何かを1から確認する
- Study 08: 少額投資を考える前の確認を整理する
- Day 0: はじまり
- Day 1: Webで1円を作る前に、まず読まれる流れを考える
- Day 2: 読まれる入口と広告審査の準備を進める
- 広告・運営方針: 広告やPRを使う場合の読者向け説明
- 初収益が出た日
- 初めて投資候補を選んだ日
- 初めて買った日

### お問い合わせ

内容:

- 現時点では連絡先未確定
- メールアドレスやフォームURLはユーザー確認なしで作らない
- 連絡手段が決まったらプライバシーポリシーも更新する

### Study 04

タイトル案:

```text
一般口座・特定口座・NISA口座の違いを整理する
```

内容:

- 一般口座、特定口座、NISA口座は何が違うのか
- 税金の扱いを1から整理する
- NISAは利益保証ではなく税制優遇制度
- 口座選びや制度の詳細は公式情報で確認する
- クイズは投資そのものの理解を問う。個人ルール暗記問題にはしない

## 表に出さないこと

以下はサイト上に出さない。

- Agentsが相談していること
- 「編集側がやること」
- 「記事を書く」など運営者向けの項目
- 読者が操作できない管理メニューのような表現

Agentsは制作・編集補助として使う。

## 会話内学習の方針

- 株、投資、NISAなどを1から学ぶ
- 解説、補足、クイズを入れる
- クイズは仕組み理解を確認するものにする
- 個人ルールを暗記する問題は出さない
- NISAなど制度が変わる可能性のある内容は、公開前に最新の公式情報を確認する
- 会話内の学習内容をWebへ載せる場合は、投資助言ではなく学習記録に整える
- 銘柄のおすすめ、買い時、利益保証の表現は使わない

## 作業時の注意

サイトは静的HTML/CSS/JSです。

主なファイル:

```text
index.html
styles.css
script.js
hajimari.html
day1.html
study-investing-01.html
privacy.html
monetization.html
profile.html
.github/workflows/pages.yml
```

GitHub Pagesは `main` にpushすると自動で公開されます。

変更後は必ず確認すること:

```powershell
git status
git add .
git commit -m "変更内容"
git push
```

公開URL:

```text
https://webkabu-log.github.io/
```
