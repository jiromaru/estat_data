# ESTAT_DATA

## 概要
ESTATの統計データを取得するためのツール。e-StatのAPIを使用している。estat_data.pyを実行するとappIdの入力画面と検索画面が表示されるので、そこに事前に取得したappIdと検索したい統計データのキーワードを打ち込む。その後検索ボタンを押すと、ヒットした統計データ名が一覧に表示される。
そこから欲しいデータを選択(複数可)→実行すると選択したデータのcsvファイルがプログラムの配置ディレクトリに作成される。ファイル名は現状ダウンロードしたままの名前。
仕組みとしては、e-StatのAPIを使用してテーブルの一覧を取得→画面に一覧を表示&選択実行→e-StatのAPIに選択したデータを受け渡しデータを取得するという流れの処理となっている。
※e-StatのAPIを使用するためにはappIdを事前に取得する必要があるため、e-Statのサイト上でappIdを取得していることが前提条件となる。

## 環境
OS:Windows10

言語:python3

使用モジュール(標準モジュール以外)
* requests

### 各プログラムの説明
* estat_data.py
  下記のプログラムを呼び出すメインプログラム。
* get_dict.py  
  検索ワードをe-Stat側に渡し、関連するデータの名前とstatsDataIdを取得する(検索にかかったものをすべて)。
* mk_display.py  
  get_dict.pyを呼び出し、取得した統計データ名を選択するための画面を作成する(tkinterを使用)。
  ※画面は下記を参照
* get_data.py  
  取得したい統計データを選択後、e-StatのAPIを使用し選択したデータをcsv形式で取得するためのプログラム。
  
### 実行画面
![実行画面](https://github.com/jiromaru/estat_data/blob/images/estat_images.png?raw=true)
