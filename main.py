import streamlit as st
import UTILS.text_utils as c_txt
import UTILS.time_utils as c_time

st.title("🏠 Hoşgeldiniz")

MetinA = "Strateji Test Sayfasına Hoşgeldiniz."
MetinB = "Bu sistem kişisel işlemler için tasarlanmıştır"

c_time.wait(1)
c_txt.slow_print(MetinA,False,0.1)
c_time.wait(1)
c_txt.slow_print(MetinB,False,0.1)
