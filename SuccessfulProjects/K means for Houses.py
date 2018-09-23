#Data Manipulation 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## Data fetching 
train=pd.read_csv('C:/Users/Wesh/Desktop/df.csv')
train.head()
print(train.shape)
plt.scatter(train['GrLivArea'],train['SalePrice'],c='violet', s=7) 
plt.xlabel('GrLivArea')
plt.ylabel('SalePrice')
plt.title('GrLivArea Against SalePrice',y=1.05)
plt.show()

from sklearn.cluster import KMeans
f1 = train['GrLivArea'].values
f2 = train['SalePrice'].values
X = np.array(list(zip(f1, f2)))

# Number of clusters
kmeans = KMeans(n_clusters=5)
# Fitting the input data
kmeans = kmeans.fit(X)
# Getting the cluster labels
labels = kmeans.predict(X)
# Centroid values
centroids = kmeans.cluster_centers_

# Comparing with scikit-learn centroids
print(centroids) # From sci-kit learn

labels = KMeans(5, random_state=0).fit_predict(X)
plt.scatter(X[:, 0], X[:, 1], c=labels, s=50, cmap='viridis');
plt.xlabel('GrLivArea')
plt.ylabel('SalePrice')
plt.title('GrLivArea Against SalePrice',y=1.05)