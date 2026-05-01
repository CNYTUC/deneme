import streamlit as st
import pandas as pd
from supabase import create_client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

#suprabase tablo adları

Tablo_Sorular = "Dla_Sorular"
Tablo_Etiketler = "Dla_Etiketler"


# DLA ANA KATEGORİLERİ LİSTESİ
#============================================================================================
def dla_ana_kategori_listesi():
    return [
        "General",
        "Scenario",
        "PictureDescription"
    ]

# DLA ETİKETLERİ İÇİN FONKSİYONLAR
#============================================================================================

def dla_etiket_ekle(Etiket):
    try:
        result = supabase.table(Tablo_Etiketler).insert({
            "Etiket": Etiket
        }).execute()

        return result

    except Exception as e:
        return str(e)

def dla_etiket_guncelle(row_id, Etiket):
    return (
        supabase
        .table(Tablo_Etiketler)
        .update({
            "Etiket": Etiket
        })
        .eq("id", row_id)
        .execute()
    )

def dla_etiketler_getir():
    return (
    supabase
    .table(Tablo_Etiketler)
    .select("id,Etiket")
    .order("id")
    .execute()
    )

def dla_etiket_sil(row_id):
    return (
        supabase
        .table(Tablo_Etiketler)
        .delete()
        .eq("id", row_id)
        .execute()
    )

# DLA SORULAR İÇİN FONKSİYONLAR
#============================================================================================
def dla_soru_ekle(category,  NewQuestion, Notes, PicPath):
    
    try:
        result = supabase.table("DlaSorular").insert({
            "AnaKategori": category,
            "Soru": NewQuestion,
            "ResimURL": PicPath,
            "Notlar": Notes,
        }).execute()

        return result

    except Exception as e:
        return str(e)

def dla_soru_ve_etiket_ekle(soru_id, etiket_id):
    try:
        result = supabase.table("DlaSoru_Etiket").insert({
            "AnaKategori": soru_id,
            "Soru": etiket_id,
        }).execute()

        return result

    except Exception as e:
        return str(e)


# DLA ALT KATEGORİLERİLER İÇİN FONKSİYONLAR
#============================================================================================

def dla_kategorileri_getir():
    #return supabase.table("DlaSinavKategori").select("*").order("id").execute()
    return (
    supabase
    .table("DlaKategoriler")
    .select("id,AnaKategori,AltKategori")
    .order("id")
    .execute()
    )

def dla_secili_kategorileri_getir(ana_kategori=None):

    query = (
        supabase
        .table("DlaKategoriler")
        .select("id,AnaKategori,AltKategori")
    )

    if ana_kategori and ana_kategori != "All":
        query = query.eq("AnaKategori", ana_kategori)

    return (
        query
        .order("id")
        .execute()
    )            

def dla_alt_kategorileri_getir(selected_category):
    rows = dla_kategorileri_getir()

    alt_kategoriler = []

    for kategori in rows.data:
        ana_kategori = kategori["AnaKategori"]
        alt_kategori = kategori["AltKategori"]

        if selected_category and ana_kategori != selected_category:
            continue

        # tekrar edenleri engelle
        if alt_kategori not in alt_kategoriler:
            alt_kategoriler.append(alt_kategori)

    return alt_kategoriler

def dla_alt_kategori_ekle(category, subcategory):
    try:
        result = supabase.table("DlaKategoriler").insert({
            "AnaKategori": category,
            "AltKategori": subcategory
        }).execute()

        return result

    except Exception as e:
        return str(e)

def dla_alt_kategori_guncelle(row_id, category, subcategory):
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

def dla_alt_kategori_sil(row_id):
    return (
        supabase
        .table("DlaKategoriler")
        .delete()
        .eq("id", row_id)
        .execute()
    )

# DLA SORULAR İÇİN FONKSİYONLAR
#============================================================================================

def dla_sorulari_getir(ana_kategori=None, alt_kategori=None):

    if ana_kategori == "All" and alt_kategori == "All":
        return (
            supabase
            .table("DlaSorular")
            .select("id,AnaKategori,AltKategori,Soru,ResimURL,Notlar")
            .order("id")
            .execute()
            )
    
    if ana_kategori != "All" and alt_kategori == "All":
            return (
                supabase
                .table("DlaSorular")
                .select("id,AnaKategori,AltKategori,Soru,ResimURL,Notlar")
                .eq("AnaKategori", ana_kategori)
                .order("id")
                .execute()
            )
    
    if ana_kategori != "All" and alt_kategori != "All":
            return (
                supabase
                .table("DlaSorular")
                .select("id,AnaKategori,AltKategori,Soru,ResimURL,Notlar")
                .eq("AnaKategori", ana_kategori)
                .eq("AltKategori", alt_kategori)
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





def dla_sorulari_toplu_ekle(category, questions_text, Notes, PicPath):
    try:
        sorular = [
            soru.strip()
            for soru in questions_text.splitlines()
            if soru.strip()
        ]

        if not sorular:
            return "Soru bulunamadı."

        data = []

        for soru in sorular:
            data.append({
                "AnaKategori": category,
                "Soru": soru,
                "ResimURL": PicPath,
                "Notlar": Notes
            })

        result = supabase.table("DlaSorular").insert(data).execute()
        return result

    except Exception as e:
        return str(e)



