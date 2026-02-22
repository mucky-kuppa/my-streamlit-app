# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 21:20:49 2026

@author: nao
"""
import streamlit as st

st.title("ファイル系ウィジェット")

# 11. ファイルアップロード
st.header("11. 📁 ファイルアップロード")
uploaded = st.file_uploader("ファイルをアップロードしてください")
if uploaded:
    st.write("アップロードされたファイル名:", uploaded.name)

# 12. カメラ入力
st.header("12. 📷 カメラ入力")
img = st.camera_input("写真を撮影")
if img:
    st.image(img)
