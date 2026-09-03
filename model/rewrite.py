import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(
    BASE_DIR,
    "final_heat_dataset.csv"
)

print("Loading:", csv_path)

df = pd.read_csv(csv_path)

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

print("\nDuplicate Columns:")
print(df.columns[df.columns.duplicated()].tolist())