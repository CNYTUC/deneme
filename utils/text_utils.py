import time
import streamlit as st

yieldtext =""
def slw():
    for word in yieldtext.split(" "):
        yield word + " "
        time.sleep(0.02)

def slow_print(text): 
    yieldtext = text
    st.write_stream(slow_print)