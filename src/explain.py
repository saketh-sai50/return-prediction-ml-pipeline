import pandas as pd
import shap
import joblib
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("../data/processed/returns_features.csv")
X = df.drop(columns=["is_return"])
model = joblib.load("../models/model.pkl")

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)
shap.summary_plot(shap_values[1], X)
