import numpy as np
import pandas as pd

a = pd.Series([4, 5, 6, 7])
b = pd.Series([5, 3, 2, 1])

# Adding : Element by element addition

c = a.add(b)
print(c)
