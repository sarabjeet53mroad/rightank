import streamlit as st
from PIL import Image

logo_png = Image.open("static/logo.png")
favicon_png = Image.open("static/favicon.png")

st.set_page_config(
    page_title = "Rightank",
    page_icon = favicon_png,
    layout = "wide",
)

st.write('Rightank - Model Marketplace')
st.image(logo_png)
