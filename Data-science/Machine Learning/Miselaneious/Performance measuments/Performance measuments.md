***Performance measurements***

Performance measurements are critical in various domains, including machine learning, data analysis, and statistics, 
to assess the quality and effectiveness of models, algorithms, systems, or processes. 
These measurements provide quantitative insights into how well a model or system is performing and help guide decision-making and improvements. 
Here are some common performance measurements and metrics used in different contexts:

1. **Classification Metrics**:

   - **Accuracy**: The proportion of correctly predicted instances out of the total instances. It is a commonly used metric for binary and multi-class classification problems. However, it may not be suitable for imbalanced datasets.

   - **Precision**: The ratio of true positive predictions to the total positive predictions. It measures the accuracy of positive predictions.

   - **Recall (Sensitivity)**: The ratio of true positive predictions to the total actual positives. It measures the ability of a model to capture all positive instances.

   - **F1-Score**: The harmonic mean of precision and recall. It balances precision and recall when the class distribution is imbalanced.

   - **Specificity**: The ratio of true negative predictions to the total actual negatives. It is particularly relevant in medical and diagnostic applications.

   - **ROC AUC (Receiver Operating Characteristic Area Under the Curve)**: It assesses the trade-off between true positive rate and false positive rate for different classification thresholds. A higher AUC indicates better model discrimination.

2. **Regression Metrics**:

   - **Mean Absolute Error (MAE)**: The average absolute difference between predicted and actual values. It is less sensitive to outliers compared to MSE.

   - **Mean Squared Error (MSE)**: The average of squared differences between predicted and actual values. It gives more weight to larger errors and is sensitive to outliers.

   - **Root Mean Squared Error (RMSE)**: The square root of the MSE, which provides an error metric in the same units as the target variable.

   - **R-squared (R2)**: Measures the proportion of the variance in the dependent variable explained by the independent variables. It ranges from 0 to 1, where a higher value indicates a better fit.

   - **Mean Absolute Percentage Error (MAPE)**: Expresses errors as a percentage of the actual values. It is commonly used in forecasting and time series analysis.

3. **Clustering Metrics**:

   - **Silhouette Score**: Measures how similar an object is to its cluster compared to other clusters. It ranges from -1 to 1, where higher values indicate better clustering.

   - **Davies-Bouldin Index**: Measures the average similarity ratio of each cluster with the cluster that is most similar to it. Lower values indicate better clustering.

4. **Anomaly Detection Metrics**:

   - **Precision at K (P@K)**: Measures the fraction of the top K predictions that are true anomalies.

   - **Recall at K (R@K)**: Measures the fraction of true anomalies that are in the top K predictions.

5. **Information Retrieval Metrics**:

   - **Precision**: Measures the fraction of retrieved instances that are relevant.

   - **Recall**: Measures the fraction of relevant instances that are retrieved.

   - **F1-Score**: The harmonic mean of precision and recall, which balances precision and recall in information retrieval.

6. **Time Series Metrics**:

   - **Mean Absolute Scaled Error (MASE)**: Measures the accuracy of forecasts in the context of out-of-sample performance.

   - **Ljung-Box Test**: A statistical test to check for the absence of autocorrections in a time series.

---

---

---
These performance measurements are just a selection of the many metrics available to assess the quality of models and analyze data. The choice of the appropriate metric depends on the specific problem, the characteristics of the data, and the goals of the analysis or modeling task. It's important to select metrics that align with your objectives and provide a comprehensive view of performance.

1. Accuracy score
2. Recall
3. Precision
4. F1 Score

- We commonly use accuracy score, sometimes another performance measurement uses. Because it won't work sometimes
- When we use another Performance measurement
- Other performance measurements used when thd give dataset is imbalanced.
- ***To find imbalanced dataset*** - group and count or value_count
---
- ***Recall***

   - gives importance for false negative, optimise false negative
   - so recall should be increased and reduce false negative
   - ``Recall = TP/(TP+FN)``
   - Recall should be high
---
- ***Precision***

   - Give important for false positive
     - ``Precision = TP/(TP+FP)``
     - Precision should be high
---
- ***F1 Score***

  - combined or balanced performance measurements of recall and precision
  - ``F1_score = 2*(recall*precision/ (recall + precision))``
