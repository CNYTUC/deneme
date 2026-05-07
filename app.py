# https://cnytcxtry.streamlit.app/
# 
# #py -m pip install -r requirements.txt
#streamlit run app.py
#py -m streamlit run app.py
#İCON KUTUPHANESİ https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded
# https://unicode.org/emoji/charts/full-emoji-list.html
#ÖRNEK KULLANIM: if st.button("Next Question", key=f"next_question_btn_{question_id}_{current_index}", icon=":material/home:"):

import streamlit as st


#Sayfanın Genel Yapısı
st.set_page_config(
    page_title="SINAV SİSTEMİ",
    page_icon="🎤",
    layout="wide"
)


# NAVIGASYON
#===================================================================================
pages = {
    
    "MAIN": [
        st.Page("main.py", title="Main", icon="🏠")
        
    ],     
    "DLA KATEGORİSİ": [
        st.Page("PAGES/01_DLA_EDITOR.py", title="D.L.A. Editör", icon="📝"),
        st.Page("PAGES/02_DLA_EXAM.py", title="D.L.A. Exam", icon="🎤")

    ],     
    "REC KATEGORİSİ": [
        st.Page("PAGES/03_REC_EDITOR.py", title="R.E.C. Editör", icon="📝"),
        st.Page("PAGES/04_REC_EXAM.py", title="R.E.C. Exam", icon="📚")

    ],    
}

pg = st.navigation(pages, position="top")
pg.run()
#===================================================================================