from supabaseFonksiyon import dla_kategorileri_getir

DLA_ANA_KATEGORI_LISTESI = [
    "General",
    "Scenario",
    "PictureDescription"
]

def DLA_ALT_KATEGORILERI_LISTESI(selected_category):
    DLA_ANA_KATEGORILER = dla_kategorileri_getir()
    alt_kategoriler = {}
    for kategori in DLA_ANA_KATEGORILER.data:
        ana_kategori = kategori["AnaKategori"]
        alt_kategori = kategori["AltKategori"]
        if selected_category and ana_kategori != selected_category:
            continue
        
        


        if ana_kategori not in alt_kategoriler:
            alt_kategoriler[ana_kategori] = []
        alt_kategoriler[ana_kategori].append(alt_kategori)
    return alt_kategoriler
