from supabaseFonksiyon import dla_kategorileri_getir

DLA_ANA_KATEGORI_LISTESI = [
    "General",
    "Scenario",
    "PictureDescription"
]


def DLA_ALT_KATEGORILERI_LISTESI(selected_category=None):
    rows = dla_kategorileri_getir()

    alt_kategoriler = {}

    for kategori in rows.data:
        ana_kategori = kategori["AnaKategori"]
        alt_kategori = kategori["SubKategori"]   # tablo kolon adı buysa

        # Eğer ana kategori seçildiyse sadece onu getir
        if selected_category and ana_kategori != selected_category:
            continue

        if ana_kategori not in alt_kategoriler:
            alt_kategoriler[ana_kategori] = []

        # Tekrar eden kayıtları engelle
        if alt_kategori not in alt_kategoriler[ana_kategori]:
            alt_kategoriler[ana_kategori].append(alt_kategori)

    return alt_kategoriler
