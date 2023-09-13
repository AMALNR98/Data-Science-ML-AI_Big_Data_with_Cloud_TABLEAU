import numpy as np
import pandas as pd

a = pd.Series([1, 2, 3, 4, 5])
b = pd.Series([6, 7, 8, 9, 10])

# append
c = a._append(b)
print(c)
print("*" * 100)
d = a._append(b, ignore_index=True)
print(d)

