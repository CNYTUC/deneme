# IMPORTLAR
# ============================================================================================
import streamlit as st
import pandas as pd
from io import BytesIO
#text
from utils.text_utils import tr_to_en_lower
#zaman
from utils.time_utils import wait
#session
from utils.session_utils import session_olustur
from utils.session_utils import session_sil

#supabase
from supabaseFonksiyon import (
    dla_ana_kategori_listesi,
    dla_etiket_ekle,
    dla_etiketler_getir,
    dla_etiket_guncelle,
    dla_etiket_sil,
)
# ============================================================================================


# BAŞLIK
# ============================================================================================
st.header("D.L.A. Editörü")


# TAB PANEL OLUSTUR
# ============================================================================================
tab1, tab2, tab3, tab4 = st.tabs(["🏷️ Yeni Etiket", "📚 Mevcut Etiketler", "➕ Yeni Soru", "📋 Mevcut Sorular"])    
    
    
with tab1:
    
    
    # Session State Oluştur
    # ============================================================================================  
    ssElamavnlar = {
        "YE_vt_kayitlar_df": pd.DataFrame,
        "YE_etiketler": str
    }
    session_olustur(ssElamavnlar)
 
    
        
    # TAB1.BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Yeni Etiket Ekle",divider="green")

        # Kayıtları Getir       
        # ===========================================  
          
    Kayitlar = dla_etiketler_getir()
    st.session_state.YE_vt_kayitlar_df = pd.DataFrame(Kayitlar.data)      
    
        # Sadece etiketleri getir
        # ===========================================
        
    veri_tabani_etiketleri = []       
    if not st.session_state.YE_vt_kayitlar_df.empty:
        veri_tabani_etiketleri = st.session_state.YE_vt_kayitlar_df["Etiket"].dropna().unique().tolist()
        
        
    # 2.ETİKET EKLEME FORMU OLUSTUR
    # ============================================================================================
    with st.form("Etiket_ekleme_formu", clear_on_submit=True):
        
        
        # KOLONLARI OLUSTUR
        # ===========================================
        col1, col2 = st.columns([5, 1])

        with col1:
            
            # YENI ETIKET ICIN *** MULTISELECT *** OLUSTUR
            # ===========================================
            with st.container(border=True,vertical_alignment="center",height="stretch"):
                st.session_state.YE_etiketler = st.multiselect(
                    "Etiket Adı",
                    options=veri_tabani_etiketleri,
                    max_selections=20,
                    accept_new_options=True,
                    placeholder="Henüz etiket yok...",
                    key="YEK_etiket_input"
                    )
        

        with col2:
            
            # YENI ETIKET ICIN *** KAYDET BUTTON *** OLUSTUR
            # ===========================================
            with st.container(border=True,vertical_alignment="center",height="stretch"):
                kaydet = st.form_submit_button("Kaydet")


        # KAYDET BUTONA BASILIRSA
        # ===========================================
        if kaydet:
                    
            if st.session_state.YE_etiketler == []:
                st.warning("Etiket / Etiketler boş bırakılamaz.")

            else:
            
                #Etiketleri Kaydet
                # ============================================================================================
                yeni_etiket_sayisi = 0
                ayni_etiket_sayisi = 0

                for Tag in st.session_state.YE_etiketler:

                    Yeni_Eklenecek_Etiket = tr_to_en_lower(Tag.strip())

                    if not Yeni_Eklenecek_Etiket in veri_tabani_etiketleri:
                        dla_etiket_ekle(Yeni_Eklenecek_Etiket)
                        yeni_etiket_sayisi += 1
                    else:
                        ayni_etiket_sayisi += 1


                if yeni_etiket_sayisi > 0: st.success(f"Eklenen etiketler: {yeni_etiket_sayisi}", icon="✅")
                if ayni_etiket_sayisi > 0: st.error(f"Eklenmeyen!!! sistemdeki etiketler: {ayni_etiket_sayisi}", icon="🚨")
                
                #3 saniye bekle
                wait(3)

                # Formu temizle
                session_sil("YE_")
                
                
                
                
with tab2: 
    
    for key in st.session_state.keys():
        del st.session_state[key]
        
    # TAB2.BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Mevcut Etiketler",divider="rainbow")

    # Etiketler için session state tanımları
    # ============================================================================================
    st.session_state.setdefault("ME_etiketler_tablo_goster", False)

        # Kayıtları Getir       
        # ===========================================  
          
    Kayitlar = dla_etiketler_getir()
    st.session_state.ME_vt_kayitlar_df = pd.DataFrame(Kayitlar.data)      
    
    
    

with tab3:
    
    # TAB3.BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Yeni Soru Ekle",divider="red")


with tab4:
    
    # TAB4.BAŞLIK BELİRLE
    # ============================================================================================
    st.subheader(f"Mevcut Sorular",divider="red")

    
    
    