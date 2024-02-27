											Machine learning
											----------------


2 types of machine learning
---------------------------
- supervised machine learning
- unsupervised machine learning


* Traditional way



			--------------------------
			|			 |
	Input   --------|         Logic		 |------------ Output
			|			 |
			--------------------------
**1) Supervised machine learning** 
----------------------------------------

Supervised machine learning is a type of machine learning in which algorithms are trained on a labeled dataset to learn the relationship between input features and their corresponding target labels. The term "supervised" refers to the fact that the algorithm is provided with a supervisor, which is the labeled data, to guide its learning process. The goal of supervised learning is to build a model that can make accurate predictions or classifications on new, unseen data.

Here are the key components and concepts of supervised machine learning:

1. **Labeled Data**:
   - Labeled data consists of input features (also called attributes or variables) and their associated target labels or outcomes. For example, in a spam email classification task, the input features might be the email content, and the labels would be "spam" or "not spam."

2. **Training Phase**:
   - During the training phase, the supervised learning algorithm learns from the labeled data. It uses this data to understand the relationships between the input features and the target labels. The algorithm adjusts its internal parameters to minimize the difference between its predictions and the true labels in the training data.

3. **Supervised Learning Algorithms**:
   - There are various supervised learning algorithms, each suited to different types of tasks:
     - **Classification**: In classification tasks, the goal is to predict a discrete label or category. Common classification algorithms include logistic regression, decision trees, support vector machines (SVMs), and neural networks.
     - **Regression**: In regression tasks, the goal is to predict a continuous numeric value. Linear regression, polynomial regression, and random forests are examples of regression algorithms.

4. **Features and Labels**:
   - Features are the input variables that the algorithm uses to make predictions. These can be any measurable characteristics or attributes that describe the data.
   - Labels are the target values or categories that the algorithm is trying to predict based on the input features.

5. **Model Evaluation**:
   - After training, the model's performance needs to be evaluated using a separate dataset known as the validation or test dataset. Common evaluation metrics for classification tasks include accuracy, precision, recall, F1-score, and the confusion matrix. For regression tasks, metrics like mean squared error (MSE) or root mean squared error (RMSE) are often used.

6. **Over-fitting and Under-fitting**:
   - Over-fitting occurs when a model learns to perform exceptionally well on the training data but doesn't generalize well to new, unseen data. Underfitting, on the other hand, occurs when the model is too simplistic and fails to capture the underlying patterns in the data.

7. **Hyperparameter Tuning**:
   - Supervised learning models often have hyperparameters (parameters not learned during training) that can be adjusted to optimize model performance. Techniques like cross-validation are used to find the best combination of hyperparameters.

8. **Deployment**:
   - Once a supervised learning model is trained and validated, it can be deployed in real-world applications to make predictions on new, unlabeled data. Deployment can be in the form of an application, web service, or integration into an existing system.

Supervised machine learning is widely used in a variety of applications, including natural language processing (NLP), computer vision, speech recognition, recommendation systems, fraud detection, and many others. It forms the basis for many practical and valuable AI and data-driven solutions.

 -  In supervised machine learning we train inputs and its corresponding outputs, then based one of these inputs and outputs create a model
   -  

          Input ===> Output ===> Model_create
          Model_based =====> predict ======> output

 Two types of supervised machine learning:
			1) Classification
			2) Regression

Classification	:
----------------
 - Classification is the task of predicting a categorical or discrete label or class for each input. 
 - It's like: True of false | yes or no | categorical
    - Algorithms:
      ----------
		 - KNN
         - SVM 
         - Decision tree random forest 
         - Naviye bayes.

 Regression :
 -------------
  - Regression is used when the goal is to predict a continuous numeric value, such as  a price, temperature, or age.
    
    -
                             input + output ===> model_creat
                             Model_create ====> Numerical data
                                     To predict a numerical data
           
    Algorithms:
    -----------
      - Simple linear regression 
      - Multiple linear regression
      - Logistic regression
      - polynomial regression



**2) Unsupervised machine learning**
------------------------------------

Unsupervised machine learning encompasses various techniques and methods that aim to discover patterns, structures, or relationships in unlabeled data. 
Here are some common types of unsupervised machine learning:

1. **Clustering**:
    - **K-Means Clustering**: K-means is one of the most popular clustering algorithms. 
   		It groups data points into K clusters based on similarity, with the goal of minimizing the intra-cluster distance.
    - **Hierarchical Clustering**: This technique creates a hierarchical representation of data by recursively merging or dividing clusters. 
		It can result in a tree-like structure (dendrogram).
    - **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**: DBSCAN identifies clusters based on the density of data points. 
         It can find clusters of arbitrary shapes and is robust to noise.

2. **Dimensionality Reduction**:
    - **Principal Component Analysis (PCA)**: PCA reduces the dimensionality of data by finding orthogonal axes (principal components) along which the variance of the data is maximized. 
   		It's often used for feature reduction and visualization.
    - **t-Distributed Stochastic Neighbor Embedding (t-SNE)**: t-SNE is a dimensionality reduction technique specifically designed for visualization. 
         It aims to maintain the similarity between data points in the reduced space.
    - **Auto-encoders**: Auto-encoders are neural network architectures used for unsupervised feature learning and dimensionality reduction. 
        They consist of an encoder and a decoder network.

3. **Association Rule Mining**:
    - **Apriori Algorithm**: Apriori is used to discover frequent item-sets in transactional datasets. 
   		It's commonly applied in market basket analysis to find associations between products that are frequently purchased together.
    - **FP-Growth Algorithm**: FP-Growth is another algorithm for finding frequent item-sets. 
         It uses a tree structure to efficiently mine association rules.

4. **Anomaly Detection**:
    - **Isolation Forest**: This algorithm isolates anomalies by randomly selecting features and building isolation trees. 
   		Anomalies are detected when they have short paths in the tree structure.
    - **One-Class SVM (Support Vector Machine)**: One-Class SVM is a binary classification algorithm that learns to separate normal data from outliers. 
         It's useful when anomalies are rare and hard to define.

5. **Generative Models**:
    - **Generative Adversarial Networks (GANs)**: GANs consist of a generator and a discriminator network that compete against each other. 
   		They are used to generate new data samples that resemble the training data and have applications in image generation and data augmentation.
    - **Variational Auto-encoders (VAEs)**: VAEs are generative models that learn a probabilistic mapping between the data space and a latent space. 
         They can be used for generating new data and data reconstruction.

6. **Self-Organizing Maps (SOM)**:
    - SOM is a type of neural network that learns to map high-dimensional data onto a lower-dimensional grid or lattice. 
   		It's often used for data visualization and exploratory data analysis.

7. **Hierarchical Density-Based Clustering**:
    - Hierarchical DBSCAN and related algorithms extend DBSCAN to create a hierarchy of clusters, 
   		which can be useful when dealing with data that exhibits varying levels of granularity in the clusters.

These unsupervised learning techniques have applications in various fields, including data analysis, image and signal processing, recommendation systems, and anomaly detection. 
The choice of the appropriate technique depends on the specific problem and the nature of the data.

1. clustering
2. dimensionality reduction
3. Association rule mining
4. Anomaly detection
5. Generative models
6. self organizing maps
7. Hierarchical density-based clustering

