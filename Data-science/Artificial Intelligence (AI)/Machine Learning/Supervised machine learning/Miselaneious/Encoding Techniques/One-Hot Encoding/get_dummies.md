`get_dummies` is not a method in scikit-learn (sklearn). Instead, it's a function provided by the pandas library for one-hot encoding categorical variables in a pandas DataFrame. If you want to use one-hot encoding with scikit-learn, you can achieve this by using the `OneHotEncoder` class, which is part of scikit-learn's preprocessing module. Here's how to use `OneHotEncoder`:

```python
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample data in a pandas DataFrame
data = {
    'Color': ['Red', 'Green', 'Blue', 'Red', 'Green'],
    'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small'],
    'Category': ['A', 'B', 'A', 'C', 'B']
}

df = pd.DataFrame(data)

# Create an instance of OneHotEncoder
encoder = OneHotEncoder(sparse=False, drop='first')  # 'sparse=False' creates a dense array, 'drop' removes one category column to prevent multicollinearity

# Fit and transform the encoder on the categorical columns
encoded_data = encoder.fit_transform(df[['Color', 'Size', 'Category']])

# Create a DataFrame with the one-hot encoded data
encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['Color', 'Size', 'Category']))

# Display the one-hot encoded DataFrame
print(encoded_df)
```

In this example:

1. We import pandas and scikit-learn.

2. We create a sample DataFrame called `df` containing three categorical columns: 'Color', 'Size', and 'Category'.

3. We create an instance of `OneHotEncoder`, specifying the `sparse=False` parameter to create a dense array and `drop='first'` to remove one of the dummy variable columns to prevent multicollinearity.

4. We use the `fit_transform` method of `OneHotEncoder` to one-hot encode the selected columns.

5. We create a new DataFrame, `encoded_df`, to store the one-hot encoded data.

6. Finally, we display the one-hot encoded DataFrame.

This code demonstrates how to use `OneHotEncoder` from scikit-learn to perform one-hot encoding on selected columns of a pandas DataFrame.