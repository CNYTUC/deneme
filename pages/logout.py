import streamlit as st

st.warning("Uygulamadan çıkış yapılıyor... Lütfen bekleyin.")

# Bahsettiğiniz yönlendirme komutu
st.markdown(
    '<meta http-equiv="refresh" content="0; url=https://www.google.com" />',
    unsafe_allow_html=True,
)