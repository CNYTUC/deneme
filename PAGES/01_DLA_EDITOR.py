# KUTUPHANELER
import streamlit as st
import pandas as pd

# UTILS import
from UTILS.text_utils import slow_print
from UTILS.text_utils import trim_text
from UTILS.time_utils import wait
from UTILS.session_utils import session_olustur

# Session State Oluştur
# ============================================================================================  
# ============================================================================================  
ssElamanlar = {
        "VT_Etiketler_df": pd.DataFrame,
        "VT_Sorular_df": pd.DataFrame,
        "VT_ana_kategoriler_list": list
    }

session_olustur(ssElamanlar)

# SAYFA YAPISI OLUSTUR
# ============================================================================================
Yeni_Soru, Mevcut_Soru, Mevcut_Etiketler = st.tabs(["❓ Yeni Soru", "📖 Mevcut Sorular", "🔖 Mevcut Etiketler"])    


# YENİ SORU EKLEME
# ============================================================================================
with Yeni_Soru:
    st.write("Yeni Soru Ekleme")


# MEVCUT SORULAR
# ============================================================================================
with Mevcut_Soru:
    st.write("Mevcut Sorular")


# MEVCUT ETİKETLER
# ============================================================================================
with Mevcut_Etiketler:
    st.write("Mevcut Etiketler")

    