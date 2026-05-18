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

        import streamlit as st

        # Başlığı ve varsayılan olarak açık/kapalı olmasını (expanded) ayarlayabilirsiniz
        with st.expander("Daha fazla bilgi için tıklayın"):
            st.write("Burada gizli olan metni veya grafikleri görebilirsiniz.")
            st.image("https://streamlit.io")
