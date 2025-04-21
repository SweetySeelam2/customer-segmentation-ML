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
✅ Cluster 0 – Balanced Spenders (Light Pink)
Customers aged 30–45 with moderate income ($40k–$60k) and moderate spending scores (40–60). They are stable, regular shoppers forming your core revenue base and are ideal for loyalty and retention strategies.
✅ Cluster 1 – Premium Customers (Pink)
Young to middle-aged professionals (25–45 years) with high income ($60k–$130k) and very high spending scores (60–100). They are your most profitable segment, responsive to premium offerings, exclusivity, and VIP engagement.
✅ Cluster 2 – High-Spend Value Seekers (Purple)
Primarily 18–35 year olds with low-to-mid income ($15k–$60k) but high spending scores (60–100). They are highly engaged, trend-driven shoppers who spend frequently despite limited income, making them ideal for budget-friendly premium promotions.
✅ Cluster 3 – Budget-Conscious Segment (Dark Purple)
Typically aged 30–50, these customers have low income ($15k–$60k) and low spending scores (0–40). They are cautious, value-focused buyers likely to respond to discounts, essentials, and practical deals.
✅ Cluster 4 – Affluent but Low Spend (Very Dark Purple / Black)
Older individuals aged 40–70 with high income ($70k–$140k) but very low spending scores (0–40). This under-engaged segment has strong purchasing power and should be reactivated with personalized luxury offers and exclusive experiences.

🧠 **Recommendations**
✅ Cluster 0 (Balanced Spenders):
Loyalty programs, cashback, occasional discounts.
Encourage frequency and upsell to mid-premium segments.
✅ Cluster 1 (Premium Customers):
VIP services, exclusive launches, and tailored experiences.
Retention is critical — give them a sense of prestige.
✅ Cluster 2 (Young High Spenders):
Trendy, limited-time offers, loyalty points.
Promote through social media, influencers.
✅ Cluster 3 (Budget-Conscious):
Discount campaigns, value packs, seasonal deals.
Keep messaging around savings and practicality.
✅ Cluster 4 (Affluent but Frugal):
Personalized re-engagement emails, luxury sampling.
Focus on what they’re missing, not what they get.

💡 **Conclusion**
✅ Identify marketing & product strategies per cluster.
✅ Improve targeting, retention, and revenue.
✅ Deployable app for real-time customer input.
✅ Clustering using K-Means has provided actionable segmentation of your customer base. With focused targeting:
   - You can increase revenue by 25–35% from Clusters 1 & 4.
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
