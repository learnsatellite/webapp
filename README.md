# ポートフォリオ
[](Todoアプリです。)
## プロジェクトの概要
日常のタスク（Todo）を効率的に管理する為のアプリです。
ユーザーはタスクを追加・編集・削除し、進行状況を把握出来ます。
また、管理サイトにて、簡単な一元管理（ユーザー、タスクの追加、参照、編集、削除）も可能です。

## 対象ユーザーの想定
対象の限定はしておらず、一般で使用可能です。
また、一元管理の為の管理者向けのサイトも作られています。

## 工程
所要日数は2～2.5か月程度です。以下に、内訳を表示します。  
- スケジュール作成  0.05月  
- 仕様策定  0.05月  
- 画面設計  0.05月  
- 開発  0.9月  
- テスト  1.3月  
※訓練の都合上開発を離れた期間があるため、所要時間を記載しています。  

<!--
　理由：就活でより優先度の高い作業を3ヶ月程度取り組んでいた為。
・訓練時間　10:30～15:30（1時間休憩）（土日祝日は休み）  
　実質の日数　48日程度（2ヶ月～2ヶ月半程度）  
-->
## 開発環境
[](フレームワーク、言語、ライブラリ)
フレームワーク：Django  
言語：Python, HTML, CSS, JavaScript  
ライブラリ：  
﻿asgiref==3.8.1  
Django==5.0.6  
python-dotenv==1.0.1  
sqlparse==0.5.0  
tzdata==2024.1  
Google Fonts  
Bootstrap==5.0.2  

## システム構成図
![システム構成図](https://github.com/user-attachments/assets/a3a370fb-7d82-46ce-9665-14c6199a5be0)

## 機能の一覧[](（何が出来るか）)
##### ユーザー側
- 新規ユーザー登録
- ログイン
- タスクの追加登録、参照、編集、削除
- 登録済みタスクの検索（フィルター機能付き）
- ログアウト  
##### 管理者側
- ユーザー、タスクの追加登録、参照、編集、削除等
<!--
（画面をデモとして貼っていく。1行くらいで、「この画面は・・をする画面。」と、画面毎に記載。
　文章は可能な限り短く。）
 -->

## デモ
ユーザーを新規登録し、ログインする流れを説明します。
##### ユーザーを新規登録する
ユーザー向けのURLを入力してログイン画面にアクセス可能です。
ログイン画面にて、「新規登録」リンク（新規ユーザー登録を行う画面）に移動します。
![機能　ログイン画面](https://github.com/user-attachments/assets/81c0669e-ed1e-4059-839c-0df51116d8aa)

## テスト
以下の観点で、1,300件程のテストケースを実施しました。

- 全画面
- 全ボタン
- 誤った情報の入力
- 画面崩れ
- ログインしない状態でのURL直接のアクセス
- ログインした状態でのURL直接のアクセス
- ボタン連打
- ブラウザバック
- 組み合わせテスト（権限）

 名前
 梶　聡史

 所属　
 就労移行支援事業所Kaien
 秋葉原サテライト訓練生　
 
 
