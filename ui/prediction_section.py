import streamlit as st
from ui.resource_loader import get_img

def render_prediction(probability, category, category_style, shap_points):
    st.markdown('<div class="section-title">Result</div>', unsafe_allow_html=True)
    img_col, gap_col, pred_col = st.columns([1.15, 0.38, 1.95])
    with img_col:
        img3 = get_img("img3.png")
        if img3:
            st.image(str(img3), use_container_width=True)

    with gap_col:
        st.write("")

    with pred_col:
        st.markdown(f'<div class="metric-big">Predicted Risk Level: {probability * 100:.2f}%</div>', unsafe_allow_html=True)
        st.markdown(f'Risk Category: <span class="risk-pill {category_style}">{category}</span>', unsafe_allow_html=True)
        st.markdown("**SHAP Explanation - Why this Prediction ?**")
        for point in shap_points:
            st.write(f"- {point}")

