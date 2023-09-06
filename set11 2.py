import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Load the transaction data
data = pd.read_csv('transaction_data.csv')

# Step 2: Explore the data and select relevant features (e.g., Total Amount Spent and Frequency of Visits)
X = data[['Total Amount Spent', 'Frequency of Visits']]

# Step 3: Standardize the data (optional but recommended for K-Means)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Determine the number of clusters (K) using the Elbow Method
wcss = []  # Within-Cluster-Sum-of-Squares

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Method graph
plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')  # Within-Cluster-Sum-of-Squares
plt.show()

# Based on the Elbow Method, select the optimal number of clusters (K)
optimal_k = 3  # Adjust this based on the elbow point in the graph

# Step 5: Apply K-Means clustering with the chosen K
kmeans = KMeans(n_clusters=optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=0)
cluster_labels = kmeans.fit_predict(X_scaled)

# Step 6: Add the cluster labels to the original dataset
data['Cluster'] = cluster_labels

# Step 7: Analyze and interpret the clusters
cluster_centers = kmeans.cluster_centers_
data['Distance'] = np.linalg.norm(X_scaled - cluster_centers[cluster_labels], axis=1)

# You can explore the cluster characteristics and interpret the results
cluster_summary = data.groupby('Cluster').agg({
    'Total Amount Spent': ['mean', 'std'],
    'Frequency of Visits': ['mean', 'std'],
    'Distance': ['mean', 'std', 'count']
}).reset_index()

print(cluster_summary)
