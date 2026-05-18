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
            portfoy = st.number_input(
                "Portföy (TL)", min_value=10000, max_value=10000000,
                value=950000, step=10000
            )
            risk_yuzde = st.slider("Risk % (1R)", 0.5, 5.0, 1.0, 0.5)

