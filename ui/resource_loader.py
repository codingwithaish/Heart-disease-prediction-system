import streamlit as st
from pathlib import Path

# Base directories
BASE_DIR = Path(__file__).parent.parent
ASSETS_DIR = BASE_DIR / "assets"
STYLES_DIR = BASE_DIR / "styles"

# CSS Loader
def load_css():
    css_path = STYLES_DIR / "styles.css"

    st.markdown(
        f"<style>{css_path.read_text()}</style>",
        unsafe_allow_html=True
    )

#load images
def get_img(name):
    path = ASSETS_DIR / name
    return path if path.exists() else None