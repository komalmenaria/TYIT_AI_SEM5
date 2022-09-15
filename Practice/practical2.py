# kmeans clustering
# Step 1 import 4 packages 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
# Step 2 generate data 

dataset = make_blobs(n_samples=200,centers=4,n_features=2,cluster_std=1.6,random_state=50)
points = dataset[0]
# Step 3 define cluster and tell them with data have to use
kmeans = KMeans(n_clusters=4)
kmeans.fit(points)
plt.scatter(dataset[0][:,0],dataset[0][:,1])
clusters = kmeans.cluster_centers_
# Step 4 predict cluster 
y_km = kmeans.fit_predict(points)
# Step 5 draw clusters 
plt.scatter(points[y_km == 0,0],points[y_km == 0,1], color='red',s=60)
plt.scatter(points[y_km == 1,0],points[y_km == 1,1], color='yellow',s=60)
plt.scatter(points[y_km == 2,0],points[y_km == 2,1], color='green',s=60)
plt.scatter(points[y_km == 3,0],points[y_km == 3,1], color='cyan',s=60)



# Step 6 draw centroid 
plt.scatter(clusters[0][0],clusters[0][1],marker="*",color='black',s=60)
plt.scatter(clusters[1][0],clusters[1][1],marker="*",color='black',s=60)
plt.scatter(clusters[2][0],clusters[2][1],marker="*",color='black',s=60)
plt.scatter(clusters[3][0],clusters[3][1],marker="*",color='black',s=60)

# Step 7 output 
plt.show()