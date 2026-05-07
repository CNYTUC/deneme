# KUTUPHANELER
import streamlit as st
import pandas as pd
from io import BytesIO

# UTILS import
import UTILS.session_utils as SsnFonk
import UTILS.supabaseFonksiyon as SpFonk
import UTILS.text_utils as TxtFonk
import UTILS.time_utils as TimeFonk

# İCERİK import
import icerikler as icerik

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
    Ana_kategoriler = st.session_state.Ana_kategoriler_list
    Secilen_ana_kategori: str = ""

    # DIŞ CONTAINER OLUSTUR
    # ============================================================================================
    with st.container(border=True,vertical_alignment="center",height="stretch"):
        
        # Ana kategori seçimi
        # ============================================================================================  
        # with st.container(border=True, vertical_alignment="center", height="stretch"):


        Secilen_ana_kategori = st.radio(
            "Ana Kategori",
            options=Ana_kategoriler,
            key="YSK_ana_kategori",
            horizontal=True
        )

        #Önerme Yaz
        if Secilen_ana_kategori == "PictureDescription":
            st.write("Gereklilikler: En az 1 Etiket, Sadece 1 Soru metni ve 1 Resim yolu.")
        else:
            st.write("Gereklilikler: En az 1 Etiket, Soru metni.")

        # st.write(Secilen_ana_kategori)


        # Etiketler girişi
        # ============================================================================================

        VT_ETIKETLER = SpFonk.dla_etiketler_DF()
        mevcut_etiketler_seti = set(VT_ETIKETLER["Etiket"].dropna().unique())
        YS_ETIKETLER: list = []
        
        # 1. Etiketler seçme
        # with st.container(border=True, vertical_alignment="center", height="stretch"):
            
        YS_ETIKETLER = st.multiselect(
            "Etiketlerinizi seçin",
            options=mevcut_etiketler_seti,
            max_selections=20,
            accept_new_options=True,
            placeholder="Etiketlerinizi seçin !!!",
            key="YSK_etiketler0",
            )
                
        # Etiketleri yazdır
        st.write(TxtFonk.tr_to_en_lower(", ".join(YS_ETIKETLER)))
    
 

    
    
# MEVCUT SORULAR
# ============================================================================================
with Mevcut_Soru:

    # ALT BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Mevcut Etiketler 🔖",divider="rainbow")

    # DIŞ CONTAINER OLUSTUR
    # ============================================================================================
    with st.container(border=True,vertical_alignment="center",height="stretch"):
        
        Mevcut_Soru_Alan = st.empty()
    
# MEVCUT ETİKETLER
# ============================================================================================
with Mevcut_Etiketler:

    # ALT BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Mevcut Sorular 📖",divider="red")

    # DIŞ CONTAINER OLUSTUR
    # ============================================================================================
    with st.container(border=True,vertical_alignment="center",height="stretch"):
        
        Mevcut_Etiket_Alan = st.empty()


# icerik.Yeni_Soru_Alan_Doldur(Yeni_Soru_Alan)
