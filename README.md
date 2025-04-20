# 📊 Customer Segmentation Using K-Means

## 📝 Project Overview
This project applies **K-Means Clustering** to segment customers based on their **Annual Income and Spending Score**. It helps businesses tailor their marketing strategies for different customer groups.

## 📂 Dataset
- The dataset contains customer information such as Annual Income, Spending Score, Gender, Age, and Customer ID.
- 📄 Source: [Kaggle Mall Customers Dataset](https://www.kaggle.com/vjchoudhary7/customer-segmentation-tutorial-in-python)

## 🔍 Key Features
✅ Data Cleaning & Preprocessing  
✅ Exploratory Data Analysis (EDA)  
✅ K-Means Clustering for Customer Segmentation  
✅ Visualizing Customer Groups  

## 💻 Technologies Used
- 🐍 Python  
- 📊 Pandas, NumPy  
- 📉 Matplotlib, Seaborn  
- 📡 Scikit-learn  

## 📜 How to Run the Project?
1️⃣ Clone this repository:  
   ```
   git clone https://github.com/SweetySeelam2/customer-segmentation-ML.git
   cd customer-segmentation-ML
2️⃣ Install dependencies:
pip install -r requirements.txt
3️⃣ Run the script:
python customer_segmentation.py

📊 Results
Scatterplot clusters of 5 customer segments identified:
--Cluster 0 – Light Pink (Center):
Customers with annual income between $40k–$70k and spending scores of 40–60, representing a balanced group with steady and moderate purchasing behavior.
--Cluster 1 – Rose/Pink (Bottom Right):
High-income individuals (≥ $75k) with low spending scores (≤ 40) who are under-engaged and have the potential to be converted into active buyers.
--Cluster 2 – Purple (Bottom Left):
Customers earning ≤ $40k with low spending scores (≤ 40) who are budget-conscious and require strong value-driven incentives to spend more.
--Cluster 3 – Dark Purple (Top Left):
Low-income consumers (≤ $40k) with high spending scores (≥ 60), likely younger or value-seeking buyers who shop frequently despite financial constraints.
--Cluster 4 – Deep Dark Purple / Black (Top Right):
Affluent customers (≥ $70k income) with high spending scores (≥ 60) who are ideal premium buyers and offer the highest revenue potential. & Insights

## Business Insights
--Cluster 0 (Balanced Income & Spending):
Maintain loyalty with seasonal discounts, email engagement, and small-value perks.
--Cluster 1 (High Income, Low Spending):
These customers have money but don’t spend much.
Use personalized marketing, targeted promotions, or interest-based recommendations to unlock potential.
--Cluster 2 (Low Income, Low Spending):
Least profitable, but can be improved.
Use heavy discounts, referral programs, or entry-level product promotions to engage.
--Cluster 3 (Low Income, High Spending):
Loyal spenders despite income limitations.
Retain through affordable bundles, EMI plans, or cashback offers.
--Cluster 4 (High Income, High Spending):
Focus on VIP treatment, loyalty rewards, and exclusive deals.
The highest ROI segment for luxury and premium offerings.

📌 For detailed analysis, check the attached Jupyter Notebook.

📷 Visualization Example
![Customer_segment_KMeans_cluster_plot](https://github.com/user-attachments/assets/4aad82c4-b9a3-4d0a-b7e5-9aae31b63f39)

🤝 Contributing
Feel free to fork this repo and create pull requests!

📩 Contact
👤 Sweety Seelam
📧 Email: sweetyseelam2@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/sweetyrao670/
