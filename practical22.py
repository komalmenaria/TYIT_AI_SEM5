from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from matplotlib import pyplot as plt
df = pd.read_csv("Book1.csv")
df.head()



plt.scatter(df.rollno,df['marks'])
plt.xlabel('rollno')
plt.ylabel('marks')


km = KMeans(n_clusters=3)
predicted = km.fit_predict(df[['rollno','marks']])
predicted



df['cluster']=predicted
df.head()

df1 = df[df.cluster==0]
df2 = df[df.cluster==1]
df3 = df[df.cluster==2]
plt.scatter(df1.rollno,df1['marks'],color='green')
plt.scatter(df2.rollno,df2['marks'],color='red')
plt.scatter(df3.rollno,df3['marks'],color='blue')
plt.xlabel('rollno')
plt.ylabel('marks')



df = df.drop(['cluster'], axis='columns')


scale = MinMaxScaler()

scale.fit(df[['marks']])
df['marks'] = scale.transform(df[['marks']])

scale.fit(df[['rollno']])
df['rollno'] = scale.transform(df[['rollno']])

km = KMeans(n_clusters=3)
predicted = km.fit_predict(df[['rollno','marks']])
predicted


km.cluster_centers_

plt.scatter(df1.rollno,df1['marks'],color='green')
plt.scatter(df2.rollno,df2['marks'],color='red')
plt.scatter(df3.rollno,df3['marks'],color='blue')
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='black',marker='*')
plt.xlabel('rollno')
plt.ylabel('marks')

plt.show()
