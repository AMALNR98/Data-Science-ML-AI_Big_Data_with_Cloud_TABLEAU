# 1. ****Importing data****
---
```python
import numpy as np
import pandas as pd
iris = pd.read_csv('/content/Iris.csv')
iris
```
# 2. ***Check the dataset balanced or imbalanced***
```python
diabetes['Outcome'].value_counts()
```
  - if the difference is than 50%, the dataset is imbalanced 
# 3. ***Separate x and y***
---
```python
x = iris_drop.iloc[:,:-1].values
y = iris_drop.iloc[:,-1].values
```
# 4. ***Giving data for training and testing***
---
```pyhton
from pandas.core.common import random_state
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30, random_state = 42)
```
# 5. ***Normalization / Preprocessing***
---
```Python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
```
# 6. ***Model creation***
---
 -***KNN***
  ---
 ```Python
    from sklearn.neighbors import KNeighborsClassifier
    # for create model
    # create object
    # assing value for k as 7
    knn = KNeighborsClassifier(n_neighbors=7)
    # To create model fit training data
    knn.fit(normalized_x_train_data, y_train)
    # y_predict : to check if the machine trained or not
    y_pred = knn.predict(normalized_x_test_data)
    y_pred
   ```
 -***Naive Bayes algorithm***
  ---
 ```python
    from sklearn.naive_bayes import GaussianNB
    model = GaussianNB()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
```
 -***support vector machine***
---
```python
    from sklearn.svm import SVC
    model = SVC()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)
    y_pred
```
 -***implementation 3 classification algorithms in same file***
---
```python
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.naive_bayes import GaussianNB
    from sklearn.svm import SVC
    # Creating objects for each classifiers
    knn = KNeighborsClassifier(n_neighbors=7)
    base = GaussianNB()
    model = SVC()
    # Pass each objects to an list
    algorithms = [knn, base, model]
```
 -***Simple Linear Regression***
  ---
```python
    from sklearn.linear_model import LinearRegression
    # Create Object(model)
    model = LinearRegression()
    # fit model
    model.fit(x_train, y_train)
    # Predict value
    y_pred = model.predict(x_test)
    y_pred
```
 -***Multiple Linear Regression***
--- 
```python
    from sklearn.linear_model import LinearRegression
    # Create Object(model)
    model = LinearRegression()
    # fit model
    model.fit(x_train, y_train)
    # Predict value
    y_pred = model.predict(x_test)
    y_pred
```
 -***Polynomial Algorithm***
---
 ```python
    # Apply polynominal algorithm
    from sklearn.preprocessing import PolynomialFeatures
    poly = PolynomialFeatures(degree = 3) # features expanded to 4
    x_poly = poly.fit_transform(x) # x tranformed to x_poly, then we have 4 features instaed of 3, x_poly(x^3,x^2,x,c), x(x) only one feature
    x_poly
    
    
    poly.fit(x_poly, y) # To correct dimension (x,y)->(2*1)  for (x_poly,y)->(3*1)
    # Model creation
    model1 = LinearRegression() # already we transormed and fited above
    model1.fit(x_poly, y)
    y_poly = model1.predict(x_poly)
    y_poly
```
# 7.***Classification Report***
---
 -***Confusion matrix***
 ```python
    from sklearn.metrics import confusion_matrix, accuracy_score
    matrix_con = confusion_matrix(y_test, y_pred)
    matrix_con
```

 -***Classification Report***
 ```python
    from sklearn.metrics import classification_report
    # Creating object
    report = classification_report(y_test, y_pred) # actual value, predited value
    print(report) # here we should use print function
```
# 8. ***Performance measurements for classification model***
---
 -***Accuracy Score***
 ```python
    from sklearn.metrics import confusion_matrix, accuracy_score
    score = accuracy_score(y_test, y_pred)
    score
```
     1. Accuracy score
     2. Recall
     3. Precision
     4. F1 Score
# 8. ***Performance Measurements for Regression Model***

      1. MAE(Mean Absolute Error)
      2. MAPE(Mean Absolute Percentage Error)
      3. MSE(Mean Squared Error)
      4. RMSE (Root Mean Squared Error)
      5. R2_score : 
```python
    # Mean Absoulte Percentage error
    from sklearn.metrics import mean_absolute_percentage_error
    print("Error percentage is ", mean_absolute_percentage_error(y_test, y_pred))
    
    # R2_Score
    from sklearn.metrics import r2_score
    print("R2 score is", r2_score(y_test, y_pred))
```
# 9. ***Plot confusion matrix***
```python
    from sklearn.metrics import ConfusionMatrixDisplay
    lables =  [1, 1]
    # The order must be in y_test
    cmd = ConfusionMatrixDisplay(matrix_con, display_labels = lables)
    cmd.plot()
```
 


