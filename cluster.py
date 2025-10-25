import pandas as pd
import subprocess
from sklearn.cluster import KMeans

# load preprocessed dataset
df = pd.read_csv("data_preprocessed.csv")

# select numeric columns only
numeric_df = df.select_dtypes(include=["number"])

if numeric_df.shape[1] < 2:
    raise ValueError("Need at least 2 numeric columns for clustering.")

# apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(numeric_df)

# count samples per cluster
cluster_counts = df["Cluster"].value_counts().sort_index()

# save result
with open("clusters.txt", "w") as f:
    for cluster, count in cluster_counts.items():
        f.write(f"Cluster {cluster}: {count} samples\n")

print("Clustering complete! results saved in clusters.txt")
