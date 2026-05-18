import streamlit as st

st.subheader("🚪 Çıkış Yapmak İstediğinize Emin misiniz?")
st.write("Uygulamadan güvenli bir şekilde ayrılmak için aşağıdaki butona tıklayın.")

# HTML ve CSS ile şık bir çıkış butonu tasarlıyoruz.
# target="_top" ifadesi sayfanın iFrame'den kurtulup ana sekmede açılmasını sağlar.
st.markdown(
    """
    <a href="https://www.google.com" target="_top" style="
        display: inline-block;
        padding: 0.5rem 1rem;
        color: white;
        background-color: #ef4444;
        text-decoration: none;
        border-radius: 0.375rem;
        font-weight: 500;
        text-align: center;
        margin-top: 10px;
    ">
        Oturumu Kapat ve Ayrıl
    </a>
    """,
    unsafe_allow_html=True
)