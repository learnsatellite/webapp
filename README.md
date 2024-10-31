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
所要日数は2～2.5か月程度です。以下に、内訳を記載します。  
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
ログイン画面にて、「新規登録」リンクをクリックすると、ユーザー新規登録画面に移動します。

![機能　ログイン画面](https://github.com/user-attachments/assets/81c0669e-ed1e-4059-839c-0df51116d8aa)

注意書きのルールを守り、「新規登録」ボタンをクリックするとユーザーの新規登録が完了します。

![新規登録](https://github.com/user-attachments/assets/d69b3100-90ef-437c-a57c-ea1355034b62)

新規登録完了直後は、タスク一覧画面に遷移されます。

![新規登録　結果](https://github.com/user-attachments/assets/39aeede9-4497-420d-a33f-1ff81cbf0fea)
##### ログインする
ログイン画面にて、登録済みのユーザー情報（ユーザー名、パスワード）を入力し、「ログイン」ボタンをクリックします。

![ログイン画面](https://github.com/user-attachments/assets/2202caef-73a9-44e7-908d-d42741abe790)

タスク一覧画面に遷移されます。

![新規登録　結果](https://github.com/user-attachments/assets/39aeede9-4497-420d-a33f-1ff81cbf0fea)  

次に、タスクの追加登録、参照、編集、削除を行う流れを説明します。
##### タスクを追加登録する
タスク一覧画面にて、「タスクの追加登録」ボタンをクリックします。

![新規登録　結果](https://github.com/user-attachments/assets/39aeede9-4497-420d-a33f-1ff81cbf0fea)

タスク追加登録画面に遷移されます。

![機能　追加登録](https://github.com/user-attachments/assets/01ade1f3-b04e-4b43-8876-05490816d298)

フォームに入力し、「追加」ボタンをクリックします。

![タスク　追加登録　入力](https://github.com/user-attachments/assets/38ebd5d3-65b1-4f7f-9060-c52f2bb6268c)

タスク一覧画面に遷移され、タスクが追加されているのが確認可能です。

![タスク追加後](https://github.com/user-attachments/assets/62630cee-ea3c-432d-bb52-41e8b7566e71)
##### タスクを参照する
タスク一覧画面にて、タスク名がリンクになっています。クリックすると、タスク詳細画面に遷移されます。

![タスク追加後](https://github.com/user-attachments/assets/62630cee-ea3c-432d-bb52-41e8b7566e71)

タスク詳細画面にて、タスクの詳細が参照可能です。

![タスク詳細画面](https://github.com/user-attachments/assets/6ca775c1-698b-4ba6-9964-902b93ab270e)
##### タスクを編集する
タスク一覧画面にて、任意のタスクの「編集」ボタンをクリックすると、対象となるタスクのタスク編集画面に遷移されます。

![タスク追加後](https://github.com/user-attachments/assets/62630cee-ea3c-432d-bb52-41e8b7566e71)

タスク編集画面です。タスクの編集が可能です。

![タスク編集](https://github.com/user-attachments/assets/60d52bca-aa5a-4dc8-8f11-1718df44a0d9)

- タスク名、詳細、ステータス、期日を編集

![タスク編集　デモ](https://github.com/user-attachments/assets/8f8d7133-b065-4ebb-86e4-36523975313b)

「更新」ボタンをクリックすると、編集内容が反映され、タスク一覧画面に遷移されます。

![タスク一覧　編集後](https://github.com/user-attachments/assets/f9836bee-062c-45a1-a9c7-4f755cc304e8)

タスク詳細画面でも、編集内容が反映されている事が確認可能です。

![タスク詳細　編集後](https://github.com/user-attachments/assets/d6946dee-eda2-4545-b67c-441f1a26c50b)
##### タスクを削除する
タスク一覧画面にて、任意のタスクの「削除」ボタンをクリックすると、対象となるタスクのタスク削除画面に遷移されます。

![タスク一覧　編集後](https://github.com/user-attachments/assets/f9836bee-062c-45a1-a9c7-4f755cc304e8)

「削除ボタン」をクリックすると、タスクが削除されます。

![タスク削除](https://github.com/user-attachments/assets/67d9046d-8d24-4b94-b5ff-d9950178a19e)

タスク一覧画面に遷移されます。上記の流れで、登録したタスクは削除された為、表示されません。

![タスク削除後　タスク一覧](https://github.com/user-attachments/assets/0827887b-a61b-40c7-bd85-3d1f81ae6157)
##### タスクを検索する
「検索」ボタンをクリックすると、「タスク名」検索フォームの内容と「ステータス」のフィルターを反映した検索結果が表示されます。

![タスク　検索](https://github.com/user-attachments/assets/ba8aed9f-28ed-4751-93a5-6db8c66cc2e0)

検索結果です。

![検索結果](https://github.com/user-attachments/assets/e65740d5-805a-4a73-9921-00aa571d50ca)

次に、ログアウトを行う流れを説明します。
##### ログアウトする
タスク一覧画面にて、ログアウトボタンをクリックします。

![タスク　検索](https://github.com/user-attachments/assets/ba8aed9f-28ed-4751-93a5-6db8c66cc2e0)

ログアウトが実施されると、ログイン画面に遷移されます。

![機能　ログイン画面](https://github.com/user-attachments/assets/81c0669e-ed1e-4059-839c-0df51116d8aa)

次に、管理サイトに関する説明をします。
##### 管理サイト
管理サイトでは、簡単な一元管理（ユーザー、タスクの追加、参照、編集、削除）が可能です。

![管理サイト](https://github.com/user-attachments/assets/cf558c22-df82-4836-b2a6-6a5af9d4a2f9)
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

テストの詳細は、後述「成果物」のテスト仕様書をご参照下さい。  
## 成果物
以下に、成果物であるTodoアプリのURLを記載します。

1.〈URL（ユーザー向け）〉 webappopen.pythonanywhere.com  
2.〈URL（管理者向け）〉 webappopen.pythonanywhere.com/admin/

また、以下に、テスト仕様書のリンクを記載します。ご参照ください。
3にはテストケース、4には不具合修正について記載されています。

3.[テスト仕様書（テストケース）](https://github.com/learnsatellite/webapp/blob/main/doc/%E3%83%86%E3%82%B9%E3%83%88%E4%BB%95%E6%A7%98%E6%9B%B8%EF%BC%88%E3%83%86%E3%82%B9%E3%83%88%E3%82%B1%E3%83%BC%E3%82%B9%EF%BC%89.pdf)  
4.[テスト仕様書（不具合修正）](https://github.com/learnsatellite/webapp/blob/main/doc/%E3%83%86%E3%82%B9%E3%83%88%E4%BB%95%E6%A7%98%E6%9B%B8%EF%BC%88%E4%B8%8D%E5%85%B7%E5%90%88%E4%BF%AE%E6%AD%A3%EF%BC%89.pdf)

付帯資料として、画面イメージ設計図を付けています。以下にリンクを記載します。ご参照下さい。

5.[画面イメージ設計図](https://github.com/learnsatellite/webapp/blob/main/doc/%E7%94%BB%E9%9D%A2%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E8%A8%AD%E8%A8%88%E5%9B%B3.pdf) 
