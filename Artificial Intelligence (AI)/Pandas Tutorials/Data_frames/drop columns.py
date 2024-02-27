import numpy as np
import pandas as pd

nested_list_1 = [[101, 'amal', 'nr', 25, 'bigdata', 1000],
                 [102, 'john', 'joseph', 24, 'python', 1000],
                 [103, 'raju', 'k', 45, 'python', 1000],
                 [104, 'ram', 'ld', 35, 'bigdata', 1000],
                 [103, 'raju', 'k', 45, 'python', 1000]
                 ]
# print(nested_list_1)
print("*" * 150)
data_frame_1 = pd.DataFrame(nested_list_1)
data_frame_1.columns = ['id', 'first_name', 'last_name', 'age', 'profession', 'salary']
# print(data_frame_1)

# new_data_frame_name = old_data_frame_name.drop(["column_name'])
# if we don't add axis=1 then only drop column name
data_frame_remove_age = data_frame_1.drop(['age'], axis=1)
print(data_frame_remove_age)

# to remove multiple column
data_frame_remove_age_salary = data_frame_1.drop(['age', 'salary'], axis=1)
print(data_frame_remove_age_salary)