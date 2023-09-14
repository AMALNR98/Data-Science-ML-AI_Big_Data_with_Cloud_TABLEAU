import numpy as np
import pandas as pd

nested_dictionary_1 = pd.Series(
    {'id': [101, 102, 103, 104, 105],
     'first_name': ['amal', 'john', 'raju', 'alwin', 'robin'],
     'lastname': ['r', 't', 'u', 'r', 'c'],
     'age': [25, 26, 26, 24, 26]})
print(nested_dictionary_1)

nested_dictionary_1_to_dataframe = pd.DataFrame(nested_dictionary_1)

print("*" * 150)

# adding new column gender
nested_dictionary_1_to_dataframe['Gender'] = ['m', 'f', 'm', 'f']
print(nested_dictionary_1_to_dataframe)
