import streamlit as st
from supabase import create_client

tab1, tab2, tab3,  tab4  = st.tabs(["Görüntüle", "Ekle", "Düzenle", "Sil"])

with tab1:
    st.header("Görüntüle")
with tab2:
    st.header("Ekle")

    st.radio(
        "Kategori Seçin 👉",
        key="visibility",
        options=["General", "Scenario", "PictureDescription"],
    )
    Alt_Kategori = st.text_input(
        "Alt Kategori Oluşturun 👇",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.enabled,
        placeholder=st.session_state.placeholder,
    )

with tab3:
    st.header("Düzenle")
with tab4:
    st.header("Sil")