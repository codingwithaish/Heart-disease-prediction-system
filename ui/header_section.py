import streamlit as st
from ui.resource_loader import get_img

def render_header():
    top_left, top_mid = st.columns([1.45, 4.45])

    with top_left:
        img2 = get_img("img2.png")
        if img2:
            st.markdown('<div class="floating-image">', unsafe_allow_html=True)
            st.image(str(img2), use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)

    with top_mid:
        st.markdown('<div class="hero-title">HEART DISEASE<br>PREDICTION SYSTEM</div>', unsafe_allow_html=True)

    st.markdown('<div class="hero-card">This system predicts heart disease risk from symptoms, lifestyle, and clinical factors. You can review not only your risk score, but also why the model reached that result.</div>', unsafe_allow_html=True)
