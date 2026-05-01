import streamlit as st
import pandas as pd
from io import BytesIO

from yardimcilar import tr_to_en_lower

from supabaseFonksiyon import (
    
    dla_etiket_ekle,
    dla_etiketler_getir,
    dla_etiket_guncelle,
    dla_etiket_sil,


    dla_alt_kategori_ekle,
    dla_ana_kategori_listesi,
    dla_alt_kategorileri_getir,
    dla_etiket_ekle,
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
tab1, tab2, tab3, tab4 = st.tabs(["🏷️ Yeni Etiket", "📚 Mevcut Etiketler", "➕ Yeni Soru", "📋 Mevcut Sorular"])

# ============================================================================================
# TAB 1: YENI ETİKET EKLE
# ============================================================================================ 
with tab1:

    with st.form("kategori_ekleme_formu", clear_on_submit=True):

        # Ana kategori, alt kategori, soru metni, resim yolu ve notlar için session state tanımları
        # ============================================================================================
        st.session_state.setdefault("YE_etiket", None)
        # ============================================================================================


        # Kategori seçimi oluştur.
        col1, col2 = st.columns([5, 1])

        with col1:
            with st.container(border=True,vertical_alignment="center",height="stretch"):
                st.session_state.YE_etiket = st.text_input(
                "Etiket Adı",
                placeholder="Örnek: Teknoloji",
                key="YEK_etiket_input"
                )
        with col2:
            with st.container(border=True,vertical_alignment="center",height="stretch"):
                kaydet = st.form_submit_button("Kaydet")


        if kaydet:
            if not st.session_state.YE_etiket.strip():
                st.warning("Etiket adı boş bırakılamaz.")
            else:
                dla_etiket_ekle(
                    tr_to_en_lower(st.session_state.YE_etiket.strip()),
                )
                
                st.success("Yeni etiket eklendi.")
                    
                # Formu temizle
                st.session_state.YE_etiket = None

# ============================================================================================
# TAB 2: ETİKETLERİ GORUNTULE VE DUZENLE
# ============================================================================================ 
with tab2:

    # Etiketler için session state tanımları
    # ============================================================================================
    st.session_state.setdefault("ME_etiketler", None)

    #Etiketleri getir butonu
    # ============================================================================================
    with st.container(border=True,vertical_alignment="center",height="stretch"):
            
        EtiketletiGetir = st.button(
            "Etiketleri Getir",
            key="MEK_etiket_getir",
            use_container_width=True
            )
                 
    # Butona basılınca seçimi kaydet
    if "Etiketler_tablosu_goster" not in st.session_state:
        st.session_state.Etiketler_tablosu_goster = False

    if EtiketletiGetir:
        st.session_state.Etiketler_tablosu_goster = True

    # Tabloyu göster
    if st.session_state.Etiketler_tablosu_goster:

        rows = dla_etiketler_getir()

        df = pd.DataFrame(rows.data)

        if not df.empty:
            
            st.subheader(f"Etiketler",divider="red")

            # Seçim kolonu ekle
            df.insert(0, "Sec", False)

            edited_df = st.data_editor(
                df,
                use_container_width=True,
                hide_index=True,
                disabled=["id"],
                row_height=42,
                column_config={
                    "sec": st.column_config.TextColumn("sec", width=80),
                    "id": st.column_config.NumberColumn("ID", width=80),  
                    "Etiket": st.column_config.TextColumn("ETİKET"),
                },
                key="MEK_etiket_editor"
            )

        else:
            st.info("Herhangi bir etiket bulunamadı.")

        #============================================================================================
        st.divider()
        #============================================================================================

        #seçili satırları al
        secili_satirlar = edited_df[edited_df["Sec"] == True]

        # seçili satır sayısına göre işlem yap
        if len(secili_satirlar) == 1:

            #Tanımalamaları yap
            #============================================================================================
            selected_row = secili_satirlar.iloc[0]
            selected_id = int(selected_row["id"])
            selected_tag = tr_to_en_lower(selected_row["Etiket"])

            st.info(f"Seçili ID: {selected_id}")

            col1, col2 = st.columns(2)

            with col1:
                if st.button("💾 Seçili Etiketi Güncelle", use_container_width=True):
                    dla_etiket_guncelle(
                        selected_id,
                        selected_tag,
                    )
                    st.success("Etiket güncellendi.")
                    st.rerun()

            with col2:
                if st.button("🗑️ Seçili Satırı Sil", use_container_width=True):
                    dla_etiket_sil(selected_id)
                    st.success("Etiket silindi.")
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
            file_name="DlaEtiketler.xlsx",
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
    st.session_state.setdefault("YS_soru_metni", None)    
    st.session_state.setdefault("YS_resim_yolu", None)    
    st.session_state.setdefault("YS_notlar", None)
    st.session_state.setdefault("YS_Etiketler", None)

    # Kategori seçim alanları için kolon düzeni
    col1, col2 = st.columns([1, 5])

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
        # Etiketler girişi
        # ============================================================================================       
        with st.container(border=True, vertical_alignment="center", height="stretch"):
            st.session_state.YS_Etiketler = st.text_input(
                "Etiketler (Opsiyonel)",
                placeholder="Örnek: Teknoloji, alışkanlık",
                key="YSK_etiketler",
            
                rows = dla_etiketler_getir()
                df = pd.DataFrame(rows.data)

                etiket_listesi = df["Etiket"].dropna().unique().tolist()

                tags = st.multiselect(
                    "Etiketlerinizi seçin",
                    etiket_listesi,
                    max_selections=20,
                    accept_new_options=True,
                )
                
                st.write("You selected:", tags)

    # with col3:

    #     # Resim yolu girişi
    #     # ============================================================================================       
    #     with st.container(border=True, vertical_alignment="center", height="stretch"):
    #         st.session_state.YS_resim_yolu = st.text_input(
    #             "Resim Yolu (Opsiyonel)",
    #             placeholder="Örnek: /images/question1.png",
    #             key="YSK_resim_yolu",
    #         )
    
 

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
    
        # Ana kategori, alt kategori, soru metni, resim yolu ve notlar için session state tanımları
    # ============================================================================================
    st.session_state.setdefault("MS_secilen_ana_kategori", None)
    st.session_state.setdefault("MS_secilen_alt_kategori", None)    
    st.session_state.setdefault("MS_soru_metni", None)    
    st.session_state.setdefault("MS_resim_yolu", None)    
    st.session_state.setdefault("MS_notlar", None)
    st.session_state.setdefault("MS_Etiketler", None)

    st.session_state.setdefault("MS_son_ana_kategori", "0")
    st.session_state.setdefault("MS_son_alt_kategori", "0")
    st.session_state.setdefault("MS_sorular_gosterilsin", False)

    # Kategori seçim alanları için kolon düzeni
    # ============================================================================================
    col1, col2 , col3 = st.columns([1, 1, 1])

    # Ana kategori seçimi
    with col1:
        with st.container(border=True, vertical_alignment="center", height="stretch"):
            st.session_state.MS_secilen_ana_kategori = st.radio(
                "Ana Kategori",
                ["All"] + dla_ana_kategori_listesi(),
                key="MSK_ana_kategori_radio",
            )

    # Alt kategori seçimi
    with col2:
        with st.container(border=True, vertical_alignment="center", height="stretch"):
                
            if st.session_state.MS_secilen_ana_kategori == "All":
            
                st.session_state.MS_secilen_alt_kategori = st.selectbox(
                "Alt Kategori",
                ["All"],
                key="MSK_alt_kategori_selectbox"
                )
            
            else:
                
                alt_kategoriler1 = dla_alt_kategorileri_getir(st.session_state.MS_secilen_ana_kategori)

                st.session_state.MS_secilen_alt_kategori = st.selectbox(
                "Alt Kategori",
                ["All"] + alt_kategoriler1,
                key="MSK_alt_kategori_selectbox"
                )
    
    #Son ana kategori ve alt kategori değerlerini kontrol et, değişiklik varsa soruları gösterme durumunu kapat  
    # ============================================================================================
     
    if (
        st.session_state.MS_son_ana_kategori != st.session_state.MS_secilen_ana_kategori
        or st.session_state.MS_son_alt_kategori != st.session_state.MS_secilen_alt_kategori
        ):
            st.session_state.MS_sorular_gosterilsin = False
            st.session_state.MS_son_ana_kategori = st.session_state.MS_secilen_ana_kategori
            st.session_state.MS_son_alt_kategori = st.session_state.MS_secilen_alt_kategori

    #============================================================================================

    # Butona basılınca seçimi kaydet
    with col3:
        with st.container(border=True, vertical_alignment="center", height="stretch"):
            sorugetir = st.button("Soruları Getir", key="MSK_soru_getir_btn")
    


    if sorugetir:
        st.session_state.MS_sorular_gosterilsin = True

    if st.session_state.MS_sorular_gosterilsin:

        st.write(f"Kontrol Edilen Ana Kategori: {st.session_state.MS_secilen_ana_kategori}")
        st.write(f"Kontrol Edilen Alt Kategori: {st.session_state.MS_secilen_alt_kategori}")

        # form_alani = st.container()

        # # VERİ ÇEK
        # # ===============================
    
        # rows = dla_sorulari_getir(ana_kategori=st.session_state.MS_secilen_ana_kategori, alt_kategori=st.session_state.MS_secilen_alt_kategori)
        # df = pd.DataFrame(rows.data)


        # #Eğer veri boş değilse tabloyu göster
        # #============================================================================================

        # if not df.empty:

        #     st.divider()
         
        #     #Gosterilecek kolonları belirle
        #     #============================================================================================
        #     if st.session_state.MS_secilen_ana_kategori == "All":
        #         gosterilecek_kolonlar = ["id", "AnaKategori", "AltKategori", "Soru", "Notlar", "ResimURL"]

        #     if st.session_state.MS_secilen_ana_kategori == "General":
        #         gosterilecek_kolonlar = ["id", "Soru"]

        #     if st.session_state.MS_secilen_ana_kategori == "Scenario":
        #         gosterilecek_kolonlar = ["id", "Soru"]

        #     if st.session_state.MS_secilen_ana_kategori == "PictureDescription":
        #         gosterilecek_kolonlar = ["id", "ResimURL"]


        #     event = st.dataframe(
        #         df[gosterilecek_kolonlar],
        #         use_container_width=True,
        #         hide_index=True,
        #         on_select="rerun",
        #         selection_mode="single-row",
        #         column_config={
        #             "id": st.column_config.NumberColumn("ID", width=20),
        #             }
        #         )
            
        #     if event.selection.rows:
        #         secili_index = event.selection.rows[0]
        #         secili_satir = df.iloc[secili_index]
        #         secili_id = secili_satir["id"]


        #     #ID İLE VERİLERİ ÇEK
        #     #============================================================================================
        #     satir = df[df["id"] == secili_id].iloc[0]

            
                
        #         #ıf ile session_state kontrolü yaparak sadece id değiştiğinde formu doldur
        #         if "Son_Id" not in st.session_state:
        #             st.session_state.Son_Id = secili_id

        #         if st.session_state.Son_Id != secili_id:
        #             st.session_state.Son_Id = secili_id
                
        #         if "Son_Ana_Kategori" not in st.session_state:
        #             st.session_state.Son_Ana_Kategori = satir["AnaKategori"]
        #         if st.session_state.Son_Ana_Kategori != satir["AnaKategori"]:
        #             st.session_state.Son_Ana_Kategori = satir["AnaKategori"]
                
        #         if "Son_Alt_Kategori" not in st.session_state:
        #             st.session_state.Son_Alt_Kategori = satir["AltKategori"]
                
        #         if st.session_state.Son_Alt_Kategori != satir["AltKategori"]:
        #             st.session_state.Son_Alt_Kategori = satir["AltKategori"]
                
        #         if "Son_Soru" not in st.session_state:
        #             st.session_state.Son_Soru = satir["Soru"]
                
        #         if st.session_state.Son_Soru != satir["Soru"]:
        #             st.session_state.Son_Soru = satir["Soru"]
                
        #         if "Son_Notlar" not in st.session_state:
        #             st.session_state.Son_Notlar = satir["Notlar"]
                
        #         if st.session_state.Son_Notlar != satir["Notlar"]:
        #             st.session_state.Son_Notlar = satir["Notlar"]
                
        #         if "Son_ResimURL" not in st.session_state:
        #             st.session_state.Son_ResimURL = satir["ResimURL"]
                
        #         if st.session_state.Son_ResimURL != satir["ResimURL"]:
        #             st.session_state.Son_ResimURL = satir["ResimURL"]
                

        #         # ===============================
        #         # ÜST FORMU BURADA DOLDUR
        #         # Ama ekranda yukarıda görünür
        #         # ===============================

        #         with form_alani:

        #             st.subheader("Seçili Soruyu Düzenle")

        #             col1, col2, col3, col4 = st.columns([1, 2, 2, 2])

        #             with col1:
        #                 t_id = st.text_input(
        #                     "ID",
        #                     key="MSK_edit_id",
        #                     disabled=True,
        #                     value=st.session_state.Son_Id
        #                 )

        #             with col2:
        #                 t_ana_kategori = st.text_input(
        #                     "Ana Kategori",
        #                     value=st.session_state.Son_Ana_Kategori,
        #                     key="MSK_edit_ana_kategori"
        #                 )

        #             with col3:
        #                 t_alt_kategori = st.text_input(
        #                     "Alt Kategori",
        #                     value=st.session_state.Son_Alt_Kategori,
        #                     key="MSK_edit_alt_kategori"
        #                 )

        #             with col4:
        #                 t_pic = st.text_input(
        #                     "Resim URL",
        #                     value=st.session_state.Son_ResimURL,
        #                     key="MSK_edit_pic"
        #                 )

        #             t_soru = st.text_area(
        #                 "Soru",
        #                 value=st.session_state.Son_Soru,
        #                 key="MSK_edit_soru",
        #                 height=120
        #             )

        #             t_not = st.text_area(
        #                 "Notlar",
        #                 value=st.session_state.Son_Notlar,
        #                 key="MSK_edit_not",
        #                 height=100
        #             )
