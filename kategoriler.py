import streamlit as st

tab1, tab2, tab3,  tab4  = st.tabs(["Görüntüle", "Ekle", "Düzenle", "Sil"])

with tab1:
    st.header("Görüntüle")
with tab2:
    st.header("Ekle")
with tab3:
    st.header("Düzenle")
with tab4:
    st.header("Sil")