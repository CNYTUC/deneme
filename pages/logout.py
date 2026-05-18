import streamlit as st

st.warning("Uygulamadan çıkış yapılıyor... Lütfen bekleyin.")

# window.parent.location.href doğrudan Streamlit'in ana penceresine müdahale eder.
js_kod = """
<script>
    window.parent.location.href = "https://www.google.com";
</script>
"""

st.components.v1.html(js_kod, height=0, width=0)