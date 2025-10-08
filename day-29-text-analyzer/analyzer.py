import streamlit as st

st.title("Simple Text Analyzer")

text = st.text_area("Enter your text here:")

if text:
    st.write(f"**Character count:** {len(text)}")
    st.write(f"**Word count:** {len(text.split())}")
    st.write(f"**Reversed text:** {text[::-1]}")
