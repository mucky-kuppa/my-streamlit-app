import streamlit as st
import pandas as pd

st.title("レイアウト系ウィジェット")

# サンプルデータ
df = pd.DataFrame({
    "商品": ["りんご", "みかん", "バナナ"],
    "価格": [120, 80, 100],
    "在庫": [30, 50, 40]
})

# 21. 2カラム
st.header("21. 📐 2カラム")
col1, col2 = st.columns(2)
col1.table(df)
col2.metric("平均価格", df["価格"].mean())

# 22. 3カラム
st.header("22. 📐 3カラム")
c1, c2, c3 = st.columns(3)
c1.write("商品一覧")
c1.table(df)
c2.write("価格")
c2.bar_chart(df["価格"])
c3.write("在庫")
c3.line_chart(df["在庫"])

# 23. タブ（3つ）
st.header("23. 📑 タブ（3つ）")
t1, t2, t3 = st.tabs(["表", "統計", "コード"])
t1.dataframe(df)
t2.write(df.describe())
t3.code("df.describe()")

# 24. エクスパンダー
st.header("24. 📦 エクスパンダー")
with st.expander("データを表示"):
    st.dataframe(df)

# 25. コンテナ（ネスト）
st.header("25. 📦 コンテナ（ネスト）")
with st.container():
    st.write("コンテナ1")
    with st.container():
        st.write("コンテナ2（ネスト）")

# 26. サイドバー
st.header("26. 📚 サイドバー")
st.sidebar.write("これはサイドバーです")
st.sidebar.table(df)

# 27. empty（プレースホルダー）
st.header("27. 🪧 empty（プレースホルダー）")
placeholder = st.empty()
placeholder.write("ここは後で書き換わります")

# 28. markdown レイアウト
st.header("28. 📝 Markdown")
st.markdown("**太字** や *斜体*、`コード` も書けます")

# 29. caption
st.header("29. 🏷️ caption")
st.caption("これはキャプションです")

# 30. divider
st.header("30. ➖ divider")
st.divider()

# 31. write（自動判別）
st.header("31. ✍️ write（自動判別）")
st.write("文字列", 123, df)

# 32. code（レイアウト用途）
st.header("32. 💻 code（レイアウト用途）")
st.code("print('Hello')")

# 33. header / subheader / title
st.header("33. 🏷️ header / subheader / title")
st.subheader("これは subheader")
st.title("これは title（デモ）")

# 34. container + columns（複合）
st.header("34. 📦 container + columns")
with st.container():
    a, b = st.columns(2)
    a.write("左")
    b.write("右")

# 35. sidebar + selectbox
st.header("35. 📚 サイドバー選択")
choice = st.sidebar.selectbox("商品を選択", df["商品"])
st.write("選択:", choice)
