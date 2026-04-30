import re

def tr_to_en_lower(text: str) -> str:
    if not text:
        return ""

    ceviri_tablosu = str.maketrans({
        "Ü": "u", "ü": "u",
        "Ğ": "g", "ğ": "g",
        "İ": "i", "ı": "i",
        "Ş": "s", "ş": "s",
        "Ç": "c", "ç": "c",
        "Ö": "o", "ö": "o",
    })

    text = text.translate(ceviri_tablosu)

    # boşlukları düzenle
    text = re.sub(r"\s+", "-", text.strip())

    return text.lower()