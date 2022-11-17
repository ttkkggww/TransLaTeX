# TransLaTeX
LaTeXをDeepLで翻訳してみようと思いました。
deeplを使用して翻訳しています。
## Example
```console
$python -m src.main --path '/hogehoge.zip' 
<class 'str'>
translating 0main.tex ...
Faild to restore: 0main.tex ['\\keywords{hogehogex,hugahuga}', '00002']
translating 1hogehoge.tex ...
translating 2hogehoge.tex ...
translating 3hogehoge.tex ...
translating 4hogehoge.tex ...
translating 6hogehoge.tex ...
translating 7hogehoge.tex ...
translating 8hogehoge.tex ...
translating 9hogehoge.tex ...
translating 5hogehoge.tex ...
$ls workspace/
2022-11-18_01:31:44_translated_hogehoge.zip
2022-11-18_01:53:24_translated_hogehoge.zip
```

## Features
Pythonのバージョンは特に意識して作成してはいません。
Python 3.10.6で作成しました。
必要なライブラリは適宜インストールをお願いします。<br>
仕組みとしては、latexのコマンドを0000,00001のようにひとまず数字に置換してdeeplを使用して翻訳し、
翻訳済みの文を改めて置換し直します。<br>
ですので、その段階で機械翻訳により数字がおかしくなってしまうと、正しく翻訳できなくなります。
## How to install
このリポジトリのpythonファイルをcloneなどして実行すればいいです。
## How to use
latexのコマンドは`escape_regular_expression.txt`にある正規表現で置換されます。<br>
よって、足りないコマンドは適宜追加する必要があります。<br>
ただし、\begin{}で始まり、\end{}で終わるコマンドはデフォルトで置換されます。<br>
overleafなどで、作成したlatexプロジェクトをzipファイルのまま翻訳することを想定しています。<br>
`python -m src.main --path target/path.zip`で実行できます。<br>
```cosole
$python -m src.main -h
usage: main.py [-h] [-P PATH] [-W WORKSPACE] [-T TMPDIR]

options:
  -h, --help            show this help message and exit
  -P PATH, --path PATH  Path of the zip file you want to translate.
  -W WORKSPACE, --workspace WORKSPACE
                        Temporary workspace location for file operations.
  -T TMPDIR, --tmpdir TMPDIR
                        Temporary workspace location for file operations.
```
