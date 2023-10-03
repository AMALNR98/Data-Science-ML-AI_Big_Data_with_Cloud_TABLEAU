**Steps**
    *1. Data Collections:*
        - To collect data
            - For study purpose : collect data from kaggle
            - GitHub
            - For project collect data from kaggle
    *2. Data Exploration and Preparation
        -

The process of applying machine learning algorithms typically involves several common steps. While the specific details and order of these steps can vary depending on the problem and the algorithm used, the following are the fundamental stages in the machine learning workflow:

1. **Data Collection**:
   - The first step is to gather relevant data for your machine learning task. Data can come from various sources, such as databases, APIs, sensors, or manual data entry. It's essential to collect high-quality, representative data that accurately reflects the problem you want to solve.
   - To collect data
            - For study purpose: collect data from kaggle
            - GitHub
            - For project collect data from kaggle
2. **Data Preprocessing / Data preparation**:
   - Data preprocessing is a critical step to clean and prepare the data for analysis. This may involve tasks such as:
     - Handling missing values: Deciding whether to impute missing data or remove incomplete records.
     - Feature engineering: Creating new features or transforming existing ones to enhance the model's performance.
     - Data scaling: Scaling features to have similar ranges to prevent some features from dominating others.
     - Encoding categorical variables: Converting categorical variables into numerical format for machine learning algorithms to work with.
     - Data splitting: Dividing the dataset into training, validation, and test sets for model evaluation.
     - Data cleaning
     - Remove unwanted data
     - Completely numerical data

3. **Feature Selection**:
   - Feature selection involves choosing the most relevant and informative features for your machine learning model. Eliminating irrelevant or redundant features can improve model efficiency and performance.

4. **Model Selection**:
   - Choose an appropriate machine learning algorithm or model for your specific task. The selection depends on whether you're dealing with a classification, regression, clustering, or other types of problems. It's also important to consider the characteristics of your data, such as its size and complexity.

5. **Model Training**:
   - In the training phase, you feed the prepared data into the selected model. The model learns from the data to capture underlying patterns and relationships. During this process, the model's parameters are adjusted to minimize the difference between its predictions and the actual target values.

6. **Hyperparameter Tuning**:
   - Most machine learning models have hyperparameters that are not learned from the data but need to be set before training. Hyperparameter tuning involves finding the best combination of hyperparameter values to optimize the model's performance. Techniques like grid search or random search are commonly used.

7. **Model Evaluation**:
   - Assess the performance of your trained model using appropriate evaluation metrics. The choice of metrics depends on the nature of your problem:
     - For classification tasks, metrics like accuracy, precision, recall, F1-score, and ROC AUC are commonly used.
     - For regression tasks, metrics like mean squared error (MSE), root mean squared error (RMSE), and R-squared are typical.
     - For clustering tasks, metrics like silhouette score and Davies-Bouldin index can be used.

8. **Model Validation**:
   - After evaluating your model on the validation dataset, you may need to fine-tune hyperparameters or adjust the model based on the results. This process may be repeated iteratively to achieve the best performance.

9. **Model Deployment**:
   - Once you are satisfied with your model's performance, you can deploy it for use in real-world applications. Deployment may involve integrating the model into a web application, API, or other systems.

10. **Monitoring and Maintenance**:
    - After deployment, it's important to continuously monitor the model's performance and retrain it as needed to adapt to changing data patterns. Models can degrade over time, so regular maintenance is crucial.

11. **Documentation and Reporting**:
    - Properly document your machine learning project, including details about data sources, preprocessing steps, model architecture, hyperparameters, and evaluation results. Clear documentation ensures that others can understand and reproduce your work.

These common steps provide a structured framework for building and deploying machine learning models. Keep in mind that machine learning is an iterative process, and you may need to revisit and adjust various stages as you gain insights from your data and model performance.

**Steps in a nutshell**
- Data collections
- Data Preparation
  - data exploration
- model creation: Apply Machine learning Algorithm
- performance evaluation
- Model improvement 