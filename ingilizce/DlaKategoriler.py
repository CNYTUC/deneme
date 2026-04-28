import streamlit as st
import pandas as pd

from supabaseFonksiyon import (
    dla_kategori_ekle,
    dla_kategorileri_getir,
    dla_kategori_guncelle,
    dla_kategori_sil
)

#BAŞLIK
#============================================================================================
st.header("Dla Kategori Editörü")


#Yenı Kategori Ekleme Formu
#============================================================================================
st.subheader("➕ Yeni Kategori Ekle")

with st.form("kategori_ekleme_formu", clear_on_submit=True):

    # Kategori seçimi oluştur.
    col1, col2 = st.columns([1, 3])

    with col1:
        with st.container(border=True,vertical_alignment="center",height="stretch"):
            yeni_ana_kategori = st.radio(
                "Ana Kategori",
                ["General", "Scenario", "PictureDescription"]
                )
    with col2:
        with st.container(border=True,vertical_alignment="center",height="stretch"):
            yeni_alt_kategori = st.text_input(
                "Alt Kategori",
                placeholder="Örnek: Prefer"
                )
            kaydet = st.form_submit_button("Kaydet")

    if kaydet:
        if not yeni_alt_kategori.strip():
            st.warning("Alt kategori boş bırakılamaz.")
        else:
            dla_kategori_ekle(
                yeni_ana_kategori,
                yeni_alt_kategori.strip()
            )
            st.success("Yeni kategori eklendi.")
            st.rerun()


#Mevcut Kategorileri Göster ve Düzenle
#============================================================================================
st.subheader("📋 Mevcut Kategoriler")

rows = dla_kategorileri_getir()
df = pd.DataFrame(rows.data)

edited_df = st.data_editor(
    df,
    use_container_width=True,
    hide_index=True,
    disabled=["id"],
    column_config={
        "id": st.column_config.NumberColumn(
            "ID",
            width=40
        ),
        "AnaKategori": st.column_config.TextColumn(
            "AnaKategori",
            width="medium"
        ),
        "SubKategori": st.column_config.TextColumn(
            "SubKategori",
            width="large"
        ),
    },

    key="kategori_editor"
)

st.divider()

if not edited_df.empty:
    selected_id = st.selectbox(
        "İşlem yapılacak ID seç:",
        edited_df["id"].tolist()
    )

    selected_row = edited_df[edited_df["id"] == selected_id].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        if st.button("💾 Seçili Satırı Güncelle", use_container_width=True):
            dla_kategori_guncelle(
                selected_id,
                selected_row["AnaKategori"],
                selected_row["SubKategori"]
            )
            st.success("Kategori güncellendi.")
            st.rerun()

    with col2:
        if st.button("🗑️ Seçili Satırı Sil", use_container_width=True):
            dla_kategori_sil(selected_id)
            st.success("Kategori silindi.")
            st.rerun()
else:
    st.info("Henüz kayıt yok.")