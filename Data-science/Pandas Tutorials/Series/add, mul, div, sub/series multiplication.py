import numpy as np
import pandas as pd

a = pd.Series([4, 5, 6, 7, 9])
b = pd.Series([5, 3, 2, 1])

# Multiplication : Element by element

c = a.multiply(b)
print(c)

# 0    20.0
# 1    15.0
# 2    12.0
# 3     7.0
# 4     NaN
# dtype: float64

# NaN is not a number
