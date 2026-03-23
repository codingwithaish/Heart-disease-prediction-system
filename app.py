import streamlit as st
import pandas as pd

from core_engine import (
    load_artifacts,
    feature_meta,
    get_risk_category
)

from ui.resource_loader import load_css
from ui.header_section import render_header
from ui.input_section import render_inputs
from ui.prediction_section import render_prediction
from ui.visualization_section import render_visualizations
from ui.recommendation_section import render_recommendations

from explainability.shap_text import shap_explanation_points

from services.recommendation_engine import personalized_recommendations
from services.pdf_report import build_pdf_report

st.set_page_config(
    page_title="Heart Disease Prediction System",
    layout="wide",
)

load_css()  
model, scaler, feature_columns = load_artifacts()  # Load ML artifacts
meta = feature_meta()  # Feature descriptions
render_header()  # Header
input_values, predict_clicked = render_inputs(feature_columns, meta)   # Input section

if predict_clicked:
   
    from explainability.shap_engine import compute_shap    # Import SHAP engine only when needed (faster startup)
    
    input_df = pd.DataFrame([input_values])[feature_columns]
    scaled_values = scaler.transform(input_df)
    probability = float(model.predict_proba(scaled_values)[0][1])
    category, category_style = get_risk_category(probability)

    shap_df, shap_values, expected_value, explainer = compute_shap(model, scaled_values, feature_columns, input_df)

    shap_points = shap_explanation_points(shap_df, probability, category, input_values)

    render_prediction(probability, category, category_style, shap_points)

    render_visualizations(shap_df, shap_values, expected_value, feature_columns, input_df, input_values)

    recommendations = personalized_recommendations(input_values, shap_df)

    render_recommendations(recommendations)

    report = build_pdf_report(input_values, probability, category, shap_points, recommendations)  
    st.download_button(
        label="Download Report (PDF)",
        data=report,
        file_name="heart_health_prediction_report.pdf",
        mime="application/pdf",
        use_container_width=True,
    )
