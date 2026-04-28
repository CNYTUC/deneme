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
st.title("Dla Kategori Editörü")
st.write("Dla Kategori Editörü sayfasına hoş geldiniz. Bu sayfa üzerinden DLA sınav kategorilerini yönetebilirsiniz.")


st.subheader("➕ Yeni Kategori Ekle")

with st.form("kategori_ekleme_formu", clear_on_submit=True):
    yeni_ana_kategori = st.selectbox(
        "Ana Kategori",
        ["General", "Scenario", "PictureDescription"]
    )

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



rows = dla_kategorileri_getir()
df = pd.DataFrame(rows.data)

edited_df = st.data_editor(
    df,
    use_container_width=True,
    hide_index=True,
    disabled=["id"],
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