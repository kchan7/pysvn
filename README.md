# pysvn

## 構築した環境をテストする
 - こちらの記事「PythonでSubversionのコミットログを解析する」のコードをコピペして構築した環境のテストと公開されているサンプルのSubversionでログインなどをテストしてみて下さい。
 - https://qiita.com/mima_ita/items/8fed6e1f29deb470764f

```
$ python3 svnlog.py http://svn.sourceforge.jp/svnroot/simyukkuri/ "admin" "admin"
```

## ファイル情報を取得する
 - Subversionのファイル一覧をCSVへ出力するサンプルコードです。
```
$ python3 file_list.py http://svn.sourceforge.jp/svnroot/simyukkuri/ "admin" "admin"
```
