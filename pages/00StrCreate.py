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

        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            
            # Onay kutusunu oluşturuyoruz
            RSI_BOX = st.checkbox("RSI Aktif")

            # Eğer onay kutusu işaretlendiyse altındaki container açılır
            if RSI_BOX:
                
                RSI_LEN = st.number_input("RSI Length", min_value=2, max_value=100, value=14, step=1) # RSI Length: 14
                RSI_Source = st.selectbox("RSI Source", ["Close", "Open"], index=0) # RSI Source: Close
                RSI_Overbought= st.number_input("RSI Overbought", min_value=0, max_value=100, value=70, step=1) # RSI Overbought: 70
                RSI_Oversold= st.number_input("RSI Oversold", min_value=0, max_value=100, value=30, step=1) # RSI Oversold: 30
                RSI_Signal = st.number_input("RSI Signal", min_value=2, max_value=100, value=14, step=1) # RSMA Length (Signal): 14
                
        with col2:
            
            # Onay kutusunu oluşturuyoruz
            MACD_BOX = st.checkbox("MACD Aktif")

            # Eğer onay kutusu işaretlendiyse altındaki container açılır
            if MACD_BOX:
                
                MADC_FAST_EMA = st.number_input("Fast EMA", min_value=2, max_value=100, value=12, step=1) # Fast EMA: 12
                MADC_SLOW_EMA = st.number_input("Slow EMA", min_value=2, max_value=100, value=26, step=1) # Slow EMA: 26
                MADC_Signal = st.number_input("Signal Length", min_value=2, max_value=100, value=9, step=1) # Signal Length: 9
                MADC_Source = st.selectbox("Source", ["Close", "Open"], index=0) # Source: Close
                


                # portfoy = st.number_input(
                #     "Portföy (TL)", min_value=10000, max_value=10000000,
                #     value=950000, step=10000
                # # )
                # risk_yuzde = st.slider("Risk % (1R)", 0.5, 5.0, 1.0, 0.5)

