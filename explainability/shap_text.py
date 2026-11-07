# creates human readable explanations based on 
# SHAP values and user input for the heart disease risk model
# It generates personalized insights about
# which factors are contributing to the user's risk category

def shap_explanation_points(shap_df, probability, category, user_input):

    # Helper function to format feature names for better readability in explanations
    # example High_BP -> High BP
    def fmt_feature(name):
        return "Male Gender" if name == "Gender" else name.replace("_", " ")

    # store user selected features in array
    # for ex if smoking:0, diabetes:1, then selected_risk_features = [diabetes]
    selected_risk_features = [
        f for f, v in user_input.items() if v == 1 and f != "Age"
    ]

    # select only user selected values & positive shap values which contribute to risk 
    # sort in descending order and store in array
    selected_with_positive_shap = shap_df[
        (shap_df["Feature"].isin(selected_risk_features)) & (shap_df["SHAP_Value"] > 0)
    ].sort_values("SHAP_Value", ascending=False)["Feature"].tolist()

    # take top 4 features 
    # if no features are selected by user, then
    # take top 4 features with highest shap values regardless of user selection
    top_selected = selected_with_positive_shap[:4] if selected_with_positive_shap else selected_risk_features[:4]
    top_selected_text = (
        ", ".join([fmt_feature(f) for f in top_selected])
        if top_selected
        else "No major selected risk factors"
    )

    age = user_input["Age"]
    if age >= 60:
        age_line = "Age is in a higher-risk range and added to the risk score."
    elif age <= 35:
        age_line = "Age is in a lower-risk range and kept the risk score lower."
    else:
        age_line = "Age is in a mid-range group with moderate influence on risk."

    if category == "Low Risk":
        return [
            f"Most major risk conditions/symptoms were not selected in your input.",
            f"Risk factors currently selected: {top_selected_text}.",
            age_line,
            "Overall, the model found no strong high-risk pattern in your profile.",
        ]
    if category == "Moderate Risk":
        return [
            f"Some important risk conditions/symptoms were selected, raising your score.",
            f"Main contributing selected factors: {top_selected_text}.",
            age_line,
            "Overall, the model detected a medium-risk pattern that needs lifestyle attention.",
        ]
    return [
        f"Several important risk conditions/symptoms were selected, strongly raising your score.",
        f"Main contributing selected factors: {top_selected_text}.",
        age_line,
        "Overall, the model detected a high-risk pattern and recommends urgent preventive action.",
    ]