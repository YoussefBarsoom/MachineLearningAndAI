import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:,[3,4]].values

#Find Optimal # OF CLUSters

from sklearn.cluster import KMeans

wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init = 'k-means++',max_iter = 300,n_init=10,random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1,11),wcss)
plt.title('WCSS')

plt.show()

#Apply Kmeans to data
kmeans = KMeans(n_clusters = 5,init ='k-means++',max_iter = 300,n_init=10,random_state =0)
y_means = kmeans.fit_predict(X)

#Visuals

plt.scatter(X[y_means==0,0],X[y_means==0,1],s = 100,c= 'red',label = 'Careful')
plt.scatter(X[y_means==1,0],X[y_means==1,1],s=100,c='blue',label='Standard')
plt.scatter(X[y_means==2,0],X[y_means==2,1],s=100,c='yellow',label='Target')
plt.scatter(X[y_means==3,0],X[y_means==3,1],s=100,c='green',label='Careless')
plt.scatter(X[y_means==4,0],X[y_means==4,1],s=100,c='orange',label='Sensible')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='cyan',label='Centroids')
plt.title('Clusters')
plt.xlabel('Annual Income  (K$)')
plt.ylabel('Spending Score  (1-100)')

plt.legend()
plt.show()