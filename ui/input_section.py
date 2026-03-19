import streamlit as st
from ui.resource_loader import get_img

def render_inputs(feature_columns, meta):
    input_left, input_right = st.columns([2.4, 1.2])
    input_values = {}

    with input_left:
        st.markdown('<div class="section-title">Enter Your Details and Check Your Heart Health.</div>',unsafe_allow_html=True,)
        st.markdown('<h3 class="tagline">Select the features that apply to you.</h3>',unsafe_allow_html=True,)
        binary_features = [f for f in feature_columns if f != "Age"]
        col1, col2, col3 = st.columns(3)
        for i, feature in enumerate(binary_features):
            target_col = [col1, col2, col3][i % 3]
            with target_col:
                if feature == "Gender":
                    checked = st.checkbox(
                        "Gender (Male)",
                        value=False,
                        key=f"input_{feature}",
                        help=meta[feature],
                    )
                else:
                    checked = st.checkbox(
                        feature.replace("_", " "),
                        value=False,
                        key=f"input_{feature}",
                        help=meta[feature],
                    )
                input_values[feature] = int(checked)

        input_values["Age"] = st.slider(
            "Age",
            min_value=18,
            max_value=100,
            value=45,
            help=meta["Age"],
        )
        predict_clicked = st.button(
            "Predict",
            type="primary",
            use_container_width=True,
        )
    with input_right:
        img7 = get_img("img7.png")
        if img7:
            st.image(str(img7), use_container_width=True)

    return input_values, predict_clicked
