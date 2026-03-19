# ❤️ Heart Disease Prediction System

## 📌 Overview

This project is a **Machine Learning-based Heart Disease Prediction System** that analyzes user health data and predicts the risk of heart disease.
It also provides **explainable insights using SHAP** and visualizes feature importance for better understanding.

---

## 🚀 Features

* Predicts heart disease risk using ML models
* Uses **XGBoost, Decision Tree, and Logistic Regression**
* Automatically selects the **best-performing model**
* Provides **SHAP-based explanations** for predictions
* Displays **feature importance graphs & visualizations**
* Generates **personalized health recommendations**
* Allows **PDF report download**

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* XGBoost
* SHAP (Explainable AI)
* Pandas, NumPy
* Plotly, Matplotlib

---

## 📂 Project Structure

```
Heart-disease-prediction-system/
│── app.py
│── core_engine.py
│── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   └── feature_columns.pkl
│── ui/
│── explainability/
│── services/
│── assets/
│── styles/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/codingwithaish/Heart-disease-prediction-system.git
cd Heart-disease-prediction-system
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

*(If requirements.txt is not available, install manually)*

```
pip install streamlit pandas numpy scikit-learn xgboost shap plotly matplotlib joblib
```

---

## ▶️ Run the Application

```
streamlit run app.py
```

👉 The app will open in your browser.

---

## 🧠 How It Works

1. User enters health details
2. Input is preprocessed (structured + scaled)
3. Model predicts probability of heart disease
4. Risk is classified (Low / Moderate / High)
5. SHAP explains feature contributions
6. Results are visualized with graphs

---

## 📊 Model Details

* Logistic Regression (baseline model)
* Decision Tree (rule-based model)
* XGBoost (final selected model)

👉 Best model is selected based on **accuracy** and saved using `joblib`.

---

## 📈 Explainability

* Uses **SHAP (SHapley Additive Explanations)**
* Shows:

  * Feature contribution
  * Prediction breakdown
  * Key risk factors

---

## 📥 Output

* Risk percentage
* Risk category
* SHAP explanation
* Visual graphs
* Personalized recommendations
* Downloadable PDF report

---

## 👩‍💻 Author

**Aishwarya**

---

## ⭐ Note

Make sure the following files exist in the `models/` folder:

* `best_model.pkl`
* `scaler.pkl`
* `feature_columns.pkl`

---

## 📌 Future Improvements

* Add real-time health data integration
* Improve model accuracy with larger datasets
* Deploy as a web application

---
