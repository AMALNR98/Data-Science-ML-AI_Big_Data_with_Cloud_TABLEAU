Activation functions play a crucial role in artificial neural networks (ANNs) by introducing non-linearities into the network. These non-linearities are essential for the network to learn and model complex relationships in the data. Here are some common activation functions used in ANNs:

1. **Sigmoid Activation Function:**
   - **Formula:** `sigma(x) = 1/(1 + e^{-x})`
   - **Range:** (0, 1)
   - **Use:** Historically used in the output layer for binary classification problems, but less common in hidden layers due to issues like vanishing gradients.

2. **Hyperbolic Tangent (tanh) Activation Function:**
   - **Formula:** \( \tanh(x) = \frac{e^{2x} - 1}{e^{2x} + 1} \)
   - **Range:** (-1, 1)
   - **Use:** Similar to the sigmoid but with an output range that is symmetric around zero. Commonly used in hidden layers.

3. **Rectified Linear Unit (ReLU):**
   - **Formula:** \( \text{ReLU}(x) = \max(0, x) \)
   - **Range:** [0, +∞)
   - **Use:** Widely used in hidden layers due to its simplicity and ability to mitigate vanishing gradient problems. However, it may suffer from the "dying ReLU" problem if not handled properly.

4. **Leaky Rectified Linear Unit (Leaky ReLU):**
   - **Formula:** \( \text{Leaky ReLU}(x) = \max(\alpha x, x) \) where \( \alpha \) is a small positive constant (e.g., 0.01).
   - **Range:** (-∞, +∞)
   - **Use:** Similar to ReLU but addresses the "dying ReLU" problem by allowing a small gradient when the input is negative.

5. **Parametric Rectified Linear Unit (PReLU):**
   - **Formula:** \( \text{PReLU}(x) = \max(\alpha x, x) \) where \( \alpha \) is a learnable parameter.
   - **Range:** (-∞, +∞)
   - **Use:** Similar to Leaky ReLU, but with the advantage of allowing the network to learn the optimal value of \( \alpha \).

6. **Exponential Linear Unit (ELU):**
   - **Formula:** \( \text{ELU}(x) = \begin{cases} x & \text{if } x > 0 \\ \alpha(e^x - 1) & \text{if } x \leq 0 \end{cases} \) where \( \alpha \) is a hyperparameter.
   - **Range:** (-α, +∞)
   - **Use:** A smooth alternative to ReLU, aiming to mitigate the vanishing gradient problem.

These activation functions are chosen based on the characteristics of the problem at hand, and experimentation is often required to determine the most suitable activation functions for a specific task and network architecture. Additionally, different layers in a neural network may use different activation functions depending on the task requirements.