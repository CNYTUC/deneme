#py -m pip install -r requirements.txt
#streamlit run app.py
#py -m streamlit run app.py
#İCON KUTUPHANESİ https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded
#ÖRNEK KULLANIM: if st.button("Next Question", key=f"next_question_btn_{question_id}_{current_index}", icon=":material/home:"):


import streamlit as st

#Sayfanın Genel Yapısı
st.set_page_config(
    page_title="DLA Speaking Practice",
    page_icon="🎤",
    layout="wide"
)

#NAVIGASYON

pages = {
    
    "MAIN": [
        st.Page("main.py", title="Main", icon="🏠"),
    ],     
    "SINAVLAR": [
        st.Page("Sinavlar/dla.py", title="DLA", icon="🎤"),
    ],     

}

pg = st.navigation(pages, position="top")
pg.run()