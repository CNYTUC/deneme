import streamlit as st
import pandas as pd

# KÜTÜPHANELER
import UTILS.session_utils as SsnFonk

#====================================================================================
# SESSION STATE OLUŞTUR
#============================================================================================

def sessionOlustur():
    ssElamanlar = {

        "Ana_kategoriler_list": list,
        "VT_Dla_Etiketler_df": pd.DataFrame,

    }

    SsnFonk.session_olustur(ssElamanlar)


#====================================================================================
# ANA KATEGORILER OLUŞTUR
#============================================================================================

def anaKategorilerOlustur():
    st.session_state.Ana_kategoriler_list = ["General", "Scenario", "PictureDescription"]


#====================================================================================
# NAVIGASYON OLUSTUR
#============================================================================================

def navigasyonOlustur():

    pages = {
    
    "MAIN": [
        st.Page("main.py", title="Main", icon="🏠")
        
    ],     
    "DLA KATEGORİSİ": [
        st.Page("PAGES/01_DLA_EDITOR.py", title="D.L.A. Editör", icon="📝"),
        st.Page("PAGES/02_DLA_EXAM.py", title="D.L.A. Exam", icon="🎤")

    ],     
    "REC KATEGORİSİ": [
        st.Page("PAGES/03_REC_EDITOR.py", title="R.E.C. Editör", icon="📝"),
        st.Page("PAGES/04_REC_EXAM.py", title="R.E.C. Exam", icon="📚")

    ],    
    }

    pg = st.navigation(pages, position="top")
    pg.run()
