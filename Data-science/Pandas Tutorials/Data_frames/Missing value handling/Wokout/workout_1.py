# shape
# head
# tail
# total number of missing value.
# missing value--> number of values

import numpy as np
import pandas as pd

missing_1 = pd.read_csv('/home/amal/Downloads/missing_data1.csv')
print(missing_1)
print("*"*100)

print(missing_1.shape)
print("*"*100)

print(missing_1.head())
print("*"*100)

print(missing_1.tail())
print("*"*100)

print(missing_1.isna().sum())
print("*"*100)