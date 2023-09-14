# Sample.txt to data frame

import numpy as np
import pandas as pd

df = pd.read_csv('/home/amal/Downloads/sample.txt')  # if the file is comma separation there is no need to define
print(df)

# if there is no header tag in file give 'header=None'
print("*"*100)
df_1 = pd.read_csv('/home/amal/Downloads/sample.txt', header=None)
print(df_1)

