import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import math
from pandas import DataFrame
df=pd.read_csv('auto-mpg.csv')
df=df.loc[:,['weight','acceleration']]
x=np.array(df.loc[:,['weight']])
print(x)
y=np.array(df.loc[:,['acceleration']])
print(y)
X = np.vstack((x, y)).T 
K = range(1, 11)
dist = []
for k in K:
    kmeans = KMeans(n_clusters=k).fit(X)
    sumMinED = 0
    sumMinED2 = 0
    for r in range(X.shape[0]):
        for c in range(kmeans.cluster_centers_.shape[0]):
            if c == 0:
                minED = ((X[r, 0] - kmeans.cluster_centers_[0, 0])**2) + ((X[r, 1] 
- kmeans.cluster_centers_[0, 1])**2)
            ED = ((X[r, 0] - kmeans.cluster_centers_[c, 0])**2) + ((X[r, 1] - 
kmeans.cluster_centers_[c, 1])**2)
            if ED < minED:
                minED = ED
        sumMinED = sumMinED + minED
    dist.append(sumMinED)
    sumMinED = 0
xDist = [c for c in K]
kmeans = KMeans(n_clusters=K, init = 'k-means++')
kmeans = kmeans.fit(df)
centroidsK = kmeans.cluster_centers_
labelsK = kmeans.labels_
xTest = [1850.5, 2310.0],[4118.2, 3210.7]
df2 = DataFrame(xTest)
df2.columns=['x', 'y']
print(f'Values to cluster:\n{df2}')
k2 = kmeans.predict(df2)
print(f'\nClusters (labels):\n{k2}')
plt.scatter(df['x'], df['y'], c=kmeans.labels_)
plt.scatter(centroidsK[:, 0], centroidsK[:, 1], c='red', label = 'centroids')
plt.plot(df2['x'], df2['y'], 'b+', markersize=12, label = 'predicted')
plt.title(f'K={K}')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()