import streamlit as st
import pandas as pd
from supabaseFonksiyon import (
    dla_kategorileri_getir,
    dla_kategori_sil
)

#BAŞLIK
#============================================================================================
st.title("Dla Kategori Editörü")
st.write("Dla Kategori Editörü sayfasına hoş geldiniz. Bu sayfa üzerinden DLA sınav kategorilerini yönetebilirsiniz.")

rows = dla_kategorileri_getir()

df = pd.DataFrame(rows.data)

st.data_editor(df, use_container_width=True)