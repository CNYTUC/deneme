import streamlit as st
import pandas as pd
from io import BytesIO

from supabaseFonksiyon import (
    dla_ana_kategori_listesi,
    dla_alt_kategorileri_getir
)

#BAŞLIK
#============================================================================================
st.header("Dla Soru Editörü")


#Yenı Soru Ekleme Formu
#============================================================================================
st.subheader("➕ Yeni Soru Ekle")

#SORU BILGILERI 
#============================================================================================
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    with st.container(border=True,vertical_alignment="center",height="stretch"):
        Ana_kategori = st.radio(
            "Ana Kategori",
            dla_ana_kategori_listesi(),
            key="ana_kategori_radio"
        )

with col2:
    with st.container(border=True,vertical_alignment="center",height="stretch"):
        if Ana_kategori:
            
            alt_kategoriler = dla_alt_kategorileri_getir(Ana_kategori)

            Alt_kategori = st.selectbox(
            "Alt Kategori",
            alt_kategoriler,
            key="alt_kategori_select"
            )
    
with col3:
        with st.container(border=True,vertical_alignment="center",height="stretch"):
            PicPath = st.text_input(
            "Resim Yolu (Opsiyonel)",
            placeholder="Örnek: /images/question1.png"
            )

NewQuestion = st.text_input(
                "Soru Metni",
                placeholder="Örnek: What do you prefer, tea or coffee?"
                )

Notes = st.text_input(
                "Notlar",
                placeholder="Örnek: Bu soru tercihleri ölçmek için kullanılır."
                )
