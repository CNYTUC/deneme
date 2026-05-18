import streamlit as st

st.warning("Uygulamadan çıkış yapılıyor...")

# JavaScript kullanarak tarayıcının en üst penceresini (window.top) yönlendiriyoruz
js_kod = """
<script>
    window.top.location.href = "https://google.com";
</script>
"""

st.components.v1.html(js_kod, height=0, width=0)