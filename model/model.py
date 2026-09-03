import pandas as pd
import numpy as np
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from xgboost import XGBRegressor

# =====================================
# LOAD DATA
# =====================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(
    BASE_DIR,
    "final_heat_dataset.csv"
)

print("Loading:", csv_path)

df = pd.read_csv(csv_path)

print("\nDataset Shape:", df.shape)

# =====================================
# TARGET COLUMN
# =====================================

target_col = "temperature_(°c)"

# =====================================
# REMOVE NULLS
# =====================================

df = df.dropna()

# =====================================
# ENCODE CATEGORICAL FEATURES
# =====================================

encoders = {}

for col in df.columns:

    if col == target_col:
        continue

    if df[col].dtype == "object":

        le = LabelEncoder()

        df[col] = le.fit_transform(
            df[col].astype(str)
        )

        encoders[col] = le

# =====================================
# FEATURES / TARGET
# =====================================

X = df.drop(columns=[target_col])

y = df[target_col]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

# =====================================
# SPLIT DATA
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# =====================================
# MODEL
# =====================================

model = XGBRegressor(
    n_estimators=500,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    objective="reg:squarederror",
    random_state=42
)

print("\nTraining XGBoost...")

model.fit(
    X_train,
    y_train
)

# =====================================
# PREDICTIONS
# =====================================

y_pred = model.predict(X_test)

# =====================================
# METRICS
# =====================================

mae = mean_absolute_error(
    y_test,
    y_pred
)

rmse = np.sqrt(
    mean_squared_error(
        y_test,
        y_pred
    )
)

r2 = r2_score(
    y_test,
    y_pred
)

print("\n======================")
print("MODEL PERFORMANCE")
print("======================")

print(f"MAE  : {mae:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R²   : {r2:.4f}")

# =====================================
# FEATURE IMPORTANCE
# =====================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 15 Features:")
print(importance.head(15))

# =====================================
# SAVE MODEL
# =====================================

model_path = os.path.join(
    BASE_DIR,
    "urban_heat_xgboost.pkl"
)

joblib.dump(
    model,
    model_path
)

print("\nModel Saved:")
print(model_path)
