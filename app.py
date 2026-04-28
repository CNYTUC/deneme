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

main_page = st.Page("main_page.py", title="Main", icon="🏠")
test_page0 = st.Page("pages/Test_Gen.py", title="General Test", icon="🎯")
test_page1 = st.Page("pages/Test1.py", title="Scenarios Test", icon="🎯")
test_page2 = st.Page("pages/Test2.py", title="Picture Description Test", icon="🎯")

pg = st.navigation([main_page, test_page0, test_page1, test_page2])
pg.run()