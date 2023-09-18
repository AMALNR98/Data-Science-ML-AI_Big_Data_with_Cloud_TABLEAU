# sort_values()

# Syntax
# new_data_frame = old_data_frame.sort_values(by='column_name')


import numpy as np
import pandas as pd

nested_list_1 = [[101, 'amal', 'nr', 25, 'bigdata', 1000],
                 [102, 'john', 'joseph', 24, 'python', 1000],
                 [103, 'raju', 'k', 45, 'python', 1000],
                 [104, 'ram', 'ld', 35, 'bigdata', 1000]]
print(nested_list_1)
print("*" * 150)
data_frame_1 = pd.DataFrame(nested_list_1)
data_frame_1.columns = ['id', 'first_name', 'last_name', 'age', 'profession', 'salary']
print(data_frame_1)

# nested list
# order
# sort_values()
print("*" * 150)

sort_by_age = data_frame_1.sort_values(by='age')
print(sort_by_age)

print("*" * 150)

sort_by_age_descending = data_frame_1.sort_values(by='age', ascending=False)
print(sort_by_age_descending)