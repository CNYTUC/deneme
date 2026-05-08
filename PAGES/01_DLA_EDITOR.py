# KUTUPHANELER
import streamlit as st
import pandas as pd
from io import BytesIO

import UTILS.ara_module as am

# BAŞLIK
# ============================================================================================
st.header("D.L.A. Editörü 🤠")

# SAYFA YAPISI OLUSTUR
# ============================================================================================
Yeni_Soru, Mevcut_Soru, Mevcut_Etiketler = st.tabs(["❓ Yeni Soru", "📖 Mevcut Sorular", "🔖 Mevcut Etiketler"])    

# YENİ SORU EKLEME
# ============================================================================================
with Yeni_Soru:   
    
    # ALT BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Yeni Soru Ekle ❓",divider="yellow")
        
    # DIŞ CONTAINER OLUSTUR
    # ============================================================================================
    with st.container(border=True,vertical_alignment="center",height="stretch"):
        

        # Ana kategori seçimi
        # ============================================================================================  
        with st.container(border=True, vertical_alignment="center", height="stretch"):

            # DEĞİŞKENLER
            Ana_kategoriler = am.DLA_Ana_Kategori_ss()

            Secilen_ana_kategori = st.radio(
                "Ana Kategori",
                options=Ana_kategoriler,
                key="YSK_ana_kategori",
                horizontal=True
            )

            #Önerme Yaz
            if Secilen_ana_kategori == "PictureDescription":
                # st.write(f"'{Secilen_ana_kategori}' için Gereklilikler: En az 1 Etiket, Sadece 1 Soru metni ve 1 Resim yolu.")
                st.markdown(f"**<span style='color:red'>{Secilen_ana_kategori}</span>** için Gereklilikler: En az 1 Etiket, Soru metni ve 1 Resim yolu.", unsafe_allow_html=True)
            else:
                # st.write(f"'{Secilen_ana_kategori}' için Gereklilikler: En az 1 Etiket, Soru metni.")
                st.markdown(f"**<span style='color:red'>{Secilen_ana_kategori}</span>** için Gereklilikler: En az 1 Etiket, Soru metni.", unsafe_allow_html=True)

        # Session'a kaydet
        st.session_state.Dla_Secilen_Ana_Kategori_Str = Secilen_ana_kategori
        

        # Soru metni ve notlar için geniş bir alan
        # ============================================================================================
        
        # DEĞİŞKENLER
        Yeni_Soru_Metni: str = ""
        Secilen_ana_kategori: str = st.session_state.Dla_Secilen_Ana_Kategori_Str

        with st.container(border=True, vertical_alignment="center", height="stretch"):

            if Secilen_ana_kategori == "PictureDescription":

                Yeni_Soru_Metni = st.text_area(
                    "Soru Metni",
                    placeholder="Describe The Picture",
                    height=100,
                    value="Describe The Picture",
                    disabled=True,
                    )

            else:

                Yeni_Soru_Metni = st.text_area(
                    "Soru Metni",
                    placeholder="Her satıra ayrı bir soru yazın.",
                    height=100,
                    key="YSK_soru_metni",
                    )
            
            #Önerme Yaz
            i=0

            if Yeni_Soru_Metni.strip() == "":
                st.session_state.Dla_Secilen_Soru_Metni_Str = ""
                st.warning("Soru metni boş bırakılamaz. En az 1 soru metni girmelisiniz.")    
            else:
                
                #atama
                st.session_state.Dla_Secilen_Soru_Metni_Str = Yeni_Soru_Metni

                for soru in st.session_state.Dla_Secilen_Soru_Metni_Str.splitlines():
                    i+=1

                st.success(f"{i} soru metni girdiğiniz görünüyor.")   


        # Etiketler girişi
        # ============================================================================================
        Secilen_ana_kategori = st.session_state.Dla_Secilen_Ana_Kategori_Str
        if not Secilen_ana_kategori == "PictureDescription":
        
            with st.container(border=True, vertical_alignment="center", height="stretch"):
                
                # DEĞİŞKENLER
                Vt_Etiketler: pd.DataFrame = am.DLA_Etiketler_ss()
                mevcut_etiketler_seti = set(Vt_Etiketler["Etiket"].dropna().unique())
                
                secilen_etiketler = st.multiselect(
                    "Etiketlerinizi seçin",
                    options=mevcut_etiketler_seti,
                    max_selections=20,
                    accept_new_options=True,
                    placeholder="Etiketlerinizi seçin !!!",
                    key="YSK_etiketler",
                    )
                    
                # Session'a kaydet
                st.session_state.Dla_Secilen_Etiketler_List = secilen_etiketler

                #Önerme Yaz
                if st.session_state.Dla_Secilen_Etiketler_List:
                    st.success(am.tr_to_en_lower(" ".join(st.session_state.Dla_Secilen_Etiketler_List)))

        # Resim yolu girişi (yalnızca PictureDescription için)
        # ============================================================================================
        with st.container(border=True, vertical_alignment="center", height="stretch"):
            
            # DEĞİŞKENLER
            Secilen_ana_kategori: str = st.session_state.Dla_Secilen_Ana_Kategori_Str
            Secilen_resim_yolu: str = ""

            if Secilen_ana_kategori == "PictureDescription":
                
                with st.container(border=True, vertical_alignment="center", height="stretch"):
                    
                    Secilen_resim_yolu = st.text_input(
                    "Resim Yolu",
                    placeholder="Örnek: /images/question1.png",
                    key="YSK_resim_yolu",
                    )
            
            # Session'a kaydet
            st.session_state.Dla_Secilen_Resim_Yolu_Str = Secilen_resim_yolu



        # Notlar alanı
        # ============================================================================================

        with st.container(border=True, vertical_alignment="center", height="stretch"):
            
            # DEĞİŞKENLER
            SecilenNotlar: str = ""

            SecilenNotlar = st.text_area(
                "Notlar (Opsiyonel)",
                placeholder="Örnek: Bu soru tercihleri ölçmek için kullanılır.",
                key="YSK_notlar",
                )

                #atama
            st.session_state.Dla_Secilen_Notlar_Str = SecilenNotlar

# # MEVCUT SORULAR
# # ============================================================================================
# with Mevcut_Soru:

#     # ALT BAŞLIK BELİRLE
#     # ============================================================================================
#     st.subheader(f"Mevcut Etiketler 🔖",divider="rainbow")

#     # DIŞ CONTAINER OLUSTUR
#     # ============================================================================================
#     with st.container(border=True,vertical_alignment="center",height="stretch"):
        
#         Mevcut_Soru_Alan = st.empty()
    
# # MEVCUT ETİKETLER
# # ============================================================================================
# with Mevcut_Etiketler:

#     # ALT BAŞLIK BELİRLE
#     # ============================================================================================
#     st.subheader(f"Mevcut Sorular 📖",divider="red")

#     # DIŞ CONTAINER OLUSTUR
#     # ============================================================================================
#     with st.container(border=True,vertical_alignment="center",height="stretch"):
        
#         Mevcut_Etiket_Alan = st.empty()
