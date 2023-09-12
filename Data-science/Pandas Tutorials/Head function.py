import numpy as np
import pandas as pd

a = pd.Series([5, 3, 4, 5, 4, 3, 2, 5, 6, 4])
print(a)

# head function is used to print first 5 lines
print("*" * 100)
print(a.head())

# tail function is used to print last 5 lines
print("*"*100)
print(a.tail())
