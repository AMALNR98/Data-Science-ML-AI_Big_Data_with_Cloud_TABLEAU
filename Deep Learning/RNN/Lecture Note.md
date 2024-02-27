# Recurrent Neural Networks
--
- Issues in the feed_forward neural network: 
    - cannot handle sequential data
    - considers only the current input
    - cannot memorize previous inputs

- The solution to these issues is the RNN. An RNN can handle sequential data

- RNN architecture
 - ![](/RNN/png_files/RNN%20architecture.png)
- RNN architecture unfolded
 - ![](/RNN/png_files/RNN%20Architecture%20Unfolded.png)

- Applications of RNN
    - Image captioning
        - RNNs are used to caption an image by analyzing the activities present
        - Here we combine CNN and RNN
    - Time series prediction
        - Any time series problem, like prediction the prices of stocks in a particular month, can be solved using an RNN.
    - Natural Language Processing
    - Machine Translation / Language Translation
        - given an input in one language, RNNs can be used to translate the input into one language to another

- ## Types of RNN
    1. one to one
        - This type of neural network is known as the vanilla Neural networks.
        - It's used for general machine learning problems, which has a single input and a single output.
    2. One to Many RNN
        - This type of neural network has a single input and multiple outputs.
        An example of this is the image captioning
    3. Many to one RNN
    4. Many to Many RNN    

## Two Issues of Standard RNNs
1. Vanishing Gradient Problem
   - Recurrent Neural Networks enable you to model time-dependent and sequential data problems, such as stock market prediction, machine translation, and text generation.
   you will find, however, RNN is hard to train because of the gradient problem.
   - RNNs suffer from the problem of vanishing gradients. The gradients carry information used in the RNN, and when the gradient becomes too small, the parameter updates become insignificant.
   This makes the learning of long data sequences difficult.
2. Exploding Gradient Problem
   - While training a neural network, if the slop tends to grow exponentially instead of decaying, this is called an exploding gradient. This problem arises when large error gradients accumulate, resulting in huge updates to the neural network model weights during the training process.
   - Long training time, poor performance, and bad accuracy are the major issues in gradient problems.
