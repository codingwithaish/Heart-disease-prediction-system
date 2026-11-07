import base64, io
import streamlit as st
from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).parent.parent
ASSETS_DIR = BASE_DIR / "assets"
STYLES_DIR = BASE_DIR / "styles"


def load_css():
    css = (STYLES_DIR / "styles.css").read_text()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def get_img(name):
    path = ASSETS_DIR / name
    return path if path.exists() else None


@st.cache_data(show_spinner=False)
def img_b64(name, max_px=720):
    """Return a downsized base64 data-URI so images can live inside custom HTML/CSS."""
    path = get_img(name)
    if not path:
        return ""
    im = Image.open(path).convert("RGBA")
    im.thumbnail((max_px, max_px))
    buf = io.BytesIO()
    im.save(buf, format="PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()
