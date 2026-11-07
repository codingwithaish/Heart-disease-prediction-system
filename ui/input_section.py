import streamlit as st
from ui.resource_loader import img_b64

GROUPS = [
    ("🩺", "Symptoms", "What are you feeling right now?",
     ["Chest_Pain", "Shortness_of_Breath", "Fatigue", "Palpitations", "Dizziness",
      "Swelling", "Pain_Arms_Jaw_Back", "Cold_Sweats_Nausea"]),
    ("💊", "Medical history", "Diagnosed conditions & family background",
     ["High_BP", "High_Cholesterol", "Diabetes", "Obesity", "Family_History"]),
    ("🏃", "Lifestyle", "Daily habits that shape heart health",
     ["Smoking", "Sedentary_Lifestyle", "Chronic_Stress"]),
]
ICONS = {"Chest_Pain": "💢", "Shortness_of_Breath": "🌬️", "Fatigue": "😴", "Palpitations": "💓",
         "Dizziness": "💫", "Swelling": "🦶", "Pain_Arms_Jaw_Back": "💪", "Cold_Sweats_Nausea": "🥶",
         "High_BP": "🩸", "High_Cholesterol": "🧈", "Diabetes": "🍬", "Obesity": "⚖️",
         "Family_History": "🧬", "Smoking": "🚬", "Sedentary_Lifestyle": "🛋️", "Chronic_Stress": "🤯",
         "Gender": "🚹"}


def _label(f):
    name = "Gender (Male)" if f == "Gender" else f.replace("_", " ")
    return f"{ICONS.get(f, '•')}  {name}"


def render_inputs(feature_columns, meta):
    st.markdown('<div class="section-title">Your health profile</div>'
                '<p class="tagline">Tap every item that applies. Hover the <b>?</b> for a plain-English explanation.</p>',
                unsafe_allow_html=True)
    left, right = st.columns([3, 1.1], gap="large")
    values = {}

    with right:
        live = st.empty()  # filled after we know the selections

    with left:
        cols = st.columns(3, gap="medium")
        for col, (icon, title, sub, feats) in zip(cols, GROUPS):
            with col, st.container(border=True):
                st.markdown(f'<div class="card-head"><span>{icon}</span><div><b>{title}</b><small>{sub}</small></div></div>',
                            unsafe_allow_html=True)
                for f in feats:
                    if f in feature_columns:
                        values[f] = int(st.checkbox(_label(f), key=f"input_{f}", help=meta.get(f)))

        with st.container(border=True):
            st.markdown('<div class="card-head"><span>👤</span><div><b>About you</b><small>Age and biological sex used by the model</small></div></div>',
                        unsafe_allow_html=True)
            a, b = st.columns([3, 1])
            with a:
                values["Age"] = st.slider("Age", 18, 100, 45, help=meta["Age"])
            with b:
                if "Gender" in feature_columns:
                    values["Gender"] = int(st.checkbox(_label("Gender"), key="input_Gender", help=meta["Gender"]))

        # make sure every model column exists
        for f in feature_columns:
            values.setdefault(f, 0)

        predict_clicked = st.button("Analyse my heart health  →", type="primary", use_container_width=True)

    chosen = [f for f, v in values.items() if v == 1 and f not in ("Age", "Gender")]
    chips = "".join(f'<span class="chip">{ICONS.get(f, "")} {f.replace("_", " ")}</span>' for f in chosen) \
        or '<span class="muted">Nothing selected yet</span>'
    live.markdown(f"""
<div class="live-card">
  <div class="bubble beat"><img src="{img_b64('heart_anatomy.png', 420)}"/></div>
  <div class="live-count"><b>{len(chosen)}</b> factor{'s' if len(chosen) != 1 else ''} selected</div>
  <div class="chips">{chips}</div>
</div>""", unsafe_allow_html=True)

    return values, predict_clicked
