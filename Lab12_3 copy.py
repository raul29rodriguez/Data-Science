'''Exercise 3
Read the entire dataset: housing.csv and perform K-means clustering where K=6. Columns
Longitude, Latitude correspond to x, y, respectively. Plot the clusters'''
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import csv
from sklearn.cluster import KMeans
from pandas import DataFrame
df=pd.read_csv('housing.csv')
x=np.array(df['Longitude'])
y=np.array(df['Latitude'])
D={'x':x,'y':y}
df=DataFrame(D)
kmeans=KMeans(n_clusters=6).fit(df)
centroids=kmeans.cluster_centers_
plt.scatter(centroids[:,0],centroids[:,1],c='r',marker='x')
plt.scatter(df['x'],df['y'])
plt.show()