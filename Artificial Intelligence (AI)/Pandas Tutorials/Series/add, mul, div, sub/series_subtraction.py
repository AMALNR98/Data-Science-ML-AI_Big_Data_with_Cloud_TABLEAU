import numpy as np
import pandas as pd

a = pd.Series([4, 5, 6, 7])
b = pd.Series([5, 3, 2, 1])

# Subtracting : Element by element subtraction

c = a.subtract(b)
print(c)
