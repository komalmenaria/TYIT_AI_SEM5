# Step 1 import necessary packages  4
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans



# Step 2 generate dataset 
dataset = make_blobs(n_samples=200,centers=4,n_features=2,cluster_std=1.6,random_state=50)
points = dataset[0]

# Step 3 create cluster and tell which datsset have to use 
kmeans = KMeans(n_clusters=4)
kmeans.fit(points)
plt.scatter(dataset[0][:,0],dataset[0][:,1])
clusters = kmeans.cluster_centers_
print(clusters)
# Step 4 predict clusters

y_km=kmeans.fit_predict(points)
# to see which value is coming in which cluster
# print(y_km)   

# Step 5 draw clusters
plt.scatter(points[y_km == 0,0],points[y_km == 0,1],color="red",s=80)
plt.scatter(points[y_km == 1,0],points[y_km == 1,1],color="yellow",s=80)
plt.scatter(points[y_km == 2,0],points[y_km == 2,1],color="green",s=80)
plt.scatter(points[y_km == 3,0],points[y_km == 3,1],color="blue",s=80)
# Step 6 draw centroid 


plt.scatter(clusters[0][0],clusters[0][1],marker="*",color="black",s=80)
plt.scatter(clusters[1][0],clusters[1][1],marker="*",color="black",s=80)
plt.scatter(clusters[2][0],clusters[2][1],marker="*",color="black",s=80)
plt.scatter(clusters[3][0],clusters[3][1],marker="*",color="black",s=80)
# Step 7 Output 
plt.show()

