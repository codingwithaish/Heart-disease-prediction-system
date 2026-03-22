import streamlit as st
import plotly.express as px
import shap
import matplotlib.pyplot as plt

def pretty_feature_name(feature_name):
    return "Male Gender" if feature_name == "Gender" else feature_name.replace("_", " ")

def render_visualizations(shap_df, shap_values, expected_value, feature_columns, input_df, input_values,):

    bar_fig = px.bar(
        shap_df.sort_values("SHAP_Value"),
        x="SHAP_Value",
        y="Feature",
        orientation="h",
        color="SHAP_Value",   #+ve values in green, -ve in red
        color_continuous_scale=["#1f9d55", "#f7fafc", "#e53e3e"],
        title="Feature Contribution to Risk",
    )

    bar_fig.update_layout(
        height=540,
        coloraxis_showscale=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(255,255,255,0.55)",
        font=dict(family="Outfit", color="#ffffff"),
        title_font=dict(family="Outfit", size=30, color="#ffffff"),
        margin=dict(l=10, r=10, t=55, b=15),
    )
    st.plotly_chart(bar_fig, use_container_width=True)

    st.markdown('<div class="shap-title-white">Prediction Breakdown</div>',unsafe_allow_html=True,)

    explanation = shap.Explanation(
        values=shap_values,
        base_values=expected_value,
        data=input_df.iloc[0].values,
        feature_names=feature_columns,
    )

    plt.figure(figsize=(1,0.5))
    shap.plots.waterfall(explanation, max_display=10, show=False)
    st.pyplot(plt.gcf(), clear_figure=True)

