# st-sample-gihyo-202410

Streamlitのサンプルアプリ

## セットアップと起動

```
(venv) $ pip install -r requirements.txt
(venv) $ streamlit run choice_app.py  # 文字変換アプリ
(venv) $ streamlit run dice_app.py  # サイコロアプリ
```


## 文字の変換アプリ

- タイトル: スペース区切りの文字列から一つを選択する
- パッケージ: st-sample-gihyo-202410
- アプリ: choice_app.py
- 説明: ボタンを押したら一つが選べる
- text_input: 1行文字入力
- 結果: 一つだけが選べる


## サイコロアプリ

- タイトル: サイコロを2つ振った結果を表示
- パッケージ: st-sample-gihyo-202410
- アプリ: dice_app.py
- 説明: サイコロ2個を何度か振って結果を表形式で表示し、散布図を表示する
- ステップ
  - サイコロを模して2つの1-6の数値を生成
  - 合計値を求める
  - サイコロの値と合計値を、表で表示
  - 合計値の散布図を書く
  - 拡張で、数値入力して、まとめてサイコロをたくさん振る