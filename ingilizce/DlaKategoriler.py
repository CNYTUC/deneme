import streamlit as st
from supabase import create_client

#Sayfanın Genel Yapısı
st.set_page_config(
    page_title="DLA Kategori Editörü",
    page_icon="🎤",
    layout="wide"
)

tab1, tab2, tab3,  tab4  = st.tabs(["Görüntüle", "Ekle", "Düzenle", "Sil"])

with tab1:
    st.header("Kategoriler")
with tab2:
    st.header("Yeni Kategori Ekle")

    st.radio(
        "Kategori Seçin 👉",
        key="visibility",
        options=["General", "Scenario", "PictureDescription"],
    )
    Dla_Alt_Kategori = st.text_input(
        "Alt Kategori Oluşturun 👇",
        placeholder="Örnek: General Test 1",
        key="Dla_alt_kategori_input",
    )
    
with tab3:
    st.header("Kategori Düzenle")
with tab4:
    st.header("Kategori Sil")