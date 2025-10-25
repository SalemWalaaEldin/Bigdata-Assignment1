import sys
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import subprocess

if len(sys.argv) < 2:
    print("Usage: python visualize.py <preprocessed_csv>")
    sys.exit(1)

input_path = sys.argv[1] 

try:
    df = pd.read_csv(input_path)
    print(f"Loaded dataset: {input_path} with shape {df.shape}")
except Exception as e:
    print(f"Error loading dataset: {e}")
    sys.exit(1)

# detect numeric and categorical columns
numeric_cols = df.select_dtypes(include='number').columns
categorical_cols = df.select_dtypes(exclude='number').columns

# create a meaningful plot
plt.figure(figsize=(10, 6))

if len(numeric_cols) > 1:
    # correlation heatmap
    corr = df[numeric_cols].corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap of Numeric Features", fontsize=14)
    print("Created correlation heatmap.")
elif len(categorical_cols) > 0:
    # fallback: count plot of first categorical column 
    sns.countplot(x=categorical_cols[0], data=df)
    plt.title(f"distribution of {categorical_cols[0]}", fontsize=14)
    plt.xticks(rotation=45)
    print(f"created count plot for '{categorical_cols[0]}'.")
else:
    print("No suitable columns found for visualization.")
    sys.exit(0)

# Save plot
plt.tight_layout()
plt.savefig("summary_plot.png")
plt.close()
print("saved visualization as summary_plot.png")

# chain to next step
if os.path.exists("cluster.py"):
    print("moving to cluster.py ...")
    subprocess.run(["python", "cluster.py", input_path])
else:
    print("cluster.py not found. pipeline stopped here.")

