from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd 
model = LinearRegression()
x1=[2.5,3.3,1,9,9.4,4,7]
x=[[2.5],[3.3],[1],[9],[9.4],[4],[7]]
y=[57,67,37,84,90,73,85]
plt.scatter(x1,y)
plt.show()
model.fit(x,y)
y_pred=[]

for i in x1:
    y_pred.append(model.predict([[i]]))
plt.scatter(x1,y)#Actual values
plt.scatter(x1,y_pred) #predicted value
df=pd.DataFrame({'Actual':y ,'Predicted':y_pred})
print(df)
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.show()
y_pred=model.predict([[8]])
print(y_pred)