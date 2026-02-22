import streamlit as st
import time

st.title("その他のウィジェット")

# 56. プログレスバー（高度版）
st.header("56. ⏳ プログレスバー（高度版）")
progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

# 57. スピナー
st.header("57. 🔄 スピナー")
with st.spinner("読み込み中..."):
    time.sleep(1)
st.success("完了！")

# 58. バルーン
st.header("58. 🎉 バルーン")
st.balloons()

# 59. トースト通知（複数）
st.header("59. 🔔 トースト通知（複数）")
st.toast("1つ目の通知です")
time.sleep(0.5)
st.toast("2つ目の通知です")

# 60. メッセージ系（info / warning / error / success）
st.header("60. 💬 メッセージ表示")
st.info("これは info メッセージです")
st.warning("これは warning メッセージです")
st.error("これは error メッセージです")
st.success("これは success メッセージです")
