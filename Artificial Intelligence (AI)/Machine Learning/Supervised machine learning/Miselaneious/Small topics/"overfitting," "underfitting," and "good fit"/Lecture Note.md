bias or error = actual value + predicted value
- ``y = mx + c + bias``
- ***variance*** = errors in testing data
- ***bias*** = errors in training data
***Over fitting***
---
- when the best fit line passed through training data, no points in testing data
- Training data error will zero
- Testing data have the probability for error
- ***condition for Over fitting*** ``low bias and high variance``
- To avoid Over fitting
  1. Cross Validation
  2. Training with more data
  3. Removing Features


***Under Fitting***
---
- ***condition for under fitting*** - ``high bias and low variance`` 
- To avoid under-fitting
  1. Training with more times ( increase ``epochs``)
  2. Increase number of features