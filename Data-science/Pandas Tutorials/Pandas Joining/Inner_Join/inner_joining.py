# Inner join
# Syntax:
# new_data_frame_name = pd.merge(df1,df2, on = 'column_name', how = 'inner')

import numpy as np
import pandas as pd

nested_dictionary_1 = {'id': [1, 2, 3, 4, 5],
                       'first_name': ['amal', 'john', 'raju', 'alwin', 'robin'],
                       'lastname': ['r', 't', 'u', 'r', 'c'],
                       'age': [25, 26, 26, 24, 26]}
personal_data = pd.DataFrame(nested_dictionary_1)
# print(nested_dictionary_1)
print(personal_data)
nested_dictionary_2 = {'id': [3, 4, 5, 6, 7],
                       'profession': ['bigdata', 'python', 'st', 'java', 'c'],
                       'salary': [10000, 1000, 1500, 2923, 2332],
                       'location': ['US', 'UK', 'UAE', 'EU', 'JPN']}
employee_data = pd.DataFrame(nested_dictionary_2)
# print(nested_dictionary_2)
print(employee_data)


inner_joined_data = pd.merge(personal_data, employee_data, on='id', how='inner') [['first_name', 'salary']]
print(inner_joined_data)