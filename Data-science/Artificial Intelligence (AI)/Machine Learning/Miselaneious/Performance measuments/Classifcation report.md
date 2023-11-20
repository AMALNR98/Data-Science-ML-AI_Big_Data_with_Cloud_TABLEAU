***Classification Report***
A classification report is a summary of the performance of a classification model, typically used in machine learning. It provides a detailed breakdown of various metrics and statistics that help you assess how well the model is performing in categorizing data into different classes or categories. Classification reports are especially useful for evaluating the accuracy, precision, recall, F1-score, and other relevant metrics of a classification model.

The classification report typically includes the following components:

1. **Class Labels**: The names or labels of the different classes or categories that the model is trying to classify data into.

2. **Precision**: Precision measures how many of the predicted positive instances were actually positive. It is calculated as:

   \[ \text{Precision} = \frac{\text{True Positives}}{\text{True Positives + False Positives}} \]

3. **Recall (Sensitivity)**: Recall measures how many of the actual positive instances were correctly predicted as positive by the model. It is calculated as:

   \[ \text{Recall} = \frac{\text{True Positives}}{\text{True Positives + False Negatives}} \]

4. **F1-Score**: The F1-Score is the harmonic mean of precision and recall, providing a single metric that balances both. It is calculated as:

   \[ \text{F1-Score} = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}} \]

5. **Support**: The number of instances in each class in the dataset.

6. **Accuracy**: Overall accuracy is the percentage of correctly classified instances:

   \[ \text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}} \]

Classification reports are used to assess the model's performance on a class-by-class basis. They provide insights into how well the model is performing for each class and can help identify potential issues with imbalanced datasets or specific classes that the model struggles with.

Here's an example of what a classification report might look like:

```
               precision    recall  f1-score   support

    Class 0       0.80      0.90      0.85       100
    Class 1       0.75      0.60      0.67        50

    accuracy                           0.79       150
   macro avg       0.78      0.75      0.76       150
weighted avg       0.79      0.79      0.78       150
```

In this example, you can see precision, recall, and F1-score values for two classes (Class 0 and Class 1) along with their support (the number of instances in each class). The accuracy of the overall model is also provided.

Classification reports are valuable for understanding the strengths and weaknesses of a classification model and for making informed decisions about model adjustments or feature engineering.

-----

-----

***Example : 2***
---

| 39| 20 |
|----|---|
| 16 | 79|

- TP : 39
- TN : 79
- FP : 20
- FN : 16

Find recall, precision, F1_score

recall
--
  - Recall(0) = TN/TN+FP = 0.71
  - Recall(1) = TP/TP+FN = 39/(39+20) = 0.71
  - Precision(1) = 0.66
  - precision(0) = 0.83
  - f1_score(1) = 0.68
  - f1_score(0) = 0.81


What is ***support*** :
---
  - Definition: Support represents the number of instances in each class in the dataset. It is the count of actual occurrences of each class in the dataset.
  -  Use: Support is essential for understanding the balance or imbalance of classes in a classification problem. Classes with low support may be more challenging to classify accurately, and it can influence performance metrics like precision and recall.
  - count of 0s and 1s
  - 0 - 99
  - 1 - 55
  - Total observation = 55 + 99 = 154
---

***Macro_average***
--
  - Definition: The macro average is the unweighted average of performance metrics (e.g., precision, recall, F1-score) calculated for each class separately. It calculates the average performance for each class and then averages those averages.
  - Use: The macro average treats each class equally and is useful when you want to assess the model's overall performance without giving more importance to larger classes. It is less affected by class imbalances.
  - ``Macro_avg(Recall) = Recall(1) + Recall(0)/2`` 
   - = 0.71 + 0.79 / 2 = 0.75
  - ``Macro_avg(Precision) = precision(1) + precision(0)/2`` 
   - = 0.66 + 0.83 / 2 = 0.74
  - ``Macro_avg(f1_score) + f1_score(1) + F1_score(0)/2 ``
   - = 0.68 + 0.81 / 2 = 0.41

***Weighted_avg***
--
  - Definition: The weighted average is the weighted average of performance metrics calculated for each class, where the weights are based on the support of each class. It accounts for class imbalances by giving more weight to classes with larger support.
  - Use: The weighted average is a more appropriate measure of overall model performance when dealing with imbalanced datasets. It reflects the performance as if you had equal representation of each class.
  - ``Weighted_avg(Recall) = Recall(1) * Support(1) * Support(0) / Total_number_of_observation``
   - 0.71 * 55 + 0.79 * 99 / 154 = 0.76
  - ``Weighted_avg_(Precision) = Precision(1)* support(0) / Total_number_of_observation``
   - 0.77
  - ``Weighted_avg_f1_score = F1_score(1)* support(0) / Total_number_of_observation``
    - 0.76