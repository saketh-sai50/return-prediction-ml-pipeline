import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

df = pd.read_csv("../data/processed/returns_features.csv")
X = df.drop(columns=["is_return"])
y = df["is_return"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)

mlflow.set_experiment("Product-Return-Prediction")
with mlflow.start_run():
    model.fit(X_train, y_train)
    preds = model.predict_proba(X_test)[:, 1]
    auc = roc_auc_score(y_test, preds)
    print("AUC:", auc)
    mlflow.log_metric("auc", auc)
    mlflow.sklearn.log_model(model, "random_forest_model")
