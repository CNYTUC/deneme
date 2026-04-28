import streamlit as st
from supabase import create_client

#BAŞLIK
#============================================================================================
st.title("Dla Kategori Editörü")
st.write("Dla Kategori Editörü sayfasına hoş geldiniz. Bu sayfa üzerinden DLA sınav kategorilerini yönetebilirsiniz.")



tab1, tab2, tab3,  tab4  = st.tabs(["Görüntüle", "Ekle", "Düzenle", "Sil"])

with tab1:
    st.header("Kategoriler")
with tab2:
    st.header("Yeni Kategori Ekle")

# Kategori seçimi oluştur.
col1, col2 = st.columns([2, 1])

with col1:
    with st.container(border=True,vertical_alignment="center",height=200,width=500):
        Ana_Kategori =st.radio(
            "Kategori Seçin 👉",
            key="visibility",
            options=["General", "Scenario", "PictureDescription"],
        )

with col2:
    with st.container(border=True,vertical_alignment="center",height=200):
        Dla_Alt_Kategori = st.text_input(
            "Alt Kategori Oluşturun 👇",
            placeholder="Örnek: Prefer",
            key="Dla_alt_kategori_input",
        )
    
    load_Clicked = st.button(
            "Load Questions",
            key="Dla_Kategori_Input",
            icon=":material/published_with_changes:",
            use_container_width=True
        )

with tab3:
    st.header("Kategori Düzenle")
with tab4:
    st.header("Kategori Sil")