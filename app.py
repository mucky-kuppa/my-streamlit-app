import streamlit as st

st.set_page_config(
    page_title="Streamlit Widgets Showcase",
    page_icon="🚀",
    layout="wide"
)

# =========================
# Hero Header
# =========================
st.markdown(
    """
    <div style="
        padding: 40px 20px;
        background: linear-gradient(135deg, #4CAF50 0%, #2E7D32 100%);
        border-radius: 16px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
    ">
        <h1 style="font-size: 48px; margin-bottom: 10px;">🚀 Streamlit ウィジェット図鑑</h1>
        <p style="font-size: 20px; opacity: 0.9;">
            Python だけでここまでできる。60種類以上のウィジェットを体験しよう。
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# Streamlit の特徴
# =========================
st.subheader("✨ Streamlit の魅力")
cols = st.columns(4)

features = [
    ("⚡", "インタラクティブ", "入力・操作に即時反応する UI"),
    ("📊", "データ可視化", "グラフ・統計・地図などを簡単表示"),
    ("📐", "レイアウト自由自在", "カラム・タブ・コンテナで構成自在"),
    ("🌐", "Webアプリ化", "Python だけでアプリ公開まで可能")
]

for i, (icon, title, desc) in enumerate(features):
    with cols[i]:
        st.markdown(
            f"""
            <div style="
                background: white;
                padding: 20px;
                border-radius: 12px;
                text-align: center;
                box-shadow: 0 3px 8px rgba(0,0,0,0.1);
            ">
                <div style="font-size: 40px;">{icon}</div>
                <h3 style="margin: 10px 0 5px;">{title}</h3>
                <p style="font-size: 14px; color: #555;">{desc}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")

# =========================
# カテゴリカード
# =========================
st.subheader("📚 カテゴリ一覧（サイドバーから開けます）")

categories = [
    ("🔤", "入力系ウィジェット", "#E3F2FD"),
    ("📁", "ファイル・メディア系", "#FFF3E0"),
    ("📐", "レイアウト系ウィジェット", "#E8F5E9"),
    ("📊", "データ表示系ウィジェット", "#F3E5F5"),
    ("📈", "チャート系ウィジェット", "#E0F7FA"),
    ("✨", "その他のウィジェット", "#FBE9E7")
]

cols = st.columns(2)

for i, (icon, title, color) in enumerate(categories):
    with cols[i % 2]:
        st.markdown(
            f"""
            <div style="
                border-radius: 14px;
                padding: 22px;
                margin-bottom: 22px;
                background-color:{color};
                box-shadow: 0 3px 8px rgba(0,0,0,0.08);
                transition: transform 0.15s ease, box-shadow 0.15s ease;
            "
            onmouseover="this.style.transform='translateY(-4px)'; this.style.boxShadow='0 6px 14px rgba(0,0,0,0.12)';"
            onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 3px 8px rgba(0,0,0,0.08)';"
            >
                <h2 style="margin-top:0; font-size:26px;">{icon} {title}</h2>
                <p style="font-size:15px; color:#333;">左のサイドバーから開けます。</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")

# =========================
# このアプリで学べること
# =========================
st.subheader("🎓 このアプリで学べること")

st.markdown(
    """
- ✔ **入力系ウィジェット 20種類**  
- ✔ **レイアウト系ウィジェット 15種類**  
- ✔ **データ表示系ウィジェット 10種類**  
- ✔ **チャート系ウィジェット 15種類以上**  
- ✔ **その他の便利機能 10種類以上**  

Python だけで、これだけの UI・データ処理・可視化ができることを体験できます。
"""
)

st.caption("※ ページ遷移は左のサイドバーから行ってください。")
