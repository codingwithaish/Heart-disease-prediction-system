def personalized_recommendations(user_input, category, shap_df):
    recommendation_map = {
        "Smoking": "Smoking is a key contributor. Reduce and quit smoking with a step-by-step quit plan.",
        "High_BP": "High blood pressure is contributing to risk. Check BP regularly and follow a low-salt diet.",
        "High_Cholesterol": "High cholesterol is increasing risk. Reduce fried/saturated fats and plan lipid follow-up.",
        "Diabetes": "Diabetes is contributing to risk. Keep sugar under control with regular monitoring and treatment adherence.",
        "Sedentary_Lifestyle": "Low activity is a major factor. Add at least 30 minutes of brisk walking most days.",
        "Obesity": "Weight is increasing your risk. Aim for gradual weight loss through diet and physical activity.",
        "Chronic_Stress": "Stress is affecting your heart-risk profile. Add daily stress management and proper sleep.",
        "Family_History": "Family history is present. Schedule regular preventive heart checkups.",
        "Chest_Pain": "Do not ignore chest pain. Seek medical evaluation quickly, especially if symptoms repeat.",
        "Shortness_of_Breath": "Breathlessness is a warning sign. Get a cardiac and respiratory checkup.",
        "Palpitations": "Frequent palpitations should be clinically evaluated with ECG/physician review.",
        "Dizziness": "Recurring dizziness should be medically assessed to rule out cardiovascular causes.",
        "Swelling": "Persistent swelling needs clinical assessment for blood pressure, kidney, and heart status.",
        "Pain_Arms_Jaw_Back": "Pain spreading to arm, jaw, or back can be serious. Seek timely medical advice.",
        "Cold_Sweats_Nausea": "Cold sweats/nausea with discomfort can indicate risk. Do not delay medical consultation.",
        "Fatigue": "Persistent fatigue may be linked to underlying health risk. Improve sleep and get clinical review.",
        "Gender": "Male gender is a non-modifiable risk factor; focus strongly on controllable lifestyle factors.",
        "Age": "Age-related risk is present; keep routine heart screening and preventive checkups.",
    }

    # Prioritize all selected user factors by SHAP values(absolute value)
    selected_features = [f for f, v in user_input.items() if v == 1 and f != "Age"]
    selected_ranked = shap_df[shap_df["Feature"].isin(selected_features)].sort_values(
        "Abs_SHAP", ascending=False
    )["Feature"].tolist()

    recs = []
    for feature in selected_ranked:
        # Never show a feature recommendation unless user selected it now.
        if user_input.get(feature, 0) != 1:
            continue
        if feature in recommendation_map:
            recs.append(recommendation_map[feature])

    # Add age recommendation when age is in higher-risk range.
    if user_input["Age"] >= 50:
        recs.append(recommendation_map["Age"])

    default_recs = [
        "Maintain a balanced diet rich in fruits, vegetables, and whole grains.",
        "Engage in at least 30 minutes of physical activity most days of the week.",
        "Ensure proper sleep and manage daily stress effectively.",
    ]
    if recs:
        recs = default_recs + recs
    else:
        recs = default_recs

    return recs
