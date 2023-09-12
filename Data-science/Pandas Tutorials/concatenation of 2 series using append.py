import numpy as np
import pandas as pd

a = pd.Series([5, 3, 4, 5, 4, 3, 2, 5, 6, 4])
b = pd.Series([3, 6, 7, 4, 8, 4, 4, 2, 8, 9])

# append
c = a.append(b)
print(c)