# import require libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans



# generate our datasets 
dataset = make_blobs(n_samples=200,centers=4,n_features=2,cluster_std=1.6,random_state=50)
# print(dataset)

points = dataset[0]


# create a kmeans object 
kmeans = KMeans(n_clusters=4)
# to say kmeans which dataset you have to use
kmeans.fit(points)
plt.scatter(dataset[0][:,0],dataset[0][:,1])
clusters = kmeans.cluster_centers_
# print out the clusters
print(clusters)




y_km = kmeans.fit_predict(points)

# to see which value is coming in which cluster
# y_km  

# to see the data
# points


plt.scatter(points[y_km == 0,0], points[y_km == 0,1], color='red' , s=80)
plt.scatter(points[y_km == 1,0], points[y_km == 1,1], color='blue' , s=80)
plt.scatter(points[y_km == 2,0], points[y_km == 2,1], color='green' , s=80)
plt.scatter(points[y_km == 3,0], points[y_km == 3,1], color='yellow' , s=80)


plt.scatter(clusters[0][0],clusters[0][1], marker="*",s=200 , color='black')
plt.scatter(clusters[1][0],clusters[1][1], marker="*",s=200 , color='black')
plt.scatter(clusters[2][0],clusters[2][1], marker="*",s=200 , color='black')
plt.scatter(clusters[3][0],clusters[3][1], marker="*",s=200 , color='black')


plt.show()