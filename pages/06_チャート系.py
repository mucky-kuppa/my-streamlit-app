import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import matplotlib.pyplot as plt

st.title("チャート系ウィジェット")

# サンプルデータ
df = pd.DataFrame({
    "月": ["1月","2月","3月","4月","5月","6月"],
    "売上": [100,120,90,150,180,130],
    "利益": [30,40,25,50,60,35]
})

# 46. Line Chart
st.header("46. 📈 Line Chart（折れ線）")
st.line_chart(df[["売上","利益"]])

# 47. Bar Chart
st.header("47. 📊 Bar Chart（棒グラフ）")
st.bar_chart(df[["売上","利益"]])

# 48. Area Chart
st.header("48. 📉 Area Chart（面グラフ）")
st.area_chart(df[["売上","利益"]])

# 49. Map
st.header("49. 🗺️ Map（地図）")
map_df = pd.DataFrame({
    "lat": [35.681236, 34.6937, 43.06417],
    "lon": [139.767125, 135.5023, 141.34694],
    "都市": ["東京", "大阪", "札幌"]
})
st.map(map_df)

# 50. Altair Line
st.header("50. 🎨 Altair（折れ線＋ポイント）")
alt_chart = (
    alt.Chart(df)
    .mark_line(point=True)
    .encode(x="月", y="売上", tooltip=["月","売上"])
)
st.altair_chart(alt_chart, use_container_width=True)

# 51. Altair Bar
st.header("51. 🎨 Altair Bar（棒グラフ）")
alt_bar = alt.Chart(df).mark_bar().encode(x="月", y="売上")
st.altair_chart(alt_bar, use_container_width=True)

# 52. Altair Area
st.header("52. 🎨 Altair Area（面グラフ）")
alt_area = alt.Chart(df).mark_area(opacity=0.6).encode(x="月", y="売上")
st.altair_chart(alt_area, use_container_width=True)

# 53. Plotly Bar
st.header("53. 📊 Plotly Bar（棒グラフ）")
fig = px.bar(df, x="月", y=["売上","利益"], barmode="group")
st.plotly_chart(fig, use_container_width=True)

# 54. Plotly Scatter
st.header("54. 🔍 Plotly Scatter（散布図）")
scatter_df = pd.DataFrame({
    "x": np.random.randn(100),
    "y": np.random.randn(100),
    "カテゴリ": np.random.choice(["A","B","C"], 100)
})
fig2 = px.scatter(scatter_df, x="x", y="y", color="カテゴリ")
st.plotly_chart(fig2, use_container_width=True)

# 55. Plotly Pie
st.header("55. 🥧 Plotly Pie（円グラフ）")
fig3 = px.pie(df, names="月", values="売上")
st.plotly_chart(fig3, use_container_width=True)

# 56. Plotly Histogram
st.header("56. 📊 Plotly Histogram（ヒストグラム）")
hist_df = pd.DataFrame({"値": np.random.randn(200)})
fig4 = px.histogram(hist_df, x="値", nbins=30)
st.plotly_chart(fig4, use_container_width=True)

# 57. Plotly Box（箱ひげ図）
st.header("57. 📦 Plotly Box（箱ひげ図）")
fig5 = px.box(scatter_df, y="y")
st.plotly_chart(fig5, use_container_width=True)

# 58. Plotly Violin（バイオリンプロット）
st.header("58. 🎻 Plotly Violin（バイオリンプロット）")
fig6 = px.violin(scatter_df, y="y")
st.plotly_chart(fig6, use_container_width=True)

# 59. Plotly Scatter Matrix（散布図行列）
st.header("59. 🔢 Plotly Scatter Matrix（散布図行列）")
matrix_df = pd.DataFrame(np.random.randn(100, 3), columns=["A","B","C"])
fig7 = px.scatter_matrix(matrix_df)
st.plotly_chart(fig7, use_container_width=True)

# 60. Matplotlib（折れ線）
st.header("60. 📐 Matplotlib（折れ線グラフ）")
fig8, ax = plt.subplots()
ax.plot(df["月"], df["売上"], marker="o")
ax.set_title("売上推移")
st.pyplot(fig8)
