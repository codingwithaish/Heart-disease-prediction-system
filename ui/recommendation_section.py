import streamlit as st
from ui.resource_loader import img_b64


HABITS = [
    ("food.png", "Eat well", "Fill half your plate with vegetables, choose lean protein and whole grains, and go easy on salt and fried food."),
    ("run.png", "Keep moving", "Aim for about 150 minutes of brisk activity a week, which is roughly 30 minutes on most days."),
    ("sleep.png", "Sleep & recover", "Regular 7-9 hours of sleep supports healthy blood pressure and helps manage stress."),
]


def render_recommendations(recommendations):
    habits = "".join(
        f'<div class="habit"><div class="tile"><img src="{img_b64(img, 360)}"/></div><h4>{t}</h4><p>{d}</p></div>'
        for img, t, d in HABITS)
    cards = "".join(f'<div class="rec"><span class="rec-n">{i:02d}</span><p>{r}</p></div>'
                    for i, r in enumerate(recommendations, 1))
    st.markdown(f"""
<div class="rec-wrap">
  <div class="rec-grid">{cards}</div>
  <div class="rec-art"><img src="{img_b64('img6.png', 700)}"/></div>
</div>
<div class="habits-title">Daily heart habits</div><div class="habits">{habits}</div>
<p class="muted center">⚕️ This tool is for awareness only and is not a medical diagnosis.</p>""",
                unsafe_allow_html=True)
