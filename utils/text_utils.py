import time
import streamlit as st


def slw(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

def slow_print(text): 

    st.write_stream(slw,text)