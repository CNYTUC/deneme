import streamlit as st

# 1. Oturum verilerini temizleyin (güvenlik için)
st.session_state.clear()

# 2. Ekrana kapanış mesajı verin
st.error("Uygulama oturumu başarıyla sonlandırıldı. Sayfayı kapatabilirsiniz.")

# 3. Streamlit'i tamamen durdurun (Ekran kararır ve tüm işlemler kesilir)
st.stop()