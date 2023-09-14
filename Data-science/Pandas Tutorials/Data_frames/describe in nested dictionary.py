import numpy as np
import pandas as pd

nested_list_1 = [[101, 'amal', 'nr', 25, 'bigdata', 1000],
                 [102, 'john', 'joseph', 24, 'python', 1000],
                 [104, 'raju', 'k', 45, 'python', 1000],
                 [104, 'ram', 'ld', 35, 'bigdata', 1000]]
print(nested_list_1)
print("*" * 150)
data_frame_1 = pd.DataFrame(nested_list_1)
print(data_frame_1)
print("*" * 150)

# Describe
print(data_frame_1.describe())

# The describe() method returns description of the data in the DataFrame.
#
# If the DataFrame contains numerical data, the description contains these information for each column:
#
# count - The number of not-empty values.
# mean - The average (mean) value.
# std - The standard deviation.
# min - the minimum value.
# 25% - The 25% percentile*.
# 50% - The 50% percentile*.
# 75% - The 75% percentile*.
# max - the maximum value.
print("*" * 150)

print(data_frame_1.describe(include='O'))  # O means object

# count: The count of non-null (non-missing) values in the "Name" column is 3. This means there are no missing values
# for names in the DataFrame
# unique: The number of unique names in the "Name" column is 3. Each name is unique in this case.
# top: The most frequent (top) name in the "Name" column is "Alice."
# freq: The frequency of the most frequent name "Alice" is 1, which means it appears once in the "Name" column.

print("*" * 150)

print(data_frame_1.describe(include='all'))
