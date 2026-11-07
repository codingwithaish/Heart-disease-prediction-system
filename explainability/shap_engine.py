# compute shap values and expected value for a given input and model

def compute_shap(model, scaled_values, feature_columns, input_df):
    import shap
    import numpy as np    #array handling
    import pandas as pd   #create dataframe for shap values
    
    # Create SHAP explainer
    explainer = shap.TreeExplainer(model)

    # Compute SHAP values that Calculates contribution of each feature
    shap_raw = explainer.shap_values(scaled_values)

    # SHAP returns values in a 2D structure even for a single input, [[]]
    # so we use [0] to extract that row.
    if isinstance(shap_raw, list):
        shap_values = np.array(shap_raw[1])[0]
    else:
        shap_values = np.array(shap_raw)[0]

    # Get expected value i.e avg value of shap_values
    expected = explainer.expected_value

    # if shap_raw is multiclass, then expected_value will be a list 
    # so we extract extracted_value for disesase class
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