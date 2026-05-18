import streamlit as st
import pandas as pd

# KÜTÜPHANELER
import UTILS.session_utils as SsnFonk
import UTILS.supabaseFonksiyon as SpFonk
import UTILS.text_utils as TxtFonk

# Veri Tabanından Çağırılanlar
def DLA_Ana_Kategoriler():
    #dondur
    return ["General", "Scenario", "PictureDescription"]


#====================================================================================
# NAVIGATION OLUŞTUR
#============================================================================================

def navigasyonOlustur():

    pages = {
    
    "MAIN": [
        st.Page("main.py", title="Main", icon="🏠")
        
    ],     
    "STRATEJİLER": [
        st.Page("PAGES/00StrCreate.py", title="Oluştur", icon="📝"),
        st.Page("PAGES/01StrEdit.py", title="Düzenle", icon="📝"),
        st.Page("PAGES/02StrTest.py", title="Test Et", icon="📝"),

    ],     
    }

    pg = st.navigation(pages, position="top")
    pg.run()


#====================================================================================
# TEXT DÜZENLEME FONKSİYONLARI
#============================================================================================

def tr_to_en_lower(text):
    return TxtFonk.tr_to_en_lower(text)