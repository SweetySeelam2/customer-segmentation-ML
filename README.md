📊 ****Customer Segmentation Using K-Means****

📝 **Project Overview**
This project applies an Unsupervised Machine learning model, **K-Means Clustering**, to segment customers based on their **Age, Annual Income, and Spending Score**. It helps businesses tailor their marketing strategies to identify different customer groups.

📂 **Dataset**
✅ 🔍 Key Features: The dataset contains customer information such as Annual Income(k$), Spending Score(1-100), Age, Gender, and Customer ID.
✅ 📄 Source: [Kaggle Mall Customers Dataset](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python)

📊 **Methodology**
✅ Data Cleaning, Preprocessing, and Visualization
✅ Exploratory Data Analysis (EDA)
✅ Standardization
✅ K-Means Clustering with Elbow method for Customer Segmentation  
✅ Visual analysis of clusters for Customer Groups
✅ Streamlit app for live predictions

💻 **Technologies**
✅ 🐍 Python  
✅ 📊 Pandas, NumPy  
✅ 📉 Matplotlib, Seaborn  
✅ 📡 Scikit-learn  

📊 **Results**
Scatterplot clusters of 5 customer segments identified:
✅ Cluster 0 – Balanced Spenders (Light Pink, Central Circle):
Age 30–45, Income $40k–$70k, Score 40–60. Steady, loyal group with moderate spend—ideal for retention programs.
✅ Cluster 1 – Affluent but Low Spend (Rose, Bottom Right):
Age 40–60, Income ≥$75k, Score ≤40. High income but under-engaged—target with premium re-engagement offers.
✅ Cluster 2 – Budget-Conscious Segment (Purple, Bottom Left):
Age 18–30, Income ≤$40k, Score ≤40. Young, price-sensitive group—focus on affordable bundles and discount campaigns.
✅ Cluster 3 – High-Spend Value Seekers (Dark Purple, Top Left):
Age 18–35, Income ≤$40k, Score ≥60. Loyal, low-income but high-spending—nurture with rewards and early access offers.
✅ Cluster 4 – Premium Customers (Deep Purple/Black, Top Right):
Age 25–50, Income ≥$70k, Score ≥60. Top-value customers—prioritize with VIP experiences and exclusive product access.

🧠 **Business Insights**
✅ Cluster 0 (Balanced Income & Spending):
Maintain loyalty with seasonal discounts, email engagement, and small-value perks.
✅ Cluster 1 (High Income, Low Spending):
These customers have money but don’t spend much.
Use personalized marketing, targeted promotions, or interest-based recommendations to unlock potential.
✅ Cluster 2 (Low Income, Low Spending):
Least profitable, but can be improved.
Use heavy discounts, referral programs, or entry-level product promotions to engage.
✅ Cluster 3 (Low Income, High Spending):
Loyal spenders despite income limitations.
Retain through affordable bundles, EMI plans, or cashback offers.
✅ Cluster 4 (High Income, High Spending):
Focus on VIP treatment, loyalty rewards, and exclusive deals.
The highest ROI segment for luxury and premium offerings.

💡 **Conclusion**
✅ Identify marketing & product strategies per cluster.
✅ Improve targeting, retention, and revenue.
✅ Deployable app for real-time customer input.
✅ Clustering using K-Means has provided actionable segmentation of your customer base. With focused targeting:
   - You can increase revenue by 20–30% from Clusters 1 & 4.
   - Reduce churn from Clusters 2 & 3 with retention strategies.
   - Make informed product & marketing investments.

📌 For detailed analysis, check the attached Jupyter Notebook.

📷 Visualization Example:
![Customer_segment_KMeans_cluster_plot](https://github.com/user-attachments/assets/4aad82c4-b9a3-4d0a-b7e5-9aae31b63f39)

📜 **How to Run the Project?**
🚀 Deployment
1️⃣ Clone this repository:
      git clone https://github.com/SweetySeelam2/customer-segmentation-ML.git
      cd customer-segmentation-ML
2️⃣ Install dependencies: (Make sure you’re in your project directory, then install all required libraries)
      pip install -r requirements.txt
3️⃣ Run the script: (Run the Streamlit dashboard locally)
      streamlit run app.py

🛠️ **Files Included**
✅ `Customer_Segmentation_KMeans_Clustering.ipynb` – Jupyter notebook for EDA & clustering
✅ `train_model.py` – Train & save KMeans model
✅ `model.pkl` – Trained model and scaler
✅ `app.py` – Streamlit app
✅ `requirements.txt` – Dependencies


   


🤝 Contributing
Feel free to fork this repo and create pull requests!

📩 Contact
👤 Sweety Seelam
📧 Email: sweetyseelam2@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/sweetyrao670/
