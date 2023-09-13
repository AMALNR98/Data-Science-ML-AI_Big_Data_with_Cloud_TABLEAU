import numpy as np
import pandas as pd

a = pd.Series([4, 5, 6, 7, 9])
b = pd.Series([5, 3, 2, 1])

# Division : Element by element

c = a.div(b)
print(c)