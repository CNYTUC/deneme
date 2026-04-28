import streamlit as st
import pandas as pd
from io import BytesIO

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


# Mevcut Kategorileri Göster ve Düzenle
# ============================================================================================
st.subheader("📋 Mevcut Kategoriler")

rows = dla_kategorileri_getir()
df = pd.DataFrame(rows.data)

if not df.empty:

    # Seçim kolonu ekle
    df.insert(0, "Sec", False)

    edited_df = st.data_editor(
        df,
        use_container_width=True,
        hide_index=True,
        disabled=["id"],
        column_config={
            "Sec": st.column_config.CheckboxColumn(
                "Seç",
                width=None
            ),
            "id": st.column_config.NumberColumn(
                "ID",
                width=None
            ),
            "AnaKategori": st.column_config.TextColumn(
                "Ana Kategori",
                width=550
            ),
            "SubKategori": st.column_config.TextColumn(
                "Alt Kategori",
                width=550
            ),
        },
        key="kategori_editor"
    )

    st.divider()

    secili_satirlar = edited_df[edited_df["Sec"] == True]

    if len(secili_satirlar) == 1:

        selected_row = secili_satirlar.iloc[0]
        selected_id = int(selected_row["id"])

        st.info(f"Seçili ID: {selected_id}")

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

    elif len(secili_satirlar) > 1:
        st.warning("Lütfen sadece bir satır seç.")
    else:
        st.info("İşlem yapmak için tablodan bir satır seç.")


    excel_buffer = BytesIO()

    with pd.ExcelWriter(excel_buffer, engine="xlsxwriter") as writer:
        edited_df.to_excel(writer, index=False, sheet_name="DlaKategoriler")

    st.download_button(
        label="📥 Excel Olarak İndir",
        data=excel_buffer.getvalue(),
        file_name="DlaKategoriler.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        use_container_width=True
    )

else:
    st.info("Henüz kayıt yok.")