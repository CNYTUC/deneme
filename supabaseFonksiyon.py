import streamlit as st
import pandas as pd
from supabase import create_client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# DLA KATEGORİLERİLER İÇİN FONKSİYONLAR
#============================================================================================
def dla_kategori_ekle(category, subcategory):
    try:
        result = supabase.table("DlaKategoriler").insert({
            "AnaKategori": category,
            "AltKategori": subcategory
        }).execute()

        return result

    except Exception as e:
        return str(e)

def dla_kategorileri_getir():
    #return supabase.table("DlaSinavKategori").select("*").order("id").execute()
    return (
    supabase
    .table("DlaKategoriler")
    .select("id,AnaKategori,AltKategori")
    .order("id")
    .execute()
    )

def dla_kategori_guncelle(row_id, category, subcategory):
    return (
        supabase
        .table("DlaKategoriler")
        .update({
            "AnaKategori": category,
            "AltKategori": subcategory
        })
        .eq("id", row_id)
        .execute()
    )

def dla_kategori_sil(row_id):
    return (
        supabase
        .table("DlaKategoriler")
        .delete()
        .eq("id", row_id)
        .execute()
    )

# DLA SORULAR İÇİN FONKSİYONLAR
#============================================================================================
def dla_soru_ekle(category, subcategory, NewQuestion, Notes, PicPath):
    try:
        result = supabase.table("DlaSorular").insert({
            "AnaKategori": category,
            "AltKategori": subcategory,
            "Soru": NewQuestion,
            "ResimURL": PicPath,
            "Notlar": Notes
        }).execute()

        return result

    except Exception as e:
        return str(e)

def dla_sorulari_getir():
    #return supabase.table("DlaSinavKategori").select("*").order("id").execute()
    return (
    supabase
    .table("DlaSorular")
    .select("id,AnaKategori,AltKategori,Soru,ResimURL,Notlar")
    .order("id")
    .execute()
    )

def dla_soru_guncelle(row_id, category, subcategory, question, notes, pic_path):
    return (
        supabase
        .table("DlaSorular")
        .update({
            "AnaKategori": category,
            "AltKategori": subcategory,
            "Soru": question,
            "ResimURL": pic_path,
            "Notlar": notes
        })
        .eq("id", row_id)
        .execute()
    )

def dla_soru_sil(row_id):
    return (
        supabase
        .table("DlaSorular")
        .delete()
        .eq("id", row_id)
        .execute()
    )




