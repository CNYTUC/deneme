import streamlit as st
import time

st.title("🏠 Main")

# st.table(
#     {
#         ":material/folder: Project": "**Streamlit** - The fastest way to build data apps",
#         ":material/code: Repository": "[github.com/streamlit/streamlit](https://github.com/streamlit/streamlit)",
#         ":material/new_releases: Version": ":gray-badge[1.45.0]",
#         ":material/license: License": ":green-badge[Apache 2.0]",
#         ":material/group: Maintainers": ":blue-badge[Core Team] :violet-badge[Community]",
#     },
#     border="horizontal",
#     width="content",
# )

MetinA = "Kişisel Sınav Sistemine Hoş Geldiniz."
MetinB = "Bu sistem üzerinden DLA ve REC sistemine hazırlanabilirsiniz."
        
def stream_data():
    
    for word in MetinA.split(" "):
        yield word + " "
        time.sleep(0.02)

    for word in MetinB.split(" "):
        yield word + " "
        time.sleep(0.02)

st.write_stream(stream_data)