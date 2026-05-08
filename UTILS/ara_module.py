import streamlit as st
import pandas as pd

# KÜTÜPHANELER
import UTILS.session_utils as SsnFonk
import UTILS.supabaseFonksiyon as SpFonk
import UTILS.text_utils as TxtFonk

#====================================================================================
# SESSION STATE OLUŞTUR
#============================================================================================
def tumSessionOlustur():
    DLA_Ana_Kategori_ss()
    DLA_Etiketler_ss()
    DLA_Digerleri_ss()

# Veri Tabanından Çağırılanlar
def DLA_Ana_Kategori_ss():
    sesName = "Dla_Ana_kategoriler_list"
    #tanımla
    ssElamanlar = {sesName: list}
    SsnFonk.session_olustur(ssElamanlar)
    #atama
    st.session_state[sesName] = ["General", "Scenario", "PictureDescription"]
    #dondur
    return st.session_state[sesName]  
def DLA_Etiketler_ss():
    sesName = "Dla_Etiketler_Df"
    #tanımla
    ssElamanlar = {sesName: pd.DataFrame}
    SsnFonk.session_olustur(ssElamanlar)
    #atama
    st.session_state[sesName] = SpFonk.dla_etiketler_DF()
    #dondur
    return st.session_state[sesName]

def DLA_Digerleri_ss():
    elemanlar = {
        "Dla_Secilen_Ana_Kategori_Str": str,
        "Dla_Secilen_Resim_Yolu_Str": str,
        "Dla_Secilen_Etiketler_List": list,
        "Dla_Secilen_Soru_Metni_Str": str,
        "Dla_Secilen_Notlar_Str": str,
        }
    
    SsnFonk.session_olustur(elemanlar)







#====================================================================================
# NAVIGATION OLUŞTUR
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


#====================================================================================
# TEXT DÜZENLEME FONKSİYONLARI
#============================================================================================

def tr_to_en_lower(text):
    return TxtFonk.tr_to_en_lower(text)