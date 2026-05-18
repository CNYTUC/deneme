# KÜTÜPHANELER
import streamlit as st

# BAŞLIK
# ============================================================================================
st.subheader("🤑 Yeni Strateji Olustur 🤠",divider="yellow")


# DIŞ CONTAINER OLUSTUR
# ============================================================================================
with st.container(border=True,vertical_alignment="center",height="stretch"):
    
    with st.container(border=True,vertical_alignment="center",height="stretch"):
        
        # Yeni Strateji Adı
        # ============================================================================================
        st.text_input(
        "Strateji Adı",
        placeholder="Ör. Murat 1",
        key="YeniStratejiAdi_SS",
        )
    

    with st.container(border=True,vertical_alignment="center",height="stretch"):

        st.write("Indicatorler")        


        # Onay kutusunu oluşturuyoruz
        formu_goster = st.checkbox("Ek seçenekleri göster")

        # Eğer onay kutusu işaretlendiyse altındaki container açılır
        if formu_goster:
            st.subheader("Gelişmiş Ayarlar")
            st.text_input("Kullanıcı Adı")
            st.password("Şifre")
