# IMPORTLAR
# ============================================================================================
import streamlit as st
import pandas as pd
from io import BytesIO
#text
from utils.text_utils import tr_to_en_lower
#zaman
from utils.time_utils import wait
#session
from utils.session_utils import session_olustur
from utils.session_utils import session_resetle

#supabase
from supabaseFonksiyon import (
    dla_ana_kategori_listesi,
    dla_etiket_ekle,
    dla_etiketler_getir,
    dla_etiket_guncelle,
    dla_etiket_sil,
    
    dla_soru_ekle,
    dla_sorulari_getir,
    dla_soru_ve_etiket_ekle,

)
# ============================================================================================


# BAŞLIK
# ============================================================================================
st.header("D.L.A. Editörü 🤠")


# TAB PANEL OLUSTUR
# ============================================================================================
tab1, tab2, tab3, tab4 = st.tabs(["🏷️ Yeni Etiket", "🔖 Mevcut Etiketler", "❓ Yeni Soru", "📖 Mevcut Sorular"])    
    
    
with tab1:
    
    # Session State Oluştur
    # ============================================================================================  
    ssElamanlar = {
        "YE_vt_kayitlar_df": pd.DataFrame,
        "YE_etiketler": str
    }
    session_olustur(ssElamanlar)
 
    
        
    # TAB1.BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Yeni Etiket Ekle 🏷️",divider="green")

        # Kayıtları Getir       
        # ===========================================  
          
    Kayitlar = dla_etiketler_getir()
    st.session_state.YE_vt_kayitlar_df = pd.DataFrame(Kayitlar.data)      
    
        # Sadece etiketleri getir
        # ===========================================
        
    veri_tabani_etiketleri = []       
    if not st.session_state.YE_vt_kayitlar_df.empty:
        veri_tabani_etiketleri = st.session_state.YE_vt_kayitlar_df["Etiket"].dropna().unique().tolist()
        
        
    # 2.ETİKET EKLEME FORMU OLUSTUR
    # ============================================================================================
    with st.form("Etiket_ekleme_formu", clear_on_submit=True):
        
        
        # KOLONLARI OLUSTUR
        # ===========================================
        col1, col2 = st.columns([5, 1])

        with col1:
            
            # YENI ETIKET ICIN *** MULTISELECT *** OLUSTUR
            # ===========================================
            with st.container(border=True,vertical_alignment="center",height="stretch"):
                st.session_state.YE_etiketler = st.multiselect(
                    "Etiket Adı",
                    options=veri_tabani_etiketleri,
                    max_selections=20,
                    accept_new_options=True,
                    placeholder="Henüz etiket yok...",
                    key="YEK_etiket_input"
                    )
        

        with col2:
            
            # YENI ETIKET ICIN *** KAYDET BUTTON *** OLUSTUR
            # ===========================================
            with st.container(border=True,vertical_alignment="center",height="stretch"):
                kaydet = st.form_submit_button("Kaydet")


        # KAYDET BUTONA BASILIRSA
        # ===========================================
        if kaydet:
                    
            if st.session_state.YE_etiketler == []:
                st.warning("Etiket / Etiketler boş bırakılamaz.")

            else:
            
                #Etiketleri Kaydet
                # ============================================================================================
                yeni_etiket_sayisi = 0
                ayni_etiket_sayisi = 0

                for Tag in st.session_state.YE_etiketler:

                    Yeni_Eklenecek_Etiket = tr_to_en_lower(Tag.strip())

                    if not Yeni_Eklenecek_Etiket in veri_tabani_etiketleri:
                        dla_etiket_ekle(Yeni_Eklenecek_Etiket)
                        yeni_etiket_sayisi += 1
                    else:
                        ayni_etiket_sayisi += 1


                if yeni_etiket_sayisi > 0: st.success(f"Eklenen etiketler: {yeni_etiket_sayisi}", icon="✅")
                if ayni_etiket_sayisi > 0: st.error(f"Eklenmeyen!!! sistemdeki etiketler: {ayni_etiket_sayisi}", icon="🚨")
                
                #3 saniye bekle
                wait(3)

                # Formu temizle
                session_resetle("YE_", ssElamanlar)
                
                
                
                
with tab2: 
    
    
    # Session State Oluştur
    # ============================================================================================  
    ssElamanlar = {
        "ME_vt_kayitlar_df": pd.DataFrame,
    }
    session_olustur(ssElamanlar)
    
    # TAB2.BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Mevcut Etiketler 🔖",divider="rainbow")
    
    
    # Kayıtları Getir       
    # ===========================================  

    Kayitlar = dla_etiketler_getir()
    st.session_state.ME_vt_kayitlar_df = pd.DataFrame(Kayitlar.data)       
    
    # DIŞ CONTAINER OLUSTUR
    # ============================================================================================
    with st.container(border=True,vertical_alignment="center",height="stretch"):
        
        #EĞER KAYIT YOKSA BILGI VER
        if st.session_state.ME_vt_kayitlar_df.empty:
            st.info("Herhangi bir etiket bulunamadı.")
        else:
            
            # Kolonları olustur
            # ============================================================================================
            col1,col2 = st.columns([1,1])
            
            with col1:
                
                # COL1 CONTAINER OLUSTUR
                # ============================================================================================
                with st.container(border=True,vertical_alignment="center",height="stretch"):    
               
                    # Arama alanı
                    # ============================================================================================
                    search_text = st.text_input("🔍 Etiket Ara", placeholder="Etiket gir...")
                    search_text = tr_to_en_lower(search_text.strip())
                    
                    filtered_df = st.session_state.ME_vt_kayitlar_df.copy()

                    if search_text:
                        filtered_df = filtered_df[
                            filtered_df["Etiket"].str.contains(search_text, case=False, na=False)
                        ]

                    # ETİKET ALANI
                    # ============================================================================================

                    # Seçim kolonu ekle
                    if "sec" not in st.session_state.ME_vt_kayitlar_df.columns:
                        filtered_df.insert(0, "sec", False)


                    edited_df = st.data_editor(
                        filtered_df,
                        use_container_width=False,
                        hide_index=True,
                        row_height=42,
                        height=300,
                        
                        column_config={
                            
                            "sec": st.column_config.CheckboxColumn("SEC", width=100),
                            "id": None,  # 👈 BU SATIR KOLONU GİZLER
                            "Etiket": st.column_config.TextColumn("ETİKET", width=1000),
                            
                        },
                        
                        key="MEK_etiket_editor"
                    )

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

            with col2:
        
                #seçili satırları al
                secili_satirlar = edited_df[edited_df["sec"] == True] 
                
                
                updated_tag = ""

                # COL2 CONTAINER OLUSTUR
                # ============================================================================================
                with st.container(border=True,vertical_alignment="center",height="stretch"):    
                                       
                    # SINAMA 1
                    # ============================================================================================
                    if len(secili_satirlar) > 1:
                        st.warning("Lütfen sadece bir satır seç.", icon="⚠️")
                    
                    # SINAMA 2
                    # ============================================================================================    
                    elif len(secili_satirlar) < 1:
                        st.info("İşlem yapmak için tablodan bir satır seç.", icon="ℹ️")
                    
                    # İŞLEM
                    # ============================================================================================
                    else:
                        
                        # Tanımalamaları yap
                        #============================================================================================
                        selected_row = secili_satirlar.iloc[0]
                        selected_id = int(selected_row["id"])
                        selected_tag = tr_to_en_lower(selected_row["Etiket"])

                        #Seçilen ID ve Etiketi yazdır
                        st.info(f"Seçili ID: {selected_id}", icon="ℹ️")
                        
                        updated_tag = st.text_input(
                            "Seçili Etiket",
                            value=selected_tag,
                            disabled=False,
                            width="stretch"
                        )
                        
                        col1, col2 = st.columns(2)
                                
                        with col1:
                            
                            
                            #  GUNCELLE BUTONU
                            if st.button("💾 Seçili Etiketi Güncelle", use_container_width=True):
                                dla_etiket_guncelle(
                                    selected_id,
                                    tr_to_en_lower(updated_tag),
                                )
                                st.success("Etiket güncellendi.", icon="✅")
                                
                                # RESET
                                session_resetle("ME_", ssElamanlar)

                        with col2:

                            #  SIL BUTONU
                            if st.button("🗑️ Seçili Satırı Sil", use_container_width=True):
                                dla_etiket_sil(selected_id)
                                st.warning("Etiket silindi.", icon="⚠️")
                                
                                # RESET
                                session_resetle("ME_", ssElamanlar)
                    
    


with tab3:
    

    # TAB3.BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Yeni Soru Ekle ❓",divider="yellow")

    # Session State Oluştur
    # ============================================================================================  
    ssElamanlar = {
        "YS_ana_kategori": str,
        "YS_etiketler_listesi": list,
        "YS_soru_metni": str,
        "YS_resim_yolu": str,
        "YS_notlar": str,
    }
    session_olustur(ssElamanlar)
        
        
    with st.container(border=True, vertical_alignment="center", height="stretch"):
            
        
        # Ana kategori seçimi
        # ============================================================================================  
        with st.container(border=True, vertical_alignment="center", height="stretch"):
            
            st.session_state.YS_ana_kategori = st.radio(
                "Ana Kategori",
                dla_ana_kategori_listesi(),
                key="YSK_ana_kategori",
                horizontal=True
            )



        # Etiketler girişi
        # ============================================================================================
             
            # Kayıtları Getir       
            # ===========================================  

        Kayitlar = dla_etiketler_getir()
        st.session_state.YS_etiketler_listesi = pd.DataFrame(Kayitlar.data)    
        
            # Sadece etiketleri getir
            # ===========================================
        sadece_etiket_listesi = st.session_state.YS_etiketler_listesi["Etiket"].dropna().unique().tolist()

        with st.container(border=True, vertical_alignment="center", height="stretch"):
            
            tags = st.multiselect(
                "Etiketlerinizi seçin",
                options=sadece_etiket_listesi,
                max_selections=20,
                accept_new_options=True,
                key="YSK_etiketler0",
                )
                    
            st.session_state.YS_etiketler_listesi = tags
            
            # Etiketleri yazdır
            st.write(", ".join(st.session_state.YS_etiketler_listesi))



        # RESİM YOLU GİRİŞİ
        # ============================================================================================
        if st.session_state.YS_ana_kategori == "PictureDescription": # dla_ana_kategori_listesi[2]
            
            with st.container(border=True, vertical_alignment="center", height="stretch"):
                
                st.session_state.YS_resim_yolu = st.text_input(
                "Resim Yolu (Opsiyonel)",
                placeholder="Örnek: /images/question1.png",
                key="YSK_resim_yolu",
                )

        else:
            
            st.session_state.YS_resim_yolu = "" 


        # Soru metni ve notlar için geniş bir alan
        # ============================================================================================

        with st.container(border=True, vertical_alignment="center", height="stretch"):
            
            st.session_state.YS_soru_metni = st.text_area(
                "Soru Metni",
                placeholder="Her satıra ayrı bir soru yazın.",
                height=100,
                key="YSK_soru_metni",
                )
            
            
        # Notlar alanı
        # ============================================================================================

        with st.container(border=True, vertical_alignment="center", height="stretch"):
            
            st.session_state.YS_notlar = st.text_area(
                "Notlar",
                placeholder="Örnek: Bu soru tercihleri ölçmek için kullanılır.",
                key="YSK_notlar",
                )

        # Kaydet butonu ve doğrulama
        # ============================================================================================
        if st.button("Kaydet", key="YSK_kaydet_buton"):

            # Sınamalar
            # ============================================================================================
            if not st.session_state.YS_soru_metni: 
                st.warning("Soru metni boş bırakılamaz.", icon="⚠️")

            if not st.session_state.YS_etiketler_listesi:
                st.warning("Etiketler boş bırakılamaz.", icon="⚠️")

            if st.session_state.YS_ana_kategori == "PictureDescription":
                # resim yolu bos bırakılamaz
                if not st.session_state.YS_resim_yolu.split(): 
                    st.warning("Resim yolu boş bırakılamaz.")
                if len(st.session_state.YS_soru_metni.splitlines()) != 1:
                    st.warning("Soru metni PictureDescription kategorisinde bir tane olmalıdır.")

            else:

                # 1.Etiketleri Kaydet
                # ============================================================================================
            
                # Etiketleri Kaydet / ID listesini hazırla
                Kayitlar2 = st.session_state.YS_etiketler_listesi.copy()

                etiket_id_listesi = [""]

                # Etiketleri kaydet
                # ============================================================================================
                for tag in st.session_state.YS_etiketler_listesi:
                    
                    NTag = tr_to_en_lower(tag.strip())

                    mevcut = Kayitlar2[Kayitlar2["Etiket"] == NTag]

                    if mevcut.empty:
                            yeni_etiket = dla_etiket_ekle(NTag)
                            etiket_id = yeni_etiket.data[0]["id"]
                    else:
                            etiket_id = mevcut.iloc[0]["id"]

                    etiket_id_listesi.append(etiket_id)
                    
                        
                # Soruyu Kaydet
                # ============================================================================================
                eklenen_soru_sayisi = 0

                Soru_Liste = dla_sorulari_getir(st.session_state.YS_ana_kategori)

                for satir in st.session_state.YS_soru_metni.splitlines():
                    if satir.strip():
                        
                        NSoru = tr_to_en_lower(satir.strip())                   

                        mevcut = Soru_Liste[Soru_Liste["Soru"] == NSoru]

                        if  mevcut.empty:
                            
                            yeni_soru = dla_soru_ekle(
                                st.session_state.YS_ana_kategori,
                                NSoru,
                                st.session_state.YS_notlar,
                                st.session_state.YS_resim_yolu
                            )

                            eklenen_soru_sayisi += 1
                            soru_id = yeni_soru.data[0]["id"]

                            for etiket_id in etiket_id_listesi:
                                dla_soru_ve_etiket_ekle(soru_id, etiket_id)

                # Eklendi mesajı
                # ============================================================================================

                st.success(f"{eklenen_soru_sayisi} soru eklendi.", icon="✅")

                # Formu temizle
                session_resetle("YS_", ssElamanlar)


with tab4:
    
    # TAB4.BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Mevcut Sorular 📖",divider="red")

    
    
    