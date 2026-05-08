import streamlit as st
import pandas as pd

# KÜTÜPHANELER
import UTILS.session_utils as SsnFonk

#====================================================================================
# SESSION STATE OLUŞTUR
#============================================================================================
def tumSessionOlustur():
    DLA_Ana_Kategori_ss()
    
    # ANA KATEGORILER
    #==========================
def DLA_Ana_Kategori_ss():
    #tanımla
    ssElamanlar = {"Dla_Ana_kategoriler_list": list}
    SsnFonk.session_olustur(ssElamanlar)
    #atama
    st.session_state.Ana_kategoriler_list = ["General", "Scenario", "PictureDescription"]
    #dondur
    return st.session_state.Dla_Ana_kategoriler_list   


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
