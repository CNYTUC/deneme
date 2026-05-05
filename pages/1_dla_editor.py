# IMPORTLAR
# ============================================================================================
import streamlit as st
import pandas as pd
from io import BytesIO
#text
from utils.text_utils import tr_to_en_lower
from utils.text_utils import ilk_harf_buyuk
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
    

# TEKRAR EDEN FONKSIYONLAR
# ============================================================================================
def VeriTabaniEtiketler_doldur():

    # Kayıtları Getir       
    # ===========================================           
    Kayitlar = dla_etiketler_getir()
    st.session_state.VT_Etiketler_df = pd.DataFrame(Kayitlar)

def VeriTabaniSorular_doldur():

    # Kayıtları Getir       
    # ===========================================           
    Kayitlar = dla_sorulari_getir()
    st.session_state.VT_Sorular_df = pd.DataFrame(Kayitlar)

# Session State Oluştur
# ============================================================================================  
ssElamanlar = {
        "VT_Etiketler_df": pd.DataFrame,
        "VT_Sorular_df": pd.DataFrame,
        "VT_ana_kategoriler_list": list,

        # TAB1 : YENI ETIKETLER
        "YE_YeniEtiketler_list": list,

        # TAB 3 : YENİ SORU EKLEME
        "YS_etiketler_listesi": list,
        "YS_secilen_ana_Kategori": str,
        "YS_resim_yolu": str,
        "YS_soru_metni": str,
        "YS_notlar": str,

    }

session_olustur(ssElamanlar)

# VT_ana_kategoriler_list = ["General","Scenario","PictureDescription"]
VT_ana_kategoriler_list = dla_ana_kategori_listesi()




#         "YS_vt_sorular_df": pd.DataFrame,

#         
#     }
#     session_olustur(ssElamanlar)

with tab1:
         
    # TAB1.BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Yeni Etiket Ekle 🏷️",divider="green")

    # ETİKET EKLEME FORMU OLUSTUR
    # ============================================================================================
    with st.form("Etiket_ekleme_formu", clear_on_submit=True):
        
        
        # KOLONLARI OLUSTUR
        # ===========================================
        col1, col2 = st.columns([5, 1])

        with col1:
            


            # # SADECE ETIKET LISTESI OLUSTUR
            # # ===========================================      
            # sadece_etiket_listesi:list = []       
            # if not vt_etiketler.empty:
            #     sadece_etiket_listesi = vt_etiketler["Etiket"].dropna().unique().tolist()


            # YENI ETIKET ICIN *** MULTISELECT *** OLUSTUR
            # ===========================================
            with st.container(border=True,vertical_alignment="center",height="stretch"):
                st.session_state.YE_YeniEtiketler_list = st.multiselect(
                    "Etiket Adı",
                    options=[],
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

            Islenecek_Etiketler = st.session_state.YE_YeniEtiketler_list.copy()

            # etiketler boş bırakılamaz
            if not Islenecek_Etiketler:
                st.warning("Etiket / Etiketler boş bırakılamaz.")
                st.stop()

            # ETİKETLERİ GETİR VE SESSION ATAMASI
            # ============================================================================================      

            # 1. Mevcut etiketleri bir kez çek ve hız için bir "set" (küme) yapısına dönüştür
            VeriTabaniEtiketler_doldur() 
            mevcut_etiketler_seti = set(st.session_state.VT_Etiketler_df["Etiket"].dropna().unique())

            # 2. İşlenecek etiketleri benzersiz hale getir (liste içinde aynı isim varsa elenir)
            benzersiz_yeni_etiketler = set(tr_to_en_lower(e) for e in Islenecek_Etiketler)

            # info
            yeni_etiket_sayisi = 0
            ayni_etiket_sayisi = 0

            for etiket in benzersiz_yeni_etiketler:
                # 3. Sadece veritabanında gerçekten yoksa ekle
                if etiket not in mevcut_etiketler_seti:
                    dla_etiket_ekle(etiket)
                    # 4. (Opsiyonel) Eklenen etiketi sete ekle ki aynı döngüde tekrar kontrol edilmesin
                    mevcut_etiketler_seti.add(etiket)
                    yeni_etiket_sayisi += 1
                else:
                    ayni_etiket_sayisi += 1


            # mesaj
            if yeni_etiket_sayisi > 0: st.success(f"Eklenen etiketler: {yeni_etiket_sayisi}", icon="✅")
            if ayni_etiket_sayisi > 0: st.error(f"Eklenmeyen!!! sistemdeki etiketler: {ayni_etiket_sayisi}", icon="🚨")

            # Formu temizle
            session_resetle("YE_", ssElamanlar)
        
                

with tab2: 
    

    # TAB2.BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Mevcut Etiketler 🔖",divider="rainbow")
    
    
    # Kayıtları Getir       
    # =========================================== 
    VeriTabaniEtiketler_doldur() 
    vt_etiketler = st.session_state.VT_Etiketler_df.copy()
    
    
    # DIŞ CONTAINER OLUSTUR
    # ============================================================================================
    with st.container(border=True,vertical_alignment="center",height="stretch"):
        
        #EĞER KAYIT YOKSA BILGI VER
        if vt_etiketler.empty:
            st.info("Herhangi bir etiket bulunamadı.")
        else:

            st.write(len(vt_etiketler), "tane etiket bulundu." )
    
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
                    
                    filtered_df = vt_etiketler.copy()

                    if search_text:
                        filtered_df = filtered_df[
                            filtered_df["Etiket"].str.contains(search_text, case=False, na=False)
                        ]



                    # ETİKET ALANI
                    # ============================================================================================

                    # Seçim kolonu ekle
                    if "sec" not in vt_etiketler.columns:
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


    # COL1 CONTAINER OLUSTUR
    # ============================================================================================
    with st.container(border=True, vertical_alignment="center", height="stretch"):
            
        
        # Ana kategori seçimi
        # ============================================================================================  
        with st.container(border=True, vertical_alignment="center", height="stretch"):
            
            AK = st.radio(
                "Ana Kategori",
                VT_ana_kategoriler_list,
                key="YSK_ana_kategori",
                horizontal=True
            )

            #Önerme Yaz
            if AK == "PictureDescription":
                st.write("Gereklilikler: En az 1 Etiket, Sadece 1 Soru metni ve 1 Resim yolu.")
            else:
                st.write("Gereklilikler: En az 1 Etiket, Soru metni.")

            st.session_state.YS_secilen_ana_Kategori = AK


        # Etiketler girişi
        # ============================================================================================
             
        # Kayıtları Getir       
        # =========================================== 
        # 1. Mevcut etiketleri bir kez çek ve hız için bir "set" (küme) yapısına dönüştür
        VeriTabaniEtiketler_doldur() 
        mevcut_etiketler_seti = set(st.session_state.VT_Etiketler_df["Etiket"].dropna().unique())

        # 2. Etiketler seçme
        with st.container(border=True, vertical_alignment="center", height="stretch"):
            
            tags = st.multiselect(
                "Etiketlerinizi seçin",
                options=mevcut_etiketler_seti,
                max_selections=20,
                accept_new_options=True,
                placeholder="Etiketlerinizi seçin !!!",
                key="YSK_etiketler0",
                )
                    
            st.session_state.YS_etiketler_listesi = tags
            
            # Etiketleri yazdır
            st.write(tr_to_en_lower(", ".join(st.session_state.YS_etiketler_listesi)))



        # RESİM YOLU GİRİŞİ
        # ============================================================================================
        if st.session_state.YS_secilen_ana_Kategori == "PictureDescription":
            
            with st.container(border=True, vertical_alignment="center", height="stretch"):
                
                st.session_state.YS_resim_yolu = st.text_input(
                "Resim Yolu",
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
                "Notlar (Opsiyonel)",
                placeholder="Örnek: Bu soru tercihleri ölçmek için kullanılır.",
                key="YSK_notlar",
                )


        # Kaydet butonu ve doğrulama
        # ============================================================================================
        if st.button("Kaydet", key="YSK_kaydet_buton"):

            # Etiketler yoksa
            if not st.session_state.YS_etiketler_listesi:
                st.warning(f"{st.session_state.YS_secilen_ana_Kategori} kategorisinde en az bir etiket seçmelisiniz.", icon="⚠️")
                st.stop()

            # Soru metni yoksa
            if not st.session_state.YS_soru_metni:
                st.warning(f"{st.session_state.YS_secilen_ana_Kategori} kategorisinde soru metni yazmalısınız.", icon="⚠️")
                st.stop()

            # Resim yolu boşsa
            if st.session_state.YS_secilen_ana_Kategori == "PictureDescription" and not st.session_state.YS_resim_yolu.split(): 
                st.warning(f"{st.session_state.YS_secilen_ana_Kategori} kategorisinde resim yolu boş bırakılamaz.", icon="⚠️") 
                st.stop()

            # Resim Soru Metni 
            if st.session_state.YS_secilen_ana_Kategori == "PictureDescription" and len(st.session_state.YS_soru_metni.splitlines()) != 1:          
                st.warning(f"{st.session_state.YS_secilen_ana_Kategori} kategorisinde bir tane soru metni olmalıdır.") 
                st.stop()
            

            # Soru Ekle
            # ============================================================================================
            # 1. Mevcut etiketleri bir kez çek ve hız için bir "set" (küme) yapısına dönüştür
            VeriTabaniSorular_doldur() 
            mevcut_sorular_seti = set(st.session_state.VT_Etiketler_df["Soru"].dropna().unique())
            df_sorular = st.session_state.VT_Sorular_df


            #Yeni Soruların Idleri
            # ===========================================
            Eklenen_secilen_soru_id_listesi: list = []


            # Yeni Soruların Metnleri
            # ===========================================
            for soru in st.session_state.YS_soru_metni.splitlines():

                # Soruyu formatla
                soru = ilk_harf_buyuk(tr_to_en_lower(soru.strip()))


                # Soru boşsa
                if soru == "": continue

                if soru not in mevcut_sorular_seti:

                    yeni_soru = dla_soru_ekle(
                        st.session_state.YS_secilen_ana_Kategori,
                        soru,
                        st.session_state.YS_notlar,
                        st.session_state.YS_resim_yolu
                    )
                    
                    if yeni_soru.data:
                        Eklenen_secilen_soru_id_listesi.append(yeni_soru.data["id"])
                        mevcut_sorular_seti.add(soru)
                    else:
                        st.error(yeni_soru.error)

                else:

                    Eklenen_secilen_soru_id_listesi.append(df_sorular[df_sorular["Soru"] == soru]["id"].iloc[0]) 



            st.success(f"{len(Eklenen_secilen_soru_id_listesi)} soru işlendi.", icon="✅")



#                 # Etiket Ekle
#                 # ============================================================================================

#                  #Yeni Etikertlerin Idleri
#                 # ===========================================
#                 Eklenen_secilen_etiket_id_listesi: list = []

#                 # Yeni Etiketler
#                 # ===========================================
#                 for etiket in st.session_state.YS_etiketler_listesi:

#                     # Etiketi formatla
#                     NewTag = tr_to_en_lower(soru.strip())

#                     # Etiket boşsa
#                     if NewTag == "":
#                         continue


#                     # Etiketleri Getir       
#                     # ===========================================  

#                     Vt_Etiketler = dla_etiketler_getir()
#                     st.session_state.YS_vt_etiketler_df = pd.DataFrame(Vt_Etiketler.data)    
                        
#                     #eğer veri tabanında kayıt yoksa;
#                     if st.session_state.YS_vt_etiketler_df.empty:
#                         st.session_state.YS_vt_etiketler_df = pd.DataFrame(columns=["id", "Etiket"])
                        

#                     df_etiketler = st.session_state.YS_vt_etiketler_df.copy()


#                     # Yeni etiket veri tabanında var mı?
#                     # ===========================================
#                     if not df_etiketler[df_etiketler["Etiket"] == NewTag].empty:
                        
#                         etiket_id = df_etiketler.loc[df_etiketler["Etiket"] == NewTag, "id"].item()
                    
#                     else:

#                         yeni_etiket = dla_etiket_ekle(NewTag)

#                         if yeni_etiket.data:
#                             etiket_id = yeni_etiket.data[0]["id"]
#                         else:
#                             st.error("Soru eklenirken bir hata oluştu veya ID dönmedi.")

                    
#                     Eklenen_secilen_etiket_id_listesi.append(etiket_id)


#                 st.success(f"{len(Eklenen_secilen_etiket_id_listesi)} etiket işlendi.", icon="✅")


#                 # Sorular ile Etiketleri Ekle
#                 # ===========================================
#                 for soruID in Eklenen_secilen_soru_id_listesi:
                    
#                     if soruID in [None, ""]:
#                         continue

#                     for etiketID in Eklenen_secilen_etiket_id_listesi:
                        
#                         if etiketID in [None, ""]:
#                             continue
                    
#                         dla_soru_ve_etiket_ekle(soruID, etiketID)


#                 st.success(f"{len(Eklenen_secilen_etiket_id_listesi)} etiket ile {len(Eklenen_secilen_soru_id_listesi)} soru işlendi.", icon="✅")

#                 # Formu temizle
#                 session_resetle("YS_", ssElamanlar)

















with tab4:
    
    # TAB4.BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Mevcut Sorular 📖",divider="red")

    
    
    