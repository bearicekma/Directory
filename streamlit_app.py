#以下をapp.pyに書き込む

# モジュールの読み込み
import pandas as pd
import streamlit as st
import pygwalker as pyg

st.title('Streamlitへようこそ')

# 初期設定
st.set_page_config(layout="wide")

# CSVファイル取得（サイドパネル）
df = None
with st.sidebar:
    input = st.file_uploader("Choose a CSV file")
    if input is not None:
        df = pd.read_csv(input)

# Graphic Walker 操作（メインパネル）
if df is not None:
    output = pyg.walk(df, env='Streamlit')
    st.write(output)
