import streamlit as st
from ui.resource_loader import img_b64

ECG = """<svg class="ecg" viewBox="0 0 600 80" preserveAspectRatio="none"><path pathLength="1" d="M0 40 H120 l12-6 l12 6 H200 l10 0 l10-34 l14 68 l12-34 H330 l12-8 l14 8 H460 l10 0 l10-30 l14 60 l12-30 H600"/></svg>"""


def render_header():
    st.markdown(f"""
<div class="hero">
  <div class="hero-orb o1"></div><div class="hero-orb o2"></div>
  <div class="hero-text">
    <span class="badge">🫀 AI-powered, explainable, instant</span>
    <div class="hero-title">Know your <b class="hl">heart</b>.<br>Before it speaks.</div>
    <p class="hero-sub">Answer a few quick questions and our XGBoost model estimates your heart-disease risk,
    then uses SHAP to show <b>exactly why</b>, with a personal action plan you can download.</p>
    <div class="stat-row">
      <div class="stat"><b>18</b><span>health factors</span></div>
      <div class="stat"><b>SHAP</b><span>explainable AI</span></div>
      <div class="stat"><b>PDF</b><span>shareable report</span></div>
    </div>
    {ECG}
  </div>
  <div class="hero-art"><div class="art-frame"><div class="glow"></div><img src="{img_b64('img2.png')}" class="float-img"/><div class="shield-badge"><img src="{img_b64('shield.png', 220)}"/><span>Protected by AI</span></div></div></div>
</div>

<div class="steps">
  <div class="step"><div class="num">1</div><h4>Tell us about you</h4><p>Tick the symptoms, conditions and habits that apply.</p></div>
  <div class="step"><div class="num">2</div><h4>Get your risk score</h4><p>The model returns a probability and a risk category.</p></div>
  <div class="step"><div class="num">3</div><h4>Understand &amp; act</h4><p>See what drove the score and what to do next.</p></div>
  <div class="step img-step"><img src="{img_b64('checklist.png', 300)}"/><h4>Download report</h4></div>
</div>
""", unsafe_allow_html=True)
