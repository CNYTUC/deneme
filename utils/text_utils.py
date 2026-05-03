import time
import streamlit as st



# Metinleri yavaş yazdırma

# ==============================================================================  
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
# ==============================================================================  






def trim_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text

def truncate_text(text, max_length):
    if len(text) > max_length:
        return text[:max_length]
    return text