# 🧠 Comparing Clustering Algorithms by Customer Segmentation

This project applies unsupervised machine learning techniques to perform customer segmentation on a marketing dataset. It uses the **BIRCH**, **K-Means** and **DBSCAN** clustering algorithms to group customers based on their demographic and behavioral features, with a focus on interpretability, performance, and scalability.

## 📁 Dataset Description

The dataset is a cleaned and scaled version of the Customer Personality Analysis dataset available on Kaggle. It contains features such as:
- **Demographic Features**: Age, Income, Family Size
- **Behavioral Features**: Total Spend, Recency, Tenure, Campaign Responses, Purchases via different channels (Web, Catalog, Store)
- **Target**: no labeled output

## 🧪 Algorithms Used

- ✅ BIRCH Clustering

- ✅ KMeans Clustering

- ✅ DBSCAN

- ✅ PCA for dimensionality reduction (visualization)

## 🔍 Project Goals

- Segment customers into meaningful groups

- Perform 3D visualization of clusters using PCA

- Extract cluster-wise insights based on statistical summaries

- Generate automatic customer personas per cluster

- Make the code modular and reusable for other models

## 📦 Project Structure

customer-segmentation

│

├── data/

│   └── processed_customers.csv      # Cleaned and scaled dataset

│

├── models/

│   ├── birch_clustering.ipynb       # BIRCH analysis

│   ├── kmeans_clustering.ipynb      # KMeans analysis

│   ├── dbscan_clustering.ipynb      # DBSCAN analysis

│   └── persona_generator.py         # assign persona to each cluster

│

├── notebooks

│   ├── eda.ipynb # Exploratory data analysis

│   ├── data_preprocessing.ipynb

│   ├── model_comparison.ipynb

│
├── processed

│   ├── birch.csv                          # dataset containing cluster labels by BIRCH Algorithm

│   ├── kmeans.csv                         # dataset containing cluster labels by K-Means Algorithm

│   ├── dbcsan.csv                         # dataset containing cluster labels by DBSCAN Algorithm

│   ├── processed_customers.csv            # dataset after performing data manipulation

│   ├── processed_customers_raw.csv        # 

│   └── processed_customers_unscaled.csv 

│

├── README.md                        # This file

└── requirements.txt                 # Dependencies

## 📊 Cluster Analysis Example (BIRCH)

Each cluster is analyzed using range estimates:
(mean ± std) for features like:

- Income: Customer’s income
- Recency: Days since last purchase
- Total Spend: Combined spend across all channels
- Customer Tenure: Days since becoming a customer
- Web, Catalog, and Store Purchases
- Campaign Responses, Complaints, Family Size, Age

Insights are used to label each cluster with customer personas, like:
- 🎯 "High-Value, Multi-Channel Spenders"
- 🧍 "Low-Engagement, Budget Shoppers"
- 📦 "Catalog Loyalists with High Income"

## 📈 3D Visualization

Clustering results are visualized using 3D PCA plots to interpret how customer segments are distributed in reduced dimensions

## 🧠 Future Enhancements
- Implement CURE hierarchical clustering
- Add cluster evaluation metrics (Silhouette, Davies-Bouldin)

## 🚀 Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/shubhro2002/Market-Basket-Analysis.git

2. Install required dependencies:

   ```bash
   pip install -r requirements.txt

4. Run the Jupyter notebooks or Python scripts to start using.
