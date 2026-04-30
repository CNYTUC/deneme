import streamlit as st
import pandas as pd
from io import BytesIO

from supabaseFonksiyon import (
    dla_alt_kategori_ekle,
    dla_ana_kategori_listesi,
    dla_alt_kategorileri_getir,
    dla_kategorileri_getir,
    dla_alt_kategori_guncelle,
    dla_alt_kategori_sil,
    dla_secili_kategorileri_getir,
    dla_sorulari_getir,
    dla_sorulari_toplu_ekle,
    dla_soru_guncelle,
    dla_soru_sil,
)

# ============================================================================================
# UST VERI
# ============================================================================================
st.header("Dla Soru Editörü")
tab1, tab2, tab3, tab4 = st.tabs(["➕ Yeni Kategori", "📚 Mevcut Kategoriler", "➕ Yeni Soru", "📋 Mevcut Sorular"])

# ============================================================================================
# TAB 1: YENI KATEGORI EKLE
# ============================================================================================ 
with tab1:

    with st.form("kategori_ekleme_formu", clear_on_submit=True):

        # Ana kategori, alt kategori, soru metni, resim yolu ve notlar için session state tanımları
        # ============================================================================================
        st.session_state.setdefault("YK_ana_kategori", None)
        st.session_state.setdefault("YK_alt_kategori", None)    

        # Kategori seçimi oluştur.
        col1, col2 = st.columns([1, 3])

        with col1:
            with st.container(border=True,vertical_alignment="center",height="stretch"):
                st.session_state.YK_ana_kategori = st.radio(
                "Ana Kategori",
                dla_ana_kategori_listesi(),
                key="YKK_ana_kategori_radio"
                )
            with col2:
                with st.container(border=True,vertical_alignment="center",height="stretch"):
                    st.session_state.YK_alt_kategori = st.text_input(
                        "Alt Kategori",
                        placeholder="Örnek: Prefer",
                        key="YKK_yeni_alt_kategori"
                    )
                    kaydet = st.form_submit_button("Kaydet")

            if kaydet:
                if not st.session_state.YK_alt_kategori.strip():
                    st.warning("Alt kategori boş bırakılamaz.")
                else:
                    dla_alt_kategori_ekle(
                        st.session_state.YK_ana_kategori,
                        st.session_state.YK_alt_kategori.strip()
                    )
                    st.success("Yeni kategori eklendi.")
                    
                    # Formu temizle
                    st.session_state.YK_ana_kategori = None
                    st.session_state.YK_alt_kategori = None

# ============================================================================================
# TAB 2: KATEGORILERI GORUNTULE VE DUZENLE
# ============================================================================================ 
with tab2:

    # Ana kategori, alt kategori, soru metni, resim yolu ve notlar için session state tanımları
    # ============================================================================================
    st.session_state.setdefault("MK_ana_kategori", None)
    st.session_state.setdefault("MK_alt_kategori", None)    

    # Kategori seçim alanları için kolon düzeni
    col1, col2 = st.columns([4, 1])

    with col1:
        with st.container(border=True,vertical_alignment="center",height="stretch"):
            st.session_state.MK_ana_kategori = st.radio(
                "Ana Kategori",
                ["All"] + dla_ana_kategori_listesi(),
                key="MKK_ana_kategori",
                horizontal=True
            )

    with col2:

        with st.container(border=True,vertical_alignment="center",height="stretch"):
            
            kategori_getir = st.button(
                "Kategorileri Getir",
                key="MKK_kategori_getir",
                use_container_width=True
                )
                 
    # Butona basılınca seçimi kaydet
    if "kategori_tablosu_goster" not in st.session_state:
        st.session_state.kategori_tablosu_goster = False

    if "secili_ana_kategori" not in st.session_state:
        st.session_state.secili_ana_kategori = None

    if kategori_getir:
        st.session_state.kategori_tablosu_goster = True
        st.session_state.secili_ana_kategori = st.session_state.MK_ana_kategori

    # Tabloyu göster
    if st.session_state.kategori_tablosu_goster:

        rows = dla_secili_kategorileri_getir(ana_kategori=st.session_state.secili_ana_kategori)

        df = pd.DataFrame(rows.data)

        if not df.empty:

            # Seçim kolonu ekle
            df.insert(0, "Sec", False)

            st.subheader(f"{st.session_state.secili_ana_kategori} Kategorileri")

            edited_df = st.data_editor(
                df,
                use_container_width=True,
                hide_index=True,
                disabled=["id"],
                column_config={
                    "id": st.column_config.NumberColumn("ID"),
                    "AnaKategori": st.column_config.TextColumn("Ana Kategori"),
                    "AltKategori": st.column_config.TextColumn("Alt Kategori"),
                },
                key="MKK_kategori_editor"
            )

        else:
            st.info("Bu kategoriye ait kayıt bulunamadı.")

        #============================================================================================
        st.divider()
        #============================================================================================

        #seçili satırları al
        secili_satirlar = edited_df[edited_df["Sec"] == True]

        # seçili satır sayısına göre işlem yap
        if len(secili_satirlar) == 1:

            selected_row = secili_satirlar.iloc[0]
            selected_id = int(selected_row["id"])

            st.info(f"Seçili ID: {selected_id}")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("💾 Seçili Satırı Güncelle", use_container_width=True):
                    dla_alt_kategori_guncelle(
                        selected_id,
                        selected_row["AnaKategori"],
                        selected_row["AltKategori"]
                    )
                    st.success("Kategori güncellendi.")
                    st.rerun()

            with col2:
                if st.button("🗑️ Seçili Satırı Sil", use_container_width=True):
                    dla_alt_kategori_sil(selected_id)
                    st.success("Kategori silindi.")
                    st.rerun()

        elif len(secili_satirlar) > 1:
            st.warning("Lütfen sadece bir satır seç.")
        else:
            st.info("İşlem yapmak için tablodan bir satır seç.")



        # Excel olarak indirme butonu
        #============================================================================================
        
        export_df = edited_df.drop(columns=["Sec"], errors="ignore")

        excel_buffer = BytesIO()

        with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
            export_df.to_excel(writer, index=False, sheet_name="DlaKategoriler")

        st.download_button(
            label="📥 Excel Olarak İndir",
            data=excel_buffer.getvalue(),
            file_name="DlaKategoriler.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True
        )




# ============================================================================================
# TAB 3: YENI SORU EKLE
# ============================================================================================ 

with tab3:

    # Ana kategori, alt kategori, soru metni, resim yolu ve notlar için session state tanımları
    # ============================================================================================
    st.session_state.setdefault("YS_ana_kategori", None)
    st.session_state.setdefault("YS_alt_kategori", None)    
    st.session_state.setdefault("YS_soru_metni", None)    
    st.session_state.setdefault("YS_resim_yolu", None)    
    st.session_state.setdefault("YS_notlar", None)
    st.session_state.setdefault("YS_Etiketler", None)

    # Kategori seçim alanları için kolon düzeni
    col1, col2, col3, col4 = st.columns([1, 1, 1, 2])

    with col1:

        # Ana kategori seçimi
        # ============================================================================================
        with st.container(border=True, vertical_alignment="center", height="stretch"):
                st.session_state.YS_ana_kategori = st.radio(
                    "Ana Kategori",
                    dla_ana_kategori_listesi(),
                    key="YSK_ana_kategori",
                )

    with col2:

        # Alt kategori seçimi
        # ============================================================================================
        with st.container(border=True, vertical_alignment="center", height="stretch"):
            
            alt_kategoriler = dla_alt_kategorileri_getir(st.session_state.YS_ana_kategori)
            st.session_state.YS_alt_kategori = st.selectbox(
                "Alt Kategori",
                alt_kategoriler,
                key="YSK_alt_kategori",
            )

    with col3:

        # Resim yolu girişi
        # ============================================================================================       
        with st.container(border=True, vertical_alignment="center", height="stretch"):
            st.session_state.YS_resim_yolu = st.text_input(
                "Resim Yolu (Opsiyonel)",
                placeholder="Örnek: /images/question1.png",
                key="YSK_resim_yolu",
            )
    
    with col4:
        # Etiketler girişi
        # ============================================================================================       
        with st.container(border=True, vertical_alignment="center", height="stretch"):
            st.session_state.YS_Etiketler = st.text_input(
                "Etiketler (Opsiyonel)",
                placeholder="Örnek: Teknoloji, alışkanlık",
                key="YSK_etiketler",
            )

    # Soru metni ve notlar için geniş bir alan
    # ============================================================================================
    st.session_state.YS_soru_metni = st.text_area(
        "Soru Metni",
        placeholder="Her satıra ayrı bir soru yazın.",
        height=220,
        key="YSK_soru_metni",
        )

    # Notlar alanı
    # ============================================================================================
    st.session_state.YS_notlar = st.text_area(
        "Notlar",
        placeholder="Örnek: Bu soru tercihleri ölçmek için kullanılır.",
        key="YSK_notlar",
        )

    # Kaydet butonu ve doğrulama
    # ============================================================================================
    if st.button("Kaydet", key="YSK_kaydet_buton"):

        # Gerekli alanların doldurulup doldurulmadığını kontrol et
        if not st.session_state.YS_ana_kategori:
            st.warning("Ana kategori boş bırakılamaz.")

        elif not st.session_state.YS_alt_kategori:
            st.warning("Alt kategori boş bırakılamaz.")

        elif not st.session_state.YS_soru_metni:
            st.warning("Soru metni boş bırakılamaz.")

        else:
            dla_sorulari_toplu_ekle(
                st.session_state.YS_ana_kategori,
                st.session_state.YS_alt_kategori,
                st.session_state.YS_soru_metni,
                st.session_state.YS_notlar,
                st.session_state.YS_Etiketler,
                st.session_state.YS_resim_yolu
            )

            # Eklenen soru sayısını hesapla
            eklenen_soru_sayisi = len([
                soru for soru in st.session_state.YS_soru_metni.splitlines()
                if soru.strip()
            ])

            st.success(f"{eklenen_soru_sayisi} soru eklendi.")

            # Formu temizle
            st.session_state.YS_ana_kategori = None
            st.session_state.YS_alt_kategori = None
            st.session_state.YS_soru_metni = None
            st.session_state.YS_resim_yolu = None
            st.session_state.YS_notlar = None
            st.session_state.YS_Etiketler = None

# ============================================================================================
# TAB 4: MEVCUT SORULARI GORUNTULE VE DUZENLE
# ============================================================================================ 
with tab4:
    st.write("Bu sekmede mevcut soruları görüntüleyebilir ve düzenleyebilirsiniz.")