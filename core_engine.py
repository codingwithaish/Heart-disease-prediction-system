import joblib
import streamlit as st
from pathlib import Path

def feature_meta():
    return {
        "Chest_Pain": "Presence of chest pain or chest discomfort.",
        "Shortness_of_Breath": "Difficulty in breathing during activity or rest.",
        "Fatigue": "Persistent tiredness not explained by usual activity.",
        "Palpitations": "Feeling of irregular or rapid heartbeat.",
        "Dizziness": "Frequent lightheadedness or balance issues.",
        "Swelling": "Swelling in ankles, feet, or legs (fluid buildup).",
        "Pain_Arms_Jaw_Back": "Pain radiating to arms, jaw, or upper back.",
        "Cold_Sweats_Nausea": "Episodes of cold sweats or nausea.",
        "High_BP": "History of high blood pressure.",
        "High_Cholesterol": "History of elevated blood cholesterol.",
        "Diabetes": "Presence of diabetes diagnosis.",
        "Smoking": "Current smoking habit.",
        "Obesity": "Weight level in obese range.",
        "Sedentary_Lifestyle": "Low physical activity in daily routine.",
        "Family_History": "Family history of heart disease.",
        "Chronic_Stress": "Long-term ongoing stress exposure.",
        "Gender": "Biological sex used in model (0 = Female, 1 = Male).",
        "Age": "Current age in years.",
    }

MODELS_DIR = Path(__file__).resolve().parent / "models"      #load models

@st.cache_resource   
def load_artifacts():
    model = joblib.load(MODELS_DIR / "best_model.pkl")
    scaler = joblib.load(MODELS_DIR / "scaler.pkl")
    feature_columns = joblib.load(MODELS_DIR / "feature_columns.pkl")

    return model, scaler, feature_columns

def get_risk_category(probability):
    if probability < 0.35:
        return "Low Risk", "pill-low"
    if probability < 0.70:
        return "Moderate Risk", "pill-medium"
    
    return "High Risk", "pill-high"