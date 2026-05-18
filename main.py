import streamlit as st
import UTILS.text_utils as c_txt
import UTILS.time_utils as c_time

st.title("🏠 Main")

MetinA = "Strateji Test Sayfasına Hoşgeldiniz."
MetinB = "Bu sistem kişisel işlemler iç.in tasarelanmıştır"

c_time.wait(1)
c_txt.slow_print(MetinA,False,0.1)
c_time.wait(1)
c_txt.slow_print(MetinB,False,0.1)
