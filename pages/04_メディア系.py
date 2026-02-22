# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 21:33:52 2026

@author: nao
"""

import streamlit as st

st.title("メディア系ウィジェット")

# 17. 画像表示
st.header("17. 🖼️ 画像表示")
st.image("https://placehold.co/600x400", caption="サンプル画像")

# 18. 音声再生
st.header("18. 🔊 音声再生")
st.audio("https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav")

# 19. 動画再生
st.header("19. 🎬 動画再生")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")
