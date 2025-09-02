# Creating this file just for live demo at streamlit purpose only

import streamlit as st

# Loading the HTML file
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Render HTML in Streamlit
st.components.v1.html(html_content, height=900, scrolling=True)
