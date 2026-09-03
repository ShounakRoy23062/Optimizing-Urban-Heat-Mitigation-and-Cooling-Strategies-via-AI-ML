import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =========================
# LOAD DATASETS
# =========================

uhi = pd.read_csv(os.path.join(BASE_DIR, "clean_uhi.csv"))
weather = pd.read_csv(os.path.join(BASE_DIR, "clean_weather.csv"))
micro = pd.read_csv(os.path.join(BASE_DIR, "clean_micro.csv"))
env = pd.read_csv(os.path.join(BASE_DIR, "clean_india_env.csv"))
disease = pd.read_csv(os.path.join(BASE_DIR, "clean_disease.csv"))

# =========================
# CLEAN COLUMN NAMES
# =========================

for df in [uhi, weather, micro, env, disease]:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

# =========================
# WEATHER FEATURES
# =========================

weather_features = pd.DataFrame({
    "weather_temp_mean": [weather["temperature_2m_max"].mean()
                          if "temperature_2m_max" in weather.columns
                          else weather.iloc[:, 2].mean()],

    "weather_rain_mean": [weather["rain_sum"].mean()
                          if "rain_sum" in weather.columns
                          else 0],

    "weather_wind_mean": [weather["wind_speed_10m_max"].mean()
                          if "wind_speed_10m_max" in weather.columns
                          else weather.iloc[:, -3].mean()]
})

# =========================
# MICROCLIMATE FEATURES
# =========================

micro_features = pd.DataFrame({
    "micro_temp_mean": [micro["temperature"].mean()],
    "micro_humidity_mean": [micro["humidity"].mean()],
    "micro_ndvi_mean": [micro["ndvi"].mean()],
    "micro_solar_mean": [micro["solar_radiation"].mean()]
})

# =========================
# ENVIRONMENT FEATURES
# =========================

env_features = pd.DataFrame({
    "env_health_impact_mean": [env["health_impact"].mean()]
    if "health_impact" in env.columns else [0],

    "env_greenness_mean": [env["urban_greenness"].mean()]
    if "urban_greenness" in env.columns else [0],

    "env_air_quality_mean": [env["air_quality_index"].mean()]
    if "air_quality_index" in env.columns else [0]
})

# =========================
# DISEASE FEATURES
# =========================

disease_features = pd.DataFrame({
    "disease_rate_mean": [disease["disease_incidence_rate_(%)"].mean()]
    if "disease_incidence_rate_(%)" in disease.columns
    else [disease.iloc[:, -1].mean()]
})

# =========================
# ATTACH TO UHI DATASET
# =========================

final_df = uhi.copy()

for col in weather_features.columns:
    final_df[col] = weather_features[col].iloc[0]

for col in micro_features.columns:
    final_df[col] = micro_features[col].iloc[0]

for col in env_features.columns:
    final_df[col] = env_features[col].iloc[0]

for col in disease_features.columns:
    final_df[col] = disease_features[col].iloc[0]

# =========================
# SAVE
# =========================

output_file = os.path.join(BASE_DIR, "final_heat_dataset.csv")

final_df.to_csv(output_file, index=False)

print("\nFinal Dataset Created")
print(final_df.shape)

print("\nTarget Column:")
print("lst_(°c)")

print("\nSaved as:")
print(output_file)