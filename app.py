# https://cnytcxtry.streamlit.app/
# 
# #py -m pip install -r requirements.txt
#streamlit run app.py
#py -m streamlit run app.py
#İCON KUTUPHANESİ https://fonts.google.com/icons?icon.set=Material+Symbols&icon.style=Rounded
# https://unicode.org/emoji/charts/full-emoji-list.html
#ÖRNEK KULLANIM: if st.button("Next Question", key=f"next_question_btn_{question_id}_{current_index}", icon=":material/home:"):


# KÜTÜPHANELER
import streamlit as st
  

# Sayfanın Genel Yapısı
# ============================================================================================

st.set_page_config(
    page_title="SINAV SİSTEMİ",
    page_icon="🎤",
    layout="wide"
)

# ============================================================================================

# NAVIGASYON OLUSTURMA
pages = {

"DOSYA": [
    st.Page("main.py", title="Ana Sayfa", icon="🏠"),
    st.Page("pages/logout.py", title="Çıkış", icon="🚪")
    
],     
"STRATEJİLER": [
    st.Page("pages/00StrCreate.py", title="Oluştur", icon="✏️"),
    st.Page("pages/01StrEdit.py", title="Düzenle", icon="📝"),
    st.Page("pages/02StrTest.py", title="Test Et", icon="📃"),

],
}

pg = st.navigation(pages, position="top")
pg.run()

