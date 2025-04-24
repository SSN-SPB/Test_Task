from sklearn.cluster import KMeans
import numpy as np

# Sample data
X = np.array([[20, 30000], [21, 32000], [90, 85000], [88, 87000]])

# KMeans with 2 clusters
kmeans = KMeans(n_clusters=2, n_init=1)
# kmeans = KMeans(n_clusters=2)
# kmeans = KMeans(n_clusters=2, random_state=42)
kmeans.fit(X)

print("Cluster labels:", kmeans.labels_)
print("Centroids:", kmeans.cluster_centers_)