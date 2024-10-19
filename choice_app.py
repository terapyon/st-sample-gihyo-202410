import random
import streamlit as st

st.title("文字列を選択するアプリ")
text = st.text_input("スペース区切りで単語を入力してください。")  # 入力ボックス
splited_text = text.replace("　", " ").split(" ")  # スペース区切りでリスト化
st.write("入力した単語: ", splited_text)  # リストを表示
if st.button("一つを選ぶ"):  # ボタンを設置し、ボタンが押されたら実行
    choice = random.choice(splited_text)  # ランダムに1つだけを選択
    st.write("選択された単語: ", choice)  # 選択されたものを表示
