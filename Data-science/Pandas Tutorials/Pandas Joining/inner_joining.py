import numpy as np
import pandas as pd

nested_dictionary_1 = pd.Series(
    {'id': [1, 2, 3, 4, 5],
     'first_name': ['amal', 'john', 'raju', 'alwin', 'robin'],
     'lastname': ['r', 't', 'u', 'r', 'c'],
     'age': [25, 26, 26, 24, 26]})
print(nested_dictionary_1)

nested_dictionary_2 = pd.Series(
    {'id': [3, 4, 5, 6, 7],
     'profession': ['bigdata', 'python', 'st', 'java', 'c'],
     'salary': [10000, 1000, 1500, 2923.2332],
     'location': ['US', 'UK', 'UAE', 'EU', 'JPN']})
print(nested_dictionary_2)