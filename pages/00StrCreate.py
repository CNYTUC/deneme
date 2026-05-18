# KÜTÜPHANELER
import streamlit as st

# BAŞLIK
# ============================================================================================
st.subheader("🤑 Yeni Strateji Olustur 🤠",divider="yellow")


# DIŞ CONTAINER OLUSTUR
# ============================================================================================
with st.container(border=True,vertical_alignment="center",height="stretch"):
    
    with st.container(border=True,vertical_alignment="center",height="stretch"):
        
        # Yeni Strateji Adı
        # ============================================================================================
        st.text_input(
        "Strateji Adı",
        placeholder="Ör. Murat 1",
        key="YeniStratejiAdi_SS",
        )
    

    with st.container(border=True,vertical_alignment="center",height="stretch"):

        st.write("Indicatorler")        


        # Onay kutusunu oluşturuyoruz
        RSI_BOX = st.checkbox("RSI Aktif")

        # Eğer onay kutusu işaretlendiyse altındaki container açılır
        if RSI_BOX:
            st.subheader("RSI ayarlar")
            st.subheader("RSI Alım ve Satım koşullar")

