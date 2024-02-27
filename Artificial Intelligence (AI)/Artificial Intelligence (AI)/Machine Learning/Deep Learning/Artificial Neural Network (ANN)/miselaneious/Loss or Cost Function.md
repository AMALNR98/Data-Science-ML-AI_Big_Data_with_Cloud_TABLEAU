- The terms "loss function" and "cost function" are often used interchangeably in the context of machine learning and neural networks, 
- but they can have slightly different interpretations in certain contexts. 
- Both refer to a mathematical function that measures the difference between the predicted values of a model and the actual target values. 
- The goal during training is to minimize this function.

Here's a breakdown of the terms:

1. **Loss Function:**
   - The loss function is a term commonly used in the context of training a single example or a single data point. It quantifies how well the model predicts the target value for a single instance. In the context of supervised learning, where the goal is to predict a target value given input features, the loss function evaluates the model's performance on an individual example.
   - The loss function is often denoted by \( \mathcal{L} \) or \( J \).

2. **Cost Function:**
   - The cost function, on the other hand, is a term more commonly used in the context of the entire training dataset or a mini-batch (a subset of the dataset used in a single iteration of training). It represents the average loss over the entire dataset or batch. The cost function is essentially the average of the loss function values across all training examples in a batch.
   - The cost function is often denoted by \( \mathcal{J} \) or \( C \).

In summary, the loss function assesses the performance of the model on a single example, while the cost function is an aggregate measure of performance over an entire dataset or a batch. The objective during training is to minimize the cost function by adjusting the model parameters (weights and biases) using optimization algorithms like gradient descent.

Common types of loss functions include mean squared error (MSE) for regression tasks and cross-entropy loss for classification tasks. The specific choice of the loss function depends on the nature of the problem being solved.

---

***Example***

| age | affordable | Insurance |
|-----|------------|-----------|
| 22  | 1          | 0         |
| 25  | 1          | 1         |
| 28  | 0          | 0         |
| 35  | 0          | 0         |
| 36  | 1          | 1         |

- For first column
  - ![](png_files/column%201.png)
  - Here we need output as 1 but we get 0.99
  - so find error
- Find for each columns
- Then find total error
  - Total error = error 1 + error 2 + error 3 +...+ error n