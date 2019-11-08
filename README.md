# KPMG_hackathon

# 環境構築

- 要インストール
  - numpy
```
pip install numpy
```
- phe
```
pip install phe
```

- 使用する外部モジュール
  - phe
  - numpy
  - socket
  - pickle
  - tkinter
  - tkinter.ttk

# 実行手順

1. `server.py`を実行
2. 別のCUI上で`user.py`を実行

# 使い方

1. 実行するとユーザA~Cの３つの進路評価システムが起動します
2. それぞれの成績をプルダウンメニューから選択します
3. 送信ボタンをクリックします
4. 復号結果及びおすすめの職業が表示されます

# 構成

## server.py

- Class Server()
  - def setlist(self, list)
    - ユーザから受け取った暗号化データをセット
  - def judge(self)
    - 重み行列と暗号化されたデータの内積をとり、判定データを秘密計算

## user.py

- Class Application(tk.Frame)
  - 3人のユーザ専用GUIを作る
- Class User(tk.Frame)
  - def buttonClick()
    - 送信ボタンがクリックされた後の処理
  - def setScore(self, seiseki1, seiseki2, seiseki3)
    - GUIの入力をセットする
  - def encList(self)
    - ユーザの成績を暗号化
  - def decList(self, list)
    - listの要素を復号する
  - def recSub(self)
    - 判定結果をGUIに表示する
  



