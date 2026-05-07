# KUTUPHANELER
import streamlit as st
import supabaseFonksiyon as SpFonk

# DLA ANA KATEGORİLERİ LİSTESİ
#============================================================================================
def dla_ana_kategori_listesi():
    return [
        "General",
        "Scenario",
        "PictureDescription"
    ] 


def Yeni_Soru_Alan_Doldur(alan):
        
        #ETİKETLERİ GETIR
        vt_etiketler = st.session_state.YE_YeniEtiketler_list
        
        #EĞER KAYIT YOKSA BILGI VER
        if vt_etiketler.empty:
            st.info("Herhangi bir etiket bulunamadı.")
        else:
            alan.write("bulundu")