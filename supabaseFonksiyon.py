import streamlit as st
import pandas as pd
from supabase import create_client

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

def dla_kategorileri_getir():
    return supabase.table("DlaSinavKategori").select("*").order("id").execute()

def dla_kategori_guncelle(row_id, category, subcategory):
    return (
        supabase
        .table("DlaSinavKategori")
        .update({
            "AnaKategori": category,
            "SubKategori": subcategory
        })
        .eq("id", row_id)
        .execute()
    )


def dla_kategori_sil(row_id):
    return (
        supabase
        .table("DlaSinavKategori")
        .delete()
        .eq("id", row_id)
        .execute()
    )