import streamlit as st

st.set_page_config(page_title="Strateji Merkezi", layout="wide")

pages = [
    st.Page("Sapan/Scan/sapan_tarama.py", title="Sapan Stratejisi Tarama", icon="🔎"),
    st.Page("Sapan/Test/sapan_backtest.py", title="Sapan Stratejisi BackTest", icon="📊"),
    st.Page("Breakout/Scan/bist_kirilim_tarama.py", title="Breakout Stratejisi Tarama", icon="🔎"),
    st.Page("Breakout/Test/bist_kirilim_backtest.py", title="Breakout Stratejisi BackTest", icon="🔎"),
]


pg = st.navigation(pages, position="hidden")

st.title("Strateji Merkezi")
st.write("Modül Listesi.")

st.page_link("Sapan/Scan/sapan_tarama.py", label="Sapan Stratejisi Tarama", icon="🔎")
st.page_link("Sapan/Test/sapan_backtest.py", label="Sapan Stratejisi BackTest", icon="📊")
st.page_link("Breakout/Scan/bist_kirilim_tarama.py", label="Breakout Stratejisi Tarama", icon="🔎")
st.page_link("Breakout/Test/bist_kirilim_backtest.py", label="Breakout Stratejisi BackTest", icon="📊")
pg.run()