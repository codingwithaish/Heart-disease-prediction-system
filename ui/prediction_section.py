import streamlit as st
from ui.resource_loader import img_b64

COLORS = {"pill-low": "#5FBF98", "pill-medium": "#F2A94E", "pill-high": "#E5586F"}
MESSAGES = {"pill-low": "Your profile looks healthy. Keep it up!",
            "pill-medium": "Some risk signals found. Small changes can help a lot.",
            "pill-high": "Strong risk signals found. Please consult a doctor soon."}


def render_prediction(probability, category, category_style, shap_points):
    pct = probability * 100
    color = COLORS.get(category_style, "#E98AA0")
    points = "".join(f"<li>{p}</li>" for p in shap_points)
    st.markdown(f"""
<div id="result" class="section-title">Your result</div>
<div class="result-grid">
  <div class="result-img"><img src="{img_b64('img3.png', 560)}"/></div>
  <div class="ring-card">
    <div class="ring" style="--target:{pct:.1f};--p:{pct:.1f};--c:{color}">
      <div class="ring-inner"><div class="count" style="--target:{round(pct)}"></div><small>RISK</small></div>
    </div>
    <span class="risk-pill {category_style}">{category}</span>
    <p class="verdict">{MESSAGES.get(category_style, '')}</p>
    <div class="scale"><i style="left:{pct:.1f}%;background:{color}"></i></div>
    <div class="scale-lbl"><span>Low</span><span>Moderate</span><span>High</span></div>
  </div>
  <div class="why-card"><h4>🧠 Why this prediction?</h4><ul>{points}</ul></div>
</div>""", unsafe_allow_html=True)
    st.toast(f"{category}: {pct:.1f}%", icon="🫀")
