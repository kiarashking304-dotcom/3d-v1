import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="نمایشگر DFF و TXD", page_icon="🚗", layout="wide")
st.markdown("<style>.block-container{padding:0.5rem 0.5rem 0}header{visibility:hidden}</style>", unsafe_allow_html=True)

html = (Path(__file__).parent / "viewer.html").read_text(encoding="utf-8")
components.html(html, height=800, scrolling=False)
