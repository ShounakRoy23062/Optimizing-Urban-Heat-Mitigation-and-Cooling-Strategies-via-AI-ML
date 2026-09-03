import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# LOAD DATASETS
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

india_env = pd.read_csv(
    os.path.join(BASE_DIR, "india_cities_dataset_2021_2025.csv")
)

weather = pd.read_csv(
    os.path.join(BASE_DIR, "india_2000_2024_daily_weather.csv")
)

disease = pd.read_csv(
    os.path.join(BASE_DIR, "Disease_Incidence_Rate.csv")
)

uhi = pd.read_csv(
    os.path.join(BASE_DIR, "urban_heat_island_dataset.csv")
)

micro = pd.read_csv(
    os.path.join(BASE_DIR, "Microclimate_dataset.csv")
)

# ==========================================
# STANDARDIZE COLUMN NAMES
# ==========================================

datasets = [india_env, weather, disease, uhi, micro]

for df in datasets:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

# ==========================================
# BASIC INFO
# ==========================================

names = [
    "Environmental",
    "Weather",
    "Disease",
    "UHI",
    "Microclimate"
]

for name, df in zip(names, datasets):

    print(f"\n{'='*50}")
    print(name)
    print('='*50)

    print("Shape:", df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nMissing Values:")
    print(df.isnull().sum())

# ==========================================
# REMOVE DUPLICATES
# ==========================================

for i in range(len(datasets)):
    datasets[i] = datasets[i].drop_duplicates()

india_env, weather, disease, uhi, micro = datasets

# ==========================================
# FILL MISSING VALUES
# ==========================================

def fill_missing(df):

    numeric_cols = df.select_dtypes(
        include=np.number
    ).columns

    for col in numeric_cols:
        df[col] = df[col].fillna(
            df[col].median()
        )

    return df

india_env = fill_missing(india_env)
weather = fill_missing(weather)
disease = fill_missing(disease)
uhi = fill_missing(uhi)
micro = fill_missing(micro)

# ==========================================
# SAVE CLEANED FILES
# ==========================================

india_env.to_csv(
    os.path.join(BASE_DIR, "clean_india_env.csv"),
    index=False
)

weather.to_csv(
    os.path.join(BASE_DIR, "clean_weather.csv"),
    index=False
)

disease.to_csv(
    os.path.join(BASE_DIR, "clean_disease.csv"),
    index=False
)

uhi.to_csv(
    os.path.join(BASE_DIR, "clean_uhi.csv"),
    index=False
)

micro.to_csv(
    os.path.join(BASE_DIR, "clean_micro.csv"),
    index=False
)

print("\nCleaned files saved successfully!")

# ==========================================
# VISUAL EDA
# ==========================================

all_data = pd.concat(
    [
        india_env.select_dtypes(include=np.number),
        weather.select_dtypes(include=np.number),
        disease.select_dtypes(include=np.number),
        uhi.select_dtypes(include=np.number),
        micro.select_dtypes(include=np.number)
    ],
    axis=1
)

# Remove duplicate column names
all_data = all_data.loc[:, ~all_data.columns.duplicated()]

# ==========================================
# CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(14, 10))

sns.heatmap(
    all_data.corr(numeric_only=True),
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.show()

# ==========================================
# DISTRIBUTIONS
# ==========================================

for col in all_data.columns[:10]:

    plt.figure(figsize=(6,4))

    sns.histplot(
        all_data[col],
        kde=True
    )

    plt.title(col)

    plt.show()

# ==========================================
# OUTLIER DETECTION
# ==========================================

for col in all_data.columns[:10]:

    plt.figure(figsize=(6,4))

    sns.boxplot(
        x=all_data[col]
    )

    plt.title(f"Outliers - {col}")

    plt.show()

print("\nEDA Completed Successfully!")