import streamlit as st
import pandas as pd
import numpy as np

st.title("データ表示系ウィジェット")

# サンプルデータ
df = pd.DataFrame({
    "都道府県": ["東京都", "大阪府", "愛知県", "福岡県"],
    "人口（万人）": [1400, 880, 755, 510],
    "面積（km²）": [2194, 1905, 5172, 4986]
})

# 36. DataFrame
st.header("36. 📊 DataFrame")
st.dataframe(df)

# 37. Table
st.header("37. 📋 Table")
st.table(df)

# 38. JSON
st.header("38. 🧾 JSON")
st.json({
    "title": "都道府県データ",
    "columns": list(df.columns),
    "sample": df.iloc[0].to_dict()
})

# 39. Code（コード表示）
st.header("39. 💻 Code")
st.code("print('Hello Streamlit')", language="python")

# 40. Metric（指標表示）
st.header("40. 📈 Metric")
st.metric("人口最大", f"{df['人口（万人）'].max()} 万人")

# 41. Data Editor（編集可能テーブル）
st.header("41. ✏️ Data Editor（編集可能）")
edited = st.data_editor(df)
st.write("編集結果:", edited)

# 42. AgGrid風（ソート・フィルタ付き DataFrame）
st.header("42. 🔍 ソート・フィルタ可能 DataFrame")
st.dataframe(df, use_container_width=True)

# 43. Describe（統計情報）
st.header("43. 📊 統計情報（describe）")
st.write(df.describe())

# 44. Highlight（ハイライト）
st.header("44. ✨ ハイライト表示")
st.dataframe(df.style.highlight_max(axis=0))

# 45. Progress（データ処理の進行表示）
st.header("45. ⏳ データ処理の進行表示")
progress = st.progress(0)
for i in range(100):
    progress.progress(i + 1)
