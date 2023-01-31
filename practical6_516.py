from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
#first feature
weather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny','Rainy','Overcast','Overcast','Sunny','Rainy']
#Second feature
temp=['Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild','Hot']
#label or target variable
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']

le=preprocessing.LabelEncoder()
#converting string into number
weather_encode=le.fit_transform(weather)
print(weather_encode)
temp_encode=le.fit_transform(temp)
print(temp_encode)
label=le.fit_transform(play)
print(label)

#combine features
features=list(zip(weather_encode,temp_encode))

model=KNeighborsClassifier(n_neighbors=3)

#train the model using traning sets
model.fit(features,label)

#predict output
predicted=model.predict([[0,2]])
print(predicted)
