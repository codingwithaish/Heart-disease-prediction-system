import streamlit as st
import plotly.graph_objects as go
import shap
import matplotlib.pyplot as plt


def _name(f):
    return "Male Gender" if f == "Gender" else f.replace("_", " ")


def render_visualizations(shap_df, shap_values, expected_value, feature_columns, input_df, input_values):
    d = shap_df.sort_values("SHAP_Value").tail(12) if len(shap_df) > 12 else shap_df.sort_values("SHAP_Value")
    d = shap_df.reindex(shap_df["Abs_SHAP"].nlargest(12).index).sort_values("SHAP_Value")
    fig = go.Figure(go.Bar(
        x=d["SHAP_Value"], y=[_name(f) for f in d["Feature"]], orientation="h",
        marker=dict(color=["#E5586F" if v > 0 else "#7FBF9E" for v in d["SHAP_Value"]], line=dict(width=0)),
        hovertemplate="<b>%{y}</b><br>Impact: %{x:+.3f}<extra></extra>"))
    fig.update_layout(
        title=dict(text="What pushed your risk up (red) or down (green)", font=dict(size=22, family="Fraunces, serif", color="#4A2F2C")),
        height=480, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Figtree, sans-serif", color="#7B5852"),
        xaxis=dict(gridcolor="rgba(74,47,44,.08)", zerolinecolor="rgba(74,47,44,.4)"),
        margin=dict(l=10, r=10, t=60, b=15))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="shap-title-white">Prediction breakdown</div>', unsafe_allow_html=True)
    explanation = shap.Explanation(values=shap_values, base_values=expected_value,
                                   data=input_df.iloc[0].values, feature_names=feature_columns)
    plt.figure(figsize=(8, 5))
    shap.plots.waterfall(explanation, max_display=10, show=False)
    st.pyplot(plt.gcf(), clear_figure=True)
