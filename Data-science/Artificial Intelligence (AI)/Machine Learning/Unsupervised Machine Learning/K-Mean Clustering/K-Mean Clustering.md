K-Means clustering is a popular unsupervised machine learning algorithm used for partitioning a dataset into K distinct, non-overlapping subsets (or clusters). The goal is to group data points that are similar to each other while keeping data points from different clusters as dissimilar as possible. The algorithm works iteratively to assign each data point to one of K clusters and update the cluster centroids until convergence.

Here's a step-by-step explanation of the K-Means clustering algorithm:

1. **Initialization:**
   - Randomly select K data points from the dataset as the initial centroids. These centroids will serve as the starting points for the clusters.

2. **Assignment:**
   - Assign each data point to the cluster whose centroid is closest in terms of Euclidean distance (other distance metrics can also be used).

3. **Update Centroids:**
   - Recalculate the centroids of each cluster by taking the mean of all the data points assigned to that cluster.

4. **Repeat:**
   - Repeat steps 2 and 3 until convergence. Convergence occurs when the assignments of data points to clusters no longer change significantly, or when a predefined number of iterations is reached.

The objective function of the K-Means algorithm is to minimize the sum of squared distances between data points and their respective cluster centroids. Mathematically, it can be expressed as:

\[ J = \sum_{i=1}^{K} \sum_{j=1}^{n} ||x_j - c_i||^2 \]

Where:
- \( J \) is the objective function to be minimized.
- \( K \) is the number of clusters.
- \( n \) is the number of data points.
- \( x_j \) is the \( j \)-th data point.
- \( c_i \) is the centroid of the \( i \)-th cluster.

K-Means has some advantages, such as simplicity and efficiency, but it also has limitations. It requires the user to specify the number of clusters (\( K \)) in advance, and its performance can be sensitive to the initial placement of centroids. Different initializations may lead to different final clusters.

Additionally, K-Means assumes that clusters are spherical and equally sized, making it less suitable for datasets with irregularly shaped clusters or clusters with different sizes. Despite these limitations, K-Means is widely used for various applications, including image segmentation, customer segmentation, and data compression.
