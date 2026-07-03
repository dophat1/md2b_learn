## Overview

Data types: this is even harder than clustering itself. Need to in depth understanding later. 

```
dataFrame.to_list()
dataFrame.to_numpy()

# unpack a list of numpy array into a clean matrix
np.stack
```

## Clustering

Use scikit-learn library. This is confusing with the installation is "scikit-learn", but the import is "sklearn".

```
from sklearn.cluster import Kmeans

# n_clusters: number of clusters, n_init: how many times to run the algo to know which one has the least inertia, max_iter: max number of iteration until stop per run

model = KMeans(n_clusters= , n_init= , max_iter= )

# X needs to be a 2 dimensional array with the form (n_samples, n_features)
model.fit(X)

# Show the labels of all dataset [1,2,4,2,1,...]
model.labels_

# Predict a new point, must have the same dimension as with other data points used to train
model.predict(X)
```

## KMeans algorithm

1. Initialization: Select random centroids (among the datasets), the number of centroid is determined by the number of cluster defined by developer.

2. Assignment: Calculate the distance (normally Euclidean distance) of all the point to the centroids, then assign the point to its closest centroid. Formular: $inertia = \sum_{i=1}^n \sum_{j=1}^n \| x_i - \mu_j \|^2$


3. Update: After that, calculating the "inertia" of the cluster by summing up all the distance of each point in the cluster to the centroid. 

4. Repeat: After calculating the inertia for all clusters, calculate the average point for each cluster (by just adding all the x,y,z... of the point up then divide by number of points), that is the new centroids, then repeat the process from step 1. 

When will this stop ?
- When the centroid doesn't move much anymore (converged)
- When the inertia is reached.
- When max_iter parameter reached. 

5. Evaluation: Once the algorithm finish, there will be criteria to evaluate its efficiency: 
- Silhouette score
- Calinski-Harabasz index
- Davies-Bouldin index