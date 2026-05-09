# KUTUPHANELER
import streamlit as st
import pandas as pd
from io import BytesIO

import UTILS.ara_module as am
import UTILS.supabaseFonksiyon as SpFonk

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
        

        # Ana kategori seçimi
        # ============================================================================================  
        with st.container(border=True, vertical_alignment="center", height="stretch"):

            # DEĞİŞKENLER
            Ana_kategoriler:list = am.DLA_Ana_Kategoriler()

            # Ana kategori seçimi
            st.radio(
                "Ana Kategori",
                options=Ana_kategoriler,
                horizontal=True,
                key="Yeni_Soru_Ana_Kategori_Radio",
            )

        # Soru metni ve notlar için geniş bir alan
        # ============================================================================================
        
        with st.container(border=True, vertical_alignment="center", height="stretch"):

            if st.session_state.Yeni_Soru_Ana_Kategori_Radio == "PictureDescription":

                st.text_area(
                    "Soru Metni",
                    placeholder="Describe The Picture",
                    height=100,
                    value="Describe The Picture",
                    disabled=True,
                    key="Yeni_Soru_Soru_Metni",
                    )

            else:

                st.text_area(
                    "Soru Metni",
                    placeholder="Her satıra ayrı bir soru yazın.",
                    height=100,
                    key="Yeni_Soru_Soru_Metni",
                    )
            
            #Önerme Yaz
            Yeni_Soru_Metni = st.session_state.Yeni_Soru_Soru_Metni

            i=0
            
            if Yeni_Soru_Metni.strip() == "":
            
                st.session_state.Dla_Secilen_Soru_Metni_Str = ""
                st.warning("Soru metni boş bırakılamaz. En az 1 soru metni girmelisiniz.")    
            
            else:

                for soru in st.session_state.Dla_Secilen_Soru_Metni_Str.splitlines():
                    i+=1

                st.success(f"{i} soru metni girdiğiniz görünüyor.")   



        # Etiketler girişi
        # ============================================================================================
        if not st.session_state.Yeni_Soru_Ana_Kategori_Radio == "PictureDescription":
                
            # DEĞİŞKENLER
            Vt_Etiketler: pd.DataFrame = SpFonk.dla_etiketler_DF()
            mevcut_etiketler_seti = set(Vt_Etiketler["Etiket"].dropna().unique())  
            
            with st.container(border=True, vertical_alignment="center", height="stretch"):
                
                st.multiselect(
                    "Etiketlerinizi seçin",
                    options=mevcut_etiketler_seti,
                    max_selections=20,
                    accept_new_options=True,
                    placeholder="Etiketlerinizi seçin !!!",
                    key="Yeni_Soru_Etiketler_Multiselect",
                    )
                    
                #Önerme Yaz
                Yeni_Soru_Etiketler = st.session_state.Yeni_Soru_Etiketler_Multiselect
                
                if Yeni_Soru_Etiketler:
                    st.success(am.tr_to_en_lower(" ".join(Yeni_Soru_Etiketler)))



        # Resim yolu girişi (yalnızca PictureDescription için)
        # ============================================================================================
        with st.container(border=True, vertical_alignment="center", height="stretch"):
            
            # DEĞİŞKENLER
            Secilen_ana_kategori: str = st.session_state.Dla_Secilen_Ana_Kategori_Str

            if Secilen_ana_kategori == "PictureDescription":
                   
                Secilen_resim_yolu = st.text_input(
                "Resim Yolu",
                placeholder="Örnek: /images/question1.png",
                key="Yeni_Soru_Resim_Yolu_Input",
                )
            

        # Notlar alanı
        # ============================================================================================

        with st.container(border=True, vertical_alignment="center", height="stretch"):
            
            st.text_area(
                "Notlar (Opsiyonel)",
                placeholder="Örnek: Bu soru tercihleri ölçmek için kullanılır.",
                key="Yeni_Soru_Notlar_TextArea",
                )


        # Kontrol alanı
        # ============================================================================================
        with st.container(border=True, vertical_alignment="center", height="stretch"):

            if st.button("Kontrol Et", key="Yeni_Soru_Kontrol_Et_Button", icon="✅"):
                
                #Önerme Yaz
                Secilen_Kategori = st.session_state.Yeni_Soru_Ana_Kategori_Radio

                if Secilen_Kategori == "PictureDescription":
                    # st.write(f"'{Secilen_ana_kategori}' için Gereklilikler: En az 1 Etiket, Sadece 1 Soru metni ve 1 Resim yolu.")
                    st.markdown(f"**<span style='color:red'>{Secilen_Kategori}</span>** için Gereklilikler: En az 1 Etiket, Soru metni ve 1 Resim yolu.", unsafe_allow_html=True)
                else:
                    # st.write(f"'{Secilen_ana_kategori}' için Gereklilikler: En az 1 Etiket, Soru metni.")
                    st.markdown(f"**<span style='color:red'>{Secilen_Kategori}</span>** için Gereklilikler: En az 1 Etiket, Soru metni.", unsafe_allow_html=True)


# # MEVCUT SORULAR
# # ============================================================================================
# with Mevcut_Soru:

#     # ALT BAŞLIK BELİRLE
#     # ============================================================================================
#     st.subheader(f"Mevcut Etiketler 🔖",divider="rainbow")

#     # DIŞ CONTAINER OLUSTUR
#     # ============================================================================================
#     with st.container(border=True,vertical_alignment="center",height="stretch"):
        
#         Mevcut_Soru_Alan = st.empty()
    
# # MEVCUT ETİKETLER
# # ============================================================================================
# with Mevcut_Etiketler:

#     # ALT BAŞLIK BELİRLE
#     # ============================================================================================
#     st.subheader(f"Mevcut Sorular 📖",divider="red")

#     # DIŞ CONTAINER OLUSTUR
#     # ============================================================================================
#     with st.container(border=True,vertical_alignment="center",height="stretch"):
        
#         Mevcut_Etiket_Alan = st.empty()
