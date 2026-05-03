import time
import streamlit as st


def slow_print(text: str, CharMode: bool = False, delay: float = 0.02):
    
    if CharMode == "char":
        generator = (char for char in text)
    else:
        generator = (word + " " for word in text.split())

    def stream():
        for item in generator:
            yield item
            time.sleep(delay)

    st.write_stream(stream())