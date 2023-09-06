import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

# Load transaction data (replace 'transaction_data.csv' with your data file)
data = pd.read_csv('transaction_data.csv')

# Select relevant features (e.g., TotalAmount and NumItems)
X = data[['TotalAmount', 'NumItems']]

# Normalize the data (optional, but can help if the features have different scales)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the Elbow Method
inertia = []
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Method to find the optimal K
plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), inertia, marker='o', linestyle='-', color='b')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia (Within-cluster Sum of Squares)')
plt.title('Elbow Method for Optimal K')
plt.grid(True)
plt.show()

# Based on the Elbow Method, select an appropriate number of clusters (K)
optimal_k = 3  # Adjust based on the plot

# Apply K-Means clustering with the chosen K
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(X_scaled)

# Add cluster labels to the original data
data['Cluster'] = kmeans.labels_

# Visualize the clusters using scatter plots
for cluster_num in range(optimal_k):
    cluster_data = data[data['Cluster'] == cluster_num]
    plt.scatter(cluster_data['TotalAmount'], cluster_data['NumItems'], label=f'Cluster {cluster_num + 1}')

plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Items Purchased')
plt.title('Customer Clusters Based on Spending and Purchase Behavior')
plt.legend()
plt.grid(True)
plt.show()

# Optionally, you can analyze and interpret the clusters further to gain insights into customer segments.
