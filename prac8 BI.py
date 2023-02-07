import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.cluster import KMeans
X=np.array([[0,0],[0,1],[0,2],[1,1],[2,1],[2,2],[5,7],[4,6],[[2,4]]])
plt.title("9 Store coordinates")
plt.scatter(X[:,0],X[:,1],label="True positions")
plt.show()
kmeans=KMeans(n_clusters=2)
kmeans.fit(X)
print(kmeans.cluster_centers_)
print(kmeans.labels_)
plt.title("9 Store coordinates")
plt.scatter(X[:,1],X[:,1],c=kmeans.labels_,cmap="autumn")
plt.scatter(kmeans.cluster_centers_[:,0])
