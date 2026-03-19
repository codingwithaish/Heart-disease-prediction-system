import streamlit as st
from ui.resource_loader import get_img

def render_recommendations(recommendations):
    st.markdown('<div class="section-title">Personalized Recommendations</div>', unsafe_allow_html=True)
    rec_text_col, rec_img_col = st.columns([2.6, 1.4])
    with rec_text_col:
        for rec in recommendations:
            st.write(f"- {rec}")

    with rec_img_col:
        img6 = get_img("img6.png")
        if img6:
            st.image(str(img6), use_container_width=True)
