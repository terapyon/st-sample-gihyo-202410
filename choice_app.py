import random
import streamlit as st

st.title("文字列を選択するアプリ")
text = st.text_input("スペース区切りで単語を入力してください。")
splited_text = text.replace("　", " ").split(" ")
st.write("入力した選択肢: ", splited_text)
if st.button("選択肢を表示"):
    choice = random.choice(splited_text)
    st.write("選択した選択肢: ", choice)
