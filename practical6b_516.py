from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=3)
trainingset=["KL","Shai","David","Faf","Hashmin","piyush"]
x=[[26,889,42.3,81.0],[72,3007,52.8,74.3],[116,4990,45.8,95.5],[143,5507,47.5,88.6],[181,8113,49.5,88.4],[25,1117,34.9,41.0]]
y=["Average","Good","Excellent","Good","Excellent","Poor"]
model.fit(x,y)  #training
print(model.predict([[228,950,20.5,30.1]]))
