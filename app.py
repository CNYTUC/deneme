# https://cnytcxtry.streamlit.app/
# 
# #py -m pip install -r requirements.txt
#streamlit run app.py
#py -m streamlit run app.py
#İCON KUTUPHANESİ https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded
# https://unicode.org/emoji/charts/full-emoji-list.html
#ÖRNEK KULLANIM: if st.button("Next Question", key=f"next_question_btn_{question_id}_{current_index}", icon=":material/home:"):

import streamlit as st
import pandas as pd 

# UTILS import
import UTILS.session_utils as SsnFonk
import Yardimci_Fonksiyonlar as Yfonk
import supabaseFonksiyon as SpFonk

#Sayfanın Genel Yapısı
st.set_page_config(
    page_title="SINAV SİSTEMİ",
    page_icon="🎤",
    layout="wide"
)


# DLA ANA KATEGORİLERİ LİSTESİ
#============================================================================================
def dla_ana_kategori_listesi():
    return [
        "General",
        "Scenario",
        "PictureDescription"
    ] 

    # ANA KATEGORİLERİ DOLDUR
    # ============================================================================================
st.session_state.VT_ana_kategoriler_list = Yfonk.dla_ana_kategori_listesi()

# SESSION STATE OLUŞTUR
#============================================================================================


ssElamanlar = {
        "VT_Etiketler_df": pd.DataFrame,
        "VT_Sorular_df": pd.DataFrame,
        "VT_ana_kategoriler_list": list
    }

SsnFonk.session_olustur(ssElamanlar)

    # ETİKETLERİ DOLDUR
    # ============================================================================================
st.session_state.YE_YeniEtiketler_list = SpFonk.dla_etiketler_DF()

#============================================================================================



# NAVIGASYON
#============================================================================================


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


#===================================================================================