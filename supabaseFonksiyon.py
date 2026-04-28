import streamlit as st
from supabaseFonksiyon import create_client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def dla_kategori_ekle(category, subcategory):
    try:
        result = supabase.table("DlaSinavKategori").insert({
            "AnaKategori": category,
            "SubKategori": subcategory
        }).execute()

        return result

    except Exception as e:
        return str(e)