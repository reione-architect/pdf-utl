# pdf-utl
PDFファイルを処理するユーティリティ

## 概要
このスクリプトは、指定したページ以降のPDFを新しいファイルとして保存するPythonプログラムです。

## 環境構築手順

### 1. 仮想環境 (venv) の作成
Python の仮想環境を作成し、パッケージの管理を行います。

```bash
python -m venv venv
```

### 2. 仮想環境の有効化
OS に応じて以下のコマンドを実行します。

- **Windows**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**
  ```bash
  source venv/bin/activate
  ```

### 3. 必要なパッケージのインストール
依存関係を `requirements.txt` に記載し、以下のコマンドでインストールします。

```bash
pip install -r requirements.txt
```

もし `requirements.txt` がない場合は、手動で以下のパッケージをインストールしてください。

```bash
pip install PyPDF2
```

## 使い方
スクリプトを実行することで、指定ページ以降のPDFを新しいファイルとして保存できます。

```bash
python split_pdf.py
```

スクリプト内の変数を変更することで、分割するページ番号やファイル名を変更できます。

## ライセンス
MIT License

