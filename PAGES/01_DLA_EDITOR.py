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
    
    # DEĞİŞKENLER
    # ============================================================================================

    Ana_kategoriler = am.DLA_Ana_Kategori_ss()
    Secilen_ana_kategori: str = ""

    Vt_Etiketler: pd.DataFrame = am.DLA_Etiketler_ss()
    mevcut_etiketler_seti = set(Vt_Etiketler["Etiket"].dropna().unique())

    
    # DIŞ CONTAINER OLUSTUR
    # ============================================================================================
    with st.container(border=True,vertical_alignment="center",height="stretch"):
        
        # Ana kategori seçimi
        # ============================================================================================  
        with st.container(border=True, vertical_alignment="center", height="stretch"):

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


        # Etiketler girişi
        # ============================================================================================
        with st.container(border=True, vertical_alignment="center", height="stretch"):

            # 1. Etiketler seçme
            # ============================================================================================            
            secilen_etiketler = st.multiselect(
                "Etiketlerinizi seçin",
                options=mevcut_etiketler_seti,
                max_selections=20,
                accept_new_options=True,
                placeholder="Etiketlerinizi seçin !!!",
                key="YSK_etiketler0",
                )
                    
            # Etiketleri yazdır
            st.write(am.tr_to_en_lower(" ".join(secilen_etiketler)))
    
 
    
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


# icerik.Yeni_Soru_Alan_Doldur(Yeni_Soru_Alan)
