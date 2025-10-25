import sys
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

if len(sys.argv) < 2:
    print("Usage: python Preprocess.py <path_to_csv>")
    sys.exit(1)

input_path = sys.argv[1]

# Load Dataset
try:
    df = pd.read_csv(input_path)
    print(f"dataset loaded!!")
except Exception as e:
    print(f"Error reading dataset: {e}")
    sys.exit(1)

# Data Cleaning
for col in df.columns:
    if df[col].dtype in ["int64", "float64"]:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

before = df.shape[0]
df.drop_duplicates(inplace=True)
after = df.shape[0]
print(f"Removed {before - after} duplicate rows.")

invalid_values = ["UNKNOWN", "ERROR", "N/A", "NULL", " "]
df.replace(invalid_values, pd.NA, inplace=True)

before = df.shape[0]
df.dropna(inplace=True)
after = df.shape[0]
print(f"Removed {before - after} rows with invalid inputs like 'UNKNOWN' or 'ERROR'.")

# Feature Transformation
categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()

if categorical_cols:
    le = LabelEncoder()
    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])
    print(f" Encoded categorical columns: {categorical_cols}")
else:
    print("No categorical columns found to encode.")

# Dimensionality Reduction
date_cols = [col for col in df.columns if "date" in col.lower()]
if date_cols:
    df.drop(columns=date_cols, inplace=True)
    print(f" Dropped date/time columns: {date_cols}")

# Save 
output_path = "data_preprocessed.csv"
df.to_csv(output_path, index=False)
print(f"data preprocessing complete and saved as {output_path}")

# Chain to next step
print(" Moving to analytics.py ...")
os.system(f"python Analytics.py {output_path}")
