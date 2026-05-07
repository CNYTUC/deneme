# KUTUPHANELER
import streamlit as st
import pandas as pd

# UTILS import


import Yardimci_Fonksiyonlar as Yfonk
import supabaseFonksiyon as SpFonk



# YENİ ETİKETLER
# ============================================================================================
st.session_state.YE_YeniEtiketler_list = SpFonk.dla_etiketler_DF()

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
        
        Yeni_Soru_Alan = st.empty()
    
 

    
    
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


Yfonk.Yeni_Soru_Alan_Doldur(Yeni_Soru_Alan)
Yfonk.Yeni_Etiket_Alan_Doldur(Mevcut_Etiket_Alan)