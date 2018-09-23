%matplotlib inline
from copy import deepcopy
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams['figure.figsize'] = (16, 9)
plt.style.use('ggplot')


data = pd.read_csv('C:/Users/Wesh/Desktop/dat.csv')
data.head()
data.info()
data.describe()

print(data.shape)
data.head()

plt.scatter(data['V1'],data['V2'],c='violet', s=7) #c for color and s for the dot size


from sklearn.cluster import KMeans
f1 = data['V1'].values
f2 = data['V2'].values
X = np.array(list(zip(f1, f2)))


# Number of clusters
kmeans = KMeans(n_clusters=3)
# Fitting the input data
kmeans = kmeans.fit(X)
# Getting the cluster labels
labels = kmeans.predict(X)
# Centroid values
centroids = kmeans.cluster_centers_

# Comparing with scikit-learn centroids
print(centroids) # From sci-kit learn


