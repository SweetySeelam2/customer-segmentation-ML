import streamlit as st
import pandas as pd
import pickle
import numpy as np
from scipy.spatial.distance import cdist

@st.cache_resource
def load_model():
    return pickle.load(open("model.pkl", "rb"))

md = load_model()
model, scaler = md["model"], md["scaler"]

try:
    cent = pd.read_csv("cluster_centroids.csv")
    label_map = {int(r["Cluster"]): r["Label"] for _, r in cent.iterrows()}
    color_map = {int(r["Cluster"]): r["Color"] for _, r in cent.iterrows()}
    position_map = {int(r["Cluster"]): r["Plot Position"] for _, r in cent.iterrows()}
    st.sidebar.subheader("🔍 Cluster Metadata")
    st.sidebar.dataframe(cent[["Cluster", "Age", "Annual Income (k$)", "Spending Score (1-100)", "Label", "Color", "Plot Position"]])
except FileNotFoundError:
    st.sidebar.error("Missing cluster_centroids.csv. Please run train_model.py")

# Load dataset for range calibration
df_raw = pd.read_csv("data/Mall_Customers.csv")
age_default = int(df_raw["Age"].median())
inc_min, inc_max = int(df_raw["Annual Income (k$)"].min()), int(df_raw["Annual Income (k$)"].max())
score_min, score_max = int(df_raw["Spending Score (1-100)"].min()), int(df_raw["Spending Score (1-100)"].max())

# Cluster descriptions
descriptions = {
    0: "**Cluster 0 – Balanced Spenders**\n\n- Insight: Steady, average-spending customers.\n\n- Recommendation: Loyalty programs, cashback, occasional discounts. Encourage frequency and upsell to mid-premium segments.",
    1: "**Cluster 1 – Premium Customers**\n\n- Insight: Wealthy, frequent spenders — top-tier value.\n\n- Recommendation: VIP services, exclusive launches, tailored experiences. Retention is critical — give them a sense of prestige.",
    2: "**Cluster 2 – High-Spend Value Seekers**\n\n- Insight: Trend-focused shoppers despite lower income.\n\n- Recommendation: Trendy, limited-time offers, loyalty points. Promote through social media, influencers.",
    3: "**Cluster 3 – Budget-Conscious Segment**\n\n- Insight: Conservative spenders, respond to value deals.\n\n- Recommendation: Discount campaigns, value packs, seasonal deals. Keep messaging around savings and practicality.",
    4: "**Cluster 4 – Affluent but Low Spend**\n\n- Insight: Wealthy but cautious — potential if engaged.\n\n- Recommendation: Personalized re-engagement emails, luxury sampling. Focus on what they’re missing, not what they get."
}

segment_notes = {
    0: "Moderate income & spend. Represents stable, average shoppers.",
    1: "High income & high spend — great for luxury or loyalty focus.",
    2: "Young, lower income but strong spending habits — trend seekers.",
    3: "Careful, price-sensitive — may need discount or essential targeting.",
    4: "High potential, low current spend — reactivation target."
}

# UI
st.title("🧠 Customer Segmentation with KMeans (Machine learning) model")
st.markdown("Select customer features: Annual income(k$) and Spending score(1-100) to predict their customer segment.\n\n**Note:** Prediction is based on standardized distance to cluster centroid, but not solely on the value ranges of Income or Spending score")

income = st.slider("Annual Income (k$)", inc_min, inc_max, (inc_min + inc_max) // 2)
score = st.slider("Spending Score (1-100)", score_min, score_max, (score_min + score_max) // 2)

if st.button("Predict Segment"):
    inp = pd.DataFrame([[age_default, income, score]], columns=["Age", "Annual Income (k$)", "Spending Score (1-100)"])
    scaled = scaler.transform(inp)
    clust = model.predict(scaled)[0]

    st.success(f"🎯 Predicted Cluster: **{clust}**")
    st.info(f"🧠 Segment Label: **{label_map[clust]}**")
    st.markdown(descriptions.get(clust, "No description available."))
    st.markdown(f"📌 **Business Insight:** {segment_notes.get(clust, '')}")

    dists = cdist(scaled, model.cluster_centers_)[0]
    with st.expander("🔎 Distances to all clusters"):
        for i in np.argsort(dists):
            st.write(f"Cluster {i}: {label_map[i]} — Distance: {dists[i]:.3f}")

# Bulk prediction
st.header("📁 Bulk Prediction")
uploaded = st.file_uploader("Upload CSV with Annual Income (k$), Spending Score (1-100), and Age.\n\n**Note:** Age is optional, and in case if the uploaded CSV does not contain the Age column, then app automatically fills an Age column with a default value - median Age value to keep predictions consistent and avoid failure.", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    if "Age" not in df:
        df["Age"] = age_default
    X = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]
    X_scaled = scaler.transform(X)
    df["Predicted Cluster"] = model.predict(X_scaled)
    df["Segment Label"] = df["Predicted Cluster"].map(label_map)
    df["Insight"] = df["Predicted Cluster"].map(segment_notes)
    st.success("✅ Predictions complete!")
    st.dataframe(df)
    st.download_button("📥 Download Results", data=df.to_csv(index=False).encode("utf-8"), file_name="bulk_predictions.csv")
