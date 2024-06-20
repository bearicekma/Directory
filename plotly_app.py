
# 以下を.pyに書き込む
import pandas as pd
import plotly.express as px
import streamlit as st

# ワイド表示
st.set_page_config(layout="wide")

# タイトル
st.title("Data Analysis with PyGWalker.")

tips = px.data.tips()
fig = px.scatter(tips, x="total_bill", y="tip")
event = st.plotly_chart(fig)

event
