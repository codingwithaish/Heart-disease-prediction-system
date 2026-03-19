def compute_shap(model, scaled_values, feature_columns, input_df):
    import shap
    import numpy as np
    import pandas as pd
    
    # Create SHAP explainer
    explainer = shap.TreeExplainer(model)

    # Compute SHAP values
    shap_raw = explainer.shap_values(scaled_values)

    # Handle model outputs (XGBoost / sklearn)
    if isinstance(shap_raw, list):
        shap_values = np.array(shap_raw[1])[0]
    else:
        shap_values = np.array(shap_raw)[0]

    # Get expected value
    expected = explainer.expected_value

    if isinstance(expected, (list, np.ndarray)):
        expected_value = float(np.array(expected).flatten()[-1])
    else:
        expected_value = float(expected)

    # Build SHAP dataframe
    shap_df = pd.DataFrame(
        {
            "Feature": feature_columns,
            "SHAP_Value": shap_values,
            "Abs_SHAP": np.abs(shap_values),
            "User_Value": input_df.iloc[0].values,
        }
    ).sort_values("Abs_SHAP", ascending=False)

    return shap_df, shap_values, expected_value, explainer