# https://cnytcxtry.streamlit.app/
# 
# #py -m pip install -r requirements.txt
#streamlit run app.py
#py -m streamlit run app.py
#İCON KUTUPHANESİ https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded
# https://unicode.org/emoji/charts/full-emoji-list.html
#ÖRNEK KULLANIM: if st.button("Next Question", key=f"next_question_btn_{question_id}_{current_index}", icon=":material/home:"):

#Gerekli Kütüphaneler

import streamlit as st
import pandas as pd 
  
# UTILS import
import Yardimci_Fonksiyonlar as Yfonk

#Sayfanın Genel Yapısı
st.set_page_config(
    page_title="SINAV SİSTEMİ",
    page_icon="🎤",
    layout="wide"
)

    # ANA KATEGORİLERİ DOLDUR
    # ============================================================================================
st.session_state.VT_ana_kategoriler_list = Yfonk.dla_ana_kategori_listesi()

# SESSION STATE OLUŞTUR
#============================================================================================

Yfonk.sessionOlustur()


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