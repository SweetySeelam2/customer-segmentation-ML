<<<<<<< HEAD
import os
import pandas as pd
import pickle
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load data
data_path = os.path.join("data", "Mall_Customers.csv")
df = pd.read_csv(data_path)
X = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
kmeans.fit(X_scaled)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump({"model": kmeans, "scaler": scaler}, f)

# Inverse transform centroids
centroids = scaler.inverse_transform(kmeans.cluster_centers_)
cent_df = pd.DataFrame(
    centroids,
    columns=["Age", "Annual Income (k$)", "Spending Score (1-100)"]
)
cent_df["Cluster"] = cent_df.index

# Manual cluster segment assignments from scatter plot
segment_map = {
    0: ("Balanced Spenders", "Light Pink", "Center"),
    1: ("Premium Customers", "Pink", "Top-right"),
    2: ("High-Spend Value Seekers", "Purple", "Top-left"),
    3: ("Budget-Conscious Segment", "Dark Purple", "Bottom-left"),
    4: ("Affluent but Low Spend", "Black", "Bottom-right"),
}
cent_df[["Label", "Color", "Plot Position"]] = cent_df["Cluster"].apply(lambda c: pd.Series(segment_map[c]))

# Remove old file if exists
out_path = "cluster_centroids.csv"
if os.path.exists(out_path):
    try:
        os.remove(out_path)
    except PermissionError:
        print(f"⚠️ Cannot overwrite {out_path}, please close the file and retry.")
        raise

# Save new centroids
cent_df.to_csv(out_path, index=False)
print("✅ Final cluster_centroids.csv saved:")
print(cent_df[["Cluster", "Age", "Annual Income (k$)", "Spending Score (1-100)", "Label", "Color", "Plot Position"]])
=======
import os
import pandas as pd
import pickle
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

# Load data
data_path = os.path.join("data", "Mall_Customers.csv")
df = pd.read_csv(data_path)
X = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
kmeans.fit(X_scaled)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump({"model": kmeans, "scaler": scaler}, f)

# Inverse transform centroids
centroids = scaler.inverse_transform(kmeans.cluster_centers_)
cent_df = pd.DataFrame(
    centroids,
    columns=["Age", "Annual Income (k$)", "Spending Score (1-100)"]
)
cent_df["Cluster"] = cent_df.index

# Manual cluster segment assignments from scatter plot
segment_map = {
    0: ("Balanced Spenders", "Light Pink", "Center"),
    1: ("Premium Customers", "Pink", "Top-right"),
    2: ("High-Spend Value Seekers", "Purple", "Top-left"),
    3: ("Budget-Conscious Segment", "Dark Purple", "Bottom-left"),
    4: ("Affluent but Low Spend", "Black", "Bottom-right"),
}
cent_df[["Label", "Color", "Plot Position"]] = cent_df["Cluster"].apply(lambda c: pd.Series(segment_map[c]))

# Remove old file if exists
out_path = "cluster_centroids.csv"
if os.path.exists(out_path):
    try:
        os.remove(out_path)
    except PermissionError:
        print(f"⚠️ Cannot overwrite {out_path}, please close the file and retry.")
        raise

# Save new centroids
cent_df.to_csv(out_path, index=False)
print("✅ Final cluster_centroids.csv saved:")
print(cent_df[["Cluster", "Age", "Annual Income (k$)", "Spending Score (1-100)", "Label", "Color", "Plot Position"]])
>>>>>>> 33ad6eab409b2fb681203bc4b60e2988192331fe
