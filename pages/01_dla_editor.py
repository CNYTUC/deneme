# IMPORTLAR
# ============================================================================================
import streamlit as st
import y_fonksiyonlar as yf

# BAŞLIK
# ============================================================================================
st.header("D.L.A. Editörü 🤠")
 

# ANA PANEL OLUŞTUR
# ============================================================================================
tab1, tab2, tab3, tab4 = st.tabs(["❓ Yeni Soru", "📖 Sorular", "🏷️ Etiketler"])   

with tab1:
    
    TB1_alan = st.empty()

with tab2:
    
    TB2_alan = st.empty()

with tab3:
    
    TB3_alan = st.empty()

with tab4:
    
    TB4_alan = st.empty()


yf.TB1_alan_doldur(TB1_alan)
