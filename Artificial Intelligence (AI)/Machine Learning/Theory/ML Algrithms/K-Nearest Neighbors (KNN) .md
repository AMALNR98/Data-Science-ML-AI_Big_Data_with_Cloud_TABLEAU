**K-Nearest Neighbors (KNN):**

### Explanation:
K-Nearest Neighbors (KNN) is a simple and intuitive machine learning algorithm used for both classification and regression tasks. In KNN, an object is classified or predicted based on the majority class or average of the k-nearest data points in the feature space.

### Working:
1. **Training:** The algorithm stores all the training examples.
2. **Prediction (Classification):** For a given input, it finds the k-nearest neighbors based on a distance metric (commonly Euclidean distance). The class of the majority of these neighbors becomes the predicted class for the input.
3. **Prediction (Regression):** For regression tasks, the algorithm predicts the average of the target values of the k-nearest neighbors.

### Advantages:
1. **Simple and Intuitive:** KNN is easy to understand and implement.
2. **No Training Phase:** KNN doesn't require a training phase, making it applicable for online learning.
3. **Non-Parametric:** It doesn't assume any underlying data distribution.

### Disadvantages:
1. **Computationally Expensive:** Calculating distances for every data point can be time-consuming, especially with large datasets.
2. **Sensitive to Outliers:** Outliers can significantly affect the algorithm's performance.
3. **Memory Intensive:** The algorithm needs to store all training examples, making it memory-intensive.

### Real-world Example:
Consider a KNN algorithm used for classifying emails as spam or not spam. The algorithm looks at the features of emails (e.g., word frequencies, sender information) and, for a new email, finds the k-nearest neighbors in the feature space. If the majority of these neighbors are spam, the algorithm classifies the new email as spam.

KNN is commonly used in recommendation systems, image recognition, and anomaly detection, among other applications.